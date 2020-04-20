# Inputs

## Inputs

The API is built around a simple idea. You send inputs \(images\) to the service and it returns predictions. In addition to receiving predictions on inputs, you can also index inputs and their predictions to later search against. You can also index inputs with concepts to later train your own model.

When you add an input to your app, the base workflow of your app runs, computing the outputs from all the models in that workflow and indexes those outputs. Those indexed outputs are what incur the indexing fee monthly, and enablessearch and training on top of the outputs of the base workflow models.

### Add Inputs

You can add inputs one by one or in bulk. If you do send bulk, you are limited to sending 128 inputs at a time.

**Important: adding inputs is an asynchronous operation.** That means it will process indexing of your inputs through your default workflow in the background, which can take some time. In order to check the status of each input you add, see the section on [Get Input by ID](inputs.md#get-input-by-id) to look for status 30000 \(INPUT\_IMAGE\_DOWNLOAD\_SUCCESS\) status code on each input to know when it's successfully been indexed.

#### Add an input using a publicly accessible URL

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.create({
  url: "https://samples.clarifai.com/metro-north.jpg"
}).then(
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

app.inputs.create_image_from_url("https://samples.clarifai.com/metro-north.jpg")
```
{% endtab %}

{% tab title="java" %}
```java
client.addInputs()
    .plus(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
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

            await client.AddInputs(
                    new ClarifaiURLImage("https://samples.clarifai.com/metro-north.jpg"))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/metro-north.jpg"];
[app addInputs:@[image] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->addInputs(
        new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'))
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
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

#### Add an input using bytes

The data must be base64 encoded. When you add a base64 image to our servers, a copy will be stored and hosted on our servers. If you already have an image hosting service we recommend using it and adding images via the `url` parameter.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.create({
  base64: "Zvfauhti4D..."
}).then(
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

# add from filename
app.inputs.create_image_from_filename(filename)

# add from base64 bytes
app.inputs.create_image_from_base64(base64_bytes)
```
{% endtab %}

{% tab title="java" %}
```java
client.addInputs()
    .plus(ClarifaiInput.forImage(new File("image.png")))
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.IO;
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

            await client.AddInputs(
                    new ClarifaiFileImage(File.ReadAllBytes("image.png")))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *imageFromImage = [[ClarifaiImage alloc] initWithImage:@"dress.jpg"];
[app addInputs:@[imageFromImage] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiFileImage;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->addInputs(
        new ClarifaiFileImage(file_get_contents('/home/user/image.png')))
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
    "inputs": [
      {
        "data": {
          "image": {
            "base64": '"`base64 /home/user/image.jpeg`"'"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

#### Add multiple inputs with ids

{% hint style="info" %}
In cases where you have your own `id` and you only have one item per image, you are encouraged to send inputs with your own `id`. This will help you later match the input to your own database. If you do not send an `id`, one will be created for you. If you have more than one item per image, it is recommended that you put the product id in metadata.
{% endhint %}

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.create([
  {
    url: "https://samples.clarifai.com/metro-north.jpg",
    id: 'train1'
  },
  {
    url: "https://samples.clarifai.com/puppy.jpeg",
    id: 'puppy1'
  }
]).then(
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
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='YOUR_API_KEY')

img1 = ClImage(url="https://samples.clarifai.com/metro-north.jpg", image_id="train1")
img2 = ClImage(url="https://samples.clarifai.com/puppy.jpeg", image_id="puppy1")

app.inputs.bulk_create_images([img1, img2])
```
{% endtab %}

{% tab title="java" %}
```java
client.addInputs()
    .plus(
        ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg")
            .withConcepts(Concept.forID("id1")),
        ClarifaiInput.forImage("https://samples.clarifai.com/wedding.jpg")
            .withConcepts(Concept.forID("id2"))
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
                        "https://samples.clarifai.com/metro-north.jpg",
                        positiveConcepts: new List<Concept> {new Concept("id1")}),
                    new ClarifaiURLImage(
                        "https://samples.clarifai.com/wedding.jpg",
                        positiveConcepts: new List<Concept> {new Concept("id2")}))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *train = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/metro-north.jpg"];
train.inputID = @"train";

ClarifaiImage *puppy = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpeg"];
puppy.inputID = @"puppy";

[app addInputs:@[train, puppy] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
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

$response = $client->addInputs([
        (new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'))
            ->withPositiveConcepts([new Concept('id1')]),
        (new ClarifaiURLImage('https://samples.clarifai.com/wedding.jpg'))
            ->withPositiveConcepts([new Concept('id2')]),
    ])
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
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        },
        "id": "{id1}"
      },
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg"
          }
        },
        "id": "{id2}"
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### Add inputs with concepts

If you would like to add an input with concepts, you can do so like this. Concepts play an important role in creating your own models using your own concepts. You can learn more about [creating your own models](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/train.md) above. Concepts also help you search for inputs. You can [learn more about search](../search/) here.

When you add a concept to an input, you need to indicate whether the concept is present in the image or if it is not present.

You can add inputs with concepts as either a URL or bytes.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.create({
  url: "https://samples.clarifai.com/puppy.jpeg",
  concepts: [
    {
      id: "boscoe",
      value: true
    }
  ]
}).then(
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
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='YOUR_API_KEY')

# add by url
app.inputs.create_image_from_url("https://samples.clarifai.com/puppy.jpeg", concepts=['boscoe'])

# add by base64 bytes
app.inputs.create_image_from_base64(base64_bytes, concepts=['boscoe'])

# add by raw bytes
app.inputs.create_image_from_bytes(raw_bytes, concepts=['boscoe'])

# add by local file
app.inputs.create_image_from_filename(local_filename, concepts=['boscoe'])

# add multiple with concepts
img1 = ClImage(url="https://samples.clarifai.com/puppy.jpeg", concepts=['boscoe'], not_concepts=['our_wedding'])
img2 = ClImage(url="https://samples.clarifai.com/wedding.jpg", concepts=['our_wedding'], not_concepts=['cat','boscoe'])

app.inputs.bulk_create_images([img1, img2])
```
{% endtab %}

{% tab title="java" %}
```java
client.addInputs()
    .plus(ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpeg")
        .withConcepts(
            // To mark a concept as being absent, chain `.withValue(false)`
            Concept.forID("boscoe")
        )
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
                        // To mark a concept as being absent, use negativeConcepts
                        positiveConcepts: new List<Concept> {new Concept("boscoe")}))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *puppy = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpeg"
                                              andConcepts:@[@"cute puppy"]];

[app addInputs:@[puppy] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
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
        (new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'))
            ->withPositiveConcepts([new Concept('id1')]))
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
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg"
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
{% endtab %}
{% endtabs %}

### Add inputs with custom metadata

In addition to adding an input with concepts, you can also add an input with custom metadata. This metadata will then be [searchable](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/advanced-searches.md#by-custom-metadata). Metadata can be any arbitrary JSON.

{% hint style="info" %}
If you have more than one item per image it is recommended to put the id in metadata like:

```text
{
  "product_id": "xyz"
}
```
{% endhint %}

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.create({
  url: "https://samples.clarifai.com/puppy.jpeg",
  metadata: {id: 'id001', type: 'plants', size: 100}
}).then(
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
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='YOUR_API_KEY')

# metadata must be defined as JSON object
metadata = {'id':'id001', 'type':'plants', 'size':100}

# adding metadata along with url, filename, etc
app.inputs.create_image_from_url(url="https://samples.clarifai.com/puppy.jpeg", metadata=metadata)
app.inputs.create_image_from_filename(filename="aa.jpg", metadata=metadata)

# define an image with metadata for bulk import
img = Image(url="", metadata=metadata)

app.inputs.bulk_create_images([img])
```
{% endtab %}

{% tab title="java" %}
```java
final JsonObject metadata = new JsonObject();
metadata.addProperty("isPuppy", true);
client.addInputs()
    .plus(
        ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpeg")
            .withMetadata(metadata)
    ).executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;
using Newtonsoft.Json.Linq;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            var metadata = new JObject(
                new JProperty("key1", "val1"),
                new JProperty("key2", "val2"));
            await client.AddInputs(
                    new ClarifaiURLImage(
                        "https://samples.clarifai.com/puppy.jpeg",
                        metadata: metadata))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *puppy = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/puppy.jpeg"
                                              andConcepts:@[@"cute puppy"]];
puppy.metadata = @{@"my_key": @[@"my",@"values"], @"cuteness": @"extra-cute"};
[app addInputs:@[puppy] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
  NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
//coming soon
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
          "metadata": {
            "key": "value",
            "list":[1,2,3]
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### Get inputs

You can list all the inputs \(images\) you have previously added either for [search](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/advanced-searches.md) or [train](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/train.md).

If you added inputs with concepts, they will be returned in the response as well.

This request is paginated.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.list({page: 1, perPage: 20}).then(
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
app.inputs.get_all()

# get a page of inputs
app.inputs.get_by_page(page=1, per_page=20)
```
{% endtab %}

{% tab title="java" %}
```java
client.getInputs() // optionally takes a perPage parameter
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

            await client.GetInputs()
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app getInputsOnPage:1 pageSize:20 completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiInput;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getInputs()->executeSync();

if ($response->isSuccessful()) {
    $inputs = $response->get();
    foreach ($inputs as $input) {
        echo $input->id() . "\n";
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
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### Get input by id

If you'd like to get a specific input by id, you can do that as well.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.get({id}).then(
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

image = app.inputs.get(input_id)
```
{% endtab %}

{% tab title="java" %}
```java
client.getInputByID("{id}").executeSync();
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

            await client.GetInput("{id}")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app getInput:input_id completion:^(ClarifaiInput *input, NSError *error) {
    NSLog(@"input": %@, input);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getInput('{input_id}')->executeSync();

if ($response->isSuccessful()) {
    // Here we "cast" from ClarifaiInput to ClarifaiURLImage.
    $input = $response->get();
    echo $input->url();
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
  https://api.clarifai.com/v2/inputs/{id}
```
{% endtab %}
{% endtabs %}

### Get inputs status

If you add inputs in bulk, they will process in the background. You can get the status of all your inputs \(processed, to\_process and errors\) like this:

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.getStatus().then(
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

app.inputs.check_status()
```
{% endtab %}

{% tab title="java" %}
```java
client.getInputsStatus().executeSync();
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

            await client.GetInputsStatus()
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app getInputsStatus:^(int numProcessed, int numToProcess, int errors, NSError *error) {
    NSLog(@"number of inputs processed: %d", numProcessed);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiInputsStatus;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getInputsStatus()->executeSync();

if ($response->isSuccessful()) {
    $inputsStatus = $response->get();
    echo 'Num. processed: ' . $inputsStatus->processed() . "\n";
    echo 'Num. processing: ' . $inputsStatus->processing() . "\n";
    echo 'Num. to process: ' . $inputsStatus->toProcess() . "\n";
    echo 'Num. errors: ' . $inputsStatus->errors() . "\n";
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
  https://api.clarifai.com/v2/inputs/status
```
{% endtab %}
{% endtabs %}

## Update inputs

### Update input with concepts

To update an input with a new concept, or to change a concept value from true/false, you can do that:

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.mergeConcepts([
  {
    id: "{id}",
    concepts: [
      {
        id: "tree"
      },
      {
        id: "water",
        value: false
      }
    ]
  },
])


// or if you have an input instance
app.inputs.get({id}).then(
  function(input) {
    input.mergeConcepts([
      {
        id: "tree",
        value: true
      },
      {
        id: "water",
        value: false
      }
    ])
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

app.inputs.merge_concepts('{id}', concepts=['tree'], not_concepts=['water'])
```
{% endtab %}

{% tab title="java" %}
```java
client.mergeConceptsForInput("{input_id}")
    .plus(
        Concept.forID("tree"),
        Concept.forID("water").withValue(false)
    )
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.API.Requests.Models;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModifyInput(
                    "{input_id}",
                    ModifyAction.Merge,
                    positiveConcepts: new List<Concept> {new Concept("tree")},
                    negativeConcepts: new List<Concept> {new Concept("water")})
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"cute cat"];
[_app addConcepts:@[concept] forInputWithID:@"{id}" completion:^(ClarifaiInput *input, NSError *error) {
    NSLog(@"input: %@", input);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ModifyAction;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modifyInput('{input_id}', ModifyAction::merge())
    ->withPositiveConcepts([new Concept('tree')])
    ->withNegativeConcepts([new Concept('water')])
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
    "inputs": [
      {
        "id": "{id}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": true
            },
            {
              "id": "water",
              "value": false
            }
          ]
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### Bulk update inputs with concepts

You can update an existing input using its Id. This is useful if you'd like to add concepts to an input after its already been added.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.mergeConcepts([
  {
    id: "{id1}",
    concepts: [
      {
        id: "tree",
        value: true
      },
      {
        id: "water",
        value: false
      }
    ]
  },
  {
    id: "{id2}",
    concepts: [
      {
        id: "animal",
        value: true
      },
      {
        id: "fruit",
        value: false
      }
    ]
  }
]).then(
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

input_ids = ["{id1}", "{id2}"]
concept_pairs = [
                 [('tree', True), ('water', False)],
                 [('animal', True), ('fruit', False)],
                ]
app.inputs.bulk_merge_concepts(input_ids, concept_pairs)
```
{% endtab %}

{% tab title="java" %}
```java
// Coming soon
```
{% endtab %}

{% tab title="csharp" %}
```csharp
// Coming soon
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiConcept *newConcept = [[ClarifaiConcept alloc] initWithConceptID:@"tree"];
[_app getInput:@"{input_id}" completion:^(ClarifaiInput *input, NSError *error) {
  // Add tree concept to each current input's concept list.
  NSMutableArray *newConceptList = [NSMutableArray arrayWithArray:input.concepts];
  [newConceptList addObject:newConcept];
  input.concepts = newConceptList;

  // Merge the new list for one or more inputs.
  [_app mergeConceptsForInputs:@[input] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error)   {
    NSLog(@"updated inputs: %@", inputs);
  }];
}];
```
{% endtab %}

{% tab title="php" %}
```php
//coming soon
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{id1}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": true
            },
            {
              "id": "water",
              "value": false
            }
          ]
        }
      },
      {
        "id": "{id2}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": true
            },
            {
              "id": "water",
              "value": false
            }
          ]
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

## Delete inputs

### Delete concepts from an input

To remove concepts that were already added to an input, you can do this:

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.deleteConcepts([
  {
    id: "{id}",
    concepts: [
      {
        id: "tree"
      },
      {
        id: "water",
        value: false
      }
    ]
  },
])

// or if you have an input instance
app.inputs.get({id}).then(
  function(input) {
    input.deleteConcepts([
      {
        id: "tree",
        value: true
      },
      {
        id: "water",
        value: false
      }
    ])
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

app.inputs.delete_concepts({id}, concepts=['tree', 'water'])
```
{% endtab %}

{% tab title="java" %}
```java
client.removeConceptsForInput("{input_id}")
    .plus(
        Concept.forID("tree"),
        Concept.forID("water")
    )
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.API.Requests.Models;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModifyInput(
                    "INPUT_ID",
                    ModifyAction.Remove,
                    positiveConcepts: new List<Concept> {new Concept("tree")},
                    negativeConcepts: new List<Concept> {new Concept("water")})
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"cute cat"];
[app deleteConcepts:@[concept] forInputWithID:{id} completion:^(ClarifaiInput *input, NSError *error) {
    NSLog(@"input: %@", input);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ModifyAction;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modifyInput('INPUT_ID', ModifyAction::remove())
    ->withPositiveConcepts([new Concept('tree')])
    ->withNegativeConcepts([new Concept('water')])
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
    "inputs": [
      {
        "id":"{{asset_id}}",
        "data": {
            "concepts":[
                {"id":"mattid2", "value":true},
                {"id":"ferrari", "value":false}
            ]
        }
      }
    ],
    "action":"remove"
  }'\
  https://api.clarifai.com/v2/inputs/
```
{% endtab %}
{% endtabs %}

### Bulk delete concepts from a list of inputs

You can bulk delete multiple concepts from a list of inputs:

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.deleteConcepts([
  {
    id: "{id1}",
    concepts: [
      { id: "tree" },
      { id: "water" }
    ]
  },
  {
    id: "{id2}",
    concepts: [
      { id: "animal" },
      { id: "fruit" }
    ]
  }
]).then(
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

input_ids = ["{id1}", "{id2}"]
concept_pairs = [
                 ['tree', 'water'],
                 ['animal', 'fruit']
                ]
app.inputs.bulk_delete_concepts(input_ids, concept_pairs)
```
{% endtab %}

{% tab title="java" %}
```java
// Coming soon
```
{% endtab %}

{% tab title="csharp" %}
```csharp
// Coming soon
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"cute cat"];
[app deleteConcepts:@[concept] forInputWithID:input_id completion:^(ClarifaiInput *input, NSError *error) {
    NSLog(@"input: %@", input);
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
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{id1}",
        "data": {
          "concepts":[
            {
              "id": "mattid2"
            },
            {
              "id": "ferrari"
            }
          ]
        }
      },
      {
        "id": "{id2}",
        "data": {
          "concepts":[
            {
              "id": "mattid2"
            },
            {
              "id": "ferrari"
            }
          ]
        }
      }
    ],
    "action":"remove"
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### Delete Input By Id

You can delete a single input by id:

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.delete(INPUT_ID).then(
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

app.inputs.delete("INPUT_ID")
```
{% endtab %}

{% tab title="java" %}
```java
client.deleteInput("INPUT_ID")
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

            await client.DeleteInputs("INPUT_ID")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app deleteInputsByIDList:@[INPUT_ID] completion:^(NSError *error) {
    NSLog(@"input has been deleted");
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->deleteInputs('INPUT_ID')
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
  https://api.clarifai.com/v2/inputs/<INPUT_ID>
```
{% endtab %}
{% endtabs %}

### Delete a list of inputs

You can also delete multiple inputs in one API call. This will happen asynchronously.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.delete([{id1}, {id2}]).then(
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

app.delete(["{id1}", "{id2}"])
```
{% endtab %}

{% tab title="java" %}
```java
client.deleteInputsBatch()
    .plus("{id1}", "{id2}");
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

            await client.DeleteInputs("{id1}", "{id2}")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[_app deleteInputsByIDList:@[{id1}, {id2}] completion:^(NSError *error) {
    NSLog(@"inputs have been deleted");
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->deleteInputs(['INPUT_ID1', 'INPUT_ID2'])
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
  -H "Content-Type: application/json" \
  -d '
  {
    "ids":["INPUT_ID1","INPUT_ID2"]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### Delete all inputs

If you would like to delete all inputs from an application, you can do that as well. This will happen asynchronously.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.delete().then(
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

app.inputs.delete_all()
```
{% endtab %}

{% tab title="java" %}
```java
client.deleteAllInputs().executeSync();
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

            await client.DeleteAllInputs()
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app deleteAllInputs:^(ClarifaiInput *input, NSError *error) {
  NSLog(@"all inputs have been deleted");
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->deleteInputs([], true)
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
  -H "Content-Type: application/json" \
  -d '
  {
    "delete_all":true
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

