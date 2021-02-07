---
description: Use AI to index your images based on semantic similarity.
---

# Index Images for Search

To get started with search, you must first add images to the search index. You can add one or more images to the index at a time. You can supply an image either with a publicly accessible URL or by directly sending image bytes. You can send up to 128 images in one API call.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder()
        .addInputs(
            Input.newBuilder()
                .setData(
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setUrl("https://samples.clarifai.com/metro-north.jpg")
                            .setAllowDuplicateUrl(true)
                    )
                )
        )
        .addInputs(
            Input.newBuilder()
                .setData(
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setUrl("https://samples.clarifai.com/wedding.jpg")
                            .setAllowDuplicateUrl(true)
                    )
                )
        )
        .addInputs(
            Input.newBuilder()
                .setData(
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setBase64(ByteString.copyFrom(Files.readAllBytes(
                                new File("{YOUR_IMAGE_FILE_LOCATION}").toPath()
                            )))
                    )
                )
        )
        .build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    for (Input input : postInputsResponse.getInputsList()) {
        System.out.println("Input " + input.getId() + " status: ");
        System.out.println(input.getStatus() + "\n");
    }

    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

const fs = require("fs");
const imageBytes = fs.readFileSync("{YOUR_IMAGE_FILE_LOCATION}");

stub.PostInputs(
    {
        inputs: [
            {
                data: {image: {url: "https://samples.clarifai.com/metro-north.jpg", allow_duplicate_url: true}}
            },
            {
                data: {image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true}}
            },
            {
                data: {image: {base64: imageBytes}}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            for (const input of response.inputs) {
                console.log("Input " + input.id + " status: ");
                console.log(JSON.stringify(input.status, null, 2) + "\n");
            }

            throw new Error("Post inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

with open("{YOUR_IMAGE_FILE_LOCATION}", "rb") as f:
    file_bytes = f.read()

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg",
                        allow_duplicate_url=True
                    )
                )
            ),
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/wedding.jpg",
                        allow_duplicate_url=True
                    )
                )
            ),
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        base64=file_bytes
                    )
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    for input_response in post_inputs_response.inputs:
        print("Input " + input_response.id + " status:")
        print(input_response.status)

    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg",
            "allow_duplicate_url": true
          }
        }
      },
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/wedding.jpg",
            "allow_duplicate_url": true
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs

# Use image's "base64" field to upload image from your local machine.
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Response JSON" %}
```javascript
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "inputs": [
    {
      "id": "edc70c917475499abdc7151f41d6cf3e",
      "created_at": "2016-11-22T17:06:02Z",
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/metro-north.jpg"
        }
      },
      "status": {
        "code": 30001,
        "description": "Download pending"
      }
    },
    {
      "id": "f96ca3bbf02041c59addcc13e3468b7d",
      "created_at": "2016-11-22T17:06:02Z",
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/wedding.jpg"
        }
      },
      "status": {
        "code": 30001,
        "description": "Download pending"
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

