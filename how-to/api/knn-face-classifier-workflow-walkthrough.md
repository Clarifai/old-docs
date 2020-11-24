---
description: Use facial recognition to identify individual people.
---

# Custom KNN Face Classifier Workflow

Let's say you want to build a face recognition system that is able to differentiate between persons of whom you only have a few samples \(per person\). Machine learning models generally require a large inputs dataset to be able to classify the inputs well.

When a large dataset is the luxury you do not have, we recommend using our **KNN Classifier Model** which uses K nearest neighbor search and plurality voting amongst the nearest neighbors to classify new instances. It's recommended when you only have a small dataset like one input per concept.

In this walkthorugh, you'll learn how to create a KNN classifier that's going to work based off the Clarifai's base Face model. The whole process below is going to be done programmatically, using the Clarifai's powerful API.

> Note: Each of the steps below can also be done manually on [the Clarifai Portal](https://portal.clarifai.com/).

## Create a new application

The first step is manual: in the Clarifai Portal, [create an new application](https://docs.clarifai.com/getting-started/applications/create-an-application) with **Face** selected as the Base Workflow.

Afterward, copy the newly-created application's _API key_ and set it as metadata \(see the initialization code\). This variable is going to be used, for authorization purposes, by all Clarifai API calls that follow.

## Add images

Add images that contain the faces you want to use as a training set.

Since the application's base model is Face, after adding an image, faces are automatically located and are available to be annotated.

{% tabs %}
{% tab title="gRPC Python" %}
```python
import time

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

# Insert here the URLs of the images
image_urls = [
    "{YOUR_IMAGE_URL_1}",
    "{YOUR_IMAGE_URL_2}"
]
post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(url=url)
                )
            )
            for url in image_urls
        ]
    ),
    metadata=metadata
)


if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Failed response, status: " + str(post_inputs_response.status))
```
{% endtab %}
{% endtabs %}

## Wait for upload & map IDs to URLs

Now we'll wait for all the images to finish uploading, and then create a dictionary mapping from an input ID to the URL. This will help us to annotate the proper image in the next step.

{% tabs %}
{% tab title="gRPC Python" %}
```python
while True:
    list_inputs_response = stub.ListInputs(
        service_pb2.ListInputsRequest(page=1, per_page=100),
        metadata=metadata
    )

    if list_inputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Failed response, status: " + str(list_inputs_response.status))

    for the_input in list_inputs_response.inputs:
        input_status_code = the_input.status.code
        if input_status_code == status_code_pb2.INPUT_DOWNLOAD_SUCCESS:
            continue
        elif input_status_code in (status_code_pb2.INPUT_DOWNLOAD_PENDING, status_code_pb2.INPUT_DOWNLOAD_IN_PROGRESS):
            print("Not all inputs have been downloaded yet. Checking again shortly.")
            break
        else:
            error_message = (
                    str(input_status_code) + " " +
                    the_input.status.description + " " +
                    the_input.status.details
            )
            raise Exception(
                f"Expected inputs to download, but got {error_message}. Full response: {list_inputs_response}"
            )
    else:
        # Once all inputs have been successfully downloaded, break the while True loop.
        print("All inputs have been successfully downloaded.")
        break
    time.sleep(2)


input_id_to_url = {inp.id: inp.data.image.url for inp in list_inputs_response.inputs}
```
{% endtab %}
{% endtabs %}

## List the annotations

Let's now print all the regions that the Face base model detected on our images.

The code below prints the annotations together with the input ID and region ID. These two IDs will be needed in the next step to annotate using our custom concepts. We'll also need the base Face model ID which is the one where `model_version_id` equals to `embedding_model_version_id`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(list_all_annotations=True, page=1, per_page=100),
    metadata=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Failed response, status: " + str(list_annotations_response.status))


for annotation in list_annotations_response.annotations:
    if not annotation.data or not annotation.data.regions:
        continue
    # Display results only for the base Face model.
    if annotation.model_version_id != annotation.embed_model_version_id:
        continue
    for region in annotation.data.regions:
        bbox = region.region_info.bounding_box
        print(f"Face was detected on input ID {annotation.input_id} (URL: {input_id_to_url[annotation.input_id]})")
        print(f"\tRegion ID: {region.id}")
        print(f"\tRegion location: left={bbox.left_col:.4f}, top={bbox.top_row:.4f}, right={bbox.right_col:.4f}, bottom={bbox.bottom_row:.4f}")
        print(f"\tConfidence: {region.value:.2f}")
        print(f"\tBase Face model version ID: {annotation.embed_model_version_id}")
        print()
```
{% endtab %}
{% endtabs %}

## Post new annotations

Let's use the above information to add annotations, in the form of a concept, to the detected face regions.

Input below the IDs from the previous call, and choose your concept ID and name that you want to annotate the region with \(you may want to use e.g. person's name\).

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_annotations_response = stub.PostAnnotations(
    service_pb2.PostAnnotationsRequest(
        annotations=[
            resources_pb2.Annotation(
                input_id="{MY_INPUT_ID}",
                embed_model_version_id="{MY_EMBED_MODEL_VERSION_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            id="{MY_REGION_ID}",
                            data=resources_pb2.Data(
                                concepts=[
                                    resources_pb2.Concept(
                                        id="{MY_CONCEPT_ID}",
                                        name="{MY_CONCEPT_NAME}",
                                        value=1
                                    )
                                ]
                            )
                        )
                    ]
                )

            )
        ],
    ),
    metadata=metadata
)

if post_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Failed response, status: " + str(post_annotations_response.status))
```
{% endtab %}
{% endtabs %}

## Create a KNN model

Let's now create a KNN model using the concept IDs that were added above. The model type ID should be set to `knn-concept`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        models=[
            resources_pb2.Model(
                id="my-knn-face-classifier-model",
                model_type_id="knn-concept",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="{MY_CONCEPT_ID_1}"),
                            resources_pb2.Concept(id="{MY_CONCEPT_ID_2}"),
                        ]
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Failed response, status: " + str(post_models_response.status))
```
{% endtab %}
{% endtabs %}

## Create a workflow

One last step before being able to do predictions: create a workflow that's going to map from the base Face model to our custom KNN model.

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_workflows_response = stub.PostWorkflows(
    service_pb2.PostWorkflowsRequest(
        workflows=[
            resources_pb2.Workflow(
                id="detect-knn-workflow",
                nodes=[
                    resources_pb2.WorkflowNode(
                        id="face-v1.3-embed",
                        model=resources_pb2.Model(
                            id="d02b4508df58432fbb84e800597b8959",  # This is the base Face model ID.
                            model_version=resources_pb2.ModelVersion(
                                id="{EMBEDDING_MODEL_VERSION_ID}"  # This is the base Face model version ID.
                            )
                        )
                    ),
                    resources_pb2.WorkflowNode(
                        id="knn-classifier",
                        model=resources_pb2.Model(
                            id="my-knn-face-classifier-model",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_MODEL_VERSION_ID}"
                            )
                        )
                    ),
                ]
            )
        ]
    ),
    metadata=metadata
)

if post_workflows_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Failed response, status: " + str(post_workflows_response.status))
```
{% endtab %}
{% endtabs %}

## Predict

We're going to run a prediction on the workflow created above.

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_workflow_results_response = stub.PostWorkflowResults(
    service_pb2.PostWorkflowResultsRequest(
        workflow_id="detect-knn-workflow",
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="{MY_URL_TO_PREDICT_FACES_ON}"
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

# We get back one result per input. Since there's one input above, one input was returned.
result = post_workflow_results_response.results[0]

for output in result.outputs:
    # At this point, two outputs will be returned: one for the base Face model, and the other for our custom model.
    # At this moment, we are only interested in the results of the latter model (if you want, you may also see the
    # half-baked results of the base Face model, which is not a list of concepts, but an embedding vector).
    if output.model.id != "my-knn-face-classifier-model":
        continue
    print(f"The prediction of the model ID `{output.model.id}` is:")
    for concept in output.data.concepts:
        print(f"\t{concept.name} (id: {concept.id}): {concept.value:.4f}")
```
{% endtab %}
{% endtabs %}

