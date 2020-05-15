# Inputs

## Inputs

The API is built around a simple idea. You send inputs \(images\) to the service and it returns predictions. In addition to receiving predictions on inputs, you can also index inputs and their predictions to later search against. You can also index inputs with concepts to later train your own model.

When you add an input to your app, the base workflow of your app runs, computing the outputs from all the models in that workflow and indexes those outputs. Those indexed outputs are what incur the indexing fee monthly, and enablessearch and training on top of the outputs of the base workflow models.

### Add Inputs

You can add inputs one by one or in bulk. If you do send bulk, you are limited to sending 128 inputs at a time.

**Important: adding inputs is an asynchronous operation.** That means it will process indexing of your inputs through your default workflow in the background, which can take some time. In order to check the status of each input you add, see the section on [Get Input by ID](inputs.md#get-input-by-id) to look for status 30000 \(INPUT\_IMAGE\_DOWNLOAD\_SUCCESS\) status code on each input to know when it's successfully been indexed.

#### Add an input using a publicly accessible URL

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder().setImage(
                Image.newBuilder()
                    .setUrl("https://samples.clarifai.com/metro-north.jpg")
                    .setAllowDuplicateUrl(true)
            )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostInputs(
    {
        inputs: [{data: {image: {url: "https://samples.clarifai.com/metro-north.jpg", allow_duplicate_url: true}}}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
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
                        url="https://samples.clarifai.com/metro-north.jpg",
                        allow_duplicate_url=True
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

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
            "url": "https://samples.clarifai.com/metro-north.jpg",
            "allow_duplicate_url": true
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import com.google.protobuf.ByteString;
import java.io.File;
import java.nio.file.Files;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder().setImage(
                Image.newBuilder()
                    .setBase64(ByteString.copyFrom(Files.readAllBytes(
                        new File("{YOUR_IMAGE_LOCATION}").toPath()
                    )))
            )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

const fs = require("fs");
const imageBytes = fs.readFileSync("{YOUR_IMAGE_LOCATION}");

stub.PostInputs(
    {
        inputs: [{data: {image: {base64: imageBytes}}}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
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

with open("{YOUR_IMAGE_LOCATION}", "rb") as f:
    file_bytes = f.read()

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
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

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

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
                .setId("train1")
                .setData(
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setUrl("https://samples.clarifai.com/metro-north.jpg")
                            .setAllowDuplicateUrl(true)
                    )
                )
        )
        .addInputs(
            Input.newBuilder()
                .setId("puppy1")
                .setData(
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setUrl("https://samples.clarifai.com/puppy.jpeg")
                            .setAllowDuplicateUrl(true)
                    )
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostInputs(
    {
        inputs: [
            {
                id: "train1",
                data: {image: {url: "https://samples.clarifai.com/metro-north.jpg", allow_duplicate_url: true}}
            },
            {
                id: "puppy1",
                data: {image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true}}
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
                id="train1",
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg",
                        allow_duplicate_url=True
                    )
                )
            ),
            resources_pb2.Input(
                id="puppy1",
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/puppy.jpeg",
                        allow_duplicate_url=True
                    )
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

% tab title="js" %}
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
            "url": "https://samples.clarifai.com/metro-north.jpg",
            "allow_duplicate_url": true
          }
        },
        "id": "train1"
      },
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
          }
        },
        "id": "puppy1"
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder()
                .setImage(
                    Image.newBuilder()
                        .setUrl("https://samples.clarifai.com/puppy.jpeg")
                        .setAllowDuplicateUrl(true)
                )
                .addConcepts(
                    Concept.newBuilder()
                        .setId("boscoe")
                        .setValue(1f)
                )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostInputs(
    {
        inputs: [{data: {
            image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true},
            concepts: [{id: "boscoe", value: 1.}]
        }}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
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
                    concepts=[resources_pb2.Concept(id="boscoe", value=1.)]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

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
            "url": "https://samples.clarifai.com/puppy.jpeg",
            "allow_duplicate_url": true
          },
          "concepts":[
            {
              "id": "boscoe",
              "value": 1
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import com.google.protobuf.Struct;
import com.google.protobuf.Value;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder()
                .setImage(
                    Image.newBuilder()
                        .setUrl("https://samples.clarifai.com/puppy.jpeg")
                        .setAllowDuplicateUrl(true)
                )
                .setMetadata(
                    Struct.newBuilder()
                        .putFields("id", Value.newBuilder().setStringValue("id001").build())
                        .putFields("type", Value.newBuilder().setStringValue("animal").build())
                        .putFields("size", Value.newBuilder().setNumberValue(100).build())
                )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostInputs(
    {
        inputs: [{data: {
            image: {url: "https://samples.clarifai.com/puppy.jpeg", allow_duplicate_url: true},
            metadata: {id: "id001", type: "animal", size: 100}
        }}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
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
from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

input_metadata = Struct()
input_metadata.update({"id": "id001", "type": "animal", "size": 100})

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/puppy.jpeg",
                        allow_duplicate_url=True
                    ),
                    metadata=input_metadata
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

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
          "metadata": {"id": "id001", "type": "animal", "size": 100}
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### List inputs

You can list all the inputs \(images\) you have previously added either for [search](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/advanced-searches.md) or [train](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/train.md).

If you added inputs with concepts, they will be returned in the response as well.

This request is paginated.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse listInputsResponse = stub.listInputs(
    ListInputsRequest.newBuilder()
        .setPage(1)
        .setPerPage(10)
        .build()
);

if (listInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List inputs failed, status: " + listInputsResponse.getStatus());
}

for (Input input : listInputsResponse.getInputsList()) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.ListInputs(
    {page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List inputs failed, status: " + response.status.description);
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
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

list_inputs_response = stub.ListInputs(
    service_pb2.ListInputsRequest(page=1, per_page=10),
    metadata=metadata
)

if list_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List inputs failed, status: " + list_inputs_response.status.description)

for input_object in list_inputs_response.inputs:
    print(input_object)
```
{% endtab %}

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
  https://api.clarifai.com/v2/inputs?page=1&per_page=10
```
{% endtab %}
{% endtabs %}


### List inputs (streaming)

This is an extension of List inputs which was built to scalably list all the inputs in an app in an iterative / streaming fashion. The idea is that the last call to StreamInputs will return a list of inputs and you can feed in the last id of those inputs into the next StreamInputs call.

The stream starts from the oldest assets and works it's way forward by default. There is a `descending` field you can set to True to reverse that order.

{% tabs %}
{% tab title="gRPC Java" %}
```java
// FIXME(rok): update for the streaming request.

import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse streaminputsResponse = stub.streaminputs(
    StreaminputsRequest.newBuilder()
        .setPage(1)
        .setPerPage(10)
        .build()
);

if (streaminputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List inputs failed, status: " + streaminputsResponse.getStatus());
}

for (Input input : streaminputsResponse.getInputsList()) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// FIXME(rok): update for the streaming request.

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.Streaminputs(
    {page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List inputs failed, status: " + response.status.description);
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
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

# First page id isn't provided.
list_inputs_response = stub.Streaminputs(
    service_pb2.StreaminputsRequest(per_page=10),
    metadata=metadata
)

if list_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List inputs failed, status: " + list_inputs_response.status.description)

for input_object in list_inputs_response.inputs:
    print(input_object)

last_id = list_inputs_response.inputs[-1].id

# second page starts from the last_id.
list_inputs_response = stub.Streaminputs(
    service_pb2.StreaminputsRequest(per_page=10, last_id=last_id),
    metadata=metadata
)
```
{% endtab %}
{% endtabs %}

### Get input by id

If you'd like to get a specific input by id, you can do that as well.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

SingleInputResponse getInputResponse = stub.getInput(
    GetInputRequest.newBuilder()
        .setInputId("{YOUR_INPUT_ID}")
        .build()
);

if (getInputResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get input failed, status: " + getInputResponse.getStatus());
}

Input input = getInputResponse.getInput();
System.out.println(input);
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.GetInput(
    {input_id: "{YOUR_INPUT_ID}"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get input failed, status: " + response.status.description);
        }

        const input = response.input;
        console.log(JSON.stringify(input, null, 2));
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

get_input_response = stub.GetInput(
    service_pb2.GetInputRequest(input_id="{YOUR_INPUT_ID}"),
    metadata=metadata
)

if get_input_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get input failed, status: " + get_input_response.status.description)

input_object = get_input_response.input
print(input_object)
```
{% endtab %}

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
  https://api.clarifai.com/v2/inputs/{YOUR_INPUT_ID}
```
{% endtab %}
{% endtabs %}

### Get inputs status

If you add inputs in bulk, they will process in the background. You can get the status of all your inputs \(processed, to\_process and errors\) like this:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

SingleInputCountResponse getInputCountResponse = stub.getInputCount(
    GetInputCountRequest.newBuilder().build()
);

if (getInputCountResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get input count failed, status: " + getInputCountResponse.getStatus());
}

InputCount inputCount = getInputCountResponse.getCounts();
System.out.println(inputCount);
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.GetInputCount(
    {},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get input count failed, status: " + response.status.description);
        }

        const counts = response.counts;
        console.log(JSON.stringify(counts, null, 2));
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

get_input_count_response = stub.GetInputCount(
    service_pb2.GetInputCountRequest(),
    metadata=metadata
)

if get_input_count_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get input count failed, status: " + get_input_count_response.status.description)

counts = get_input_count_response.counts
print(counts)
```
{% endtab %}

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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("tree")
                                .setValue(1f)  // 1 means true, this concept is present.
                        )
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("water")
                                .setValue(0f)  // 0 means false, this concept is not present.
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PatchInputs(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove.
        inputs: [
            {
                id: "{YOUR_INPUT_ID}",
                // 1 means true, this concept is present.
                // 0 means false, this concept is not present.
                data: {concepts: [{id: "tree", value: 1}, {id: "water", value: 0}]}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch inputs failed, status: " + response.status.description);
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

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                        resources_pb2.Concept(id="water", value=0.)  # 0 means false, this concept is not present.
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

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
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
# Supported actions: overwrite, merge, remove.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{YOUR_INPUT_ID}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": 1
            },
            {
              "id": "water",
              "value": 0
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_1}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("tree")
                                .setValue(1f)  // 1 means true, this concept is present.
                        )
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("water")
                                .setValue(0f)  // 0 means false, this concept is not present.
                        )
                )
                .build()
        )
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_2}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("animal")
                                .setValue(1f)
                        )
                        .addConcepts(
                            Concept.newBuilder()
                                .setId("fruit")
                                .setValue(0f)
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PatchInputs(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove.
        inputs: [
            {
                id: "{YOUR_INPUT_ID_1}",
                data: {concepts: [{id: "tree", value: 1}, {id: "water", value: 0}]}
            },
            {
                id: "{YOUR_INPUT_ID_2}",
                data: {concepts: [{id: "animal", value: 1}, {id: "fruit", value: 0}]}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch inputs failed, status: " + response.status.description);
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

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_1}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                        resources_pb2.Concept(id="water", value=0.)  # 0 means false, this concept is not present.
                    ]
                )
            ),
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_2}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="animal", value=1.),
                        resources_pb2.Concept(id="fruit", value=0.)
                    ]
                )
            ),
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

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
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
# Supported actions: overwrite, merge, remove.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{YOUR_INPUT_ID_1}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": 1
            },
            {
              "id": "water",
              "value": 0
            }
          ]
        }
      },
      {
        "id": "{YOUR_INPUT_ID_2}",
        "data": {
          "concepts": [
            {
              "id": "animal",
              "value": 1
            },
            {
              "id": "fruit",
              "value": 0
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            // We're removing the concept, so there's no need to specify
                            // the concept value.
                            Concept.newBuilder().setId("tree")
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            // We're removing the concept, so there's no need to specify
                            // the concept value.
                            Concept.newBuilder().setId("tree")
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="remove",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    concepts=[
                        # We're removing the concept, so there's no need to specify
                        # the concept value.
                        resources_pb2.Concept(id="water"),
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

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
# We're removing the concept, so there's no need to specify
# the concept value.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id":"{YOUR_INPUT_ID}",
        "data": {
            "concepts":[
                {"id":"water"}
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse patchInputsResponse = stub.patchInputs(
    PatchInputsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove.
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_1}")
                .setData(
                    Data.newBuilder()
                        // We're removing the concepts, so there's no need to specify
                        // the concept value.
                        .addConcepts(
                            Concept.newBuilder().setId("tree")
                        )
                        .addConcepts(
                            Concept.newBuilder().setId("water")
                        )
                )
                .build()
        )
        .addInputs(
            Input.newBuilder()
                .setId("{YOUR_INPUT_ID_2}")
                .setData(
                    Data.newBuilder()
                        .addConcepts(
                            Concept.newBuilder().setId("animal")
                        )
                        .addConcepts(
                            Concept.newBuilder().setId("fruit")
                        )
                )
                .build()
        )
        .build()
);

if (patchInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch inputs failed, status: " + patchInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PatchInputs(
    {
        action: "remove",  // Supported actions: overwrite, merge, remove.
        inputs: [
            {
                id: "{YOUR_INPUT_ID_1}",
                // We're removing the concepts, so there's no need to specify
                // the concept value.
                data: {concepts: [{id: "tree"}, {id: "water"}]}
            },
            {
                id: "{YOUR_INPUT_ID_2}",
                data: {concepts: [{id: "animal"}, {id: "fruit"}]}
            },
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch inputs failed, status: " + response.status.description);
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

patch_inputs_response = stub.PatchInputs(
    service_pb2.PatchInputsRequest(
        action="remove",  # Supported actions: overwrite, merge, remove.
        inputs=[
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_1}",
                data=resources_pb2.Data(
                    concepts=[
                        # We're removing the concepts, so there's no need to specify
                        # the concept value.
                        resources_pb2.Concept(id="tree"),
                        resources_pb2.Concept(id="water"),
                    ]
                )
            ),
            resources_pb2.Input(
                id="{YOUR_INPUT_ID_2}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="animal"),
                        resources_pb2.Concept(id="fruit"),
                    ]
                )
            ),
        ]
    ),
    metadata=metadata
)

if patch_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch inputs failed, status: " + patch_inputs_response.status.description)
```
{% endtab %}

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
# We're removing the concept, so there's no need to specify
# the concept value.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "id": "{YOUR_INPUT_ID_1}",
        "data": {
          "concepts":[
            {
              "id": "tree"
            },
            {
              "id": "water"
            }
          ]
        }
      },
      {
        "id": "{YOUR_INPUT_ID_2}",
        "data": {
          "concepts":[
            {
              "id": "animal"
            },
            {
              "id": "fruit"
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

BaseResponse deleteInputResponse = stub.deleteInput(
    DeleteInputRequest.newBuilder()
        .setInputId("{YOUR_INPUT_ID}")
        .build()
);

if (deleteInputResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete input failed, status: " + deleteInputResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.DeleteInput(
    {
        input_id: "{YOUR_INPUT_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete input failed, status: " + response.status.description);
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

delete_input_response = stub.DeleteInput(
    service_pb2.DeleteInputRequest(input_id="{YOUR_INPUT_ID}"),
    metadata=metadata
)

if delete_input_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete input failed, status: " + delete_input_response.status.description)
```
{% endtab %}

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
  https://api.clarifai.com/v2/inputs/{YOUR_INPUT_ID}
```
{% endtab %}
{% endtabs %}

### Delete a list of inputs

You can also delete multiple inputs in one API call. This will happen asynchronously.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

BaseResponse listInputsResponse = stub.deleteInputs(
    DeleteInputsRequest.newBuilder()
        .addIds("{YOUR_INPUT_ID_1}")
        .addIds("{YOUR_INPUT_ID_2}")
        .build()
);

if (listInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete inputs failed, status: " + listInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.DeleteInputs(
    {
        ids: ["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete inputs failed, status: " + response.status.description);
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

delete_inputs_response = stub.DeleteInputs(
    service_pb2.DeleteInputsRequest(
        ids=["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"]
    ),
    metadata=metadata
)

if delete_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete inputs failed, status: " + delete_inputs_response.status.description)
```
{% endtab %}

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
    "ids":["{YOUR_INPUT_ID_1}","{YOUR_INPUT_ID_2}"]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}

### Delete all inputs

If you would like to delete all inputs from an application, you can do that as well. This will happen asynchronously.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

BaseResponse listInputsResponse = stub.deleteInputs(
    DeleteInputsRequest.newBuilder()
        .setDeleteAll(true)
        .build()
);

if (listInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete inputs failed, status: " + listInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.DeleteInputs(
    {
        delete_all: true
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2



delete_inputs_response = stub.DeleteInputs(
    service_pb2.DeleteInputsRequest(
        delete_all=True
    ),
    metadata=metadata
)

if delete_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete inputs failed, status: " + delete_inputs_response.status.description)
```
{% endtab %}

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
    "delete_all": true
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}
{% endtabs %}
