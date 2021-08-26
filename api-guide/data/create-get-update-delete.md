---
description: Manage the data in your app.
---

# Adding and Removing Data

## Inputs

The API is built around a simple idea. You send inputs \(images\) to the service and it returns predictions. In addition to receiving predictions on inputs, you can also index inputs and their predictions to later search against. You can also index inputs with concepts to later train your own model.

When you add an input to your app, the base workflow of your app runs, computing the outputs from all the models in that workflow and indexes those outputs. Those indexed outputs are what incur the indexing fee monthly, and enable search and training on top of the outputs of the base workflow models.

### Add Inputs

You can add inputs one by one or in bulk. If you do send bulk, you are limited to sending 128 inputs at a time.

**Important: adding inputs is an asynchronous operation.** That means it will process indexing of your inputs through your default workflow in the background, which can take some time. In order to check the status of each input you add, see the section on [Get Input by ID](https://github.com/Clarifai/docs/tree/1c1d25cdd43190c38a2edb313297c0d566b3a0e3/api-guide/inputs/inputs.md#get-input-by-id) to look for status 30000 \(INPUT\_IMAGE\_DOWNLOAD\_SUCCESS\) status code on each input to know when it's successfully been indexed.

#### Add an input using a publicly accessible URL

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder().setImage(
                Image.newBuilder()
                    .setUrl("https://samples.clarifai.com/metro-north.jpg")
                    .setAllowDuplicateUrl(true)
            )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostInputs(
    {
        inputs: [{data: {image: {url: "https://samples.clarifai.com/metro-north.jpg", allow_duplicate_url: true}}}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
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
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
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
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/metro-north.jpg",
          "allow_duplicate_url": true
        }
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

#### Add an input using bytes

The data must be base64 encoded. When you add a base64 image to our servers, a copy will be stored and hosted on our servers. If you already have an image hosting service we recommend using it and adding images via the `url` parameter.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import com.google.protobuf.ByteString;
import java.io.File;
import java.nio.file.Files;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder().setImage(
                Image.newBuilder()
                    .setBase64(ByteString.copyFrom(Files.readAllBytes(
                        new File("{YOUR_IMAGE_LOCATION}").toPath()
                    )))
            )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

const fs = require("fs");
const imageBytes = fs.readFileSync("{YOUR_IMAGE_LOCATION}");

stub.PostInputs(
    {
        inputs: [{data: {image: {base64: imageBytes}}}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
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

with open("{YOUR_IMAGE_LOCATION}", "rb") as f:
    file_bytes = f.read()

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        base64=file_bytes
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
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
            "base64": '"`base64 /home/user/image.jpeg`"'"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "data": {
        "image": {
          "base64": "{YOUR_BYTES_STRING}"
        },
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

#### Add multiple inputs with ids

{% hint style="info" %}
In cases where you have your own `id` and you only have one item per image, you are encouraged to send inputs with your own `id`. This will help you later match the input to your own database. If you do not send an `id`, one will be created for you. If you have more than one item per image, it is recommended that you put the product id in metadata.
{% endhint %}

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
                .setId("train1")
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
                .setId("puppy1")
                .setData(
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setUrl("https://samples.clarifai.com/puppy.jpeg")
                            .setAllowDuplicateUrl(true)
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

stub.PostInputs(
    {
        inputs: [
            {
                id: "train1",
                data: {image: {url: "https://samples.clarifai.com/metro-north.jpg", allow_duplicate_url: true}}
            },
            {
                id: "puppy1",
                data: {image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true}}
            },
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

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                id="train1",
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg",
                        allow_duplicate_url=True
                    )
                )
            ),
            resources_pb2.Input(
                id="puppy1",
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/puppy.jpeg",
                        allow_duplicate_url=True
                    )
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    for input_object in post_inputs_response.inputs:
        print("Input " + input_object.id + " status:")
        print(input_object.status)

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
        },
        "id": "train1"
      },
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
          }
        },
        "id": "puppy1"
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
    "inputs": [
        {
        "data": {
            "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg",
            "allow_duplicate_url": true
            }
        },
        "id": "input1"
        },
            {
        "data": {
            "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
            }
        },
        "id": "puppy1"
        }
    ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Add inputs with concepts

If you would like to add an input with concepts, you can do so like this. Concepts play an important role in creating your own models using your own concepts. You can learn more about [creating your own models](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/train.md) above. Concepts also help you search for inputs. You can [learn more about search](../search/) here.

When you add a concept to an input, you need to indicate whether the concept is present in the image or if it is not present.

You can add inputs with concepts as either a URL or bytes.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder()
                .setImage(
                    Image.newBuilder()
                        .setUrl("https://samples.clarifai.com/puppy.jpeg")
                        .setAllowDuplicateUrl(true)
                )
                .addConcepts(
                    Concept.newBuilder()
                        .setId("charlie")
                        .setValue(1f)
                )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostInputs(
    {
        inputs: [{data: {
            image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true},
            concepts: [{id: "charlie", value: 1.}]
        }}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
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

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/puppy.jpeg",
                        allow_duplicate_url=True
                    ),
                    concepts=[resources_pb2.Concept(id="charlie", value=1.)]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
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
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
          },
          "concepts":[
            {
              "id": "charlie",
              "value": 1
            }
          ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
      {
      "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
          },
          // Optionally add a concept with your input
          "concepts": [
          {
            "id": "charlie",
            "value": 1
          }
        ]
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Add inputs with custom metadata

In addition to adding an input with concepts, you can also add an input with custom metadata. This metadata will then be [searchable](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/advanced-searches.md#by-custom-metadata). Metadata can be any arbitrary JSON.

{% hint style="info" %}
If you have more than one item per image it is recommended to put the id in metadata like:

```text
{
  "product_id": "xyz"
}
```
{% endhint %}

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import com.google.protobuf.Struct;
import com.google.protobuf.Value;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder()
                .setImage(
                    Image.newBuilder()
                        .setUrl("https://samples.clarifai.com/puppy.jpeg")
                        .setAllowDuplicateUrl(true)
                )
                .setMetadata(
                    Struct.newBuilder()
                        .putFields("id", Value.newBuilder().setStringValue("id001").build())
                        .putFields("type", Value.newBuilder().setStringValue("animal").build())
                        .putFields("size", Value.newBuilder().setNumberValue(100).build())
                )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostInputs(
    {
        inputs: [{data: {
            image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true},
            metadata: {id: "id001", type: "animal", size: 100}
        }}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

input_metadata = Struct()
input_metadata.update({"id": "id001", "type": "animal", "size": 100})

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/puppy.jpeg",
                        allow_duplicate_url=True
                    ),
                    metadata=input_metadata
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
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
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
          },
          "metadata": {"id": "id001", "type": "animal", "size": 100}
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/puppy.jpeg",
          "allow_duplicate_url": true
        },
        "metadata": {"id": "id001", "type": "animal", "size": 100}
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### List inputs

You can list all the inputs \(images\) you have previously added either for [search](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/advanced-searches.md) or [train](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/train.md).

If you added inputs with concepts, they will be returned in the response as well.

This request is paginated.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse listInputsResponse = stub.listInputs(
    ListInputsRequest.newBuilder()
        .setPage(1)
        .setPerPage(10)
        .build()
);

if (listInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List inputs failed, status: " + listInputsResponse.getStatus());
}

for (Input input : listInputsResponse.getInputsList()) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListInputs(
    {page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List inputs failed, status: " + response.status.description);
        }

        for (const input of response.inputs) {
            console.log(JSON.stringify(input, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_inputs_response = stub.ListInputs(
    service_pb2.ListInputsRequest(page=1, per_page=10),
    metadata=metadata
)

if list_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List inputs failed, status: " + list_inputs_response.status.description)

for input_object in list_inputs_response.inputs:
    print(input_object)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs?page=1&per_page=10
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/inputs?page=1&per_page=10`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### List inputs \(streaming\)

Another method for listing inputs which was built to scalably list app's inputs in an iterative / streaming fashion. `StreamInputs` will return `per_page` number of inputs from a certain input onward, controlled by the optional `last_id` parameter \(defaults to the first input\).

By default, the stream will return inputs from oldest to newest. Set the `descending` field to true to reverse that order.

{% tabs %}
{% tab title="Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

// To start from beginning, do not provide the last ID parameter.
MultiInputResponse firstStreamInputsResponse = stub.streamInputs(
    StreamInputsRequest.newBuilder()
        .setPerPage(10)
        .build()
);

if (firstStreamInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Stream inputs failed, status: " + firstStreamInputsResponse.getStatus());
}

System.out.println("First response (starting from the first input):");
List<Input> inputs = firstStreamInputsResponse.getInputsList();
for (Input input : inputs) {
    System.out.println("\t" + input.getId());
}

String lastId = inputs.get(inputs.size() - 1).getId();

// Set last ID to get the next set of inputs. The returned inputs will not include the last ID input.
MultiInputResponse secondStreamInputsResponse = stub.streamInputs(
    StreamInputsRequest.newBuilder()
        .setLastId(lastId)
        .setPerPage(10)
        .build()
);

if (secondStreamInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Stream inputs failed, status: " + secondStreamInputsResponse.getStatus());
}

System.out.println(String.format("Second response (first input is the one following input ID %s)", lastId));
for (Input input : secondStreamInputsResponse.getInputsList()) {
    System.out.println("\t" + input.getId());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.StreamInputs(
    {
        per_page: 10
    },
    metadata,
    (err, firstResponse) => {
        if (err) {
            done(err);
            return;
        }

        if (firstResponse.status.code !== 10000) {
            done(new Error("Received status: " + firstResponse.status.description + "\n" + firstResponse.status.details));
            return;
        }

        console.log("First response (starting from the first input):");
        for (const input of firstResponse.inputs) {
            console.log("\t" + input.id);
        }

        const lastId = firstResponse.inputs[firstResponse.inputs.length - 1].id;
        stub.StreamInputs(
            {
                last_id: lastId,
                per_page: 10
            },
            metadata,
            (err, secondResponse) => {
                if (err) {
                    done(err);
                    return;
                }

                if (secondResponse.status.code !== 10000) {
                    done(new Error("Received status: " + secondResponse.status.description + "\n" + secondResponse.status.details));
                    return;
                }

                console.log("Second response (first input is the one following input ID " + lastId + ")");
                for (const input of secondResponse.inputs) {
                    console.log("\t" + input.id);
                }

                done();
            }
        );
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

# To start from beginning, do not provide the last_id parameter.
stream_inputs_response = stub.StreamInputs(
    service_pb2.StreamInputsRequest(per_page=10),
    metadata=metadata
)

if stream_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Stream inputs failed, status: " + stream_inputs_response.status.description)

print("First response (starting from the first input):")
for input_object in stream_inputs_response.inputs:
    print("\t" + input_object.id)

last_id = stream_inputs_response.inputs[-1].id

# Set last_id to get the next set of inputs. The returned inputs will not include the last_id input.
stream_inputs_response = stub.StreamInputs(
    service_pb2.StreamInputsRequest(per_page=10, last_id=last_id),
    metadata=metadata
)

print(f"Second response (first input is the one following input ID {last_id}):")
for input_object in stream_inputs_response.inputs:
    print("\t" + input_object.id)
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
// We can implement the API call with a Promise
const streamInputs = (reqAddress) => {
  return new Promise(async (resolve, reject) => {
    fetch(reqAddress, requestOptions)
    .then(data => {
        return data.json()
    }).then(data => {
        resolve(data)
    }).catch(e => {
        console.error('REQUEST -> ', e)
        reject(e)
    })
  })
}

// Async function that will allow us to wait for the first API call
const run = async () => {

	const appId = '{YOUR_APP_ID}'

  const requestOptions = {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
    }
  };

  const REQ_ADDRESS = `https://api.clarifai.com/v2/users/me/apps/${appId}/inputs/stream?per_page=5`

  const req1 = await streamInputs(REQ_ADDRESS)
	
	// Grab the last input_id from the first request to use it in the second request
  const lastId = req1['inputs'][req1['inputs'].length - 1].id 

  const req2 = await streamInputs(REQ_ADDRESS + `&last_id=${lastId}`)
	
	// You're only receiving the inputs from up to the last_id onward
  console.log(req2)
}

run()
```
{% endtab %}

{% endtabs %}

### Get input by id

If you'd like to get a specific input by id, you can do that as well.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

SingleInputResponse getInputResponse = stub.getInput(
    GetInputRequest.newBuilder()
        .setInputId("{YOUR_INPUT_ID}")
        .build()
);

if (getInputResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get input failed, status: " + getInputResponse.getStatus());
}

Input input = getInputResponse.getInput();
System.out.println(input);
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.GetInput(
    {input_id: "{YOUR_INPUT_ID}"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get input failed, status: " + response.status.description);
        }

        const input = response.input;
        console.log(JSON.stringify(input, null, 2));
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_input_response = stub.GetInput(
    service_pb2.GetInputRequest(input_id="{YOUR_INPUT_ID}"),
    metadata=metadata
)

if get_input_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get input failed, status: " + get_input_response.status.description)

input_object = get_input_response.input
print(input_object)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs/{YOUR_INPUT_ID}
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const inputId = '{YOUR_INPUT_ID}'
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/inputs/${inputId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Get inputs status

If you add inputs in bulk, they will process in the background. You can get the status of all your inputs \(processed, to\_process and errors\) like this:

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

SingleInputCountResponse getInputCountResponse = stub.getInputCount(
    GetInputCountRequest.newBuilder().build()
);

if (getInputCountResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get input count failed, status: " + getInputCountResponse.getStatus());
}

InputCount inputCount = getInputCountResponse.getCounts();
System.out.println(inputCount);
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.GetInputCount(
    {},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get input count failed, status: " + response.status.description);
        }

        const counts = response.counts;
        console.log(JSON.stringify(counts, null, 2));
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_input_count_response = stub.GetInputCount(
    service_pb2.GetInputCountRequest(),
    metadata=metadata
)

if get_input_count_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get input count failed, status: " + get_input_count_response.status.description)

counts = get_input_count_response.counts
print(counts)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs/status
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_KEY}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/inputs/status`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Update inputs

### Update input with concepts

To update an input with a new concept, or to change a concept value from true/false, you can do that:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("tree")
                                .setValue(1f)  // 1 means true, this concept is present.
                        )
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("water")
                                .setValue(0f)  // 0 means false, this concept is not present.
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchInputs(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove.
        inputs: [
            {
                id: "{YOUR_INPUT_ID}",
                // 1 means true, this concept is present.
                // 0 means false, this concept is not present.
                data: {concepts: [{id: "tree", value: 1}, {id: "water", value: 0}]}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                        resources_pb2.Concept(id="water", value=0.)  # 0 means false, this concept is not present.
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
# Supported actions: overwrite, merge, remove.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{YOUR_INPUT_ID}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": 1
            },
            {
              "id": "water",
              "value": 0
            }
          ]
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "id": "{YOUR_INPUT_ID}",
      "data": {
        "concepts": [
          {
            "id": "tree",
						"value": 1
          },
          {
            "id": "water",
						"value": 0
          }
        ]
      }
    }
  ],
  "action": "merge"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Bulk update inputs with concepts

You can update an existing input using its Id. This is useful if you'd like to add concepts to an input after its already been added.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_1}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("tree")
                                .setValue(1f)  // 1 means true, this concept is present.
                        )
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("water")
                                .setValue(0f)  // 0 means false, this concept is not present.
                        )
                )
                .build()
        )
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_2}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("animal")
                                .setValue(1f)
                        )
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("fruit")
                                .setValue(0f)
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchInputs(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove.
        inputs: [
            {
                id: "{YOUR_INPUT_ID_1}",
                data: {concepts: [{id: "tree", value: 1}, {id: "water", value: 0}]}
            },
            {
                id: "{YOUR_INPUT_ID_2}",
                data: {concepts: [{id: "animal", value: 1}, {id: "fruit", value: 0}]}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_1}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                        resources_pb2.Concept(id="water", value=0.)  # 0 means false, this concept is not present.
                    ]
                )
            ),
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_2}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="animal", value=1.),
                        resources_pb2.Concept(id="fruit", value=0.)
                    ]
                )
            ),
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
# Supported actions: overwrite, merge, remove.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{YOUR_INPUT_ID_1}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": 1
            },
            {
              "id": "water",
              "value": 0
            }
          ]
        }
      },
      {
        "id": "{YOUR_INPUT_ID_2}",
        "data": {
          "concepts": [
            {
              "id": "animal",
              "value": 1
            },
            {
              "id": "fruit",
              "value": 0
            }
          ]
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "id": "{YOUR_INPUT_ID_1}",
      "data": {
        "concepts": [
          {
            "id": "tree",
            "value": 1
          },
          {
            "id": "water",
            "value": 0
          }
        ]
      }
    },
    {
      "id": "{YOUR_INPUT_ID_2}",
      "data": {
        "concepts": [
          {
            "id": "animal",
            "value": 1
          },
          {
            "id": "fruit",
            "value": 0
          }
        ]
      }
    }
  ],
  "action": "merge"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Delete inputs

