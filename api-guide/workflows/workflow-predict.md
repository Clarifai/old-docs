# Workflow Predict

The Workflow Predict API allows you to predict using 1 or more model\(s\), regardless of them being Clarifai or custom, within a single API call. The max number of inputs processed at once with any given workflow is 32.

Now that you have that all set up, you will be able to predict under a workflow using the `POST /v2/workflows/{workflow_id}/results` endpoint. Your `{workflow-id}` currently is whatever you set as your ID. Then as far as your request body, nothing has changed with how you would normally do a predict. In the response body, you will see a `results` object and each object will be the response from the models in the same ordering from the workflow you set up.

![Image showing the Portal&apos;s workflow prediction results](../../.gitbook/assets/preview-workflows-new%20%282%29%20%282%29%20%282%29%20%283%29%20%283%29%20%283%29.png)

You can also use the Explorer in Clarifai Portal to see the results of your workflow's predictions on a given input.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

PostWorkflowResultsResponse postWorkflowResultsResponse = stub.postWorkflowResults(
    PostWorkflowResultsRequest.newBuilder()
        .setWorkflowId("{YOUR_WORKFLOW_ID}")
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder().setUrl(
                        "https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        )
        .build()
);

if (postWorkflowResultsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post workflow results failed, status: " + postWorkflowResultsResponse.getStatus());
}

// We'll get one WorkflowResult for each input we used above. Because of one input, we have here
// one WorkflowResult.
WorkflowResult results = postWorkflowResultsResponse.getResults(0);

// Each model we have in the workflow will produce one output.
for (Output output : results.getOutputsList()) {
    Model model = output.getModel();

    System.out.println("Predicted concepts for the model `" + model.getName() + "`:");
    for (Concept concept : output.getData().getConceptsList()) {
        System.out.printf("\t%s %.2f%n", concept.getName(), concept.getValue());
    }
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostWorkflowResults(
    {
        workflow_id: "{YOUR_WORKFLOW_ID}",
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
            throw new Error("Post workflow results failed, status: " + response.status.description);
        }

        // We'll get one WorkflowResult for each input we used above. Because of one input, we have here
        // one WorkflowResult.
        const results = response.results[0];

        // Each model we have in the workflow will produce one output.
        for (const output of results.outputs) {
            const model = output.model;

            console.log("Predicted concepts for the model `" + model.name + "`:");
            for (const concept of output.data.concepts) {
                console.log("\t" + concept.name + " " + concept.value);
            }
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_workflow_results_response = stub.PostWorkflowResults(
    service_pb2.PostWorkflowResultsRequest(
        workflow_id="{YOUR_WORKFLOW_ID}",
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
if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post workflow results failed, status: " + post_workflow_results_response.status.description)

# We'll get one WorkflowResult for each input we used above. Because of one input, we have here
# one WorkflowResult.
results = post_workflow_results_response.results[0]

# Each model we have in the workflow will produce one output.
for output in results.outputs:
    model = output.model

    print("Predicted concepts for the model `%s`" % model.name)
    for concept in output.data.concepts:
        print("\t%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="js" %}
```javascript
app.workflow.predict('{workflow-id}', "https://samples.clarifai.com/metro-north.jpg").then(
    function(response){
      // Do something with response
    },
    function(err){
      // There was an error
    }
);
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
from clarifai.rest import Workflow

app = ClarifaiApp(api_key='YOUR_API_KEY')
workflow = Workflow(app.api, workflow_id="YOUR_WORKFLOW_ID")

response = workflow.predict_by_url('https://samples.clarifai.com/metro-north.jpg')
```
{% endtab %}

{% tab title="java" %}
```java
client.workflowPredict("{workflow-id}")
        .withInputs(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
        .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.WorkflowPredict(
                    "{workflow-id}",
                    new List<IClarifaiInput>
                    {
                        new ClarifaiURLImage("https://samples.clarifai.com/puppy.jpeg")
                    })
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
// Coming Soon
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Predictions\Concept;
use Clarifai\DTOs\Workflows\WorkflowPredictResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->workflowPredict('your-workflow-id',
        new ClarifaiURLImage('https://samples.clarifai.com/puppy.jpeg'))
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";

    /** @var WorkflowPredictResult $workflowResult */
    $workflowResult = $response->get();

    echo "Predicted concepts:\n";
    /** @var Concept $concept */
    foreach ($workflowResult->workflowResult()->predictions() as $output) {
        echo 'Predictions for output ' . $output->id() . "\n";
        /** @var Concept $concept */
        foreach ($output->data() as $concept) {
            echo "\t" . $concept->name() . ': ' . $concept->value() . "\n";
        }
    }
} else {
    echo "Response is not successful. Reason: \n";
    echo $response->status()->description() . "\n";
    echo $response->status()->errorDetails() . "\n";
    echo "Status code: " . $response->status()->statusCode();
}
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H 'authorization: Key YOUR_API_KEY' \
  -H 'content-type: application/json' \
  -d '{
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
https://api.clarifai.com/v2/workflows/{YOUR_WORKFLOW_ID}/results
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
  "workflow": {
    "id": "my-workflow",
    "app_id": "c54b7637df12407aa9c57dfd6d5c057f",
    "created_at": "2017-07-10T01:45:05.672880Z"
  },
  "results": [
    {
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "input": {
        "id": "c88aeed9d04c471cace6f8e4801f1a1c",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      },
      "outputs": [
        {
          "id": "feae971167a04d1bbebb7ea49d6ba0f7",
          "status": {
            "code": 10000,
            "description": "Ok"
          },
          "created_at": "2017-07-10T12:01:44.929928529Z",
          "model": {
            "id": "d16f390eb32cad478c7ae150069bd2c6",
            "name": "moderation",
            "created_at": "2017-05-12T21:28:00.471607Z",
            "app_id": "main",
            "output_info": {
              "message": "Show output_info with: GET /models/{model_id}/output_info",
              "type": "concept",
              "type_ext": "concept"
            },
            "model_version": {
              "id": "b42ac907ac93483484483a0040a386be",
              "created_at": "2017-05-12T21:28:00.471607Z",
              "status": {
                "code": 21100,
                "description": "Model trained successfully"
              }
            }
          },
          "data": {
            "concepts": [
              {
                "id": "ai_QD1zClSd",
                "name": "safe",
                "value": 0.99999714,
                "app_id": "main"
              },
              {
                "id": "ai_kBBGf7r8",
                "name": "gore",
                "value": 3.7771046e-05,
                "app_id": "main"
              },
              {
                "id": "ai_8QQwMjQR",
                "name": "drug",
                "value": 1.0449563e-05,
                "app_id": "main"
              },
              {
                "id": "ai_V76bvrtj",
                "name": "explicit",
                "value": 5.2887003e-06,
                "app_id": "main"
              },
              {
                "id": "ai_RtXh5qkR",
                "name": "suggestive",
                "value": 4.7939684e-06,
                "app_id": "main"
              }
            ]
          }
        },
        {
          "id": "f635b40cbeee47ddb7b348a981e14faf",
          "status": {
            "code": 10000,
            "description": "Ok"
          },
          "created_at": "2017-07-10T12:01:44.929941126Z",
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
              },
              {
                "id": "ai_46lGZ4Gm",
                "name": "railroad track",
                "value": 0.9690325,
                "app_id": "main"
              },
              {
                "id": "ai_tr0MBp64",
                "name": "traffic",
                "value": 0.9687052,
                "app_id": "main"
              },
              {
                "id": "ai_l4WckcJN",
                "name": "blur",
                "value": 0.9667078,
                "app_id": "main"
              },
              {
                "id": "ai_2gkfMDsM",
                "name": "platform",
                "value": 0.9624243,
                "app_id": "main"
              },
              {
                "id": "ai_CpFBRWzD",
                "name": "urban",
                "value": 0.960752,
                "app_id": "main"
              },
              {
                "id": "ai_786Zr311",
                "name": "no person",
                "value": 0.95864904,
                "app_id": "main"
              },
              {
                "id": "ai_6lhccv44",
                "name": "business",
                "value": 0.95720303,
                "app_id": "main"
              },
              {
                "id": "ai_971KsJkn",
                "name": "track",
                "value": 0.9494642,
                "app_id": "main"
              },
              {
                "id": "ai_WBQfVV0p",
                "name": "city",
                "value": 0.94089437,
                "app_id": "main"
              },
              {
                "id": "ai_dSCKh8xv",
                "name": "fast",
                "value": 0.9399334,
                "app_id": "main"
              },
              {
                "id": "ai_TZ3C79C6",
                "name": "road",
                "value": 0.93121606,
                "app_id": "main"
              },
              {
                "id": "ai_VSVscs9k",
                "name": "terminal",
                "value": 0.9230834,
                "app_id": "main"
              }
            ]
          }
        }
      ]
    }
  ]
}
```
{% endtab %}
{% endtabs %}

