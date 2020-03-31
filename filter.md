### By Image

You can use images to search through your collection. The API will return ranked results based on
how similar the results are to the image you provided in your query.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.inputs.search(
  {
    input: {
      url: 'https://samples.clarifai.com/puppy.jpg'
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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

ClarifaiSearchTerm *searchTerm = [ClarifaiSearchTerm searchVisuallyWithImageURL:@"https://samples.clarifai.com/metro-north.jpg"];

[app search:@[searchTerm] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
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
{% endcode-tabs-item %}
{% endcode-tabs %}



### By Image With Crop
You can search using a crop of an image through your collection. The API will still return ranked results
based upon on how similar the results are to the crop of the image you provide in your query.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
app.inputs.search(
  {
    input: {
      url: 'https://samples.clarifai.com/puppy.jpg',
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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

search = app.inputs.search_by_image(url='https://samples.clarifai.com/puppy.jpg', crop=[0.1, 0.1, 0.9, 0.9])

print search
```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
client.searchInputs(SearchClause.matchImageVisually(ClarifaiImage.of("https://samples.clarifai.com/puppy.jpg")
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

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
// Coming Soon
```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL
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
                    "url": "https://samples.clarifai.com/puppy.jpg",
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
{% endcode-tabs-item %}
{% endcode-tabs %}



### By Public and Custom Concepts

You can combine a search to find inputs that have concepts you have supplied as well as predictions from your model.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
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

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
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

            await client.SearchInputs(
                    SearchBy.UserTaggedConceptName("cat"),
                    SearchBy.ConceptID("dog"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

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

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
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
{% endcode-tabs-item %}
{% endcode-tabs %}



### By Custom Metadata

After you have [added inputs with custom metadata](inputs.md#add-inputs-with-custom-metadata),
you can search by that metadata.

Below is an example of searching over custom metadata. You can exact match any `key`: `value` pair no matter
how nested it is. For example, if the metadata on an input is:

```json
{
  "keyname": "value1",
  "somelist": [1,2,3],
  "somenesting": {
     "keyname2":"value2",
     "list2":[4,5]
   }
}
```
Then the following searches will find this:

```json
{
  "keyname": "value1"
}
```

```json
{
  "somelist": [1,2,3]
}
```

```json
{
  "somelist": [1,2]
}
```

```json
{
  "somenesting": {"keyname2":"value2"}
}
```

```json
{
  "somenesting": {"list2":[5]}
}
```

How to perform searches:



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

// Search with only metadata
app.inputs.search({
  input: {
    metadata: {
      key: 'value'
    }
  }
}).then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

// Search with nested metadata
app.inputs.search({
  input: {
    metadata: {
      parent: {
        key: 'value'
      }
    }
  }
}).then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);

// Search with metadata and concepts or input source
app.inputs.search([
  {
    input: { metadata: { key: 'value' } }
  },
  {
    concept: { name: 'cat' }
  },
  {
    concept: { type: 'output', name: 'group', value: false }
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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp, InputSearchTerm, OutputSearchTerm, SearchQueryBuilder
app = ClarifaiApp(api_key='YOUR_API_KEY')

# search with simple metadata only
app.inputs.search_by_metadata(metadata={'name':'bla'})

# search with nested metadata only
app.inputs.search_by_metadata(metadata={'my_class1': { 'name' : 'bla' }})

# search with metadata combined with others
query = SearchQueryBuilder()
query.add_term(InputSearchTerm(concept='cat'))
query.add_term(InputSearchTerm(metadata={'name':'value'}))
query.add_term(OutputSearchTerm(concept='group', value=False))

app.inputs.search(query)

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

JsonObject metadata = new JsonObject();
metadata.addProperty("isPuppy", true);

List<SearchHit> hits = client
  .searchInputs(SearchClause.matchMetadata(metadata))
  .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp

using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Searches;
using Newtonsoft.Json.Linq;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            var metadata = new JObject();
            metadata.Add("isPuppy", true);
            await client.SearchInputs(
                    SearchBy.Metadata(metadata))
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

// Search by metadata only.
[_app searchByMetadata:@{@"my_key": @[@"my", @"values"]} page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
}];

// Search metadata in conjunction with other ClarifaiSearchTerms. For example, the
// following will search for inputs with predicted tag "fast" and matching metadata.
ClarifaiConcept *conceptFromGeneralModel = [[ClarifaiConcept alloc] initWithConceptName:@"fast"];
ClarifaiSearchTerm *searchTerm1 = [ClarifaiSearchTerm searchByPredictedConcept:conceptFromGeneralModel];

ClarifaiSearchTerm *searchTerm2 = [ClarifaiSearchTerm searchInputsWithMetadata:@{@"my_key": @[@"my", @"values"]}];

[app search:@[searchTerm1, searchTerm2] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
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

curl -X POST \
  -H "Authorization: Key {api-key}" \
  -H "Content-Type: application/json" \
  -d '
  {
    "query": {
      "ands": [
        {
          "input":{
            "data": {
              "metadata": {
                "key": "value"
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



### By Url

You can also search for an input by URL.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.inputs.search(
  {
    input: {
      type: 'input',
      url: 'https://samples.clarifai.com/puppy.jpg'
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

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

meta = {"url":"https://samples.clarifai.com/metro-north.jpg"}
app.inputs.search_by_metadata(meta)

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

// Lookup images with this URL
client.searchInputs(SearchClause.matchImageURL(ClarifaiImage.of("https://samples.clarifai.com/puppy.jpg")))
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

            await client.SearchInputs(
                    SearchBy.ImageURL("https://samples.clarifai.com/metro-north.jpg"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c


// Lookup images with this URL
ClarifaiSearchTerm *term = [ClarifaiSearchTerm searchInputsWithImageURL:@"https://samples.clarifai.com/metro-north.jpg"];

[app search:@[term] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
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
{% endcode-tabs-item %}
{% endcode-tabs %}



### By Geo Location

Search by geo location allows you to restrict your search results to a bounding box based on longitude and latitude
points. There are two ways you can provide longitude/latitude points. You can provide one point and a radius
or you can provide two points.

It is important to note that a search by geo location acts as a filter and returns results ranked by any other provided
search criteria, whether that is a visual search, concept search or something else. If no other criteria is
provided, results will return in the order the inputs were created, NOT by their distance to center of the
search area.

If you are providing one point and a radius, the radius can be in "mile", "kilometer", "degree", or "radian",
marked by keywords `withinMiles`, `withinKilometers`, `withinDegrees`, `withinRadians`.

If you are providing two points, a box will be drawn from the uppermost point to the lowermost point and the
leftmost point to the rightmost point.

Before you perform a search by geo location, make sure you have added inputs with longitude and latitude points.

#### Add inputs with longitiude and latitude points

Provide a geo point to an input. The geo point is a JSON object consisting of a longitude and a latitude in
GPS coordinate system (SRID 4326). There can be at most one single geo point associated with each input.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
app.inputs.create({
  url: "https://samples.clarifai.com/puppy.jpg",
  geo: { longitude: 116.2317, latitude: 39.5427},
}).then(
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
from clarifai.rest import ClarifaiApp, Geo, GeoPoint
app = ClarifaiApp(api_key='YOUR_API_KEY')

geo_p1 = Geo(geo_point=GeoPoint(116.2317,39.5427))

app.inputs.create_image_from_url(url="https://samples.clarifai.com/puppy.jpg", geo=geo_p1)
```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
client.addInputs().plus(ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpg")
    .withGeo(PointF.at(116.2317F, 39.5427F))).executeSync();
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp

using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs;
using Clarifai.DTOs.Inputs;

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
                        geo: new GeoPoint(116.2317M, 39.5427M)))
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/metro-north.jpg"];
image.location = [[ClarifaiLocation alloc] initWithLatitude:116.2317 longitude:39.5427];

[_app addInputs:@[image] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
  NSLog(@"%@",inputs);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\GeoPoint;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->addInputs(
        (new ClarifaiURLImage('https://samples.clarifai.com/puppy.jpeg'))
            ->withGeo(new GeoPoint(116.2317, 39.5427)))
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
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/dog.tiff",
            "allow_duplicate_url": true
          },
          "geo": {
            "geo_point": {
              "longitude": -30,
              "latitude": 40
            }
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs

```
{% endcode-tabs-item %}
{% endcode-tabs %}



#### Perform a search with one geo point and radius in kilometers



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
app.inputs.search({
  input: {
    geo: {
      longitude: 116.2317,
      latitude: 39.5427,
      type: 'withinKilometers',
      value: 1
    }
  }
}).then(
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
from clarifai.rest import ClarifaiApp, GeoPoint, GeoLimit
app = ClarifaiApp(api_key='YOUR_API_KEY')

geo_p = GeoPoint(116.2317, 39.5427)
geo_l = GeoLimit(limit_type='kilometer', limit_range=1)

imgs = app.inputs.search_by_geo(geo_point=geo_p, geo_limit=geo_l)
```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
client.searchInputs(SearchClause.matchGeo(PointF.at(59F, 29.75F), Radius.of(500, Radius.Unit.KILOMETER)))
            .getPage(1)
            .executeSync();

```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

            await client.SearchInputs(
                    SearchBy.Geo(
                        new GeoPoint(59M, 29.75M),
                        new GeoRadius(500, GeoRadius.RadiusUnit.WithinKilometers)))
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

ClarifaiLocation *loc = [[ClarifaiLocation alloc] initWithLatitude:116.2317 longitude:39.5427];
ClarifaiGeo *geoFilterKilos = [[ClarifaiGeo alloc] initWithLocation:loc radius:50.0 andRadiusUnit:ClarifaiRadiusUnitKilometers];
ClarifaiSearchTerm *term = [ClarifaiSearchTerm searchInputsWithGeoFilter:geoFilterKilos];

[_app search:@[term] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of predicted concept: %@", results[0].score);
}];


```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\GeoPoint;
use Clarifai\DTOs\GeoRadius;
use Clarifai\DTOs\GeoRadiusUnit;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs(
        SearchBy::geoCircle(
            new GeoPoint(3, 0),
            new GeoRadius(500, GeoRadiusUnit::withinKilometers())))
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
          "input": {
            "data": {
              "geo": {
                "geo_point": {
                  "longitude": 59,
                  "latitude": 29.75
                },
                "geo_limit": {
                  "type": "withinKilometers",
                  "value": 1
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



#### Perform a search with two geo points



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
app.inputs.search({
  input: {
    geo: [{
      latitude: 116.2316,
      longitude: 39.5426
    }, {
      latitude: 116.2318,
      longitude: 39.5428
    }]
  }
}).then(
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
from clarifai.rest import ClarifaiApp, GeoBox, GeoPoint
app = ClarifaiApp(api_key='YOUR_API_KEY')

p1 = GeoPoint(116.2316, 39.5426)
p2 = GeoPoint(116.2318, 39.5428)
box1 = GeoBox(point1=p1, point2=p2)

imgs = app.inputs.search_by_geo(geo_box=box1)
```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
client.searchInputs(SearchClause.matchGeo(PointF.at(3F, 0F), PointF.at(70, 30F)))
            .getPage(1)
            .executeSync()
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
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

            await client.SearchInputs(
                    SearchBy.Geo(
                        new GeoPoint(3M, 0M),
                        new GeoPoint(70M, 30M)))
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

ClarifaiLocation *startLoc = [[ClarifaiLocation alloc] initWithLatitude:50 longitude:58];
ClarifaiLocation *endLoc = [[ClarifaiLocation alloc] initWithLatitude:32 longitude:-30];
ClarifaiGeo *geoBox = [[ClarifaiGeo alloc] initWithGeoBoxFromStartLocation:startLoc toEndLocation:endLoc];

[_app search:@[term] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of predicted concept: %@", results[0].score);
}];

```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\GeoPoint;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs(
        SearchBy::geoRectangle(new GeoPoint(3, 0), new GeoPoint(70, 30)))
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
          "input": {
            "data": {
              "geo": {
                "geo_box": [
                  {
                    "geo_point": {
                      "latitude": 35,
                      "longitude": -30
                    }
                  },
                  {
                    "geo_point": {
                      "latitude": 50,
                      "longitude": -35
                    }
                  }
                ]
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



### Search ANDing

You can also combine searches using AND.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js

app.inputs.search([
  { input: { url: 'https://samples.clarifai.com/puppy.jpg' } },
  { concept: { name: 'cat', type: 'input' } },
  { concept: { name: 'dog' } }
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
from clarifai.rest import ClarifaiApp, InputSearchTerm, OutputSearchTerm, SearchQueryBuilder
app = ClarifaiApp(api_key='YOUR_API_KEY')

term1 = InputSearchTerm(concept='cat')
term2 = OutputSearchTerm(concept='dog', value=False)
term3 = OutputSearchTerm(url="https://samples.clarifai.com/metro-north.jpg")

query = SearchQueryBuilder()
query.add_term(term1)
query.add_term(term2)
query.add_term(term3)

app.inputs.search(query)

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java

client.searchInputs()
    .ands(
        SearchClause.matchUserTaggedConcept(Concept.forName("cat")),
        SearchClause.matchConcept(Concept.forName("dog").withValue(false)),
        SearchClause.matchImageVisually(ClarifaiImage.of("https://samples.clarifai.com/metro-north.jpg"))
    )
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

            await client.SearchInputs(
                    SearchBy.UserTaggedConceptName("cat"),
                    SearchBy.ConceptName("dog"),
                    SearchBy.ImageURL("https://samples.clarifai.com/metro-north.jpg"))
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c

//Search for inputs that are predicted as "fast" and visually similar to the given image.
ClarifaiConcept *conceptFromGeneralModel = [[ClarifaiConcept alloc] initWithConceptName:@"fast"];
ClarifaiSearchTerm *term1 = [ClarifaiSearchTerm searchByPredictedConcept:conceptFromGeneralModel];

ClarifaiSearchTerm *term2 = [ClarifaiSearchTerm searchVisuallyWithImageURL:@"https://samples.clarifai.com/metro-north.jpg"];

[_app search:@[term1, term2] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  // Print output of first search result.
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of input matching search query: %@", results[0].score);
}];
```

{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->searchInputs([
        SearchBy::userTaggedConceptName('cat'),
        SearchBy::conceptName('dog'),
        SearchBy::imageURL('https://samples.clarifai.com/metro-north.jpg')
    ])
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

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL

curl -X POST \
  -H "Authorization: Key {api-key}" \
  -H "Content-Type: application/json" \
-d '
{
    "query": {
        "ands": [
            {
                "output": {
                    "input":{
                        "data": {
                            "image": {
                                "url": "http://i.imgur.com/HEoT5xR.png"
                            }
                        }
                    }
                }
            },
            {
                "output": {
                    "data": {
                        "concepts": [
                            {"name":"fast", "value":true}
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
