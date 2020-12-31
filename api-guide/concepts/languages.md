---
description: Multilingual support in Clarifai
---

# Languages

The Clarifai API supports many languages in addition to English. These are represented as translations of the names of concepts so that when you search by concept name or get predictions from a model's concepts you can utilize the language of your choice.

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

![create new app](../../.gitbook/assets/create-new-app-new%20%282%29%20%282%29%20%284%29%20%286%29%20%286%29%20%286%29%20%286%29%20%283%29.png)

## List language translations by concept ID

You can see all the language translations for a given concept ID with a GET call. This call supports [pagination](../api-overview/pagination.md).

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptResponse listConceptLanguagesResponse = stub.listConceptLanguages(
    ListConceptLanguagesRequest.newBuilder()
        .setConceptId("charlie")
        .build()
);

if (listConceptLanguagesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List concept languages failed, status: " + listConceptLanguagesResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListConceptLanguages(
    {
      concept_id: "charlie"
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
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_concept_languages_response = stub.ListConceptLanguages(
    service_pb2.ListConceptLanguagesRequest(
        concept_id="charlie"
    ),
    metadata=metadata
)

if list_concept_languages_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List concept failed, status: " + list_concept_languages_response.status.description)
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

## Get specific language translation for a concept

To get a single language translation you have for a concept you can get by the language code and concept id.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptResponse getConceptLanguageResponse = stub.getConceptLanguage(
    ListConceptLanguageRequest.newBuilder()
        .setConceptId("charlie")
        .setLanguage("ja")
        .build()
);

if (getConceptLanguageResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List concept languages failed, status: " + getConceptLanguageResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.GetConceptLanguage(
    {
      concept_id: "charlie",
      language: "ja"
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
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_concept_language_response = stub.GetConceptLanguage(
    service_pb2.GetConceptLanguageRequest(
        concept_id="charlie",
        language="ja"
    ),
    metadata=metadata
)

if get_concept_langauge_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get concept failed, status: " + get_concept_language_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/concepts/{concept_id}/languages/{language}
```
{% endtab %}
{% endtabs %}

## Add a language translation for a concept

To create a langauge translation for a concept you can POST that language translation.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptResponse postConceptLanguageResponse = stub.postConceptLanguage(
    PostConceptLanguageRequest.newBuilder()
        .setConceptId("charlie")
        .addConceptLanguages(ConceptLanguage.newBuilder().setId("ja").setName("ボスコ"))
        .build()
);

if (postConceptLanguageResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post concept languages failed, status: " + postConceptLanguageResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostConceptLanguage(
    {
      concept_id: "charlie",
      concept_languages: [
        {
          id: "ja",
          name: "ボスコ"
        }
      ]
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
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_concept_language_response = stub.PostConceptLanguage(
    service_pb2.PostConceptLanguageRequest(
        concept_id="charlie",
        concept_languages=[resources_pb2.ConceptLanguages(
          id="ja",
          name="ボスコ"
        )]
    ),
    metadata=metadata
)

if get_concept_langauge_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get concept failed, status: " + get_concept_language_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/concepts/{concept_id}/languages/{language}
```
{% endtab %}
{% endtabs %}

## Update a language translation for a concept

To update a langauge translation for a concept you can PATCH that language translation.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptResponse patchConceptLanguageResponse = stub.patchConceptLanguage(
    PatchConceptLanguageRequest.newBuilder()
        .setAction("overwrite")
        .setConceptId("charlie")
        .addConceptLanguages(ConceptLanguage.newBuilder().setId("ja").setName("new name"))
        .build()
);

if (patchConceptLanguageResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch concept languages failed, status: " + patchConceptLanguageResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchConceptLanguage(
    {
      action: "overwrite",
      concept_id: "charlie",
      concept_languages: [
        {
          id: "ja",
          name: "new name"
        }
      ]
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
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_concept_language_response = stub.PatchConceptLanguage(
    service_pb2.PatchConceptLanguageRequest(
        concept_id="charlie",
        concept_languages=[resources_pb2.ConceptLanguages(
          id="ja",
          name="new name"
        )],
        action="overwrite"
    ),
    metadata=metadata
)

if get_concept_langauge_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get concept failed, status: " + get_concept_language_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/concepts/{concept_id}/languages/{language}
```
{% endtab %}
{% endtabs %}

