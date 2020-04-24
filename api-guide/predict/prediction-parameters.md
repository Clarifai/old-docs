# Prediction parameters

You can set additional parameters to gain flexibility in the predict operation.

## Select Concepts

By putting this additional parameter on your predict calls, you can receive predict value\(s\) for **only** the concepts that you want to. You can specify particular concepts by either their id and/or their name. The concept names and ids are case sensitive, and so, these must be exact matches.

To retrieve an entire list of concepts from a given model use the `GET /v2/models/{model_id}/output_info` endpoint. Check out the [Advanced Models](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/models.md#get-model-output-info-by-id) section for how to use with any of the API clients!

If you submit a request with not an exact match of the concept id or name, you will receive an invalid model argument error. However, if one or more matches while one or more do not, the API will respond with a Mixed Success.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.StatusCode;

...

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the publicly available General model.
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

{% tab title="gRPC NodeJS" %}
```js
stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the publicly available General model.
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

...

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the publicly available General model.
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

{% tab title="js" %}
```javascript
app.models.predict(Clarifai.GENERAL_MODEL, 'https://samples.clarifai.com/metro-north.jpg', {
  selectConcepts: [
    {name: 'train'},
    {id: 'ai_6kTjGfF6'}
  ]
})
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp, Concept
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('general-v1.3')

select_concept_list = [Concept(concept_name='train'), Concept(concept_id='ai_6kTjGfF6')]
model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg', select_concepts=select_concept_list)
```
{% endtab %}

{% tab title="java" %}
```java
client.predict(client.getDefaultModels().generalModel().id())
    .withInputs(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
    .selectConcepts(Concept.forID("dog"), Concept.forID("cat"))
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.Predict<Concept>(
                    client.PublicModels.GeneralModel.ModelID,
                    new ClarifaiURLImage("https://samples.clarifai.com/metro-north.jpg"),
                    selectConcepts: new List<Concept>
                    {
                        new Concept(id: "", name: "dog"),
                        new Concept(id: "", name: "cat")
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
use Clarifai\DTOs\Models\ModelType;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->predict(ModelType::concept(),
        $client->publicModels()->generalModel()->modelID(),
        new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'))
    ->withSelectConcepts([(new Concept(''))->withName('dog'), (new Concept(''))->withName('cat')])
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    $output = $response->get();

    echo "Predicted concepts:\n";

    foreach ($output->data() as $concept) {
        echo $concept->name() . ': ' . $concept->value() . "\n";
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the publicly available General model.
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

{% tab title="gRPC NodeJS" %}
```js
stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the publicly available General model
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

...

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the publicly available General model.
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

{% tab title="js" %}
```javascript
app.models.predict(Clarifai.GENERAL_MODEL, 'https://samples.clarifai.com/metro-north.jpg', { maxConcepts: 3 })
  .then(response => {
    // There was a successful response
  })
  .catch(error => {
    // There was an error
  });
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('general-v1.3')

model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg', max_concepts=3)
```
{% endtab %}

{% tab title="java" %}
```java
client.predict(client.getDefaultModels().generalModel().id())
    .withInputs(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
    .withMaxConcepts(3)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.Predict<Concept>(
                    client.PublicModels.GeneralModel.ModelID,
                    new ClarifaiURLImage("https://samples.clarifai.com/metro-north.jpg"),
                    maxConcepts: 3)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
//Coming soon
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Models\ModelType;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->predict(ModelType::concept(),
        $client->publicModels()->generalModel()->modelID(),
        new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'))
    ->withMaxConcepts(3)
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var ClarifaiOutput $output */
    $output = $response->get();

    echo "Predicted concepts:\n";
    /** @var Concept $concept */
    foreach ($output->data() as $concept) {
        echo $concept->name() . ': ' . $concept->value() . "\n";
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the publicly available General model.
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

{% tab title="gRPC NodeJS" %}
```js
stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the publicly available General model
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

...

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the publicly available General model.
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

{% tab title="js" %}
```javascript
app.models.predict(Clarifai.GENERAL_MODEL, 'https://samples.clarifai.com/metro-north.jpg', { minValue: 0.97 })
  .then(response => {
    // There was a successful response
  })
  .catch(error => {
    // There was an error
  });
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_CLARIFAI_KEY')

model = app.models.get('general-v1.3')

model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg', min_value=0.97)
```
{% endtab %}

{% tab title="java" %}
```java
client.predict(client.getDefaultModels().generalModel().id())
    .withInputs(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
    .withMinValue(0.9)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.Predict<Concept>(
                    client.PublicModels.GeneralModel.ModelID,
                    new ClarifaiURLImage("https://samples.clarifai.com/metro-north.jpg"),
                    minValue: 0.9M)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
//Coming soon
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Models\ModelType;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->predict(ModelType::concept(),
        $client->publicModels()->generalModel()->modelID(),
        new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'))
    ->withMinValue(0.9)
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var ClarifaiOutput $output */
    $output = $response->get();

    echo "Predicted concepts:\n";
    /** @var Concept $concept */
    foreach ($output->data() as $concept) {
        echo $concept->name() . ': ' . $concept->value() . "\n";
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
          "min_value": 0.97
        }
      }
    }
  }'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the publicly available General model.
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

{% tab title="gRPC NodeJS" %}
```js
stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",  // This is model ID of the publicly available General model
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

...

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the publicly available General model.
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

{% tab title="js" %}
```javascript
let app = new Clarifai.App({apiKey: 'YOUR_API_KEY'});

app.models.predict({id:'MODEL_ID', version:'MODEL_VERSION_ID'}, "https://samples.clarifai.com/metro-north.jpg").then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('YOUR_MODEL_ID')
model.model_version = 'YOUR_MODEL_VERSION_ID'

response = model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')
```
{% endtab %}

{% tab title="java" %}
```java
ModelVersion modelVersion = client.getModelVersionByID("MODEL_ID", "MODEL_VERSION_ID")
        .executeSync()
        .get();

    client.predict("MODEL_ID")
        .withVersion(modelVersion)
        .withInputs(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
        .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

                 var response = await Client.Predict<Concept>(
                    "YOUR_MODEL_ID",
                    new ClarifaiURLImage("https://samples.clarifai.com/metro-north.jpg"),
                    modelVersionID: "MODEL_VERSION_ID")
                  .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
//Coming soon
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Models\ModelType;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->predict(ModelType::concept(), '{model_id}',
        new ClarifaiURLImage('https://samples.clarifai.com/puppy.jpeg'))
    ->withModelVersionID('MODEL_VERSION_ID')
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var ClarifaiOutput $output */
    $output = $response->get();

    echo "Predicted concepts:\n";
    /** @var Concept $concept */
    foreach ($output->data() as $concept) {
        echo $concept->name() . ': ' . $concept->value() . "\n";
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
  https://api.clarifai.com/v2/models/<model_id>/versions/<model_version_id>/outputs
```
{% endtab %}
{% endtabs %}
