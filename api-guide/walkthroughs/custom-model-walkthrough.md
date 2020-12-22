# Custom Models

You do not need many images to get started. We recommend starting with 10 and adding more as needed. Before you train your first model you will have needed to [create an application](../../getting-started/applications/#create-an-application) and select a [base workflow](../../getting-started/applications/#base-workflow).

![](../../.gitbook/assets/illustration-training%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29.png)

## Add images with concepts

To get started training your own model, you must first add images that already contain the concepts you want your model to see.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder()
        .addInputs(
            Input.newBuilder()
                .setData(
                    Data.newBuilder()
                        .setImage(
                            Image.newBuilder()
                                .setUrl("https://samples.clarifai.com/puppy.jpeg")
                                .setAllowDuplicateUrl(true)
                        )
                        .addConcepts(Concept.newBuilder().setId("charlie").setValue(1))
                        .addConcepts(Concept.newBuilder().setId("our_wedding").setValue(0))
                )
        )
        .addInputs(
            Input.newBuilder()
                .setData(
                    Data.newBuilder()
                        .setImage(
                            Image.newBuilder()
                                .setUrl("https://samples.clarifai.com/wedding.jpg")
                                .setAllowDuplicateUrl(true)
                        )
                        .addConcepts(Concept.newBuilder().setId("our_wedding").setValue(1))
                        .addConcepts(Concept.newBuilder().setId("charlie").setValue(0))
                        .addConcepts(Concept.newBuilder().setId("cat").setValue(0))
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

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostInputs(
    {
        inputs: [
            {
                data: {
                    image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true},
                    concepts: [{id: "charlie", value: 1}, {id: "our_wedding", value: 0}]
                }
            },
            {
                data: {
                    image: {url: "https://samples.clarifai.com/wedding.jpg", allow_duplicate_url: true},
                    concepts: [{id: "our_wedding", value: 1}, {id: "charlie", value: 0}, {id: "cat", value: 0}]
                }
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/puppy.jpeg",
                        allow_duplicate_url=True
                    ),
                    concepts=[
                        resources_pb2.Concept(id="charlie", value=1),
                        resources_pb2.Concept(id="our_wedding", value=0),
                    ]
                )
            ),
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/wedding.jpg",
                        allow_duplicate_url=True
                    ),
                    concepts=[
                        resources_pb2.Concept(id="our_wedding", value=1),
                        resources_pb2.Concept(id="charlie", value=0),
                        resources_pb2.Concept(id="cat", value=0),
                    ]
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

{% tab title="js" %}
```javascript
app.inputs.create({
  url: "https://samples.clarifai.com/puppy.jpeg",
  concepts: [
    {
      id: "charlie",
      value: true
    }
  ]
});
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='YOUR_API_KEY')

# add multiple images with concepts
img1 = ClImage(url="https://samples.clarifai.com/puppy.jpeg", concepts=['charlie'], not_concepts=['our_wedding'])
img2 = ClImage(url="https://samples.clarifai.com/wedding.jpg", concepts=['our_wedding'], not_concepts=['cat','charlie'])

app.inputs.bulk_create_images([img1, img2])
```
{% endtab %}

{% tab title="java" %}
```java
client.addInputs()
    .plus(
        ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpeg")
            .withConcepts(Concept.forID("charlie"))
    )
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

            await client.AddInputs(
                    new ClarifaiURLImage(
                        "https://samples.clarifai.com/puppy.jpeg",
                        positiveConcepts: new List<Concept> {new Concept(id: "charlie")}))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpeg" andConcepts:@"cute puppy"];
[_app addInputs:@[image] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->addInputs(
        (new ClarifaiURLImage('https://samples.clarifai.com/puppy.jpeg'))
        ->withAllowDuplicateUrl(true)
        ->withPositiveConcepts([new Concept('charlie')]))
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";
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
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
          },
          "concepts":[
            {
              "id": "charlie",
              "value": 1
            },
            {
              "id": "our_wedding",
              "value": 0
            }
          ]
        }
      },
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/wedding.jpg",
            "allow_duplicate_url": true
          },
          "concepts":[
            {
              "id": "our_wedding",
              "value": 1
            },
            {
              "id": "charlie",
              "value": 0
            },
            {
              "id": "cat",
              "value": 0
            }
          ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
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
      "id": "e82fd13b11354d808cc48dc8f94ec3a9",
      "created_at": "2016-11-22T17:16:00Z",
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/puppy.jpeg"
        },
        "concepts": [
          {
            "id": "charlie",
            "name": "charlie",
            "app_id": "f09abb8a57c041cbb94759ebb0cf1b0d",
            "value": 1
          }
        ]
      },
      "status": {
        "code": 30000,
        "description": "Download complete"
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Create a model

Once your images with concepts are added, you are now ready to create the model. You'll need a name for the model and you'll also need to provide it with the concepts you added above.

Take note of the `model id` that is returned in the response. You'll need that for the next two steps.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

SingleModelResponse postModelsResponse = stub.postModels(
    PostModelsRequest.newBuilder().addModels(
        Model.newBuilder()
            .setId("pets")
            .setOutputInfo(
                OutputInfo.newBuilder()
                    .setData(
                        Data.newBuilder().addConcepts(Concept.newBuilder().setId("charlie"))
                    )
                    .setOutputConfig(
                        OutputConfig.newBuilder()
                            .setConceptsMutuallyExclusive(false)
                            .setClosedEnvironment(false)
                    )
            )
    ).build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostModels(
    {
        models: [
            {
                id: "pets",
                output_info: {
                    data: {concepts: [{id: "charlie"}]},
                    output_config: {concepts_mutually_exclusive: false, closed_environment: false}
                }
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        models=[
            resources_pb2.Model(
                id="pets",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[resources_pb2.Concept(id="charlie", value=1)]
                    ),
                    output_config=resources_pb2.OutputConfig(
                        concepts_mutually_exclusive=False,
                        closed_environment=False
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.create(
  "pets",
  [
    { "id": "charlie" }
  ]
).then(
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

model = app.models.create('pets', concepts=['charlie'])
```
{% endtab %}

{% tab title="java" %}
```java
client.createModel("pets")
    .withOutputInfo(ConceptOutputInfo.forConcepts(
        Concept.forID("charlie")
    ))
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.CreateModel(
                    "pets",
                    concepts: new List<Concept> {new Concept("charlie")})
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app createModel:@[concept] name:modelName conceptsMutuallyExclusive:NO closedEnvironment:NO
      completion:^(ClarifaiModel *model, NSError *error) {
        NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->createModel('pets')
    ->withConcepts([new Concept('charlie')])
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";
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
    "model": {
      "id": "pets",
      "output_info": {
        "data": {
          "concepts": [
            {
              "id": "charlie"
            }
          ]
        },
        "output_config": {
          "concepts_mutually_exclusive": false,
          "closed_environment":false
        }
      }
    }
  }'\
  https://api.clarifai.com/v2/models
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
  "model": {
    "name": "pets",
    "id": "a10f0cf48cf3426cbb8c4805e246c214",
    "created_at": "2016-11-22T17:17:36Z",
    "app_id": "f09abb8a57c041cbb94759ebb0cf1b0d",
    "output_info": {
      "message": "Show output_info with: GET /models/{model_id}/output_info",
      "type": "concept",
      "output_config": {
        "concepts_mutually_exclusive": false,
        "closed_environment": false
      }
    },
    "model_version": {
      "id": "e7bcd534b61b4874a3ab69fba974c012",
      "created_at": "2016-11-22T17:17:36Z",
      "status": {
        "code": 21102,
        "description": "Model not yet trained"
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

## Train the model

Now that you've added images with concepts, then created a model with those concepts, the next step is to train the model. When you train a model, you are telling the system to look at all the images with concepts you've provided and learn from them. This train operation is asynchronous. It may take a few seconds for your model to be fully trained and ready.

Keep note of the `model_version id` in the response. We'll need that for the next section when we predict with the model.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

SingleModelResponse postModelVersionsResponse = stub.postModelVersions(
    PostModelVersionsRequest.newBuilder()
        .setModelId("pets")
        .build()
);

if (postModelVersionsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model versions failed, status: " + postModelVersionsResponse.getStatus());
}

String modelVersionId = postModelVersionsResponse.getModel().getModelVersion().getId();
System.out.println("New model version ID: " + modelVersionId);
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostModelVersions(
    {model_id: "pets"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model versions failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_model_versions = stub.PostModelVersions(
    service_pb2.PostModelVersionsRequest(
        model_id="pets"
    ),
    metadata=metadata
)

if post_model_versions.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post model versions failed, status: " + post_model_versions.status.description)
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.train("{model_id}").then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

// or if you have an instance of a model

model.train().then(
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

model = app.models.get('{model_id}')
model.train()
```
{% endtab %}

{% tab title="java" %}
```java
client.trainModel("{model_id}").executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.TrainModel<Concept>("{model_id}")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpeg"]
[app getModel:@"{id}" completion:^(ClarifaiModel *model, NSError *error) {
    [model train:^(ClarifaiModel *model, NSError *error) {
        NSLog(@"model: %@", model);
    }];
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Models\ModelType;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->trainModel(ModelType::concept(), 'MODEL_ID')
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";
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
  https://api.clarifai.com/v2/models/pets/versions
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
  "model": {
    "name": "pets",
    "id": "a10f0cf48cf3426cbb8c4805e246c214",
    "created_at": "2016-11-22T17:17:36Z",
    "app_id": "f09abb8a57c041cbb94759ebb0cf1b0d",
    "output_info": {
      "message": "Show output_info with: GET /models/{model_id}/output_info",
      "type": "concept",
      "output_config": {
        "concepts_mutually_exclusive": false,
        "closed_environment": false
      }
    },
    "model_version": {
      "id": "d1b38fd2251148d08675c5542ef00c7b",
      "created_at": "2016-11-22T17:21:13Z",
      "status": {
        "code": 21103,
        "description": "Custom model is currently in queue for training, waiting on inputs to process."
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

## Predict with the model

Now that we have a trained model we can start making predictions with it. In our predict call we specify three items. The `model id`, `model version id` \(optional, defaults to the latest trained version\) and the `input` we want a prediction for.

_Note: you can repeat the above steps as often as you like. By adding more images with concepts and training, you can get the model to predict exactly how you want it to._

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("pets")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")  // This is optional. Defaults to the latest model version.
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
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostModelOutputs(
    {
        model_id: "pets",
        version_id: "{YOUR_MODEL_VERSION_ID}",  // This is optional. Defaults to the latest model version.
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="pets",
        version_id="{YOUR_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
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

model = app.models.get('MODEL_ID')
model.model_version = 'MODEL_VERSION_ID'  # This is optional. Defaults to the latest model version.

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
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpeg"]
[app getModel:@"{id}" completion:^(ClarifaiModel *model, NSError *error) {
    [model predictOnImages:@[image]
                completion:^(NSArray<ClarifaiSearchResult *> *outputs, NSError *error) {
                    NSLog(@"outputs: %@", outputs);
                }];
}];
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

$response = $client->predict(ModelType::concept(), 'MODEL_ID,
        new ClarifaiURLImage('https://samples.clarifai.com/puppy.jpeg'))
    ->executeSync();

if ($response-> isSuccessful()) {
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
  https://api.clarifai.com/v2/models/pets/versions/{YOUR_MODEL_VERSION_ID}/outputs
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
      "id": "e8b6eb27de764f3fa8d4f7752a3a2dfc",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2016-11-22T17:22:23Z",
      "model": {
        "name": "pets",
        "id": "a10f0cf48cf3426cbb8c4805e246c214",
        "created_at": "2016-11-22T17:17:36Z",
        "app_id": "f09abb8a57c041cbb94759ebb0cf1b0d",
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept",
          "output_config": {
            "concepts_mutually_exclusive": false,
            "closed_environment": false
          }
        },
        "model_version": {
          "id": "d1b38fd2251148d08675c5542ef00c7b",
          "created_at": "2016-11-22T17:21:13Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "e8b6eb27de764f3fa8d4f7752a3a2dfc",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "charlie",
            "name": "charlie",
            "app_id": "f09abb8a57c041cbb94759ebb0cf1b0d",
            "value": 0.98308545
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

