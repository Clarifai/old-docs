# Search

Note: The Search API currently is only available for images.

A common case for using Clarifai is to get the concepts predicted in an image and then use those concepts to power search.

The Search API allows you to send images \(url or bytes\) to the service and have them indexed by 'general' model concepts and their visual representations. Once indexed, you can search for images by concept or by image.

![Image illustrating how to search by images using Clarifai&apos;s concepts](/images/illustration-search.png)

#### Add Images to Search Index

To get started with search, you must first add images to the search index. You can add one or more images to the index at a time. You can supply an image either with a publicly accessible URL or by directly sending image bytes. You can send up to 128 images in one API call.

{% code-tabs %}
{% code-tabs-item title="js" %}
```js
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
{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='YOUR_API_KEY')

img1 = ClImage(url="https://samples.clarifai.com/metro-north.jpg")
img2 = ClImage(url="https://samples.clarifai.com/puppy.jpg")
img3 = ClImage(file_obj=open('/home/user/image.jpeg', 'rb'))

app.inputs.bulk_create_images([img1, img2, img3])
```
{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
client.addInputs()
    .plus(
        ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"),
        ClarifaiInput.forImage("https://samples.clarifai.com/wedding.jpg")
    )
    .executeSync();
```
{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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
{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
ClarifaiImage *image1 = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/metro-north.jpg"];
ClarifaiImage *image2 = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/wedding.jpg"];

[app addInputs:@[image1, image2] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Response JSON" %}
```json
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
{% endcode-tabs-item %}
{% endcode-tabs %}

#### Search By Concept

Once your images are indexed, you can search for them by concept.

{% code-tabs %}
{% code-tabs-item title="js" %}
```js
app.inputs.search({ concept: {name: 'people'} }).then(
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

# search by public concept
app.inputs.search_by_predicted_concepts(concept='people')

# search by a list of concepts
app.inputs.search_by_predicted_concepts(concepts=['people'])

# search by concept id
app.inputs.search_by_predicted_concepts(concept_id='ai_dP13sXL4')

# search by a list of concept ids
app.inputs.search_by_predicted_concepts(concept_ids=['ai_dP13sXL4'])
```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
client.searchInputs(SearchClause.matchConcept(Concept.forName("people")))
    .getPage(1)
    .executeSync();
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Searches;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.SearchInputs(SearchBy.ConceptName("people"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
// First create a search term with a concept you want to search.
ClarifaiConcept *conceptFromGeneralModel = [[ClarifaiConcept alloc] initWithConceptName:@"people"];
ClarifaiSearchTerm *searchTerm = [ClarifaiSearchTerm searchByPredictedConcept:conceptFromGeneralModel];

[app search:@[searchTerm] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of public concept: %@", results[0].score);
}];
```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs(SearchBy::conceptName('people'))->executeSync();

if ($response-> isSuccessful()) {

    /** @var SearchInputsResult $result */
    $result = $response->get();
    foreach ($result->searchHits() as $searchHit) {
        echo $searchHit->input()->id() . ' ' . $searchHit->score() . "\n";
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
    "query": {
      "ands": [
        {
          "output": {
            "data": {
              "concepts": [
                {
                  "name": "people"
                }
              ]
            }
          }
        }
      ]
    }
  }'\
  https://api.clarifai.com/v2/searches
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Response JSON" %}
```json
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "id":"d275a3c0f3e748378617d6ba9bd0f8d4",
  "hits": [
    {
      "score": 0.98155165,
      "input": {
        "id": "f96ca3bbf02041c59addcc13e3468b7d",
        "created_at": "2016-11-22T17:06:02Z",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/wedding.jpg"
          }
        },
        "status": {
          "code": 30000,
          "description": "Download complete"
        }
      }
    }
  ]
}
```
{% endcode-tabs-item %}
{% endcode-tabs %}

#### Search By Image

You can also search for images using another image. In this case, you provide an image \(url or bytes\) and the results will return all the images in your search index that are visually similar to the one provided.


{% code-tabs %}
{% code-tabs-item title="js" %}
```js
app.inputs.search({ input: {url: 'https://samples.clarifai.com/puppy.jpg'} }).then(
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

# search by image url
app.inputs.search_by_image(url="https://samples.clarifai.com/metro-north.jpg")

# search by existing input id
input_id = "some_existing_input_id"
app.inputs.search_by_image(image_id=input_id)

# search by raw bytes
data = "image_raw_bytes"
app.inputs.search_by_image(imgbytes=data)

# search by base64 bytes
base64_data = "image_bytes_encoded_in_base64"
app.inputs.search_by_image(base64bytes=base64_data)

# search by local filename
filename="filename_on_local_disk.jpg"
app.inputs.search_by_image(filename=filename)

# search from fileio
fio = open("filename_on_local_disk.jpg", 'rb')
app.inputs.search_by_image(fileobj=fio)
```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
client.searchInputs(SearchClause.matchImageVisually(ClarifaiImage.of("https://samples.clarifai.com/metro-north.jpg")))
    .getPage(1)
    .executeSync();
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Searches;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.SearchInputs(SearchBy.ImageURL("https://samples.clarifai.com/metro-north.jpg"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
ClarifaiSearchTerm *searchTerm = [ClarifaiSearchTerm searchVisuallyWithImageURL:@"https://samples.clarifai.com/metro-north.jpg"];

[app search:@[searchTerm] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of visual similarity: %@", results[0].score);
}];
```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs(
        SearchBy::imageURL('https://samples.clarifai.com/metro-north.jpg'))
    ->executeSync();

if ($response-> isSuccessful()) {

    /** @var SearchInputsResult $result */
    $result = $response->get();
    foreach ($result->searchHits() as $searchHit) {
        echo $searchHit->input()->id() . ' ' . $searchHit->score() . "\n";
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
    "query": {
      "ands": [
        {
          "output": {
            "input": {
              "data": {
                "image": {
                  "url": "https://samples.clarifai.com/metro-north.jpg"
                }
              }
            }
          }
        }
      ]
    }
  }'\
  https://api.clarifai.com/v2/searches
```
{% endcode-tabs-item %}
{% endcode-tabs %}

{% code-tabs %}
{% code-tabs-item title="Response JSON" %}
```json
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "id": "bd94239099d44d4686f38ca753495e22",
  "hits": [
    {
      "score": 0.9999997,
      "input": {
        "id": "edc70c917475499abdc7151f41d6cf3e",
        "created_at": "2016-11-22T17:06:02Z",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        },
        "status": {
          "code": 30000,
          "description": "Download complete"
        }
      }
    },
    {
      "score": 0.3915897,
      "input": {
        "id": "f96ca3bbf02041c59addcc13e3468b7d",
        "created_at": "2016-11-22T17:06:02Z",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/wedding.jpg"
          }
        },
        "status": {
          "code": 30000,
          "description": "Download complete"
        }
      }
    }
  ]
}
```
{% endcode-tabs-item %}
{% endcode-tabs %}
