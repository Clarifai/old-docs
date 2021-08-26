---
description: Make predictions on video inputs
---

# Video

With a video input, the Predict API response will return a list of predicted concepts for every frame of a video. By default, video is processed at 1 frame per second \(but this is configurable in the predict request\). This means you will receive a list of concepts for every second of your video.

You can run Predict on your video using a select number of [Clarifai Models](https://www.clarifai.com/models). The models that are currently supported are: Apparel, Food, General, NSFW, Travel, and Wedding. You make an API call by providing the `{model-id}` parameter and your data parameter is `video` instead of `image`.

**Video limits**

The Predict API has limits to the length and size it can support. A video, uploaded through URL, can be anywhere up to 80MB in size or 10mins in length. When a video is sent through by bytes, the Predict API can support 10MB in size.

If your video exceeds the limits, please follow our [tutorial](https://www.clarifai.com/blog/splitting-video-into-smaller-pieces) on how to break up a large video into smaller components, and send those into the Video API. Otherwise, the processing will time out and you will receive an error response.

**Via URL**

Below is an example of how you would send video URLs and receive back predictions from the `general` model.

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
                    video=resources_pb2.Video(
                        url="https://samples.clarifai.com/beer.mp4"
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

# A separate prediction is available for each "frame".
for frame in output.data.frames:
    print("Predicted concepts on frame " + str(frame.frame_info.time) + ":")
    for concept in frame.data.concepts:
        print("\t%s %.2f" % (concept.name, concept.value))
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
// In the Clarifai platform a video is defined by a special Video object.
// There are several ways in which an Video object can be populated including
// by url and video bytes (base64).
//
$video = new Video([
    'url' => 'https://samples.clarifai.com/beer.mp4'
]);

//
// After a Video object is created, a Data object is constructed around it.
// The Data object offers a container that contains additional video independent
// metadata.  In this particular use case, no other metadata is needed to be
// specified.
//
$data = new Data([
    'video' => $video
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
// we loop through all of the frames of the video and print out the predicted 
// concepts for each along with their numerical prediction value (confidence).
//
foreach ($output->getData()->getFrames() as $frame) {
    echo "Predicted concepts on frame " . $frame->getFrameInfo()->getTime() . ":";
    foreach ($frame->getData()->getConcepts() as $concept) {
        echo "   " . $concept->getName() . ": " . number_format($concept->getValue(), 2) . "\n";
    }
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
                Data.newBuilder().setVideo(
                    Video.newBuilder().setUrl("https://samples.clarifai.com/beer.mp4")
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

// A separate prediction is available for each "frame".
for (Frame frame : output.getData().getFramesList()) {
    System.out.println("Predicted concepts on frame " + frame.getFrameInfo().getTime() + ":");
    for (Concept concept : frame.getData().getConceptsList()) {
        System.out.printf("\t%s %.2f%n", concept.getName(), concept.getValue());
    }
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
            {data: {video: {url: "https://samples.clarifai.com/beer.mp4"}}}
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
        const output = response.outputs[0]

        // A separate prediction is available for each "frame".
        for (const frame of output.data.frames) {
            console.log("Predicted concepts on frame " + frame.frame_info.time + ":");
            for (const concept of frame.data.concepts) {
                console.log("\t" + concept.name + " " + concept.value);
            }
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
          "video": {
            "url": "https://samples.clarifai.com/beer.mp4"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/{THE_MODEL_ID}/versions/{THE_MODEL_VERSION_ID}/outputs

# Model version ID is optional. It defaults to the latest model version.
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
      "id": "d8234da5d1f04ca8a2e13e34d51f9b85",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-06-28T14:58:41.835370141Z",
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
        "id": "f0fc1a005f124d389da4d80823a3125b",
        "data": {
          "video": {
            "url": "https://samples.clarifai.com/beer.mp4"
          }
        }
      },
      "data": {
        "frames": [
          {
            "frame_info": {
              "index": 0,
              "time": 0
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.98658466,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": "main"
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.9783862,
                  "app_id": "main"
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.97157896,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.96628696,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.95581007,
                  "app_id": "main"
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.92861253,
                  "app_id": "main"
                },
                {
                  "id": "ai_7vR9zv7l",
                  "name": "bubble",
                  "value": 0.9082134,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9020835,
                  "app_id": "main"
                },
                {
                  "id": "ai_7Xg5SQRW",
                  "name": "luxury",
                  "value": 0.8990605,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.89708906,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": "main"
                },
                {
                  "id": "ai_7qwGxLch",
                  "name": "gold",
                  "value": 0.8892093,
                  "app_id": "main"
                },
                {
                  "id": "ai_wmbvr5TG",
                  "name": "celebration",
                  "value": 0.88606626,
                  "app_id": "main"
                },
                {
                  "id": "ai_4lvjn8qv",
                  "name": "closeup",
                  "value": 0.881963,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": "main"
                },
                {
                  "id": "ai_12dz73B9",
                  "name": "bottle",
                  "value": 0.86288416,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.86252767,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.86069393,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 1,
              "time": 1000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.98658466,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": "main"
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.9783862,
                  "app_id": "main"
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.97157896,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.96628696,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.95581007,
                  "app_id": "main"
                },
                {
                  "id": "ai_7vR9zv7l",
                  "name": "bubble",
                  "value": 0.9082134,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9020835,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.89708906,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": "main"
                },
                {
                  "id": "ai_7qwGxLch",
                  "name": "gold",
                  "value": 0.8834515,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": "main"
                },
                {
                  "id": "ai_b01mhdxB",
                  "name": "party",
                  "value": 0.8603341,
                  "app_id": "main"
                },
                {
                  "id": "ai_XNmzgDnF",
                  "name": "pub",
                  "value": 0.85809004,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.85319245,
                  "app_id": "main"
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.8506696,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.84634554,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": "main"
                },
                {
                  "id": "ai_wmbvr5TG",
                  "name": "celebration",
                  "value": 0.8383831,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 2,
              "time": 2000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9856042,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": "main"
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.9755833,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9733174,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.94170487,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.92778283,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9227257,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": "main"
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.90887475,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.87420183,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.8699659,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": "main"
                },
                {
                  "id": "ai_XNmzgDnF",
                  "name": "pub",
                  "value": 0.85809004,
                  "app_id": "main"
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.8506696,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": "main"
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.8397074,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 3,
              "time": 3000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.996614,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9794438,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9733174,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.9645849,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.94761443,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.92864025,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9227257,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.91797745,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.889248,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.8689867,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.86591685,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8546975,
                  "app_id": "main"
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8544879,
                  "app_id": "main"
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.852397,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": "main"
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.837438,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 4,
              "time": 4000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.996614,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9748836,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.9645849,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.96217895,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9030821,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.8983356,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.894987,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.889248,
                  "app_id": "main"
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8860091,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.8837219,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8712319,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.8695712,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.8664293,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8546975,
                  "app_id": "main"
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.852397,
                  "app_id": "main"
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 5,
              "time": 5000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.997158,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97719705,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9748836,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.96217895,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9210669,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9124408,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.90667903,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9046865,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9030821,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.8983356,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.8947689,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8852426,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8789175,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.8762902,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.87279737,
                  "app_id": "main"
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8544879,
                  "app_id": "main"
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.849733,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 6,
              "time": 6000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.99790645,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9273318,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.892028,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.88797945,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": "main"
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 7,
              "time": 7000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.99790645,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9273318,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.892028,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8913312,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": "main"
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 8,
              "time": 8000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.99790645,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9210669,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.88797945,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": "main"
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": "main"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

**Via bytes**

Below is an example of how you would send the bytes of a video and receive back predictions from the general model.

{% tabs %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

with open("{YOUR_VIDEO_FILE_LOCATION}", "rb") as f:
    file_bytes = f.read()

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="{THE_MODEL_ID}",
        version_id="{THE_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    video=resources_pb2.Video(
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

# A separate prediction is available for each "frame".
for frame in output.data.frames:
    print("Predicted concepts on frame " + str(frame.frame_info.time) + ":")
    for concept in frame.data.concepts:
        print("\t%s %.2f" % (concept.name, concept.value))
```
{% endtab %}
{% tab title="PHP" %}
```php
<?php
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

//
// For this example, the bytes of a video are needed and can be read in
// using PHP provided functions.
//
video = "https://samples.clarifai.com/beer.mp4";
$videoData = file_get_contents($image); // Get the video data from the URL

///////////////////////////////////////////////////////////////////////////////
// Specifying the Request Data
///////////////////////////////////////////////////////////////////////////////
//
// In the Clarifai platform a video is defined by a special Video object.
// There are several ways in which an Video object can be populated including
// by url and video bytes (base64).
//
$video = new Video([
    'base64' => $videoData
]);

//
// After a Video object is created, a Data object is constructed around it.
// The Data object offers a container that contains additional image independent
// metadata.  In this particular use case, no other metadata is needed to be
// specified.
//
$data = new Data([
    'video' => $video
]);

//
// The Data object is then wrapped in a Video object in order to meet the
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
// we loop through all of the frames of the video and print out the predicted 
// concepts for each along with their numerical prediction value (confidence).
//
foreach ($output->getData()->getFrames() as $frame) {
    echo "Predicted concepts on frame " . $frame->getFrameInfo()->getTime() . ":";
    foreach ($frame->getData()->getConcepts() as $concept) {
        echo "   " . $concept->getName() . ": " . number_format($concept->getValue(), 2) . "\n";
    }
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
                Data.newBuilder().setVideo(
                    Video.newBuilder()
                        .setBase64(ByteString.copyFrom(Files.readAllBytes(
                            new File("{YOUR_VIDEO_FILE_LOCATION}").toPath()
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

// A separate prediction is available for each "frame".
for (Frame frame : output.getData().getFramesList()) {
    System.out.println("Predicted concepts on frame " + frame.getFrameInfo().getTime() + ":");
    for (Concept concept : frame.getData().getConceptsList()) {
        System.out.printf("\t%s %.2f%n", concept.getName(), concept.getValue());
    }
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

const fs = require("fs");
const videoBytes = fs.readFileSync("{YOUR_VIDEO_FILE_LOCATION}");

stub.PostModelOutputs(
    {
        model_id: "{THE_MODEL_ID}",
        version_id: "{YOUR_MODEL_VERSION_ID}",  // This is optional. Defaults to the latest model version.
        inputs: [
            {data: {video: {base64: videoBytes}}}
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
        const output = response.outputs[0]

        // A separate prediction is available for each "frame".
        for (const frame of output.data.frames) {
            console.log("Predicted concepts on frame " + frame.frame_info.time + ":");
            for (const concept of frame.data.concepts) {
                console.log("\t" + concept.name + " " + concept.value);
            }
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
          "video": {
            "base64": "'"$(base64 video_file_path.mp4)"'"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/{THE_MODEL_ID}/versions/{THE_MODEL_VERSION_ID}/outputs

# The model version ID is optional. It defaults to the latest model version.
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
            "id": "f6f9e1b007d742fb9d777f35cf3bffd0",
            "status": {
                "code": 10000,
                "description": "Ok"
            },
            "created_at": "2017-06-28T16:00:51.258194418Z",
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
                "id": "b17d29ad1b714869a8c729e510ab22d0",
                "data": {
                    "video": {
                        "url": "https://s3.amazonaws.com/clarifai-api/vid/prod/ib81c84d5b2341858b86da18a2bd21d2/e86fbf516521425098081dd42e157a12",
                        "base64": "true"
                    }
                }
            },
            "data": {
                "frames": [
                    {
                        "frame_info": {
                            "index": 0,
                            "time": 0
                        },
                        "data": {
                            "concepts": [
                                {
                                    "id": "ai_VTlCx2f2",
                                    "name": "window",
                                    "value": 0.99909437,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_l8TKp2h5",
                                    "name": "people",
                                    "value": 0.99610686,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_VPmHr5bm",
                                    "name": "adult",
                                    "value": 0.9958472,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_SVshtN54",
                                    "name": "one",
                                    "value": 0.9937376,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_TJ9wFfK5",
                                    "name": "portrait",
                                    "value": 0.9899301,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_ZrPNDjxN",
                                    "name": "daylight",
                                    "value": 0.9885398,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_dxSG2s86",
                                    "name": "man",
                                    "value": 0.9833108,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_86sS08Pw",
                                    "name": "wear",
                                    "value": 0.9807093,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_GxSDhQ34",
                                    "name": "facial expression",
                                    "value": 0.9769263,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_Pf2b7clG",
                                    "name": "indoors",
                                    "value": 0.96838474,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_VRmbGVWh",
                                    "name": "travel",
                                    "value": 0.96641624,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_XNzGRk0F",
                                    "name": "side view",
                                    "value": 0.9603646,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_Zmhsv0Ch",
                                    "name": "outdoors",
                                    "value": 0.9434113,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_n9vjC1jB",
                                    "name": "light",
                                    "value": 0.94182396,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_WcnFrjw1",
                                    "name": "backlit",
                                    "value": 0.9347838,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_QKqjh1CM",
                                    "name": "vehicle window",
                                    "value": 0.92699903,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_mlrv94tv",
                                    "name": "reflection",
                                    "value": 0.90993655,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_41s912fX",
                                    "name": "fair weather",
                                    "value": 0.90100014,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_rsX6XWc2",
                                    "name": "building",
                                    "value": 0.88111985,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_L83krFdq",
                                    "name": "veil",
                                    "value": 0.8785704,
                                    "app_id": "main"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}
```
{% endtab %}
{% endtabs %}

