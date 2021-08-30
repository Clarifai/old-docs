---
description: Learn about model prediction parameters.
---

# Prediction Parameters

You can set additional parameters to gain flexibility in the predict operation.

## Select Concepts

By putting this additional parameter on your predict calls, you can receive predict value\(s\) for **only** the concepts that you want to. You can specify particular concepts by either their id and/or their name. The concept names and ids are case sensitive, and so, these must be exact matches.

To retrieve an entire list of concepts from a given model use the `GET /v2/models/{model_id}/output_info` endpoint. Check out the [Advanced Models](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/models.md#get-model-output-info-by-id) section for how to use with any of the API clients!

If you submit a request with not an exact match of the concept id or name, you will receive an invalid model argument error. However, if one or more matches while one or more do not, the API will respond with a Mixed Success.

{% tabs %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the clarifai/main General model.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        ],
        model=resources_pb2.Model(
            output_info=resources_pb2.OutputInfo(
                output_config=resources_pb2.OutputConfig(
                    select_concepts=[
                        # When selecting concepts, value is ignored, so no need to specify it.
                        resources_pb2.Concept(name="train"),
                        resources_pb2.Concept(id="ai_6kTjGfF6")
                    ]
                )
            )
        )
    ),
    metadata=metadata
)
if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# Since we have one input, one output will exist here.
output = post_model_outputs_response.outputs[0]