### Delete concepts from an input

To remove concepts that were already added to an input, you can do this:

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            // We're removing the concept, so there's no need to specify
                            // the concept value.
                            Concept.newBuilder().setId("tree")
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            // We're removing the concept, so there's no need to specify
                            // the concept value.
                            Concept.newBuilder().setId("tree")
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="remove",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    concepts=[
                        # We're removing the concept, so there's no need to specify
                        # the concept value.
                        resources_pb2.Concept(id="water"),
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
# We're removing the concept, so there's no need to specify
# the concept value.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id":"{YOUR_INPUT_ID}",
        "data": {
            "concepts":[
                {"id":"water"}
            ]
        }
      }
    ],
    "action":"remove"
  }'\
  https://api.clarifai.com/v2/inputs/
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "id":"{YOUR_INPUT_ID}",
      "data": {
          "concepts":[
              {"id":"water"}
          ]
      }
    }
  ],
  "action":"remove"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Bulk delete concepts from a list of inputs

You can bulk delete multiple concepts from a list of inputs:

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_1}")
                .setData(
                    Data.newBuilder()
                        // We're removing the concepts, so there's no need to specify
                        // the concept value.
                        .addConcepts(
                            Concept.newBuilder().setId("tree")
                        )
                        .addConcepts(
                            Concept.newBuilder().setId("water")
                        )
                )
                .build()
        )
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_2}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder().setId("animal")
                        )
                        .addConcepts(
                            Concept.newBuilder().setId("fruit")
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchInputs(
    {
        action: "remove",  // Supported actions: overwrite, merge, remove.
        inputs: [
            {
                id: "{YOUR_INPUT_ID_1}",
                // We're removing the concepts, so there's no need to specify
                // the concept value.
                data: {concepts: [{id: "tree"}, {id: "water"}]}
            },
            {
                id: "{YOUR_INPUT_ID_2}",
                data: {concepts: [{id: "animal"}, {id: "fruit"}]}
            },
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="remove",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_1}",
                data=resources_pb2.Data(
                    concepts=[
                        # We're removing the concepts, so there's no need to specify
                        # the concept value.
                        resources_pb2.Concept(id="tree"),
                        resources_pb2.Concept(id="water"),
                    ]
                )
            ),
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_2}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="animal"),
                        resources_pb2.Concept(id="fruit"),
                    ]
                )
            ),
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
# We're removing the concept, so there's no need to specify
# the concept value.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{YOUR_INPUT_ID_1}",
        "data": {
          "concepts":[
            {
              "id": "tree"
            },
            {
              "id": "water"
            }
          ]
        }
      },
      {
        "id": "{YOUR_INPUT_ID_2}",
        "data": {
          "concepts":[
            {
              "id": "animal"
            },
            {
              "id": "fruit"
            }
          ]
        }
      }
    ],
    "action":"remove"
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "id": "{YOUR_INPUT_ID_1}",
      "data": {
        "concepts":[
          {
            "id": "tree"
          },
          {
            "id": "water"
          }
        ]
      }
    },
    {
      "id": "{YOUR_INPUT_ID_2}",
      "data": {
        "concepts":[
          {
            "id": "animal"
          },
          {
            "id": "fruit"
          }
        ]
      }
    }
  ],
  "action":"remove"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Delete Input By Id

