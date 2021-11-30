---
description: Capture information from an organization's form that are stored as PDF documents.
---

# Intelligent Document Processing

## Introduction

> In this series of posts, advanced users at Clarifai will present working solutions to help you kick-start your own AI solutions.

### The Use Case

There is an a problem facing many organizations as they attempt to modernize: digitizing documents.
In order to effectivelt gain insights from their old paper records, organizations must transform them into a digital version.
Now, simply making a digital copy of the document is actually rather easy; simply scan it, or even just upload a photo.
The problem though is that while this changes how the document is stored, it doesn't give us any real improvements to accessing the data therein.
For the longest time this required a laborious, manual, data entry process.
Someone would have to transcribe the documents, one-by-one, and enter each field into the books.
This presents a problem to organizations that potentially have thousands-upon-thousands of documents in their records: which can be intractable when it comes to the time and cost of the effort.
Luckily though, there's a middle-ground.

Using Clarifai's publicly-available Optical Character Recognition (OCR) models, we can leverge Artifical Intelligence to both do this in a quick and cost-effective manner, but without sacraficing the insights they would have from recording every single value.  

### Assumptions

Before we begin, let us make some assumptions:

1. The form is a standard for, with static regions for fixed values, ie the "name" field will always appear in the same location across all forms
1. All of the entries will be in English, using the Roman alphabet
1. The organization has a simple means of converting their paper documents to pdf documents, and storing them to a local file system; which is a common feature on most commercial print stations
1. All of the forms will be type-filled, not handwritten; so as to make generating examples easier.

These assumptions were largely made to make this example succinct and easily digestable.

## Setup

Before we get to the implementation, let's take a moment to provide an overview thereof.

First off, the broad strokes have already been laid out: convert pdf to image, use Clarifai for OCR, and from that you'll have the text, which you then store in order to access later.
Clearly there are some gaps that need to be filled in though; the largest of which is just _how_ the document will be processed.

Working backwards a bit, the way in which the information will be recorded will be highly dependent on the organization's data policies.
So to simplify things, we will simply utilize Clarifai's platform to store the annotated documents.

Given assumption 1 above, we know that the fields will be in fixed locations.
This means we can define those ahead of time, and here we've chosen to do so using a JSON file, in which we define the document's structure in a manner similar to:

```json
{
    "field_1": [0.25, 0.25, 0.50, 0.50],
    "field_2": [0.50, 0.25, 0.75, 0.50],
    .
    .
    .
    "field_n": [0.25, 0.75, 0.50, 1.00]
}
```

Each key-value pair in the JSON file corresponds to the field name, the key (`"field_n"`), and the region coordinates in the form of $[x_0, y_0, x_1, y_1]$.

> Note: All of the region coordinates on the Clarifai are relative, not pixel values.
> This is important, as other image processing libraries might use the pixel values instead.
> We will address converting between these values below.

Given that we know the name of the field, and where it is on the image, we can easily iterate through all of these field values, and annotate the corresponding region on the image. Having the coordinate values will also let us take sub-crops of the document to use the OCR model to predict on; isolating the text associated with a given field.

With this, we have a more fleshed out plan:

> We assume that the user is already familiar with basic platform usage, and has an account.
> If more information is needed here, please find the appropriate section of the document in order to access more indepth information.

1. Convert PDF to Image, and upload it the the Clarifai platform for storage.
1. Read values from the JSON where the form's fields and their locations are defined.
1. For each field and region:
    - Extract a sub-crop for the field
    - Use Clarifai's OCR model to predict the text associated with the field
    - Write the predicted text back to the input as an annotation

Now let's dive into the implementation:

Starting with the conversion of a PDF document to an image, we can handle this with the open-source library `pdf2image`; which does exactly what the name suggests.
In order to be a bit more defensive with our programming we with wrap the call to the `pdf2image.convert_from_path` method in a separate function, and do some quick sanity checking to make sure the PDF file exists.

{% tabs %}
{% tab title="Python" %}

```python
import os

from pdf2image import convert_from_path


def pdf_to_page_images(file_path):
    """return an iterable of images that span the pages of the document"""
    assert os.path.exists(file_path), f"file not found: {file_path}"
    pdf_images = convert_from_path(file_path)

    return pdf_images
```

{% endtab %}

This will return an iterable of images that correspond to the individual pages of the document.

> Note: For simplicity's sake, our form only has one page.

## Full implementation

