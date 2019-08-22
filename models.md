## Models

There are many methods to work with models.

### Create Model

You can create your own model and train it with your own images and concepts. Once you train it to see how
you would like it to see, you can then use that model to make predictions.

When you create a model you give it a name and an id. If you don't supply an id, one will be created for you.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.create("petsID").then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.models.create('petsID')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.createModel("petsID").executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app createModel:nil name:@"petsModel" modelID:@"petsID" conceptsMutuallyExclusive:NO closedEnvironment:NO completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

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
{% endcode-tabs-item %}
{% endcode-tabs %}






### Create Model With Concepts

You can also create a model and initialize it with the concepts it will contain. You can always add and
remove concepts later.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.create('petsID', concepts=['boscoe'])

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.createModel("petsID")
    .withOutputInfo(ConceptOutputInfo.forConcepts(
        Concept.forID("boscoe")
    ))
    .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app createModel:@[@"cat", @"dog"] name:@"petsModel" modelID:@"petsID" conceptsMutuallyExclusive:NO closedEnvironment:NO completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

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
{% endcode-tabs-item %}
{% endcode-tabs %}




### Add Concepts To A Model

You can add concepts to a model at any point. As you add concepts to inputs, you may want to add them to your
model.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{model_id}')
model.add_concepts(['boscoe'])

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"dress"];
[app addConcepts:@[concept] toModelWithID:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

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
{% endcode-tabs-item %}
{% endcode-tabs %}




### Remove Concepts From A Model

Conversely, if you'd like to remove concepts from a model, you can also do that.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{model_id}')
model.delete_concepts(['boscoe'])

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"dress"];
[app deleteConcepts:@[concept] fromModelWithID:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

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
{% endcode-tabs-item %}
{% endcode-tabs %}




### Update Concept Name
The code below showcases how to update a concept's name given its id.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
** Coming Soon
```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.concepts.update(concept_id='concept_id', concept_name='new_concept_name')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

** Coming Soon

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

** Coming Soon

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

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
{% endcode-tabs-item %}
{% endcode-tabs %}




### Update Model Name and Configuration

Here we will change the model name to 'newname' and the model's configuration to have concepts_mutually_exclusive=true and closed_environment=true.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.modifyModel("{{model_id}}")
    .withName("newname")
    .withConceptsMutuallyExclusive(true)
    .withClosedEnvironment(true)
    .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app updateModel:@"{model_id}" name:@"newName" conceptsMutuallyExclusive:NO closedEnvironment:NO completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

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
{% endcode-tabs-item %}
{% endcode-tabs %}





### Get Models

To get a list of all models including models you've created as well as
[public models](public-models.md):




{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.list().then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

# this is a generator
app.models.get_all()

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.getModels().getPage(1).executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app getModels:1 resultsPerPage:30 completion:^(NSArray<ClarifaiModel *> *models, NSError *error) {
    NSLog(@"models: %@", models);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Get Model By Id

All models have unique Ids. You can get a specific model by its id:




{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.get({model_id}).then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

# get model by id
model = app.models.get(model_id')

# get model by name
model = app.models.get('my_model1')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.getModelByID("{model_id}").executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app getModel:@"model_id" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Get Model Output Info By Id

The output info of a model lists what concepts it contains.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('my_model1')
model.get_info(verbose=True)

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.getModelByID("{model_id}").executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app getModelByID:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
    NSLog(@"model: %@", model);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/output_info

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### List Model Versions

Every time you train a model, it creates a new version. You can list all the versions created.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{id}')
model.list_versions()

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.getModelVersions("{model_id}").getPage(1).executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[app listVersionsForModel:@"{model_id}" page:1 resultsPerPage:30 completion:^(NSArray<ClarifaiModelVersion *> *versions, NSError *error) {
    NSLog(@"versions: %@", versions);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Get Model Version By Id

To get a specific model version, you must provide the model_id as well as the version_id. You can inspect the
model version status to determine if your model is trained or still training.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{id}')
model.get_version('{version_id}')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.getModelVersionByID("{model_id}", "{version_id}").executeSync();

// Or in a more object-oriented manner:
client.getModelByID("{model_id}")
    .executeSync().get() // Returns Model object
    .getVersionByID("{version_id}").executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[app getVersionForModel:@"{model_id}" versionID:{version_id} completion:^(ClarifaiModelVersion *version, NSError *error) {
    NSLog(@"version: %@", version);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions/{version_id}

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Get Model Training Inputs

You can list all the inputs that were used to train the model.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{id}')
model.get_inputs()

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.getModelInputs("{model_id}").getPage(1).executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[app listTrainingInputsForModel:@"{model_id}" page:1 resultsPerPage:30 completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
// Coming soon
```


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/inputs

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Get Model Training Inputs By Version

You can also list all the inputs that were used to train a specific model version.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{id}')
model.get_inputs('{version_id}')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.getModelInputs("{model_id}")
    .fromSpecificModelVersion("{version_id}")
    .getPage(1)
    .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app listTrainingInputsForModel:@"{model_id}" page:1 resultsPerPage:30 completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
// Coming soon
```


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions/{version_id}/inputs

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Delete A Model

You can delete a model using the model_id.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.delete('{id}').then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.models.delete('{id}')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.deleteModel("{model_id}").executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[app deleteModel:@"{model_id}" completion:^(NSError *error) {
    NSLog(@"model is deleted");
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Delete A Model Version

You can also delete a specific version of a model with the model_id and version_id.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.delete('{model_id}', '{version_id}').then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.models.delete('{id}', '{version_id}')

# or

model = app.models.get('{id}')
model.delete_version('{version_id}')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.deleteModelVersion("{model_id}", "{version_id}").executeSync();

// Or in a more object-oriented manner:
client.getModelByID("{model_id}")
    .executeSync().get() // Returns Model object
    .deleteVersion("{version_id}")
    .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[app deleteVersionForModel:{model_id} versionID:{version_id} completion:^(NSError *error) {
    NSLog(@"model version deleted");
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/{model_id}/versions/{version_id}

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Delete All Models

If you would like to delete all models associated with an application, you can also do that. Please proceed
with caution as these cannot be recovered.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.delete().then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.models.delete_all()

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.deleteAllModels().executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[_app deleteAllModels:^(NSError *error) {
    NSLog(@"delete all models");
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Train A Model

When you train a model, you are telling the system to look at all the images with concepts
you've provided and learn from them. This train operation is asynchronous. It may take a few seconds for your
model to be fully trained and ready.

*Note: you can repeat this operation as often as you like. By adding more images with concepts and training,
you can get the model to predict exactly how you want it to.*



{% code-tabs %}
{% code-tabs-item title="js" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('{model_id}')
model.train()

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.trainModel("{model_id}").executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpg"]
[app getModel:@"{id}" completion:^(ClarifaiModel *model, NSError *error) {
    [model train:^(ClarifaiModel *model, NSError *error) {
        NSLog(@"model: %@", model);
    }];
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/models/{model_id}/versions

```
{% endcode-tabs-item %}
{% endcode-tabs %}




## Predict With A Model

Once you have trained a model you are ready to use your new model to get
predictions. The predictions returned will only contain the concepts that you told it to see.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.predict("{model_id}", ["https://samples.clarifai.com/puppy.jpg"]).then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

// or if you have an instance of a model

model.predict("https://samples.clarifai.com/puppy.jpg").then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('YOUR_MODEL_ID')

response = model.predict_by_url('https://samples.clarifai.com/puppy.jpg')
```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.predict("{model_id}")
    .withInputs(
        ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpg")
    )
    .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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
                    new ClarifaiURLImage("https://samples.clarifai.com/puppy.jpg"))
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpg"]
[app getModel:@"{model_id}" completion:^(ClarifaiModel *model, NSError *error) {
    [model predictOnImages:@[image]
                completion:^(NSArray<ClarifaiSearchResult *> *outputs, NSError *error) {
                    NSLog(@"outputs: %@", outputs);
                }];
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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


{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
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
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/{model_id}/outputs

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Search Models By Name And Type

You can search all your models by name and type of model.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.models.search('general-v1.3', 'concept').then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

# search model name
app.models.search('general-v1.3')

# search model name and type
app.models.search(model_name='general-v1.3', model_type='concept')

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.findModel()
    .withModelType(ModelType.CONCEPT)
    .withName("general-v1.3")
    .getPage(1)
    .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

[app searchForModelByName:@"general-v1.3" modelType:ClarifaiModelTypeConcept completion:^(NSArray<ClarifaiModel *> *models, NSError *error) {
    NSLog(@"models: %@", models);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

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
{% endcode-tabs-item %}
{% endcode-tabs %}
