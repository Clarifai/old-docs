# Knowledge Graph

# What is the Clarifai Knowledge Graph?

You will find that some of our endpoints have additional information returned from the clarifai/main app which contains our pre-trained models but also a large knowledge graph we've assembled over the years.

The nodes of the knowledge graph are concpets (aka unique things in the world). In the knowledge graph we have done significant AI research and human verification to split apart concepts that have different meanings into different concepts.

Once we had different and clear meanings for the concepts, we could introduce translations of the concept name into other languages and relationships between concepts such as "dog" is an "animal" or
  "pup" and "puppy" are synonyms.


When interacting with concepts in search queries, model predict requests, etc. we allow in many cases to perform operations with the names of concpets in the other languages.

Since names can appear in differnt languages and have different meanings, it is always important to remember to use concept IDs when interacting with our API and not concept names.

## Supported Languages

The currently supported languages are listed below.

| Language | Code |
| :--- | :--- |
| Arabic \(ar\) | ar |
| Bengali \(bn\) | bn |
| Danish \(da\) | da |
| German \(de\) | de |
| English \(en\) | en |
| Spanish \(es\) | es |
| Finnish \(fi\) | fi |
| French \(fr\) | fr |
| Hindi \(hi\) | hi |
| Hungarian \(hu\) | hu |
| Italian \(it\) | it |
| Japanese \(ja\) | ja |
| Korean \(ko\) | ko |
| Dutch \(nl\) | nl |
| Norwegian \(no\) | no |
| Punjabi \(pa\) | pa |
| Polish \(pl\) | pl |
| Portuguese \(pt\) | pt |
| Russian \(ru\) | ru |
| Swedish \(sv\) | sv |
| Turkish \(tr\) | tr |
| Chinese Simplified \(zh\) | zh |
| Chinese Traditional \(zh-TW\) | zh-TW |

## Default Language

When you create a new Application, you must specify a default language. This will be the default language concepts are returned in when you do not explicitly set a language in an API request. You cannot change the default language. You can however change languages per request.

![create new app](../../images/create-new-app-new.png)


## List Language trasnaltions by concept ID

You can see all the language translations for a given concept ID with a GET call. This call supports [pagination](../api-overview/pagination.md).


{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiConceptResponse listConceptLanguagesResponse = stub.listConceptLanguages(
    ListConceptLanguagesRequest.newBuilder()
        .setConceptId("boscoe")
        .build()
);

if (listConceptLanguagesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List concept languages failed, status: " + listConceptLanguagesResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.ListConceptLanguages(
    {
      concept_id: "boscoe"
    },
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

list_concept_languages_response = stub.ListConceptLanguages(
    service_pb2.ListConceptLanguagesRequest(
        concept_id="boscoe"
    ),
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
  https://api.clarifai.com/v2/concepts/{concept_id}/languages
```
{% endtab %}
{% endtabs %}
<