{% tabs %}
{% tab title="intelligent_document_processing.py"}
```python
#!/usr/bin/env python3
import io
import os
import json
import time
import argparse

from pdf2image import convert_from_path
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2


def pdf_to_page_images(file_path):
    """return an iterable of images that span the pages of the document"""
    assert os.path.exists(file_path), f"file not found: {file_path}"
    pdf_images = convert_from_path(file_path)

    return pdf_images

def post_image_bytes_as_input(image_bytes, stub, metadata):
    """post an image in bytes format to the platform as an input"""
    post_inputs_response = stub.PostInputs(  # what is an intellgent way to handle these platform objects? Obvi singleton object that acts as a unified permissions manager...  
        service_pb2.PostInputsRequest(
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=image_bytes
                        )
                    )
                ) 
            ]    
        ),
        metadata=metadata
    )

    return post_inputs_response

def image_to_bytes(img):
    """convert a PIL image object to a byte array"""
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')
    return byte_arr.getvalue()

def pixels_to_proportions(coordinates, image):
    """
    This function expects a sequence of coordinates as inputs, along with the image it corresponds to.
    That is, something like: $[(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)]$
    """
    w, h = image.size
    output = []

    for (x, y) in coordinates:
        # x /= w
        # y /= h
        output.append((x/w, y/h))

    return output


def proportions_to_pixels(coordinates, image):
    """see docstring for `pixels_to_proportions`"""
    w, h = image.size
    output = []
    for (x, y) in coordinates:
        output.append((x*w, y*h))

    return output

def unpack_tuple_list(a):
    """flatten a nested list. Currently fixed at a depth of k=2."""
    return [i for sub in a for i in sub]

def grouped(iterable, n):
    """h/t https://stackoverflow.com/a/5389547
    Given the iterable `S`, and the integer n
    $S \to (s_{0,0}, s_{0,1}, s_{0,2}, \dots, s_{0, n-1}), \ldots, (s_{m,0}, s_{m,1} , s_{m,2},...s_{m, n-1})$
    """
    return zip(*[iter(iterable)]*n)

def read_json_fields(json_file):
    """
    parse the document fields defined in json_file
    """
    with open(json_file, 'rb') as f:
        d = json.load(f)

    for k, v in d.items():
        yield k, v


def _hold_for_upload(asset_id, stub, metadata, t=.5):
    """function that will halt the program while we wait for the input to finish uploading"""
    from itertools import count
    for i in count():
        get_inputs_response = stub.GetInput(
            request=service_pb2.GetInputRequest(
                input_id=asset_id,
            ),
            metadata=metadata
        )
        assert get_inputs_response.status.code == status_code_pb2.SUCCESS

        if get_inputs_response.input.status.code == status_code_pb2.INPUT_DOWNLOAD_SUCCESS:
            break
        else:
            time.sleep(t)
            continue

    return True 


def predict_text(image, model_id, stub, metadata):
    """return the text value output by the specified OCR model. This is """
    image_bytes = image_to_bytes(image)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            model_id=model_id,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=image_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    predicted_text = post_model_outputs_response.outputs[0].data.text.raw

    return predicted_text

def make_concept(concept, value=1.):
    """create a concept object. Note: By default this will create a positive association - value=1. - with the concept."""
    return resources_pb2.Concept(id=concept, value=value)

def coords_to_bbox(x0, y0, x1, y1):
    """create a BoundingBox object from a set of 2d Cartesian coordinates"""
    return resources_pb2.BoundingBox(
        left_col=x0,
        top_row=y0,
        right_col=x1,
        bottom_row=y1
    )

def make_annotation(input_id, coords, body, stub, metadata, *concepts):
    """we're going to simply post a single region annotation at a time"""
    post_annotations_response = stub.PostAnnotations(
        service_pb2.PostAnnotationsRequest(
            annotations=[
                resources_pb2.Annotation(
                    input_id=input_id,
                    data=resources_pb2.Data(
                        regions=[
                            resources_pb2.Region(
                                region_info=resources_pb2.RegionInfo(
                                    bounding_box=coords_to_bbox(*coords),
                                    text=resources_pb2.Text(raw=body)
                                ),
                                data=resources_pb2.Data(
                                    concepts=[make_concept(concept) for concept in concepts],
                                )
                            )
                        ]
                    ),
                ),
            ]
        ),
        metadata=metadata
    )

    if post_annotations_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Post annotations failed, status: " + post_annotations_response.status.description)    

    return post_annotations_response

def main(args):
    # initialize the Clarifai client
    print(args)
    channel = ClarifaiChannel.get_json_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', f'Key {args.api_key}'),)

    # import the pdf document, and convert it to an iterable of images for the pages
    doc, *_ = pdf_to_page_images(args.file) # we know our document is only one page, so we isolate the first item in the iterable. Isomorphic to pdf_to_page_images(args.file)[0]
    doc_bytes = image_to_bytes(doc)

    # post the doc as an input
    post_input_response = post_image_bytes_as_input(doc_bytes, stub, metadata)

    doc_id = post_input_response.inputs[0].id  # we know there will only be one input, given the setup above
    
    print(f"[DOC] - {doc_id}")
    _ = _hold_for_upload(doc_id, stub, metadata)  # ensure that the input is uploaded, so that we can annotate the regions-of-interest

    doc_fields = read_json_fields(args.layout)    

    for field, value in doc_fields:
        relative_coords = grouped(value, 2)  # xy-coords -> n=2
        pixel_coords = proportions_to_pixels(relative_coords, doc)
        pixel_coords_flat = unpack_tuple_list(pixel_coords)

        # get a crop of the region
        region = doc.crop(pixel_coords_flat)

        # predicted text in cropped region
        predicted_text = predict_text(region, args.model_id, stub, metadata)
        print("\t-", f"{field} | {predicted_text}")

        post_annotation_response = make_annotation(doc_id, tuple(value), predicted_text, stub, metadata, field)

        if post_annotation_response.status.code != status_code_pb2.SUCCESS:
            breakpoint()

    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help="File path to the PDF document you would like to parse and annotate.")
    parser.add_argument('-k', '--api_key', type=str, help="The Clarifai API key associate with your application.")
    parser.add_argument('-m', '--model_id', type=str, help="The ID of the Clarifai model you would like to use for OCR.", default='eng-ocr')
    parser.add_argument('-l', '--layout', type=str, help="Path to the JSON file in which the document layout is defined.", default='assets/field_regions.json')

    args = parser.parse_args()

    _ = main(args)

```
{% endtab %}