You can delete a single input by id:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteInputResponse = stub.deleteInput(
    DeleteInputRequest.newBuilder()
        .setInputId("{YOUR_INPUT_ID}")
        .build()
);

if (deleteInputResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete input failed, status: " + deleteInputResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteInput(
    {
        input_id: "{YOUR_INPUT_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete input failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_input_response = stub.DeleteInput(
    service_pb2.DeleteInputRequest(input_id="{YOUR_INPUT_ID}"),
    metadata=metadata
)

if delete_input_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete input failed, status: " + delete_input_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs/{YOUR_INPUT_ID}
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const inputId = '{YOUR_INPUT_ID}'
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/inputs/${inputId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Delete a list of inputs

You can also delete multiple inputs in one API call. This will happen asynchronously.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse listInputsResponse = stub.deleteInputs(
    DeleteInputsRequest.newBuilder()
        .addIds("{YOUR_INPUT_ID_1}")
        .addIds("{YOUR_INPUT_ID_2}")
        .build()
);

if (listInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete inputs failed, status: " + listInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteInputs(
    {
        ids: ["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_inputs_response = stub.DeleteInputs(
    service_pb2.DeleteInputsRequest(
        ids=["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"]
    ),
    metadata=metadata
)

if delete_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete inputs failed, status: " + delete_inputs_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "ids":["{YOUR_INPUT_ID_1}","{YOUR_INPUT_ID_2}"]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "ids":["{YOUR_INPUT_ID_1}","{YOUR_INPUT_ID_2}"]
});

const requestOptions = {
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/inputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

