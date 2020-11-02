# Combine or Negate

You can also combine searches using AND.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

// Here we search for images which we labeled with "cat" and for which the General prediction model does not find
// a "dog" concept.
MultiSearchResponse postSearchesResponse = stub.postSearches(
    PostSearchesRequest.newBuilder().setQuery(
        Query.newBuilder()
            .addAnds(
                And.newBuilder().setInput( // Setting Input indicates we search for images that have the concept(s)
                                           // which we added to the input manually.
                    Input.newBuilder().setData(
                        Data.newBuilder().addConcepts(
                            Concept.newBuilder()
                                .setName("cat")
                                .setValue(1f)
                        )
                    )
                )
            )
            .addAnds(
                And.newBuilder().setOutput(  // Setting Output indicates we search for images that have the concept(s)
                                             // which were predicted by the General model.
                    Output.newBuilder().setData(
                        Data.newBuilder().addConcepts(
                            Concept.newBuilder()
                                .setName("dog")
                                .setValue(0f)
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
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

// Here we search for images which we labeled with "cat" and for which the General prediction model does not find
// a "dog" concept.
stub.PostSearches(
    {
        query: {
            ands: [
                {
                    input: {  // Setting Input indicates we search for images that have the concept(s)
                              // which we added to the input manually.
                        data: {
                            concepts: [
                                {
                                    name: "cat",
                                    value: 1
                                }
                            ]
                        }
                    }
                },
                {
                    output: {  // Setting Output indicates we search for images that have the concept(s)
                               // which were predicted by the General model.
                        data: {
                            concepts: [
                                {
                                    name: "dog",
                                    value: 0
                                }
                            ]
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
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

# Here we search for images which we labeled with "cat" and for which the General prediction model does not find
# a "dog" concept.
post_searches_response = stub.PostSearches(
    service_pb2.PostSearchesRequest(
        query=resources_pb2.Query(
            ands=[
                resources_pb2.And(
                    input=resources_pb2.Input(  # Setting Input indicates we search for images that have the concept(s)
                                                # which we added to the input manually.
                        data=resources_pb2.Data(
                            concepts=[
                                resources_pb2.Concept(
                                    name="cat",
                                    value=1
                                )
                            ]
                        )
                    )
                ),
                resources_pb2.And(
                    output=resources_pb2.Output(  # Setting Output indicates we search for images that have the concept(s)
                                                  # which were predicted by the General model.
                        data=resources_pb2.Data(
                            concepts=[
                                resources_pb2.Concept(
                                    name="dog",
                                    value=0
                                )
                            ]
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
app.inputs.search([
  { input: { url: 'https://samples.clarifai.com/puppy.jpeg' } },
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
{% endtab %}

{% tab title="python" %}
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
{% endtab %}

{% tab title="java" %}
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
                    SearchBy.ConceptName("dog"),
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
{% endtab %}

{% tab title="php" %}
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
{% endtab %}

{% tab title="cURL" %}
```text
# Here we search for images which we labeled with "cat" and for which the General prediction model does not find
# a "dog" concept.

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
                        "concepts": [
                            {
                                "name": "cat",
                                "value": 1
                            }
                        ]
                    }
                }
            },
            {
                "output": {
                    "data": {
                        "concepts": [
                            {
                                "name": "dog",
                                "value": 0
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

