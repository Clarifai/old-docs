# Index images for search

To get started with search, you must first add images to the search index. You can add one or more images to the index at a time. You can supply an image either with a publicly accessible URL or by directly sending image bytes. You can send up to 128 images in one API call.

{% tabs %}
{% tab title="gRPC Java" %}
```java
MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder()
        .addInputs(
            Input.newBuilder()
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
                .setData(
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setUrl("https://samples.clarifai.com/wedding.jpg")
                            .setAllowDuplicateUrl(true)
                    )
                )
        )
        .addInputs(
            Input.newBuilder()
                .setData(
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
```
{% endtab %}


{% tab title="gRPC Python" %}
```python
```
{% endtab %}

{% tab title="js" %}
```javascript
app.inputs.create([
  {url: "https://samples.clarifai.com/metro-north.jpg"},
  {url: "https://samples.clarifai.com/wedding.jpg"},
  {base64: "G7p3m95uAl..."}
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

img1 = ClImage(url="https://samples.clarifai.com/metro-north.jpg")
img2 = ClImage(url="https://samples.clarifai.com/puppy.jpeg")
img3 = ClImage(file_obj=open('/home/user/image.jpeg', 'rb'))

app.inputs.bulk_create_images([img1, img2, img3])
```
{% endtab %}

{% tab title="java" %}
```java
client.addInputs()
    .plus(
        ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"),
        ClarifaiInput.forImage("https://samples.clarifai.com/wedding.jpg")
    )
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
                new ClarifaiURLImage("https://samples.clarifai.com/metro-north.jpg"),
                new ClarifaiURLImage("https://samples.clarifai.com/wedding.jpg")
            ).ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *image1 = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/metro-north.jpg"];
ClarifaiImage *image2 = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/wedding.jpg"];

[app addInputs:@[image1, image2] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->addInputs([
    new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'),
    new ClarifaiURLImage('https://samples.clarifai.com/wedding.jpg'),
])->executeSync();

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
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      },
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/wedding.jpg"
          }
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
      "id": "edc70c917475499abdc7151f41d6cf3e",
      "created_at": "2016-11-22T17:06:02Z",
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/metro-north.jpg"
        }
      },
      "status": {
        "code": 30001,
        "description": "Download pending"
      }
    },
    {
      "id": "f96ca3bbf02041c59addcc13e3468b7d",
      "created_at": "2016-11-22T17:06:02Z",
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/wedding.jpg"
        }
      },
      "status": {
        "code": 30001,
        "description": "Download pending"
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

