The concepts in your model can be used to power search.
The Search API allows you to send images (url or bytes) to the service and have them indexed by model concepts and their visual representations. Once indexed, you can search for images by concept, image, or many advanced search parameters.
Search API lets you combine search criteria 
## Rank 
Order your search results with the intuitive insights of AI. Your model can identify concepts in your data and rank your search results by how confident it is that a given concept is present. You can even rank search results by how similar one input is to another input.
## Filter 
Trim down the amount of data returned in search. For example, you may only want to see inputs that one of your collaborators has labeled with the word “dog”. Or perhaps you want only those inputs that were captured in a certain geographical region.
## 'AND' 
Combine multiple search parameters. For example, you can find all the inputs within a geographical region with a "weapon" in them, or all annotations assigned to user "Joe", or visually similar product images that are assigned the word "XL" in metadata.

{% hint style="info" %}
The Search API currently is only available for images.
{% endhint %}

![Image illustrating how to search by images using Clarifai&apos;s concepts](/images/illustration-search.png)


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