print("Predicted concepts:")
for concept in output.data.concepts:
    print("%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

///////////////////////////////////////////////////////////////////////////////
// Specifying the Request Data
///////////////////////////////////////////////////////////////////////////////
//
// In the Clarifai platform an image is defined by a special Image object.
// There are several ways in which an Image object can be populated including
// by url and image bytes (base64).
//
$image = new Image([
    'url' => 'https://samples.clarifai.com/dog2.jpeg'
]);

//
// After an Image object is created, a Data object is constructed around it.
// The Data object offers a container that contains additional image independent
// metadata.  In this particular use case, no other metadata is needed to be
// specified.
//
$data = new Data([
    'image' => $image
]);

//
// The Data object is then wrapped in an Input object in order to meet the
// API specification.  Additional fields are available to populate in the Input
// object, but for the purposes of this example we can send in just the
// Data object.
//
$input = new Input([
    'data' => $data
]);

///////////////////////////////////////////////////////////////////////////////
// Specifying Output Configuration 
///////////////////////////////////////////////////////////////////////////////
//
// Output configuration can be specified by the OutputConfig object.  Here
// we specify a concept by both the name and the id for what we want to narrow
// down to in the results.
//
$outputConfig = new OutputConfig([
    'select_concepts' => [
        new Concept(['name' => 'train']),
        new Concept(['id' => 'ai_6kTjGfF6'])
    ]
])

//
// The OutputInfo object is a wrapper around the OutputConfig object
// 
$outputInfo = new OutputInfo([
    'output_config' => $outputConfig
])

//
// The model object is a wrapper around the OutputInfo object.  This is the
// final part needed to define an output configuration.
//
$model = new Model([
    'output_info' => $outputInfo
]);

///////////////////////////////////////////////////////////////////////////////
// Creating the request object 
///////////////////////////////////////////////////////////////////////////////
//
// Finally, the request object itself is created.  This object carries the request
// along with the request status and other metadata related to the request itself.
// In this example we populate:
//    - the `user_app_id` field with the UserAppIDSet constructed above
//    - the `model_id` field with the ID of the model we are referencing
//    - the `inputs` field with an array of input objects constructed above 
//    - the `model` field with the output configuration specified above
//
$request = new PostModelOutputsRequest([
    'user_app_id' => $userDataObject, // This is defined above
    'model_id' => 'aaa03c23b3724a16a56b629203edc62c',  // This is the ID of the publicly available General model.
    'inputs' => [$input],
    'model' => $model
]);

///////////////////////////////////////////////////////////////////////////////
// Making the RPC Call
///////////////////////////////////////////////////////////////////////////////
//
// Once the request object is constructed, we can call the actual request to the
// Clarifai platform.  This uses the opened gRPC client channel to communicate the
// request and then wait for the response.
//
[$response, $status] = $client->PostModelOutputs(
    $request,
    $metadata
)->wait();

///////////////////////////////////////////////////////////////////////////////
// Handling the Response
///////////////////////////////////////////////////////////////////////////////
//
// The response is returned and the first thing we do is check the status of it.
// A successful response will have a status code of 0, otherwise there is some 
// reported error.
//
if ($status->code !== 0) throw new Exception("Error: {$status->details}");

//
// In addition to the RPC response status, there is a Clarifai API status that
// reports if the operationo was a success or failure (not just that the commuunication)
// was successful.
//
if ($response->getStatus()->getCode() != StatusCode::SUCCESS) {
    throw new Exception("Failure response: " . $response->getStatus()->getDescription() . " " .
        $response->getStatus()->getDetails());
}

//
// The output of a successful call can be used in many ways.  In this example,
// we loop through all of the predicted concepts and print them out along with
// their numerical prediction value (confidence).
//
echo "Predicted concepts:\n";
foreach ($response->getOutputs()[0]->getData()->getConcepts() as $concept) {
    echo $concept->getName() . ": " . number_format($concept->getValue(), 2) . "\n";
}
?>
```
{% endtab %}

{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.StatusCode;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the clarifai/main General model.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder().setUrl("https://samples.clarifai.com/metro-north.jpg")
                )
            )
        )
        .setModel(
            Model.newBuilder().setOutputInfo(
                OutputInfo.newBuilder().setOutputConfig(
                    OutputConfig.newBuilder()
                        // When selecting concepts, value is ignored, so no need to specify it.
                        .addSelectConcepts(Concept.newBuilder().setName("train"))
                        .addSelectConcepts(Concept.newBuilder().setId("ai_6kTjGfF6")
                        )
                )
            )
        )
        .build()
);

if (postModelOutputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model outputs failed, status: " + postModelOutputsResponse.getStatus());
}

// Since we have one input, one output will exist here.
Output output = postModelOutputsResponse.getOutputs(0);

System.out.println("Predicted concepts:");
for (Concept concept : output.getData().getConceptsList()) {
    System.out.printf("%s %.2f%n", concept.getName(), concept.getValue());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the clarifai/main General model.
        inputs: [
            {data: {image: {url: "https://samples.clarifai.com/metro-north.jpg"}}}
        ],
        // When selecting concepts, value is ignored, so no need to specify it.
        model: {output_info: {output_config: {select_concepts: [{name: "train"}, {id: "ai_6kTjGfF6"}]}}}
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model outputs failed, status: " + response.status.description);
        }

        // Since we have one input, one output will exist here.
        const output = response.outputs[0];

        console.log("Predicted concepts:");
        for (const concept of output.data.concepts) {
            console.log(concept.name + " " + concept.value);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H 'authorization: Key YOUR_API_KEY' \
  -H 'content -type: application/json' \
  -d '{
  "inputs": [
    {
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/metro-north.jpg"
        }
      }
    }
  ],
  "model": {
    "output_info": {
      "output_config": {
        "select_concepts": [
          {"name": "train"},
          {"id": "ai_6kTjGfF6"}
        ]
      }
    }
  }
}'\
https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs

# Above is model ID of the publicly available General model.
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
          "url": "https://samples.clarifai.com/metro-north.jpg"
        }
      }
    }
  ],
  "model": {
    "output_info": {
      "output_config": {
        "select_concepts": [
          {"name": "train"},
          {"id": "ai_6kTjGfF6"}
        ]
      }
    }
  }
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/outputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
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
  "outputs": [
    {
      "id": "c8abf5cbe52746efa9df8a2319d49d0a",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-06-27T13:31:57.493797045Z",
      "model": {
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "name": "general-v1.3",
        "created_at": "2016-03-09T17:11:39.608845Z",
        "app_id": "main",
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept",
          "type_ext": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T01:19:12.147644Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "c613b3254da34382b2fca65365da7c49",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "ai_HLmqFqBf",
            "name": "train",
            "value": 0.9989112,
            "app_id": "main"
          },
          {
            "id": "ai_6kTjGfF6",
            "name": "station",
            "value": 0.992573,
            "app_id": "main"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Maximum Concepts

Setting the max concepts parameter will customize how many concepts and their corresponding probability scores the predict endpoint will return. If not specified, the predict endpoint will return the top 20 concepts. You can currently set the max concepts parameter to any number in the range: \[1-200\]. If your use case requires more concepts, please contact [Support](mailto:support@clarifai.com).

{% tabs %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the clarifai/main General model.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        ],
        model=resources_pb2.Model(
            output_info=resources_pb2.OutputInfo(
                output_config=resources_pb2.OutputConfig(
                    max_concepts=3
                )
            )
        )
    ),
    metadata=metadata
)
if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# Since we have one input, one output will exist here.
output = post_model_outputs_response.outputs[0]

print("Predicted concepts:")
for concept in output.data.concepts:
    print("%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

///////////////////////////////////////////////////////////////////////////////
// Specifying the Request Data
///////////////////////////////////////////////////////////////////////////////
//
// In the Clarifai platform an image is defined by a special Image object.
// There are several ways in which an Image object can be populated including
// by url and image bytes (base64).
//
$image = new Image([
    'url' => 'https://samples.clarifai.com/dog2.jpeg'
]);

//
// After an Image object is created, a Data object is constructed around it.
// The Data object offers a container that contains additional image independent
// metadata.  In this particular use case, no other metadata is needed to be
// specified.
//
$data = new Data([
    'image' => $image
]);

//
// The Data object is then wrapped in an Input object in order to meet the
// API specification.  Additional fields are available to populate in the Input
// object, but for the purposes of this example we can send in just the
// Data object.
//
$input = new Input([
    'data' => $data
]);

///////////////////////////////////////////////////////////////////////////////
// Specifying Output Configuration 
///////////////////////////////////////////////////////////////////////////////
//
// Output configuration can be specified by the OutputConfig object.  Here
// we specify the max number of concepts to return at 3.
//
$outputConfig = new OutputConfig([
    'max_concepts' => 3
])

//
// The OutputInfo object is a wrapper around the OutputConfig object
// 
$outputInfo = new OutputInfo([
    'output_config' => $outputConfig
])

//
// The model object is a wrapper around the OutputInfo object.  This is the
// final part needed to define an output configuration.
//
$model = new Model([
    'output_info' => $outputInfo
]);

///////////////////////////////////////////////////////////////////////////////
// Creating the request object 
///////////////////////////////////////////////////////////////////////////////
//
// Finally, the request object itself is created.  This object carries the request
// along with the request status and other metadata related to the request itself.
// In this example we populate:
//    - the `user_app_id` field with the UserAppIDSet constructed above
//    - the `model_id` field with the ID of the model we are referencing
//    - the `inputs` field with an array of input objects constructed above 
//    - the `model` field with the output configuration specified above
//
$request = new PostModelOutputsRequest([
    'user_app_id' => $userDataObject, // This is defined above
    'model_id' => 'aaa03c23b3724a16a56b629203edc62c',  // This is the ID of the publicly available General model.
    'inputs' => [$input],
    'model' => $model
]);

///////////////////////////////////////////////////////////////////////////////
// Making the RPC Call
///////////////////////////////////////////////////////////////////////////////
//
// Once the request object is constructed, we can call the actual request to the
// Clarifai platform.  This uses the opened gRPC client channel to communicate the
// request and then wait for the response.
//
[$response, $status] = $client->PostModelOutputs(
    $request,
    $metadata
)->wait();

///////////////////////////////////////////////////////////////////////////////
// Handling the Response
///////////////////////////////////////////////////////////////////////////////
//
// The response is returned and the first thing we do is check the status of it.
// A successful response will have a status code of 0, otherwise there is some 
// reported error.
//
if ($status->code !== 0) throw new Exception("Error: {$status->details}");

//
// In addition to the RPC response status, there is a Clarifai API status that
// reports if the operationo was a success or failure (not just that the commuunication)
// was successful.
//
if ($response->getStatus()->getCode() != StatusCode::SUCCESS) {
    throw new Exception("Failure response: " . $response->getStatus()->getDescription() . " " .
        $response->getStatus()->getDetails());
}

//
// The output of a successful call can be used in many ways.  In this example,
// we loop through all of the predicted concepts and print them out along with
// their numerical prediction value (confidence).
//
echo "Predicted concepts:\n";
foreach ($response->getOutputs()[0]->getData()->getConcepts() as $concept) {
    echo $concept->getName() . ": " . number_format($concept->getValue(), 2) . "\n";
}
?>
```
{% endtab %}

{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the clarifai/main General model.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder().setUrl("https://samples.clarifai.com/metro-north.jpg")
                )
            )
        )
        .setModel(
            Model.newBuilder().setOutputInfo(
                OutputInfo.newBuilder().setOutputConfig(
                    OutputConfig.newBuilder().setMaxConcepts(3)
                )
            )
        )
        .build()
);

