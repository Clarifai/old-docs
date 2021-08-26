---
description: Make predictions on image inputs
---

# Images

## Via URL

To get predictions for an input, you need to supply an image and the model you'd like to get predictions from. You can supply an image either with a publicly accessible URL or by directly sending bytes. You can send up to 128 images in one API call. You specify the model you'd like to use with the `{model-id}` parameter.

Below is an example of how you would send image URLs and receive back predictions from the `general` model.

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
    print("%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

use Clarifai\Api\Data;
use Clarifai\Api\Image;
use Clarifai\Api\Input;
use Clarifai\Api\PostModelOutputsRequest;
use Clarifai\Api\UserAppIDSet;
use Clarifai\Api\Status\StatusCode;

// The Clarifai PHP Client includes an autoload.php helper file that needs to be included
require 'vendor/autoload.php';

use Clarifai\ClarifaiClient;

// Construct the actual gRPC client object
$client = ClarifaiClient::grpc();

// Specify the Authorization key.  This should be changed to your Personal Access Token.
// Example: $metadata = ['Authorization' => ['Key 123456789123456789']]; 
$metadata = ['Authorization' => ['Key {YOUR PERSONAL ACCESS TOKEN HERE}']]; // Using the PAT in these examples

//
// A UserAppIDSet object is needed for the rpc call.  This object cotnains
// two pieces of information: the user id and the app id.  Both of these are
// specified as string values.
//
$userDataObject = new UserAppIDSet([
    'user_id' => '{YOUR USER NAME HERE}', // This is your user id
    'app_id' => '{YOUR APPLICATION ID HERE}' // This is the app id which contains the model of interest
]);

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

//
// Once the request object is constructed, we can call the actual request to the
// Clarifai platform.  This uses the opened gRPC client channel to communicate the
// request and then wait for the response.
//
[$response, $status] = $client->PostModelOutputs(
    $request,
    $metadata
)->wait();

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
        model_id: "{THE_MODEL_ID}",
        version_id: "{THE_MODEL_VERSION_ID}",  // This is optional. Defaults to the latest model version.
        inputs: [
            {data: {image: {url: "https://samples.clarifai.com/metro-north.jpg"}}}
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
            "image": {
              "url": "https://samples.clarifai.com/metro-north.jpg"
            }
          }
        }
      ]
    }'
    https://api.clarifai.com/v2/models/{THE_MODEL_ID}/versions/{THE_MODEL_VERSION_ID}/outputs
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
      "id": "ea68cac87c304b28a8046557062f34a0",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2016-11-22T16:50:25Z",
      "model": {
        "name": "general-v1.3",
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "created_at": "2016-03-09T17:11:39Z",
        "app_id": null,
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T01:19:12Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "ea68cac87c304b28a8046557062f34a0",
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
            "app_id": null,
            "value": 0.9989112
          },
          {
            "id": "ai_fvlBqXZR",
            "name": "railway",
            "app_id": null,
            "value": 0.9975532
          },
          {
            "id": "ai_Xxjc3MhT",
            "name": "transportation system",
            "app_id": null,
            "value": 0.9959158
          },
          {
            "id": "ai_6kTjGfF6",
            "name": "station",
            "app_id": null,
            "value": 0.992573
          },
          {
            "id": "ai_RRXLczch",
            "name": "locomotive",
            "app_id": null,
            "value": 0.992556
          },
          {
            "id": "ai_VRmbGVWh",
            "name": "travel",
            "app_id": null,
            "value": 0.98789215
          },
          {
            "id": "ai_SHNDcmJ3",
            "name": "subway system",
            "app_id": null,
            "value": 0.9816359
          },
          {
            "id": "ai_jlb9q33b",
            "name": "commuter",
            "app_id": null,
            "value": 0.9712483
          },
          {
            "id": "ai_46lGZ4Gm",
            "name": "railroad track",
            "app_id": null,
            "value": 0.9690325
          },
          {
            "id": "ai_tr0MBp64",
            "name": "traffic",
            "app_id": null,
            "value": 0.9687052
          },
          {
            "id": "ai_l4WckcJN",
            "name": "blur",
            "app_id": null,
            "value": 0.9667078
          },
          {
            "id": "ai_2gkfMDsM",
            "name": "platform",
            "app_id": null,
            "value": 0.9624243
          },
          {
            "id": "ai_CpFBRWzD",
            "name": "urban",
            "app_id": null,
            "value": 0.960752
          },
          {
            "id": "ai_786Zr311",
            "name": "no person",
            "app_id": null,
            "value": 0.95864904
          },
          {
            "id": "ai_6lhccv44",
            "name": "business",
            "app_id": null,
            "value": 0.95720303
          },
          {
            "id": "ai_971KsJkn",
            "name": "track",
            "app_id": null,
            "value": 0.9494642
          },
          {
            "id": "ai_WBQfVV0p",
            "name": "city",
            "app_id": null,
            "value": 0.94089437
          },
          {
            "id": "ai_dSCKh8xv",
            "name": "fast",
            "app_id": null,
            "value": 0.9399334
          },
          {
            "id": "ai_TZ3C79C6",
            "name": "road",
            "app_id": null,
            "value": 0.93121606
          },
          {
            "id": "ai_VSVscs9k",
            "name": "terminal",
            "app_id": null,
            "value": 0.9230834
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Via bytes

Below is an example of how you would send the bytes of an image and receive back predictions from the `general` model.

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
                    image=resources_pb2.Image(
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

use Clarifai\Api\Data;
use Clarifai\Api\Image;
use Clarifai\Api\Input;
use Clarifai\Api\PostModelOutputsRequest;
use Clarifai\Api\UserAppIDSet;
use Clarifai\Api\Status\StatusCode;

// The Clarifai PHP Client includes an autoload.php helper file that needs to be included
require 'vendor/autoload.php';

use Clarifai\ClarifaiClient;

// Construct the actual gRPC client object
$client = ClarifaiClient::grpc();

// Specify the Authorization key.  This should be changed to your Personal Access Token.
// Example: $metadata = ['Authorization' => ['Key 123456789123456789']]; 
$metadata = ['Authorization' => ['Key {YOUR PERSONAL ACCESS TOKEN HERE}']]; // Using the PAT in these examples

//
// For this example, the bytes of an image are needed and can be read in
// using PHP provided functions.
//
$image = "https://samples.clarifai.com/dog2.jpeg";
$imageData = file_get_contents($image); // Get the image data from the URL

//
// A UserAppIDSet object is needed for the rpc call.  This object cotnains
// two pieces of information: the user id and the app id.  Both of these are
// specified as string values.
//
$userDataObject = new UserAppIDSet([
    'user_id' => '{YOUR USER NAME HERE}', // This is your user id
    'app_id' => '{YOUR APPLICATION ID HERE}' // This is the app id which contains the model of interest
]);

//
// In the Clarifai platform an image is defined by a special Image object.
// There are several ways in which an Image object can be populated including
// by url and image bytes (base64).
//
$image = new Image([
    'base64' => $imageData
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

//
// Once the request object is constructed, we can call the actual request to the
// Clarifai platform.  This uses the opened gRPC client channel to communicate the
// request and then wait for the response.
//
[$response, $status] = $client->PostModelOutputs(
    $request,
    $metadata
)->wait();

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
            {data: {image: {base64: imageBytes}}}
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
          "image": {
            "base64": "'"$(base64 /home/user/image.jpeg)"'"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/{THE_MODEL_ID}/outputs

// Larger Files (Greater than 195 KB)

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- https://api.clarifai.com/v2/models/{model-id}/outputs << FILEIN
  {
    "inputs": [
      {
        "data": {
          "image": {
            "base64": "$(base64 /home/user/image.png)"
          }
        }
      }
    ]
  }
FILEIN
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
      "id": "e1cf385843b94c6791bbd9f2654db5c0",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2016-11-22T16:59:23Z",
      "model": {
        "name": "general-v1.3",
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "created_at": "2016-03-09T17:11:39Z",
        "app_id": null,
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T01:19:12Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "e1cf385843b94c6791bbd9f2654db5c0",
        "data": {
          "image": {
            "url": "https://s3.amazonaws.com/clarifai-api/img/prod/b749af061d564b829fb816215f6dc832/e11c81745d6d42a78ef712236023df1c.jpeg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "ai_l4WckcJN",
            "name": "blur",
            "app_id": null,
            "value": 0.9973569
          },
          {
            "id": "ai_786Zr311",
            "name": "no person",
            "app_id": null,
            "value": 0.98865616
          },
          {
            "id": "ai_JBPqff8z",
            "name": "art",
            "app_id": null,
            "value": 0.986006
          },
          {
            "id": "ai_5rD7vW4j",
            "name": "wallpaper",
            "app_id": null,
            "value": 0.9722556
          },
          {
            "id": "ai_sTjX6dqC",
            "name": "abstract",
            "app_id": null,
            "value": 0.96476805
          },
          {
            "id": "ai_Dm5GLXnB",
            "name": "illustration",
            "app_id": null,
            "value": 0.922542
          },
          {
            "id": "ai_5xjvC0Tj",
            "name": "background",
            "app_id": null,
            "value": 0.8775655
          },
          {
            "id": "ai_tBcWlsCp",
            "name": "nature",
            "app_id": null,
            "value": 0.87474406
          },
          {
            "id": "ai_rJGvwlP0",
            "name": "insubstantial",
            "app_id": null,
            "value": 0.8196385
          },
          {
            "id": "ai_2Bh4VMrb",
            "name": "artistic",
            "app_id": null,
            "value": 0.8142488
          },
          {
            "id": "ai_mKzmkKDG",
            "name": "Christmas",
            "app_id": null,
            "value": 0.7996079
          },
          {
            "id": "ai_RQccV41p",
            "name": "woman",
            "app_id": null,
            "value": 0.7955615
          },
          {
            "id": "ai_20SCBBZ0",
            "name": "vector",
            "app_id": null,
            "value": 0.7775099
          },
          {
            "id": "ai_4sJLn6nX",
            "name": "dark",
            "app_id": null,
            "value": 0.7715479
          },
          {
            "id": "ai_5Kp5FMJw",
            "name": "still life",
            "app_id": null,
            "value": 0.7657637
          },
          {
            "id": "ai_LM64MDHs",
            "name": "shining",
            "app_id": null,
            "value": 0.7542407
          },
          {
            "id": "ai_swtdphX8",
            "name": "love",
            "app_id": null,
            "value": 0.74926054
          },
          {
            "id": "ai_h45ZTxZl",
            "name": "square",
            "app_id": null,
            "value": 0.7449074
          },
          {
            "id": "ai_cMfj16kJ",
            "name": "design",
            "app_id": null,
            "value": 0.73926914
          },
          {
            "id": "ai_LxrzLJmf",
            "name": "bright",
            "app_id": null,
            "value": 0.73790145
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

