# Rank

Rank Order your search results with the intuitive insights of AI. Your model can identify concepts in your data and rank your search results by how confident it is that a given concept is present. You can even rank search results by how similar one input is to another input.

## Search By Concept

Once your images are indexed, you can search for them by concept.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.search({ concept: {name: 'people'} }).then(
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

# search by public concept
app.inputs.search_by_predicted_concepts(concept='people')

# search by a list of concepts
app.inputs.search_by_predicted_concepts(concepts=['people'])

# search by concept id
app.inputs.search_by_predicted_concepts(concept_id='ai_dP13sXL4')

# search by a list of concept ids
app.inputs.search_by_predicted_concepts(concept_ids=['ai_dP13sXL4'])
```
{% endtab %}

{% tab title="java" %}
```java
client.searchInputs(SearchClause.matchConcept(Concept.forName("people")))
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
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
{% endtab %}

{% tab title="objective-c" %}
```text
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
{% endtab %}

{% tab title="php" %}
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
{% endtab %}

{% tab title="cURL" %}
```text
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
{% endtab %}
{% endtabs %}

### By Public Concepts

When you add an input, it automatically gets predictions from the general model. You can search for those predictions.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.search([
  {
    concept: {
      name: 'cat'
    }
  },
  {
    concept: {
      name: 'dog'
    }
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
app = ClarifaiApp(api_key='YOUR_CLARIFAI_KEY')

# search by single concept name
app.inputs.search_by_predicted_concepts(concept='cat')

# search by single concept id
app.inputs.search_by_predicted_concepts(concept_id='ai_mFqxrph2')

# search by multiple concepts with name
app.inputs.search_by_predicted_concepts(concepts=['cat', 'cute'])

# search by multiple concepts with ids
app.inputs.search_by_predicted_concepts(concept_ids=['ai_mFqxrph2', 'ai_4CRlSvbV'])

# search by multiple concepts with not logic
app.inputs.search_by_predicted_concepts(concepts=['cat', 'dog'], values=[True, False])
```
{% endtab %}

{% tab title="java" %}
```java
// Search concept by name
client.searchInputs(SearchClause.matchConcept(Concept.forName("cat")))
    .getPage(1)
    .executeSync();

// Search concept by ID
client.searchInputs(SearchClause.matchConcept(Concept.forID("ai_mFqxrph2")))
    .getPage(1)
    .executeSync();

// Search multiple concepts
client.searchInputs(SearchClause.matchConcept(Concept.forID("cat")))
    .and(SearchClause.matchConcept(Concept.forID("cute")))
    .getPage(1)
    .executeSync();

// Search NOT by concept
client.searchInputs(SearchClause.matchConcept(Concept.forID("cat").withValue(false)))
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
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

            // Search concept by name
            await client.SearchInputs(SearchBy.ConceptName("cat"))
                .Page(1)
                .ExecuteAsync();

            // Search concept by ID
            await client.SearchInputs(SearchBy.ConceptID("cat"))
                .Page(1)
                .ExecuteAsync();

            // Search multiple concepts
            await client.SearchInputs(
                    SearchBy.ConceptID("cat"),
                    SearchBy.ConceptID("cute"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
// First create a search term with a concept you want to search.
ClarifaiConcept *conceptFromGeneralModel = [[ClarifaiConcept alloc] initWithConceptName:@"fast"];
ClarifaiSearchTerm *searchTerm = [ClarifaiSearchTerm searchByPredictedConcept:conceptFromGeneralModel];

[app search:@[searchTerm] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

// Search concept by name
$response = $client->searchInputs(SearchBy::conceptName('cat'))
    ->executeSync();

/*
// Search concept by ID
$response = $client->searchInputs(SearchBy::conceptID('cat'))
    ->executeSync();
*/

/*
// Search multiple concepts
$response = $client->searchInputs([SearchBy::conceptID('cat'), SearchBy::conceptID('cute')])
    ->executeSync();
*/

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

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
{% endtab %}

{% tab title="cURL" %}
```text
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
                  "name":"dog"
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
{% endtab %}
{% endtabs %}

### By Custom Concepts

After you have [added inputs with concepts](../data-management/inputs.md#add-inputs-with-concepts), you can search by those concepts.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.search([
  {
    concept: {
      type: 'input',
      name: 'cat'
    }
  },
  {
    concept: {
      type: 'input',
      name: 'dog'
    }
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
app = ClarifaiApp(api_key='YOUR_CLARIFAI_KEY')

# search by single concept name
app.inputs.search_by_annotated_concepts(concept='cat')

# search by single concept id
app.inputs.search_by_annotated_concepts(concept_id='ai_mFqxrph2')

# search by multiple concepts with name
app.inputs.search_by_annotated_concepts(concepts=['cat', 'cute'])

# search by multiple concepts with ids
app.inputs.search_by_annotated_concepts(concept_ids=['ai_mFqxrph2', 'ai_4CRlSvbV'])

# search by multiple concepts with not logic
app.inputs.search_by_annotated_concepts(concepts=['cat', 'dog'], values=[True, False])
```
{% endtab %}

{% tab title="java" %}
```java
// Search concept by name
client.searchInputs(SearchClause.matchUserTaggedConcept(Concept.forName("cat")))
    .getPage(1)
    .executeSync();

// Search concept by ID
client.searchInputs(SearchClause.matchUserTaggedConcept(Concept.forID("ai_mFqxrph2")))
    .getPage(1)
    .executeSync();

// Search multiple concepts
client.searchInputs(SearchClause.matchUserTaggedConcept(Concept.forID("cat")))
    .and(SearchClause.matchUserTaggedConcept(Concept.forID("cute")))
    .getPage(1)
    .executeSync();

// Search NOT by concept
client.searchInputs(SearchClause.matchUserTaggedConcept(Concept.forID("cat").withValue(false)))
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
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

            // Search concept by name
            await client.SearchInputs(SearchBy.UserTaggedConceptName("cat")
                )
                .Page(1)
                .ExecuteAsync();

            // Search concept by ID
            await client.SearchInputs(SearchBy.UserTaggedConceptID("ai_mFqxrph2")
                )
                .Page(1)
                .ExecuteAsync();

            // Search multiple concepts
            await client.SearchInputs(
                    SearchBy.UserTaggedConceptID("cat"),
                    SearchBy.UserTaggedConceptID("cute"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
// If you have previously added inputs tagged with "dog", you can search for them by the same tag.
ClarifaiConcept *concept = [[ClarifaiConcept alloc] initWithConceptName:@"dog"];
ClarifaiSearchTerm *term = [ClarifaiSearchTerm searchInputsByConcept:concept];

[app search:@[term] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

// Search concept by name
$response = $client->searchInputs(SearchBy::userTaggedConceptName('cat'))
    ->executeSync();

/*
// Search concept by ID
$response = $client->searchInputs(SearchBy::userTaggedConceptID('cat'))
    ->executeSync();
*/

/*
// Search multiple concepts
$response = $client->searchInputs([SearchBy::userTaggedConceptName('cat'),
        SearchBy::userTaggedConceptID('dog')])
    ->executeSync();
*/

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

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
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "query": {
      "ands": [
        {
          "input": {
            "data": {
              "concepts": [
                {
                  "name":"dog"
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
{% endtab %}
{% endtabs %}

### By public and custom concepts

You can combine a search to find inputs that have concepts you have supplied as well as predictions from your model.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.search([
  // this is the public concept
  {
    concept: {
      name: 'cat'
    }
  },
  // this is the user-supplied concept
  {
    concept: {
      type: 'input',
      name: 'dog'
    }
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
from clarifai.rest import ClarifaiApp, InputSearchTerm, OutputSearchTerm, SearchQueryBuilder
app = ClarifaiApp(api_key='YOUR_API_KEY')

term1 = InputSearchTerm(concept='cat')
term2 = OutputSearchTerm(concept='dog', value=False)
query = SearchQueryBuilder()
query.add_term(term1)
query.add_term(term2)

app.inputs.search(query)
```
{% endtab %}

{% tab title="java" %}
```java
client.searchInputs()
    // Matches images we tagged as "cat", and that the API tagged as not having "dog"
    .ands(
        SearchClause.matchUserTaggedConcept(Concept.forName("cat")),
        SearchClause.matchConcept(Concept.forName("dog").withValue(false))
    )
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
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

            await client.SearchInputs(
                    SearchBy.UserTaggedConceptName("cat"),
                    SearchBy.ConceptID("dog"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiConcept *conceptFromGeneralModel = [[ClarifaiConcept alloc] initWithConceptName:@"fast"];
ClarifaiConcept *conceptFromTrainedCustomModel = [[ClarifaiConcept alloc] initWithConceptName:@"dog"];

ClarifaiSearchTerm *term1 = [ClarifaiSearchTerm searchByPredictedConcept:conceptFromGeneralModel];
ClarifaiSearchTerm *term2 = [ClarifaiSearchTerm searchByPredictedConcept:conceptFromTrainedCustomModel];

[_app search:@[term1, term2] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs([SearchBy::userTaggedConceptName('cat'),
        SearchBy::conceptID('dog')])
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

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
{% endtab %}

{% tab title="cURL" %}
```text
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
                "name": "fast"
              }
            ]
          }
        }
      },
      {
        "input": {
          "data": {
            "concepts": [
              {
                "name": "ferrari23",
                "value": true
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
{% endtab %}
{% endtabs %}

## By Image

You can use images to search through your collection. The API will return ranked results based on how similar the results are to the image you provided in your query.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.search(
  {
    input: {
      url: 'https://samples.clarifai.com/puppy.jpeg'
    }
  }
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
app = ClarifaiApp(api_key='YOUR_CLARIFAI_KEY')

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
{% endtab %}

{% tab title="java" %}
```java
// Search by image URL (String or java.net.URL)
client.searchInputs(SearchClause.matchImageVisually(ClarifaiImage.of("https://samples.clarifai.com/metro-north.jpg")))
    .getPage(1)
    .executeSync();

// Search by local image (java.io.File or byte[])
client.searchInputs(SearchClause.matchImageVisually(ClarifaiImage.of(new File("image.png"))))
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.IO;
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

            // Search by image URL
            await client.SearchInputs(
                    SearchBy.ImageVisually("https://samples.clarifai.com/metro-north.jpg"))
                .Page(1)
                .ExecuteAsync();

            // Search by local image
            await client.SearchInputs(
                    SearchBy.ImageVisually(File.ReadAllBytes("image.png")))
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiSearchTerm *searchTerm = [ClarifaiSearchTerm searchVisuallyWithImageURL:@"https://samples.clarifai.com/metro-north.jpg"];

[app search:@[searchTerm] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs(
        SearchBy::urlImageVisually('https://samples.clarifai.com/metro-north.jpg'))
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

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
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "query": {
      "ands": [
        {
          "output":{
            "input":{
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
{% endtab %}
{% endtabs %}

### By Url

You can also search for an input by URL.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.search(
  {
    input: {
      type: 'input',
      url: 'https://samples.clarifai.com/puppy.jpeg'
    }
  }
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

meta = {"url":"https://samples.clarifai.com/metro-north.jpg"}
app.inputs.search_by_metadata(meta)
```
{% endtab %}

{% tab title="java" %}
```java
// Lookup images with this URL
client.searchInputs(SearchClause.matchImageURL(ClarifaiImage.of("https://samples.clarifai.com/puppy.jpeg")))
    .getPage(1)
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
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

            await client.SearchInputs(
                    SearchBy.ImageURL("https://samples.clarifai.com/metro-north.jpg"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
// Lookup images with this URL
ClarifaiSearchTerm *term = [ClarifaiSearchTerm searchInputsWithImageURL:@"https://samples.clarifai.com/metro-north.jpg"];

[app search:@[term] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs(
        SearchBy::imageURL('https://samples.clarifai.com/metro-north.jpg'))
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

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
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "query": {
      "ands": [
        {
          "input":{
            "data": {
              "image": {
                "url": "https://samples.clarifai.com/metro-north.jpg"
              }
            }
          }
        }
      ]
    }
  }'\
  https://api.clarifai.com/v2/searches
```
{% endtab %}
{% endtabs %}

### By Image With Crop

You can search using a crop of an image through your collection. The API will still return ranked results based upon on how similar the results are to the crop of the image you provide in your query.

{% tabs %}
{% tab title="js" %}
```javascript
app.inputs.search(
  {
    input: {
      url: 'https://samples.clarifai.com/puppy.jpeg',
      crop: [0.1, 0.1, 0.9, 0.9]
    }
  }
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

search = app.inputs.search_by_image(url='https://samples.clarifai.com/puppy.jpeg', crop=[0.1, 0.1, 0.9, 0.9])

print search
```
{% endtab %}

{% tab title="java" %}
```java
client.searchInputs(SearchClause.matchImageVisually(ClarifaiImage.of("https://samples.clarifai.com/puppy.jpeg")
    .withCrop(Crop.create()
        .top(0.1F)
        .left(0.1F)
        .bottom(0.9F)
        .right(0.9F)
    )
))
.getPage(1)
.executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs;
using Clarifai.DTOs.Searches;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.SearchInputs(SearchBy.ImageVisually(
                    "https://samples.clarifai.com/metro-north.jpg",
                    crop: new Crop(0.1M, 0.1M, 0.9M, 0.9M)))
                .Page(1)
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
use Clarifai\DTOs\Crop;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs(
        SearchBy::urlImageVisually('https://samples.clarifai.com/metro-north.jpg')
            ->withCrop(new Crop(0.1, 0.1, 0.9, 0.9)))
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

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
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H 'authorization: Key YOUR_API_KEY' \
  -H 'content-type: application/json' \
  -d '{
  "query": {
    "ands": [
      {
        "output": {
          "input": {
              "data": {
                "image": {
                    "url": "https://samples.clarifai.com/puppy.jpeg",
                    "crop": [0.1,0.1,0.9,0.9]
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
{% endtab %}
{% endtabs %}

