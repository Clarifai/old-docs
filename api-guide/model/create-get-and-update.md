# Create, get and update

### Create Model

You can create your own model and train it with your own images and concepts. Once you train it to see how you would like it to see, you can then use that model to make predictions.

When you create a model you give it a name and an id. If you don't supply an id, one will be created for you.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

SingleModelResponse postModelsResponse = stub.postModels(
    PostModelsRequest.newBuilder().addModels(
        Model.newBuilder().setId("petsID")
    ).build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.PostModels(
    {
        models: [
            {
                id: "petsID",
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
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.create("petsID").then(
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

app.models.create('petsID')
```
{% endtab %}

{% tab title="java" %}
```java
client.createModel("petsID").executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.CreateModel("petsID")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app createModel:nil name:@"petsModel" modelID:@"petsID" conceptsMutuallyExclusive:NO closedEnvironment:NO completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->createModel('{model_id}')
    ->executeSync();

if ($response->isSuccessful()) {
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
      "id": "petsID"
    }
  }'\
  https://api.clarifai.com/v2/models
```
{% endtab %}
{% endtabs %}

### Create Model With Concepts

You can also create a model and initialize it with the concepts it will contain. You can always add and remove concepts later.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

SingleModelResponse postModelsResponse = stub.postModels(
    PostModelsRequest.newBuilder().addModels(
        Model.newBuilder()
            .setId("petsID")
            .setOutputInfo(
                OutputInfo.newBuilder().setData(
                    Data.newBuilder().addConcepts(Concept.newBuilder().setId("boscoe"))
                )
            )
    ).build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.PostModels(
    {
        models: [
            {
                id: "petsID",
                output_info: {
                    data: {concepts: [{id: "boscoe"}]},
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
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.create(
  "petsID",
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
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.create('petsID', concepts=['boscoe'])
```
{% endtab %}

{% tab title="java" %}
```java
client.createModel("petsID")
    .withOutputInfo(ConceptOutputInfo.forConcepts(
        Concept.forID("boscoe")
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
                    "petsID",
                    concepts: new List<Concept> {new Concept("boscoe")})
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app createModel:@[@"cat", @"dog"] name:@"petsModel" modelID:@"petsID" conceptsMutuallyExclusive:NO closedEnvironment:NO completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->createModel('MODEL_ID')
    ->withConcepts([new Concept('CONCEPT1')])
    ->executeSync();

if ($response->isSuccessful()) {
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
      "id": "petsID",
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
{% endtab %}
{% endtabs %}

### Add Concepts To A Model

You can add concepts to a model at any point. As you add concepts to inputs, you may want to add them to your model.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiModelResponse patchModelsResponse = stub.patchModels(
    PatchModelsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove
        .addModels(
            Model.newBuilder()
                .setId("petsID")
                .setOutputInfo(
                    OutputInfo.newBuilder().setData(
                        Data.newBuilder().addConcepts(Concept.newBuilder().setId("boscoe"))
                    )
                )
        )
        .build()
);

if (patchModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch models failed, status: " + patchModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.PatchModels(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove
        models: [
            {
                id: "petsID",
                output_info: {data: {concepts: [{id: "boscoe"}]}}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel({model_id}).then(function(model) {
  updateModel,
  function(err) {
    // there was an error
  }
});

function updateModel(model) {
  model.mergeConcepts({"id": "boscoe"}).then(
    function(response) {
      // do something with response
    },
    function(err) {
      // there was an error
    }
  );
}
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{model_id}')
model.add_concepts(['boscoe'])
```
{% endtab %}

{% tab title="java" %}
```java
client.modifyModel("{{model_id}}")
    .withConcepts(Action.MERGE, Concept.forID("dogs"))
    .executeSync();

// Or, if you have a ConceptModel object, you can do it in an OO fashion
final ConceptModel model = client.getModelByID("{model_id}").executeSync().get().asConceptModel();
model.modify()
    .withConcepts(Action.MERGE, Concept.forID("dogs"))
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.API.Requests.Models;
using Clarifai.DTOs.Models;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModifyModel(
                    "petsID",
                    ModifyAction.Merge,
                    concepts: new List<Concept> {new Concept("dogs")})
                .ExecuteAsync();

            // Or, if you have a ConceptModel object, you can do it in an OO fashion
            ConceptModel model = (ConceptModel) (
                await client.GetModel<Concept>("petsID")
                    .ExecuteAsync()).Get();
            await model.Modify(
                    ModifyAction.Merge,
                    concepts: new List<Concept> {new Concept("dogs")})
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"dress"];
[app addConcepts:@[concept] toModelWithID:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ModifyAction;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modifyModel('MODEL_ID')
    ->withModifyAction(ModifyAction::merge())
    ->withConcepts([new Concept('CONCEPT')])
    ->executeSync();

if ($response->isSuccessful()) {
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
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "models": [
      {
        "id": "{model_id}",
        "output_info": {
          "data": {
            "concepts": [
              {
                "id": "dogs"
              }
            ]
          }
        }
      }
    ],
    "action": "merge"
  }'\
  https://api.clarifai.com/v2/models/
```
{% endtab %}
{% endtabs %}

### Remove Concepts From A Model

Conversely, if you'd like to remove concepts from a model, you can also do that.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;


...

MultiModelResponse patchModelsResponse = stub.patchModels(
    PatchModelsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove
        .addModels(
            Model.newBuilder()
                .setId("petsID")
                .setOutputInfo(
                    OutputInfo.newBuilder().setData(
                        Data.newBuilder().addConcepts(Concept.newBuilder().setId("boscoe"))
                    )
                )
        )
        .build()
);

if (patchModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch models failed, status: " + patchModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.PatchModels(
    {
        action: "remove",  // Supported actions: overwrite, merge, remove
        models: [
            {
                id: "petsID",
                output_info: {data: {concepts: [{id: "boscoe"}]}}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel({model_id}).then(function(model) {
  updateModel,
  function(err) {
    // there was an error
  }
});

function updateModel(model) {
  model.deleteConcepts({"id": "boscoe"}).then(
    function(response) {
      // do something with response
    },
    function(err) {
      // there was an error
    }
  );
}
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{model_id}')
model.delete_concepts(['boscoe'])
```
{% endtab %}

{% tab title="java" %}
```java
client.modifyModel("{{model_id}}")
    .withConcepts(Action.REMOVE, Concept.forID("dogs"))
    .executeSync();

// Or, if you have a ConceptModel object, you can do it in an OO fashion
final ConceptModel model = client.getModelByID("{{model_id}}").executeSync().get().asConceptModel();
model.modify()
    .withConcepts(Action.REMOVE, Concept.forID("dogs"))
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.API.Requests.Models;
using Clarifai.DTOs.Models;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModifyModel(
                    "petsID",
                    ModifyAction.Remove,
                    concepts: new List<Concept> {new Concept("dogs")})
                .ExecuteAsync();

// Or, if you have a ConceptModel object, you can do it in an OO fashion
            ConceptModel model = (ConceptModel) (
                    await client.GetModel<Concept>("petsID")
                        .ExecuteAsync())
                .Get();
            await model.Modify(
                    ModifyAction.Remove,
                    concepts: new List<Concept> {new Concept("dogs")})
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"dress"];
[app deleteConcepts:@[concept] fromModelWithID:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ModifyAction;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modifyModel('MODEL_ID')
    ->withModifyAction(ModifyAction::remove())
    ->withConcepts([new Concept('CONCEPT')])
    ->executeSync();

if ($response->isSuccessful()) {
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
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "models": [
      {
        "id": "{model_id}",
        "output_info": {
          "data": {
            "concepts": [
              {
                "id": "dogs"
              }
            ]
          }
        }
      }
    ],
    "action": "remove"
  }'\
  https://api.clarifai.com/v2/models/
```
{% endtab %}
{% endtabs %}

### Update Concept Name

The code below showcases how to update a concept's name given its id.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiConceptResponse patchConceptsResponse = stub.patchConcepts(
    PatchConceptsRequest.newBuilder()
        .setAction("overwrite")  // The only supported action right now is overwrite.
        .addConcepts(Concept.newBuilder().setId("boscoe").setName("Boscoe Name"))
        .build()
);

if (patchConceptsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch concepts failed, status: " + patchConceptsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.PatchConcepts(
    {
        action: "overwrite",  // The only supported action right now is overwrite
        concepts: [{id: "boscoe", name: "Boscoe Name"}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch concepts failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
** Coming Soon
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.concepts.update(concept_id='concept_id', concept_name='new_concept_name')
```
{% endtab %}

{% tab title="java" %}
```java
** Coming Soon
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

            await client.ModifyConcepts(
                    new Concept("{concept-id}", name: "{new-concept-name}"))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
** Coming Soon
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modifyConcepts((new Concept('CONCEPT'))->withName('UPDATED_CONCEPT_NAME'))
    ->executeSync();

if ($response->isSuccessful()) {
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
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "concepts": [
      {
        "id": "{concept_id}",
        "name": "{new_concept_name}"
      }
      ],
    "action": "overwrite"
  }'\
  https://api.clarifai.com/v2/concepts
```
{% endtab %}
{% endtabs %}

### Update Model Name and Configuration

Here we will change the model name to 'newname' and the model's configuration to have concepts\_mutually\_exclusive=true and closed\_environment=true.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiModelResponse patchModelsResponse = stub.patchModels(
    PatchModelsRequest.newBuilder()
        .setAction("overwrite")
        .addModels(
            Model.newBuilder()
                .setId("petsID")
                .setName("newname")
                .setOutputInfo(
                    OutputInfo.newBuilder()
                        .setData(
                            Data.newBuilder()
                                .addConcepts(Concept.newBuilder().setId("birds"))
                                .addConcepts(Concept.newBuilder().setId("hurd"))
                        )
                        .setOutputConfig(
                            OutputConfig.newBuilder()
                                .setConceptsMutuallyExclusive(true)
                                .setClosedEnvironment(true)
                        )
                )
    ).build()
);

if (patchModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch models failed, status: " + patchModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
stub.PatchModels(
    {
        action: "overwrite",
        models: [
            {
                id: "petsID",
                name: "newname",
                output_info: {
                    data: {concepts: [{id: "birds"}, {id: "hurd"}]},
                    output_config: {concepts_mutually_exclusive: true, closed_environment: true}
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
            throw new Error("Patch models failed, status: " + response.status.description);
        }
    }
);
```js
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel({model_id}).then(
  updateModel,
  function(err) {
    // there was an error
  }
);

function updateModel(model) {
  model.update({
    name: 'newname',
    conceptsMutuallyExclusive: true,
    closedEnvironment: true,
    concepts: ['birds', 'hurd']
  }).then(
}
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{model_id}')

# only update the name
model.update(model_name="newname")

# update the model attributes
model.update(concepts_mutually_exclusive=True, closed_environment=True)

# update more together
model.update(model_name="newname",
             concepts_mutually_exclusive=True, closed_environment=True)

# update attributes together with concepts
model.update(model_name="newname",
             concepts_mutually_exclusive=True,
             concepts=["birds", "hurd"])
```
{% endtab %}

{% tab title="java" %}
```java
client.modifyModel("{{model_id}}")
    .withName("newname")
    .withConceptsMutuallyExclusive(true)
    .withClosedEnvironment(true)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModifyModel(
                    "someModel",
                    name: "{newName}",
                    areConceptsMutuallyExclusive: true,
                    isEnvironmentClosed: false)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app updateModel:@"{model_id}" name:@"newName" conceptsMutuallyExclusive:NO closedEnvironment:NO completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modifyModel('MODEL_ID')
    ->withName('NEW_MODEL_NAME')
    ->withAreConceptsMutuallyExclusive(false)
    ->withIsEnvironmentClosed(false)
    ->executeSync();

if ($response->isSuccessful()) {
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
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "models": [
      {
        "id": "MODEL_ID",
        "name": "newname",
        "output_info": {
          "output_config": {
            "concepts_mutually_exclusive": true,
            "closed_environment": true
          }
        }
      }
    ],
    "action": "overwrite"
  }'\
  https://api.clarifai.com/v2/models/
```
{% endtab %}
{% endtabs %}

### Get Models

To get a list of all models including models you've created as well as [public models]():

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

...

MultiModelResponse listModelsResponse = stub.listModels(
    ListModelsRequest.newBuilder().build()
);

if (listModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List models failed, status: " + listModelsResponse.getStatus());
}

List<Model> models = listModelsResponse.getModelsList();
for (Model model : models) {
    System.out.println(model);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.ListModels(
    {},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List models failed, status: " + response.status.description);
        }

        for (const model of response.models) {
            console.log(JSON.stringify(model, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.list().then(
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

# this is a generator
app.models.get_all()
```
{% endtab %}

{% tab title="java" %}
```java
client.getModels().getPage(1).executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.GetModels()
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app getModels:1 resultsPerPage:30 completion:^(NSArray<ClarifaiModel *> *models, NSError *error) {
    NSLog(@"models: %@", models);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Models\Model;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getModels()
    ->executeSync();

if ($response->isSuccessful()) {
    $models = $response->get();

    foreach ($models as $model) {
        echo $model->modelID() . ' ' . $model->type() . "\n";
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
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models
```
{% endtab %}
{% endtabs %}

### Get Model By Id

All models have unique Ids. You can get a specific model by its id:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

SingleModelResponse getModelResponse = stub.getModel(
    GetModelRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (getModelResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get model failed, status: " + getModelResponse.getStatus());
}

Model model = getModelResponse.getModel();
System.out.println(model);
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.GetModel(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List models failed, status: " + response.status.description);
        }

        const model = response.model;
        console.log(JSON.stringify(model, null, 2));
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.get({model_id}).then(
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

# get model by id
model = app.models.get(model_id')

# get model by name
model = app.models.get('my_model1')
```
{% endtab %}

{% tab title="java" %}
```java
client.getModelByID("{model_id}").executeSync();
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

            // Change Concept to whatever the model's type is.
            await client.GetModel<Concept>("{model_id}")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app getModel:@"model_id" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Models\Model;
use Clarifai\DTOs\Models\ModelType;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getModel(ModelType::concept(), 'MODEL_ID')
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    $model = $response->get();

    echo $model->modelID() . ' ' . $model->type() . "\n";
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
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}
```
{% endtab %}
{% endtabs %}

### Get Model Output Info By Id

The output info of a model lists what concepts it contains.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

SingleModelResponse getModelOutputInfoResponse = stub.getModelOutputInfo(
    GetModelRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (getModelOutputInfoResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get model output info failed, status: " + getModelOutputInfoResponse.getStatus());
}

Model model = getModelOutputInfoResponse.getModel();
System.out.println(model);
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.GetModelOutputInfo(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List models failed, status: " + response.status.description);
        }

        const model = response.model;
        console.log(JSON.stringify(model, null, 2));
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel({model_id}).then(
  getModelOutputInfo,
  handleError
);

function getModelOutputInfo(model) {
  model.getOutputInfo().then(
    function(response) {
      // do something with response
    },
    function(err) {
      // there was an error
    }
  );
}
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('my_model1')
model.get_info(verbose=True)
```
{% endtab %}

{% tab title="java" %}
```java
client.getModelByID("{model_id}").executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Models;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            var r = await client.GetModel<Concept>("{model-id}")
                .ExecuteAsync();
            var model = (ConceptModel) r.Get();
            var outputInfo = model.OutputInfo;
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app getModelByID:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Models\Model;
use Clarifai\DTOs\Models\ModelType;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getModel(ModelType::concept(), 'MODEL_ID')
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var Model $model */
    $model = $response->get();

    $modelOutputInfo = $model->outputInfo();

    echo $modelOutputInfo->typeExt() . "\n";
    echo $modelOutputInfo->message() . "\n";
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
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/output_info
```
{% endtab %}
{% endtabs %}

### List Model Versions

Every time you train a model, it creates a new version. You can list all the versions created.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

...

MultiModelVersionResponse listModelVersionsResponse = stub.listModelVersions(
    ListModelVersionsRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (listModelVersionsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List model versions failed, status: " + listModelVersionsResponse.getStatus());
}

List<ModelVersion> modelVersions = listModelVersionsResponse.getModelVersionsList();
for (ModelVersion modelVersion : modelVersions) {
    System.out.println(modelVersion);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.ListModelVersions(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List model versions failed, status: " + response.status.description);
        }

        for (const model_version of response.model_versions) {
            console.log(JSON.stringify(model_version, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel('{id}').then(
  function(model) {
    model.getVersions().then(
      function(response) {
        // do something with response
      },
      function(err) {
        // there was an error
      }
    );
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

model = app.models.get('{id}')
model.list_versions()
```
{% endtab %}

{% tab title="java" %}
```java
client.getModelVersions("{model_id}").getPage(1).executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.GetModelVersions("{model_id}")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app listVersionsForModel:@"{model_id}" page:1 resultsPerPage:30 completion:^(NSArray<ClarifaiModelVersion *> *versions, NSError *error) {
    NSLog(@"versions: %@", versions);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Models\ModelVersion;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getModelVersions('MODEL_ID')
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var ModelVersion[] $modelVersions */
    $modelVersions = $response->get();
    foreach ($modelVersions as $modelVersion) {
        echo $modelVersion->id() . ' ' . $modelVersion->modelTrainingStatus() . "\n";
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
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions
```
{% endtab %}
{% endtabs %}

### Get Model Version By Id

To get a specific model version, you must provide the model\_id as well as the version\_id. You can inspect the model version status to determine if your model is trained or still training.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...


SingleModelVersionResponse getModelVersionResponse = stub.getModelVersion(
    GetModelVersionRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")
        .build()
);

if (getModelVersionResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get model version failed, status: " + getModelVersionResponse.getStatus());
}

ModelVersion modelVersion = getModelVersionResponse.getModelVersion();
System.out.println(modelVersion);
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.GetModelVersion(
    {model_id: "petsID", version_id: "{YOUR_MODEL_VERSION_ID}"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get model version failed, status: " + response.status.description);
        }

        const model_version = response.model_version;
        console.log(JSON.stringify(model_version, null, 2));
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel('{id}').then(
  function(model) {
    model.getVersion('{version_id}').then(
      function(response) {
        // do something with response
      },
      function(err) {
        // there was an error
      }
    );
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

model = app.models.get('{id}')
model.get_version('{version_id}')
```
{% endtab %}

{% tab title="java" %}
```java
client.getModelVersionByID("{model_id}", "{version_id}").executeSync();

// Or in a more object-oriented manner:
client.getModelByID("{model_id}")
    .executeSync().get() // Returns Model object
    .getVersionByID("{version_id}").executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.GetModelVersion("{model_id}", "{version_id}")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app getVersionForModel:@"{model_id}" versionID:{version_id} completion:^(ClarifaiModelVersion *version, NSError *error) {
    NSLog(@"version: %@", version);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Models\ModelVersion;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getModelVersion('MODEL_ID', 'MODEL_VERSION_ID')
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var ModelVersion $modelVersion */
    $modelVersion = $response->get();
    echo $modelVersion->id() . ' ' . $modelVersion->modelTrainingStatus() . "\n";

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
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions/{version_id}
```
{% endtab %}
{% endtabs %}

### Get Model Training Inputs

You can list all the inputs that were used to train the model.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiInputResponse listModelInputsResponse = stub.listModelInputs(
    ListModelInputsRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (listModelInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List model inputs failed, status: " + listModelInputsResponse.getStatus());
}

List<Input> inputs = listModelInputsResponse.getInputsList();
for (Input input : inputs) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.ListModelInputs(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List model inputs failed, status: " + response.status.description);
        }

        for (const input of response.inputs) {
            console.log(JSON.stringify(input, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel('{id}').then(
  function(model) {
    model.getInputs().then(
      function(response) {
        // do something with response
      },
      function(err) {
        // there was an error
      }
    );
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

model = app.models.get('{id}')
model.get_inputs()
```
{% endtab %}

{% tab title="java" %}
```java
client.getModelInputs("{model_id}").getPage(1).executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.GetModelInputs("{model_id}")
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app listTrainingInputsForModel:@"{model_id}" page:1 resultsPerPage:30 completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
// Coming soon
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/inputs
```
{% endtab %}
{% endtabs %}

### Get Model Training Inputs By Version

You can also list all the inputs that were used to train a specific model version.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

...

MultiInputResponse listModelInputsResponse = stub.listModelInputs(
    ListModelInputsRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")
        .build()
);

if (listModelInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List model inputs failed, status: " + listModelInputsResponse.getStatus());
}

List<Input> inputs = listModelInputsResponse.getInputsList();
for (Input input : inputs) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.ListModelInputs(
    {
        model_id: "petsID",
        version_id: "{YOUR_MODEL_VERSION_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List model inputs failed, status: " + response.status.description);
        }

        for (const input of response.inputs) {
            console.log(JSON.stringify(input, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.initModel({id: '{model_id}', version: '{version_id}'}).then(
  function(model) {
    model.getInputs().then(
      function(response) {
        // do something with response
      },
      function(err) {
        // there was an error
      }
    );
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

model = app.models.get('{id}')
model.get_inputs('{version_id}')
```
{% endtab %}

{% tab title="java" %}
```java
client.getModelInputs("{model_id}")
    .fromSpecificModelVersion("{version_id}")
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.GetModelInputs("{model_id}", "{version_id}")
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app listTrainingInputsForModel:@"{model_id}" page:1 resultsPerPage:30 completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
// Coming soon
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions/{version_id}/inputs
```
{% endtab %}
{% endtabs %}

### Delete A Model

You can delete a model using the model\_id.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

BaseResponse deleteModelResponse = stub.deleteModel(
    DeleteModelRequest.newBuilder()
        .setModelId("pets")
        .build()
);

if (deleteModelResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete model failed, status: " + deleteModelResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.DeleteModel(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete model failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.delete('{id}').then(
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

app.models.delete('{id}')
```
{% endtab %}

{% tab title="java" %}
```java
client.deleteModel("{model_id}").executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.DeleteModel("{model_id}")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app deleteModel:@"{model_id}" completion:^(NSError *error) {
    NSLog(@"model is deleted");
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->deleteModel('MODEL_ID')
    ->executeSync();

if ($response->isSuccessful()) {
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
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}
```
{% endtab %}
{% endtabs %}

### Delete A Model Version

You can also delete a specific version of a model with the model\_id and version\_id.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

BaseResponse deleteModelVersionResponse = stub.deleteModelVersion(
    DeleteModelVersionRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")
        .build()
);

if (deleteModelVersionResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete model version failed, status: " + deleteModelVersionResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.DeleteModelVersion(
    {
        model_id: "petsID",
        version_id: "{YOUR_MODEL_VERSION_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete model version failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.delete('{model_id}', '{version_id}').then(
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

app.models.delete('{id}', '{version_id}')

# or

model = app.models.get('{id}')
model.delete_version('{version_id}')
```
{% endtab %}

{% tab title="java" %}
```java
client.deleteModelVersion("{model_id}", "{version_id}").executeSync();

// Or in a more object-oriented manner:
client.getModelByID("{model_id}")
    .executeSync().get() // Returns Model object
    .deleteVersion("{version_id}")
    .executeSync();
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

            await client.DeleteModelVersion("{model_id}", "{version_id}")
                .ExecuteAsync();

            // Or in a more object-oriented manner:
            var model = (await client.GetModel<Concept>("{model_id}")
                .ExecuteAsync()).Get();  // Returns a Model<Concept> object.
            await model.DeleteModelVersion("{version_id}").ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app deleteVersionForModel:{model_id} versionID:{version_id} completion:^(NSError *error) {
    NSLog(@"model version deleted");
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->deleteModelVersion('MODEL_ID', 'MODEL_VERSION_ID')
    ->executeSync();

if ($response->isSuccessful()) {
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
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions/{version_id}
```
{% endtab %}
{% endtabs %}

### Delete All Models

If you would like to delete all models associated with an application, you can also do that. Please proceed with caution as these cannot be recovered.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

BaseResponse deleteModelsResponse = stub.deleteModels(
    DeleteModelsRequest.newBuilder()
        .setDeleteAll(true)
        .build()
);

if (deleteModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete models failed, status: " + deleteModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.DeleteModels(
    {delete_all: true},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.delete().then(
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

app.models.delete_all()
```
{% endtab %}

{% tab title="java" %}
```java
client.deleteAllModels().executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.DeleteAllModels()
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app deleteAllModels:^(NSError *error) {
    NSLog(@"delete all models");
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use ClarifaiIntTests\BaseIntTest;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->deleteAllModels()
    ->executeSync();

if ($response->isSuccessful()) {
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
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/
```
{% endtab %}
{% endtabs %}

### Train A Model

When you train a model, you are telling the system to look at all the images with concepts you've provided and learn from them. This train operation is asynchronous. It may take a few seconds for your model to be fully trained and ready.

_Note: you can repeat this operation as often as you like. By adding more images with concepts and training, you can get the model to predict exactly how you want it to._

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

SingleModelResponse postModelVersionsResponse = stub.postModelVersions(
    PostModelVersionsRequest.newBuilder()
        .setModelId("petsID")
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
```js
stub.PostModelVersions(
    {model_id: "petsID"},
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

if ($response->isSuccessful()) {
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
  https://api.clarifai.com/v2/models/{model_id}/versions
```
{% endtab %}
{% endtabs %}

## Predict With A Model

Once you have trained a model you are ready to use your new model to get predictions. The predictions returned will only contain the concepts that you told it to see.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")  // Optional. Defaults to the latest version.
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
        model_id: "petsID",
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
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.predict("{model_id}", ["https://samples.clarifai.com/puppy.jpeg"]).then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

// or if you have an instance of a model

model.predict("https://samples.clarifai.com/puppy.jpeg").then(
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

response = model.predict_by_url('https://samples.clarifai.com/puppy.jpeg')
```
{% endtab %}

{% tab title="java" %}
```java
client.predict("{model_id}")
    .withInputs(
        ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpeg")
    )
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
                    "{model_id}",
                    new ClarifaiURLImage("https://samples.clarifai.com/puppy.jpeg"))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpeg"]
[app getModel:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
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

$response = $client->predict(ModelType::concept(), 'MODEL_ID',
        new ClarifaiURLImage('https://samples.clarifai.com/puppy.jpeg'))
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
            "url": "https://samples.clarifai.com/puppy.jpeg"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/{model_id}/outputs
```
{% endtab %}
{% endtabs %}

### Search Models By Name And Type

You can search all your models by name and type of model.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

...

MultiModelResponse postModelsSearchesResponse = stub.postModelsSearches(
    PostModelsSearchesRequest.newBuilder()
        .setModelQuery(
            ModelQuery.newBuilder()
                .setName("gen*")
                .setType("concept")
        )
        .build()
);

if (postModelsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models searches failed, status: " + postModelsSearchesResponse.getStatus());
}

List<Model> models = postModelsSearchesResponse.getModelsList();
for (Model model : models) {
    System.out.println(model);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.PostModelsSearches(
    {
        model_query: {
            name: "gen*",
            type: "concept"
        }
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model searches failed, status: " + response.status.description);
        }

        const models = response.models;
        for (const model of models) {
            console.log(JSON.stringify(model, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.models.search('general-v1.3', 'concept').then(
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

# search model name
app.models.search('general-v1.3')

# search model name and type
app.models.search(model_name='general-v1.3', model_type='concept')
```
{% endtab %}

{% tab title="java" %}
```java
client.findModel()
    .withModelType(ModelType.CONCEPT)
    .withName("general-v1.3")
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Models;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.SearchModels(
                    modelType: ModelType.Concept,
                    name: "general-v1.3")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app searchForModelByName:@"general-v1.3" modelType:ClarifaiModelTypeConcept completion:^(NSArray<ClarifaiModel *> *models, NSError *error) {
    NSLog(@"models: %@", models);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Models\Model;
use Clarifai\DTOs\Models\ModelType;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchModels('general*', ModelType::concept())
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var Model[] $models */
    $models = $response->get();

    foreach ($models as $model) {
        echo $model->name() . ' ' . $model->type() . "\n";
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
    "model_query": {
      "name": "general-v1.3",
      "type": "concept"
    }
  }'\
  https://api.clarifai.com/v2/models/searches
```
{% endtab %}
{% endtabs %}

