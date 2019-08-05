## Train

Clarifai provides many different models that 'see' the world differently. A model contains a group of
concepts. A model will only see the concepts it contains.

There are times when you wish you had a model that sees the world the way you see it. The API allows you to
do this. You can create your own model and train it with your own images and concepts. Once you train it to
see how you would like it to see, you can then use that model to make predictions.

You do not need many images to get started. We recommend starting with 10 and adding more as needed. Before you train your first model you will have needed to [create an application](applications.md#create-an-application). From there you will be able to change your [Base Workflow](applications#base-workflow) to optimize custom training using the knowledge base from select public models.

![inputs outputs](/images/illustration-training.png)  

### Add Images With Concepts

To get started training your own model, you must first add images that already contain the concepts you want
your model to see.



```js

app.inputs.create({
  url: "https://samples.clarifai.com/puppy.jpg",
  concepts: [
    {
      id: "boscoe",
      value: true
    }
  ]
});

```

```python
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='YOUR_API_KEY')

# add multiple images with concepts
img1 = ClImage(url="https://samples.clarifai.com/puppy.jpg", concepts=['boscoe'], not_concepts=['our_wedding'])
img2 = ClImage(url="https://samples.clarifai.com/wedding.jpg", concepts=['our_wedding'], not_concepts=['cat','boscoe'])

app.inputs.bulk_create_images([img1, img2])

```

```java

client.addInputs()
    .plus(
        ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpg")
            .withConcepts(Concept.forID("boscoe"))
    )
    .executeSync();
```

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
                        "https://samples.clarifai.com/puppy.jpg",
                        positiveConcepts: new List<Concept> {new Concept(id: "boscoe")}))
                .ExecuteAsync();
        }
    }
}

```

```objective-c

ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpg" andConcepts:@"cute puppy"];
[_app addInputs:@[image] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];

```

```php

use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->addInputs(
        (new ClarifaiURLImage('https://samples.clarifai.com/puppy.jpeg'))
        ->withAllowDuplicateUrl(true)
        ->withPositiveConcepts([new Concept('boscoe')]))
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

```cURL

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpg"
          },
          "concepts":[
            {
              "id": "boscoe",
              "value": true
            }
          ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs

```




```response

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
            "id": "boscoe",
            "name": "boscoe",
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

### Create A Model

Once your images with concepts are added, you are now ready to create the model. You'll need a name for the
model and you'll also need to provide it with the concepts you added above.

Take note of the `model id` that is returned in the response. You'll need that for the next two steps.



```js

app.models.create(
  "pets",
  [
    { "id": "boscoe" }
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

```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.create('pets', concepts=['boscoe'])

```

```java

client.createModel("pets")
    .withOutputInfo(ConceptOutputInfo.forConcepts(
        Concept.forID("boscoe")
    ))
    .executeSync();
```

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
                    concepts: new List<Concept> {new Concept("boscoe")})
                .ExecuteAsync();
        }
    }
}

```

```objective-c

[app createModel:@[concept] name:modelName conceptsMutuallyExclusive:NO closedEnvironment:NO
      completion:^(ClarifaiModel *model, NSError *error) {
        NSLog(@"model: %@", model);
}];

```

```php

use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->createModel('pets')
    ->withConcepts([new Concept('boscoe')])
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

```cURL

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
              "id": "boscoe"
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




```response

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

### Train The Model

Now that you've added images with concepts, then created a model with those concepts, the next step is to
train the model. When you train a model, you are telling the system to look at all the images with concepts
you've provided and learn from them. This train operation is asynchronous. It may take a few seconds for your
model to be fully trained and ready.

Keep note of the `model_version id` in the response. We'll need that for the next section when we predict with the model. 



```js

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

```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{model_id}')
model.train()

```

```java

client.trainModel("{model_id}").executeSync();
```

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

```objective-c

ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpg"]
[app getModel:@"{id}" completion:^(ClarifaiModel *model, NSError *error) {
    [model train:^(ClarifaiModel *model, NSError *error) {
        NSLog(@"model: %@", model);
    }];
}];

```

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

```cURL

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/models/<model_id>/versions

```




```response

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

### Predict With The Model

Now that we have a trained model. We can start making predictions with it. In our predict call we need to specify three items. 
The `model id`, `model_version id` and the `input` we want a prediction for.

*Note: you can repeat the above steps as often as you like. By adding more images with concepts and training,
you can get the model to predict exactly how you want it to.*



```js

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

```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('MODEL_ID')
model.model_version = 'MODEL_VERSION_ID'  # This is optional. Defaults to the latest model version.

response = model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')
```

```java

ModelVersion modelVersion = client.getModelVersionByID("MODEL_ID", "MODEL_VERSION_ID")
        .executeSync()
        .get();

    client.predict("MODEL_ID")
        .withVersion(modelVersion)
        .withInputs(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
        .executeSync();


```

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

```objective-c

ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpg"]
[app getModel:@"{id}" completion:^(ClarifaiModel *model, NSError *error) {
    [model predictOnImages:@[image]
                completion:^(NSArray<ClarifaiSearchResult *> *outputs, NSError *error) {
                    NSLog(@"outputs: %@", outputs);
                }];
}];

```

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

```cURL

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



```response

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
            "id": "boscoe",
            "name": "boscoe",
            "app_id": "f09abb8a57c041cbb94759ebb0cf1b0d",
            "value": 0.98308545
          }
        ]
      }
    }
  ]
}

```
