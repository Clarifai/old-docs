Within your app you can create concpets, modify them after creation an get them from yoru app. We currently do not support deleting concepts since they are such an integral tie across almost all other data structures in the platform like inputs, models, searches, etc.

You will find that some of our endpoints have additional information returned from the clarifai/main app which contains our pre-trained models but also a large knowledge graph we've assembled over the years.

### Create
#### Add Concepts

To create a new concept in you app you POST the concept with an id and name. You can also post more than one concept in the same API by sending a list of concepts.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiConceptResponse postConceptsResponse = stub.postConcepts(
    PostConceptsRequest.newBuilder()
        .addConcepts(Concept.newBuilder().setId("charlie").setName("Charlie Name"))
        .build()
);

if (postConceptsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post concepts failed, status: " + postConceptsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostConcepts(
    {
        concepts: [{id: "charlie", name: "Charlie Name"}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post concepts failed, status: " + response.status.description);
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

post_concepts_response = stub.PostConcepts(
    service_pb2.PostConceptsRequest(
        concepts=[resources_pb2.Concept(id="charlie", name="Charlie Name")]
    ),
    metadata=metadata
)

if post_concepts_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post concept failed, status: " + post_concepts_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "concepts": [
      {
        "id": "{concept_id}",
        "name": "{new_concept_name}"
      }
      ]
  }'\
  https://api.clarifai.com/v2/concepts
```
{% endtab %}
{% endtabs %}



### Get
#### Get Concept by ID

You can get a singular concept by it's ID.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

SingleConceptResponse getConceptResponse = stub.getConcept(
    GetConceptRequest.newBuilder()
        .setConceptId("charlie")
        .build()
);

if (getConceptsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get concepts failed, status: " + getConceptsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.GetConcept(
    {
        concept_id: "bosco"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get concepts failed, status: " + response.status.description);
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

get_concepts_response = stub.GetConcept(
    service_pb2.GetConceptRequest(
        concept_id="charlie"
    ),
    metadata=metadata
)

if get_concepts_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get concept failed, status: " + get_concepts_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/concepts/{concept_id}
```
{% endtab %}
{% endtabs %}


#### List concepts

You can get a list of concepts within your app with a GET call. This call supports [pagination](../api-overview/pagination.md)

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiConceptResponse listConceptsResponse = stub.listConcepts(
    ListConceptsRequest.newBuilder()
        .build()
);

if (listConceptsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List concepts failed, status: " + listConceptsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.ListConcepts(
    {},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List concepts failed, status: " + response.status.description);
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

list_concepts_response = stub.ListConcepts(
    service_pb2.ListConceptsRequest(),
    metadata=metadata
)

if list_concepts_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List concept failed, status: " + list_concepts_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/concepts
```
{% endtab %}
{% endtabs %}


### Update
#### Update Concept Name

The code below showcases how to update a concept's name given its id by using the "overwrite" action. You can also patch multiple concepts by sending a list of concepts.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiConceptResponse patchConceptsResponse = stub.patchConcepts(
    PatchConceptsRequest.newBuilder()
        .setAction("overwrite")  // The only supported action right now is overwrite.
        .addConcepts(Concept.newBuilder().setId("charlie").setName("Charlie Name"))
        .build()
);

if (patchConceptsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch concepts failed, status: " + patchConceptsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PatchConcepts(
    {
        action: "overwrite",  // The only supported action right now is overwrite
        concepts: [{id: "charlie", name: "Charlie Name"}]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch concepts failed, status: " + response.status.description);
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

patch_concepts_response = stub.PatchConcepts(
    service_pb2.PatchConceptsRequest(
        action="overwrite",  # The only supported action right now is overwrite.
        concepts=[resources_pb2.Concept(id="charlie", name="Charlie Name")]
    ),
    metadata=metadata
)

if patch_concepts_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch concept failed, status: " + patch_concepts_response.status.description)
```
{% endtab %}

{% tab title="js" %}
```javascript
** Coming Soon
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.concepts.update(concept_id='concept_id', concept_name='new_concept_name')
```
{% endtab %}

{% tab title="java" %}
```java
** Coming Soon
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModifyConcepts(
                    new Concept("{concept-id}", name: "{new-concept-name}"))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
** Coming Soon
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modifyConcepts((new Concept('CONCEPT'))->withName('UPDATED_CONCEPT_NAME'))
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
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "concepts": [
      {
        "id": "charlie",
        "name": "Charlie Name"
      }
      ],
    "action": "overwrite"
  }'\
  https://api.clarifai.com/v2/concepts
```
{% endtab %}
{% endtabs %}