if (postModelOutputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model outputs failed, status: " + postModelOutputsResponse.getStatus());
}

// Since we have one input, one output will exist here.
Output output = postModelOutputsResponse.getOutputs(0);

System.out.println("Predicted concepts:");
for (Concept concept : output.getData().getConceptsList()) {
    System.out.printf("%s %.2f%n", concept.getName(), concept.getValue());
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the clarifai/main General model
        inputs: [
            {data: {image: {url: "https://samples.clarifai.com/metro-north.jpg"}}}
        ],
        model: {output_info: {output_config: {max_concepts: 3}}}
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model outputs failed, status: " + response.status.description);
        }

        // Since we have one input, one output will exist here.
        const output = response.outputs[0];

        console.log("Predicted concepts:");
        for (const concept of output.data.concepts) {
            console.log(concept.name + " " + concept.value);
        }
    }
);
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
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      }
    ],
    "model":{
      "output_info":{
        "output_config":{
          "max_concepts": 3
        }
      }
    }
  }'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs
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
          "url": "https://samples.clarifai.com/metro-north.jpg"
        }
      }
    }
  ],
  "model":{
    "output_info":{
      "output_config":{
        "max_concepts": 3
      }
    }
  }
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/outputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
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
  "outputs": [
    {
      "id": "c8c400234b0d47df9084857df0d69efb",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-06-15T16:09:48.984389535Z",
      "model": {
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "name": "general-v1.3",
        "created_at": "2016-02-26T23:38:40.086101Z",
        "app_id": "main",
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept",
          "type_ext": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T00:58:55.915745Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "fd99d9e345f3495a8bd2802151d09efa",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "ai_HLmqFqBf",
            "name": "train",
            "value": 0.9989112,
            "app_id": "main"
          },
          {
            "id": "ai_fvlBqXZR",
            "name": "railway",
            "value": 0.9975532,
            "app_id": "main"
          },
          {
            "id": "ai_Xxjc3MhT",
            "name": "transportation system",
            "value": 0.9959158,
            "app_id": "main"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Minimum Prediction Value

This parameter lets you set a minimum probability threshold for the outputs you want to view for the Predict operation. For example if you want to see all concepts with a probability score of .90 or higher, this parameter will allow you to accomplish that. Also note that if you don't specify the number of max concepts, you will only see the top 20. If your result can contain more values you will have to increase the number of maximum concepts as well.

{% tabs %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the clarifai/main General model.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        ],
        model=resources_pb2.Model(
            output_info=resources_pb2.OutputInfo(
                output_config=resources_pb2.OutputConfig(
                    min_value=0.95
                )
            )
        )
    ),
    metadata=metadata
)
if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# Since we have one input, one output will exist here.
output = post_model_outputs_response.outputs[0]

print("Predicted concepts:")
for concept in output.data.concepts:
    print("%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

///////////////////////////////////////////////////////////////////////////////
// Specifying the Request Data
///////////////////////////////////////////////////////////////////////////////
//
// In the Clarifai platform an image is defined by a special Image object.
// There are several ways in which an Image object can be populated including
// by url and image bytes (base64).
//
$image = new Image([
    'url' => 'https://samples.clarifai.com/dog2.jpeg'
]);

//
// After an Image object is created, a Data object is constructed around it.
// The Data object offers a container that contains additional image independent
// metadata.  In this particular use case, no other metadata is needed to be
// specified.
//
$data = new Data([
    'image' => $image
]);

//
// The Data object is then wrapped in an Input object in order to meet the
// API specification.  Additional fields are available to populate in the Input
// object, but for the purposes of this example we can send in just the
// Data object.
//
$input = new Input([
    'data' => $data
]);

///////////////////////////////////////////////////////////////////////////////
// Specifying Output Configuration 
///////////////////////////////////////////////////////////////////////////////
//
// Output configuration can be specified by the OutputConfig object.  Here
// we specify the minimum threshold value to 0.95.
//
$outputConfig = new OutputConfig([
    'min_value' => 0.95
])

//
// The OutputInfo object is a wrapper around the OutputConfig object
// 
$outputInfo = new OutputInfo([
    'output_config' => $outputConfig
])

//
// The model object is a wrapper around the OutputInfo object.  This is the
// final part needed to define an output configuration.
//
$model = new Model([
    'output_info' => $outputInfo
]);

///////////////////////////////////////////////////////////////////////////////
// Creating the request object 
///////////////////////////////////////////////////////////////////////////////
//
// Finally, the request object itself is created.  This object carries the request
// along with the request status and other metadata related to the request itself.
// In this example we populate:
//    - the `user_app_id` field with the UserAppIDSet constructed above
//    - the `model_id` field with the ID of the model we are referencing
//    - the `inputs` field with an array of input objects constructed above 
//    - the `model` field with the output configuration specified above
//
$request = new PostModelOutputsRequest([
    'user_app_id' => $userDataObject, // This is defined above
    'model_id' => 'aaa03c23b3724a16a56b629203edc62c',  // This is the ID of the publicly available General model.
    'inputs' => [$input],
    'model' => $model
]);

///////////////////////////////////////////////////////////////////////////////
// Making the RPC Call
///////////////////////////////////////////////////////////////////////////////
//
// Once the request object is constructed, we can call the actual request to the
// Clarifai platform.  This uses the opened gRPC client channel to communicate the
// request and then wait for the response.
//
[$response, $status] = $client->PostModelOutputs(
    $request,
    $metadata
)->wait();

///////////////////////////////////////////////////////////////////////////////
// Handling the Response
///////////////////////////////////////////////////////////////////////////////
//
// The response is returned and the first thing we do is check the status of it.
// A successful response will have a status code of 0, otherwise there is some 
// reported error.
//
if ($status->code !== 0) throw new Exception("Error: {$status->details}");

//
// In addition to the RPC response status, there is a Clarifai API status that
// reports if the operationo was a success or failure (not just that the commuunication)
// was successful.
//
if ($response->getStatus()->getCode() != StatusCode::SUCCESS) {
    throw new Exception("Failure response: " . $response->getStatus()->getDescription() . " " .
        $response->getStatus()->getDetails());
}

//
// The output of a successful call can be used in many ways.  In this example,
// we loop through all of the predicted concepts and print them out along with
// their numerical prediction value (confidence).
//
echo "Predicted concepts:\n";
foreach ($response->getOutputs()[0]->getData()->getConcepts() as $concept) {
    echo $concept->getName() . ": " . number_format($concept->getValue(), 2) . "\n";
}
?>
```
{% endtab %}

{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the clarifai/main General model.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder().setUrl("https://samples.clarifai.com/metro-north.jpg")
                )
            )
        )
        .setModel(
            Model.newBuilder().setOutputInfo(
                OutputInfo.newBuilder().setOutputConfig(
                    OutputConfig.newBuilder().setMinValue(0.95f)
                )
            )
        )
        .build()
);

if (postModelOutputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model outputs failed, status: " + postModelOutputsResponse.getStatus());
}

// Since we have one input, one output will exist here.
Output output = postModelOutputsResponse.getOutputs(0);

System.out.println("Predicted concepts:");
for (Concept concept : output.getData().getConceptsList()) {
    System.out.printf("%s %.2f%n", concept.getName(), concept.getValue());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the clarifai/main General model
        inputs: [
            {data: {image: {url: "https://samples.clarifai.com/metro-north.jpg"}}}
        ],
        model: {output_info: {output_config: {min_value: 0.95}}}
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model outputs failed, status: " + response.status.description);
        }

        // Since we have one input, one output will exist here.
        const output = response.outputs[0];

        console.log("Predicted concepts:");
        for (const concept of output.data.concepts) {
            console.log(concept.name + " " + concept.value);
        }
    }
);
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
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      }
    ],
    "model":{
      "output_info":{
        "output_config":{
          "min_value": 0.95
        }
      }
    }
  }'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs
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
          "url": "https://samples.clarifai.com/metro-north.jpg"
        }
      }
    }
  ],
  "model":{
    "output_info":{
      "output_config":{
        "min_value": 0.95
      }
    }
  }
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/outputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
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
  "outputs": [
    {
      "id": "b2027bccf4964d03b062ce653cff85b6",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-06-15T20:22:05.841603659Z",
      "model": {
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "name": "general-v1.3",
        "created_at": "2016-02-26T23:38:40.086101Z",
        "app_id": "main",
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept",
          "type_ext": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T00:58:55.915745Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "f7640568d37f47fbba9d6fdc892ec64d",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "ai_HLmqFqBf",
            "name": "train",
            "value": 0.9989112,
            "app_id": "main"
          },
          {
            "id": "ai_fvlBqXZR",
            "name": "railway",
            "value": 0.9975532,
            "app_id": "main"
          },
          {
            "id": "ai_Xxjc3MhT",
            "name": "transportation system",
            "value": 0.9959158,
            "app_id": "main"
          },
          {
            "id": "ai_6kTjGfF6",
            "name": "station",
            "value": 0.992573,
            "app_id": "main"
          },
          {
            "id": "ai_RRXLczch",
            "name": "locomotive",
            "value": 0.992556,
            "app_id": "main"
          },
          {
            "id": "ai_VRmbGVWh",
            "name": "travel",
            "value": 0.98789215,
            "app_id": "main"
          },
          {
            "id": "ai_SHNDcmJ3",
            "name": "subway system",
            "value": 0.9816359,
            "app_id": "main"
          },
          {
            "id": "ai_jlb9q33b",
            "name": "commuter",
            "value": 0.9712483,
            "app_id": "main"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## By Model Version ID

Every time you train a custom model, it creates a new model version. By specifying `version id` in your predict call, you can continue to predict on a previous version, for consistent prediction results. Clarifai also updates our pre-built models on a regular basis.

If you are looking for consistent results from your predict calls, use `version id`. If the model `version id` is not specified, predict will default to the most current model.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the clarifai/main General model.
        .setVersionId("aa7f35c01e0642fda5cf400f543e7c40")  // This is optional. Defaults to the latest model version.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder().setUrl("https://samples.clarifai.com/metro-north.jpg")
                )
            )
        )
        .build()
);

if (postModelOutputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model outputs failed, status: " + postModelOutputsResponse.getStatus());
}

// Since we have one input, one output will exist here.
Output output = postModelOutputsResponse.getOutputs(0);

System.out.println("Predicted concepts:");
for (Concept concept : output.getData().getConceptsList()) {
    System.out.printf("%s %.2f%n", concept.getName(), concept.getValue());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the clarifai/main General model
        version_id: "aa7f35c01e0642fda5cf400f543e7c40",  // This is optional. Defaults to the latest model version.
        inputs: [
            {data: {image: {url: "https://samples.clarifai.com/metro-north.jpg"}}}
        ],
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model outputs failed, status: " + response.status.description);
        }

        // Since we have one input, one output will exist here.
        const output = response.outputs[0];

        console.log("Predicted concepts:");
        for (const concept of output.data.concepts) {
            console.log(concept.name + " " + concept.value);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the clarifai/main General model.
        version_id="aa7f35c01e0642fda5cf400f543e7c40",  # This is optional. Defaults to the latest model version.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# Since we have one input, one output will exist here.
output = post_model_outputs_response.outputs[0]

print("Predicted concepts:")
for concept in output.data.concepts:
    print("\t%s %.2f" % (concept.name, concept.value))
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
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/versions/aa7f35c01e0642fda5cf400f543e7c40/outputs

# Above is model ID of the publicly available General model.
# Version ID is optional. It defaults to the latest model version.
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
          "url": "https://samples.clarifai.com/metro-north.jpg"
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

// NOTE: MODEL_VERSION_ID is optional, you can also call prediction with the MODEL_ID only
// https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/outputs
// this will default to the latest version_id

fetch("https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/versions/{YOUR_MODEL_VERSION_ID}outputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

