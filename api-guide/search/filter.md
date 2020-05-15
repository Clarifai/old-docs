# Filter

## By Custom Metadata

After you have [added inputs with custom metadata](../data-management/inputs.md#add-inputs-with-custom-metadata), you can search by that metadata.

Below is an example of searching over custom metadata. You can exact match any `key`: `value` pair no matter how nested it is. For example, if the metadata on an input is:

```javascript
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

```javascript
{
  "keyname": "value1"
}
```

```javascript
{
  "somelist": [1,2,3]
}
```

```javascript
{
  "somelist": [1,2]
}
```

```javascript
{
  "somenesting": {"keyname2":"value2"}
}
```

```javascript
{
  "somenesting": {"list2":[5]}
}
```

How to perform searches:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import com.google.protobuf.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postSearchesResponse = stub.postSearches(
    PostSearchesRequest.newBuilder().setQuery(
        Query.newBuilder().addAnds(
            And.newBuilder().setInput(
                Input.newBuilder().setData(
                    Data.newBuilder().setMetadata(
                        Struct.newBuilder()
                            .putFields("type", Value.newBuilder().setStringValue("animal").build())
                    )
                )
            )
        )
    )
    .build()
);

if (postSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post searches failed, status: " + postSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postSearchesResponse.getHitsCount() + ":");
for (Hit hit : postSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for %s\n", hit.getScore(), hit.getInput().getId());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostSearches(
    {
        query: {
            ands: [
                {
                    input: {
                        data: {
                            metadata: {
                                "type": "animal"
                            }
                        }
                    }
                }
            ]
        }
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post searches failed, status: " + response.status.description);
        }

        console.log("Found inputs:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for " + hit.input.id);
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

search_metadata = Struct()
search_metadata.update({"type": "animal"})

post_searches_response = stub.PostSearches(
    service_pb2.PostSearchesRequest(
        query=resources_pb2.Query(
            ands=[
                resources_pb2.And(
                    input=resources_pb2.Input(
                        data=resources_pb2.Data(
                            metadata=search_metadata
                        )
                    )
                )
            ]
        )
    ),
    metadata=metadata
)

if post_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_searches_response.status.description)

print("Found inputs:")
for hit in post_searches_response.hits:
    print("\tScore %.2f for %s" % (hit.score, hit.input.id))
```
{% endtab %}

{% tab title="js" %}
```javascript
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
{% endtab %}

{% tab title="python" %}
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
{% endtab %}

{% tab title="java" %}
```java
JsonObject metadata = new JsonObject();
metadata.addProperty("isPuppy", true);

List<SearchHit> hits = client
  .searchInputs(SearchClause.matchMetadata(metadata))
  .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
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
{% endtab %}

{% tab title="objective-c" %}
```text
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
{% endtab %}

{% tab title="php" %}
```php
// Coming soon
```
{% endtab %}

{% tab title="cURL" %}
```text
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
                "type": "animal"
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

## By Geo Location

Search by geo location allows you to restrict your search results to a bounding box based on longitude and latitude points. There are two ways you can provide longitude/latitude points. You can provide one point and a radius or you can provide two points.

It is important to note that a search by geo location acts as a filter and returns results ranked by any other provided search criteria, whether that is a visual search, concept search or something else. If no other criteria is provided, results will return in the order the inputs were created, NOT by their distance to center of the search area.

If you are providing one point and a radius, the radius can be in "mile", "kilometer", "degree", or "radian", marked by keywords `withinMiles`, `withinKilometers`, `withinDegrees`, `withinRadians`.

If you are providing two points, a box will be drawn from the uppermost point to the lowermost point and the leftmost point to the rightmost point.

Before you perform a search by geo location, make sure you have added inputs with longitude and latitude points.

### Add inputs with longitude and latitude points

Provide a geo point to an input. The geo point is a JSON object consisting of a longitude and a latitude in GPS coordinate system \(SRID 4326\). There can be at most one single geo point associated with each input.

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
                        .setUrl("https://samples.clarifai.com/dog.tiff")
                        .setAllowDuplicateUrl(true)
                )
                .setGeo(
                    Geo.newBuilder().setGeoPoint(
                        GeoPoint.newBuilder()
                            .setLongitude(-30)
                            .setLatitude(40)
                    )
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
        inputs: [
            {
                data: {
                    image: {url: "https://samples.clarifai.com/dog.tiff", allow_duplicate_url: true},
                    geo: {
                        geo_point: {
                            longitude: -30,
                            latitude: 40
                        }
                    }
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
                        url="https://samples.clarifai.com/dog.tiff",
                        allow_duplicate_url=True
                    ),
                    geo=resources_pb2.Geo(
                        geo_point=resources_pb2.GeoPoint(
                            longitude=-30.0,
                            latitude=40.0,
                        )
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
  url: "https://samples.clarifai.com/puppy.jpeg",
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
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp, Geo, GeoPoint
app = ClarifaiApp(api_key='YOUR_API_KEY')

geo_p1 = Geo(geo_point=GeoPoint(116.2317,39.5427))

app.inputs.create_image_from_url(url="https://samples.clarifai.com/puppy.jpeg", geo=geo_p1)
```
{% endtab %}

{% tab title="java" %}
```java
client.addInputs().plus(ClarifaiInput.forImage("https://samples.clarifai.com/puppy.jpeg")
    .withGeo(PointF.at(116.2317F, 39.5427F))).executeSync();
```
{% endtab %}

{% tab title="csharp" %}
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
                        "https://samples.clarifai.com/puppy.jpeg",
                        geo: new GeoPoint(116.2317M, 39.5427M)))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/metro-north.jpg"];
image.location = [[ClarifaiLocation alloc] initWithLatitude:116.2317 longitude:39.5427];

[_app addInputs:@[image] completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
  NSLog(@"%@",inputs);
}];
```
{% endtab %}

{% tab title="php" %}
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
{% endtab %}
{% endtabs %}

### Perform a search with one geo point and radius in kilometers

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postSearchesResponse = stub.postSearches(
    PostSearchesRequest.newBuilder().setQuery(
        Query.newBuilder().addAnds(
            And.newBuilder().setInput(
                Input.newBuilder().setData(
                    Data.newBuilder().setGeo(
                        Geo.newBuilder()
                            .setGeoPoint(
                                GeoPoint.newBuilder()
                                    .setLongitude(-29)
                                    .setLatitude(40)
                            )
                            .setGeoLimit(
                                GeoLimit.newBuilder()
                                    .setType("withinKilometers")
                                    .setValue(150.0f)
                            )
                    )
                )
            )
        )
    )
    .build()
);

if (postSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post searches failed, status: " + postSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postSearchesResponse.getHitsCount() + ":");
for (Hit hit : postSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for %s\n", hit.getScore(), hit.getInput().getId());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostSearches(
    {
        query: {
            ands: [
                {
                    input: {
                        data: {
                            geo: {
                                geo_point: {
                                    longitude: -29,
                                    latitude: 40
                                },
                                geo_limit: {
                                    type: "withinKilometers",
                                    value: 150.0
                                }
                            }
                        }
                    }
                }
            ]
        }
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post searches failed, status: " + response.status.description);
        }

        console.log("Found inputs:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for " + hit.input.id);
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

post_searches_response = stub.PostSearches(
    service_pb2.PostSearchesRequest(
        query=resources_pb2.Query(
            ands=[
                resources_pb2.And(
                    input=resources_pb2.Input(
                        data=resources_pb2.Data(
                            geo=resources_pb2.Geo(
                                geo_point=resources_pb2.GeoPoint(
                                    longitude=-29.0,
                                    latitude=40.0,
                                ),
                                geo_limit=resources_pb2.GeoLimit(
                                    type="withinKilometers",
                                    value=150.0
                                )
                            )
                        )
                    )
                )
            ]
        )
    ),
    metadata=metadata
)

if post_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_searches_response.status.description)

print("Found inputs:")
for hit in post_searches_response.hits:
    print("\tScore %.2f for %s" % (hit.score, hit.input.id))
```
{% endtab %}

{% tab title="js" %}
```javascript
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
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp, GeoPoint, GeoLimit
app = ClarifaiApp(api_key='YOUR_API_KEY')

geo_p = GeoPoint(116.2317, 39.5427)
geo_l = GeoLimit(limit_type='kilometer', limit_range=1)

imgs = app.inputs.search_by_geo(geo_point=geo_p, geo_limit=geo_l)
```
{% endtab %}

{% tab title="java" %}
```java
client.searchInputs(SearchClause.matchGeo(PointF.at(59F, 29.75F), Radius.of(500, Radius.Unit.KILOMETER)))
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
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiLocation *loc = [[ClarifaiLocation alloc] initWithLatitude:116.2317 longitude:39.5427];
ClarifaiGeo *geoFilterKilos = [[ClarifaiGeo alloc] initWithLocation:loc radius:50.0 andRadiusUnit:ClarifaiRadiusUnitKilometers];
ClarifaiSearchTerm *term = [ClarifaiSearchTerm searchInputsWithGeoFilter:geoFilterKilos];

[_app search:@[term] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of predicted concept: %@", results[0].score);
}];
```
{% endtab %}

{% tab title="php" %}
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
              "geo": {
                "geo_point": {
                  "longitude": -29.0,
                  "latitude": 40.0
                },
                "geo_limit": {
                  "type": "withinKilometers",
                  "value": 150
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

### Perform a search with two geo points

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postSearchesResponse = stub.postSearches(
    PostSearchesRequest.newBuilder().setQuery(
        Query.newBuilder().addAnds(
            And.newBuilder().setInput(
                Input.newBuilder().setData(
                    Data.newBuilder().setGeo(
                        Geo.newBuilder()
                            .addGeoBox(
                                GeoBoxedPoint.newBuilder().setGeoPoint(
                                    GeoPoint.newBuilder()
                                        .setLongitude(-31)
                                        .setLatitude(42)
                                )
                            )
                            .addGeoBox(
                                GeoBoxedPoint.newBuilder().setGeoPoint(
                                    GeoPoint.newBuilder()
                                        .setLongitude(-29)
                                        .setLatitude(39)
                                ).build()
                            )
                    )
                )
            )
        )
    )
    .build()
);

if (postSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post searches failed, status: " + postSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postSearchesResponse.getHitsCount() + ":");
for (Hit hit : postSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for %s\n", hit.getScore(), hit.getInput().getId());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostSearches(
    {
        query: {
            ands: [
                {
                    input: {
                        data: {
                            geo: {
                                geo_box: [
                                    {
                                        geo_point: {
                                            longitude: -31,
                                            latitude: 42
                                        }
                                    },
                                    {
                                        geo_point: {
                                            longitude: -29,
                                            latitude: 39
                                        }
                                    }
                                ]
                            }
                        }
                    }
                }
            ]
        }
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post searches failed, status: " + response.status.description);
        }

        console.log("Found inputs:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for " + hit.input.id);
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

post_searches_response = stub.PostSearches(
    service_pb2.PostSearchesRequest(
        query=resources_pb2.Query(
            ands=[
                resources_pb2.And(
                    input=resources_pb2.Input(
                        data=resources_pb2.Data(
                            geo=resources_pb2.Geo(
                                geo_box=[
                                    resources_pb2.GeoBoxedPoint(
                                        geo_point=resources_pb2.GeoPoint(
                                            longitude=-31.0,
                                            latitude=42.0,
                                        ),
                                    ),
                                    resources_pb2.GeoBoxedPoint(
                                        geo_point=resources_pb2.GeoPoint(
                                            longitude=-29.0,
                                            latitude=39.0,
                                        ),
                                    ),
                                ]
                            )
                        )
                    )
                )
            ]
        )
    ),
    metadata=metadata
)

if post_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_searches_response.status.description)

print("Found inputs:")
for hit in post_searches_response.hits:
    print("\tScore %.2f for %s" % (hit.score, hit.input.id))
```
{% endtab %}

{% tab title="js" %}
```javascript
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
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp, GeoBox, GeoPoint
app = ClarifaiApp(api_key='YOUR_API_KEY')

p1 = GeoPoint(116.2316, 39.5426)
p2 = GeoPoint(116.2318, 39.5428)
box1 = GeoBox(point1=p1, point2=p2)

imgs = app.inputs.search_by_geo(geo_box=box1)
```
{% endtab %}

{% tab title="java" %}
```java
client.searchInputs(SearchClause.matchGeo(PointF.at(3F, 0F), PointF.at(70, 30F)))
            .getPage(1)
            .executeSync()
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
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiLocation *startLoc = [[ClarifaiLocation alloc] initWithLatitude:50 longitude:58];
ClarifaiLocation *endLoc = [[ClarifaiLocation alloc] initWithLatitude:32 longitude:-30];
ClarifaiGeo *geoBox = [[ClarifaiGeo alloc] initWithGeoBoxFromStartLocation:startLoc toEndLocation:endLoc];

[_app search:@[term] page:@1 perPage:@20 completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  NSLog(@"inputID: %@", results[0].inputID);
  NSLog(@"URL: %@", results[0].mediaURL);
  NSLog(@"probability of predicted concept: %@", results[0].score);
}];
```
{% endtab %}

{% tab title="php" %}
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
              "geo": {
                "geo_box": [
                  {
                    "geo_point": {
                      "latitude": 42,
                      "longitude": -31
                    }
                  },
                  {
                    "geo_point": {
                      "latitude": 39,
                      "longitude": -29
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
{% endtab %}
{% endtabs %}

