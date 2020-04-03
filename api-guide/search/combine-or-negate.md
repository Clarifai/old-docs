# Combine or negate

You can also combine searches using AND.

{% tabs %}
{% tab title="js" %}
```javascript
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
{% endtab %}
{% endtabs %}

