# Rank

Rank Order your search results with the intuitive insights of AI. Your model can identify concepts in your data and rank your search results by how confident it is that a given concept is present. You can even rank search results by how similar one input is to another input.

## Search By Concept

Once your images are indexed, you can search for them by concept.

### By clarifai/main App Concepts

When you add an input, it automatically gets predictions from the models in your default which are typically models from the clarifai/main app such as the general model. You can search by those predictions.

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
            And.newBuilder().setOutput( // Setting Output indicates we search for images that have the concept(s)
                                        // which were predicted by the General model.
                Output.newBuilder().setData(
                    Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                        Concept.newBuilder()
                            .setName("people")  // You could search by concept ID as well.
                            .setValue(1f)  // Value of 0 will search for images that don't have the concept.
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
                    output: {  // Setting Output indicates we search for images that have the concept(s)
                               // which were predicted by the General model.
                        data: {
                            concepts: [  // You can search by multiple concepts.
                                {
                                    name: "people",  // You could search by concept ID as well.
                                    value: 1  // Value of 0 will search for images that don't have the concept
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
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_searches_response = stub.PostSearches(
    service_pb2.PostSearchesRequest(
        query=resources_pb2.Query(
            ands=[
                resources_pb2.And(
                    output=resources_pb2.Output( # Setting Output indicates we search for images that have the concept(s)
                                                 # which were predicted by the General model.
                        data=resources_pb2.Data(
                            concepts=[  # You can search by multiple concepts.
                                resources_pb2.Concept(
                                    name="people",  # You could search by concept ID as well.
                                    value=1  # Value of 0 will search for images that don't have the concept.
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
# Setting "output" indicates we search for images that have the concept(s) which were predicted by
# the General model.
#
# Value of 0 will search for images that don't have the concept.
#
# Instead of "name" you can search by "id" as well.

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
                  "name":"people",
                  "value": 1
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postSearchesResponse = stub.postSearches(
    PostSearchesRequest.newBuilder().setQuery(
        Query.newBuilder().addAnds(
            And.newBuilder().setInput( // Setting Input indicates we search for images that have the concept(s)
                                       // which we added to the input manually.
                Input.newBuilder().setData(
                    Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                        Concept.newBuilder()
                            .setName("people")  // You could search by concept ID as well.
                            .setValue(1f)  // Value of 0 will search for images that we marked not to have the concept.
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
                    input: {  // Setting Input indicates we search for images that have the concept(s)
                              // which we added to the input manually.
                        data: {
                            concepts: [  // You can search by multiple concepts.
                                {
                                    name: "people",  // You could search by concept ID as well.
                                    value: 1  // Value of 0 will search for images that we marked not to have the concept.
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
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_searches_response = stub.PostSearches(
    service_pb2.PostSearchesRequest(
        query=resources_pb2.Query(
            ands=[
                resources_pb2.And(
                    input=resources_pb2.Input(  # Setting Input indicates we search for images that have the concept(s)
                                                # which we added to the input manually.
                        data=resources_pb2.Data(
                            concepts=[  # You can search by multiple concepts.
                                resources_pb2.Concept(
                                    name="people",  # You could search by concept ID as well.
                                    value=1  # Value of 0 will search for images that we marked not to have the concept.
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
# Setting "input" indicates we search for images that have the concept(s) which we added to the
# input manually.
#
# Value of 0 will search for images that don't have the concept.
#
# Instead of "name" you can search by "id" as well.

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
                  "name":"people",
                  "value": 1
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

### By clarifai/main and custom concepts

You can combine a search to find inputs that have concepts you have supplied as well as predictions from your model.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
                                .setValue(0f)  // Because of 0, the dog must not be present in the image.
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
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
# Here we search for images which we labeled with "cat" and for which the General prediction model
# does not find a "dog" concept.

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


### By concept in another language

Concepts that have a translation into another langauge can be searched for in that language, even without having the default language for your app being in that language. This uses Clarifai's knowledge graph to lookup the translation and then perform the search. For example, if you app is in english and you want to search for "dog" in Japanese, then you could search wiht `language="ja"` and `name="犬"`.

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
            And.newBuilder().setOutput( // Setting Output indicates we search for images that have the concept(s)
                                        // which were predicted by the General model.
                Output.newBuilder().setData(
                    Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                        Concept.newBuilder()
                            .setName("犬")  // You could search by concept ID as well.
                            .setLanguage("ja") // japanese
                            .setValue(1f)  // Value of 0 will search for images that don't have the concept.
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
                    output: {  // Setting Output indicates we search for images that have the concept(s)
                               // which were predicted by the General model.
                        data: {
                            concepts: [  // You can search by multiple concepts.
                                {
                                    name: "犬",  // You could search by concept ID as well.
                                    language: "ja", // japanese
                                    value: 1  // Value of 0 will search for images that don't have the concept
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
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_searches_response = stub.PostSearches(
    service_pb2.PostSearchesRequest(
        query=resources_pb2.Query(
            ands=[
                resources_pb2.And(
                    output=resources_pb2.Output( # Setting Output indicates we search for images that have the concept(s)
                                                 # which were predicted by the General model.
                        data=resources_pb2.Data(
                            concepts=[  # You can search by multiple concepts.
                                resources_pb2.Concept(
                                    name="犬",  # You could search by concept ID as well.
                                    language="ja", # japanese
                                    value=1  # Value of 0 will search for images that don't have the concept.
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
                  "name":"犬",
                  "language": "ja",
                  "value": 1
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
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postSearchesResponse = stub.postSearches(
    PostSearchesRequest.newBuilder().setQuery(
        Query.newBuilder().addAnds(
            And.newBuilder().setOutput(
                Output.newBuilder().setInput(
                    Input.newBuilder().setData(
                        Data.newBuilder().setImage(
                            Image.newBuilder()
                                .setUrl("{YOUR_IMAGE_URL}")
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
                    output: {
                        input: {
                            data: {
                                image: {
                                    url: "{YOUR_IMAGE_URL}"
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
                    output=resources_pb2.Output(
                        input=resources_pb2.Input(
                            data=resources_pb2.Data(
                                image=resources_pb2.Image(
                                    url="{YOUR_IMAGE_URL}"
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
                  "url": "{YOUR_IMAGE_URL}"
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
                    Data.newBuilder().setImage(
                        Image.newBuilder()
                            .setUrl("{YOUR_IMAGE_URL}")
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
                            image: {
                                url: "{YOUR_IMAGE_URL}"
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
                            image=resources_pb2.Image(
                                url="{YOUR_IMAGE_URL}"
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
                "url": "{YOUR_IMAGE_URL}"
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
