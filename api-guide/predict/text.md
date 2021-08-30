---
description: Make predictions on passages of text
---

# Text

### Make text predictions via URL

You can make predictions on passages of text hosted on the web

{% tabs %}
{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="{THE_MODEL_ID}",
        version_id="{THE_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    text=resources_pb2.Text(
                        base64=file_bytes
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
// In the Clarifai platform a text is defined by a special Text object.
// There are several ways in which a Text object can be populated including
// by url and raw string.
//
$text = new Text([
    'url' => 'https://samples.clarifai.com/negative_sentence_12.txt'
]);

//
// After an Text object is created, a Data object is constructed around it.
// The Data object offers a container that contains additional text independent
// metadata.  In this particular use case, no other metadata is needed to be
// specified.
//
$data = new Data([
    'text' => $text
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
// Creating the request object 
///////////////////////////////////////////////////////////////////////////////
//
// Finally, the request object itself is created.  This object carries the request
// along with the request status and other metadata related to the request itself.
// In this example we populate:
//    - the `user_app_id` field with the UserAppIDSet constructed above
//    - the `model_id` field with the ID of the model we are referencing
//    - the `inputs` field with an array of input objects constructed above 
//
$request = new PostModelOutputsRequest([
    'user_app_id' => $userDataObject, // This is defined above
    'model_id' => 'aaa03c23b3724a16a56b629203edc62c',  // This is the ID of the publicly available General model.
    'inputs' => [$input]
]);

///////////////////////////////////////////////////////////////////////////////
// Making the RPC call
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
        .setModelId("{THE_MODEL_ID}")
        .setVersionId("{THE_MODEL_VERSION_ID")  // This is optional. Defaults to the latest model version.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setText(
                    Text.newBuilder().setUrl("https://samples.clarifai.com/negative_sentence_12.txt")
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
        model_id: "{THE_MODEL_ID}",
        version_id: "{THE_MODEL_VERSION_ID}",  // This is optional. Defaults to the latest model version.
        inputs: [
            {data: {text: {url: "https://samples.clarifai.com/negative_sentence_12.txt"}}}
        ]
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
curl -X POST
    -H 'Authorization: Key YOUR_API_KEY'
    -H "Content-Type: application/json"
    -d '
    {
      "inputs": [
        {
          "data": {
            "text": {
              "url": "https://samples.clarifai.com/negative_sentence_12.txt"
            }
          }
        }
      ]
    }'
    https://api.clarifai.com/v2/models/{THE_MODEL_ID}/versions/{THE_MODEL_VERSION_ID}/outputs
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
        "text": {
          "url": "https://samples.clarifai.com/negative_sentence_12.txt"
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

fetch("https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/versions/{MODEL_VERSION_ID}/outputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Make text predictions on local text files

Make predictions based on local text files.

{% tabs %}
{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

with open("{YOUR_IMAGE_FILE_LOCATION}", "rb") as f:
    file_bytes = f.read()

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="{THE_MODEL_ID}",
        version_id="{THE_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    text=resources_pb2.Text(
                        raw="Butchart Gardens contains over 900 varieties of plants."
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
    print("%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import com.google.protobuf.ByteString;
import java.io.File;
import java.nio.file.Files;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("{THE_MODEL_ID}")
        .setVersionId("{THE_MODEL_VERSION_ID")  // This is optional. Defaults to the latest model version.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setText(
                    Text.newBuilder()
                        .setRaw(ByteString.copyFrom(Files.readAllBytes(
                            new File("{YOUR_IMAGE_FILE_LOCATION}").toPath()
                        )))
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

const fs = require("fs");
const imageBytes = fs.readFileSync("{YOUR_IMAGE_FILE_LOCATION}");

stub.PostModelOutputs(
    {
        model_id: "{THE_MODEL_ID}",
        version_id: "{THE_MODEL_VERSION_ID}",  // This is optional. Defaults to the latest model version.
        inputs: [
            {data: {text: {raw: textFile}}}
        ]
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
// Smaller files (195 KB or less)

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "text": {
            "raw": "'"$(raw /home/user/image.jpeg)"'"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/{THE_MODEL_ID}/outputs
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
        "text": {
          "raw": "{YOUR_RAW_TEXT}"
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

fetch("https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/versions/{MODEL_VERSION_ID}/outputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

