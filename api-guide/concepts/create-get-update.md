---
description: Manage your concepts.
---

# Create, Get, Update

Within your app you can create concpets, modify them after creation an get them from yoru app. We currently do not support deleting concepts since they are such an integral tie across almost all other data structures in the platform like inputs, models, searches, etc.

You will find that some of our endpoints have additional information returned from the clarifai/main app which contains our pre-trained models but also a large knowledge graph we've assembled over the years.

## Create

### Add Concepts

To create a new concept in you app you POST the concept with an id and name. You can also post more than one concept in the same API by sending a list of concepts.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "concepts": [
    {
      "id": "{CONCEPT_ID}",
      "name": "{CONCEPT_NAME}"
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/concepts", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Get

### Get Concept by ID

You can get a singular concept by it's ID.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Javascript (REST)" %}
```javascript
const conceptId = '{CONCEPT_ID}'
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/concepts/${conceptId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### List concepts

You can get a list of concepts within your app with a GET call. This call supports [pagination](../advanced-topics/pagination.md)

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptResponse listConceptsResponse = stub.listConcepts(
    ListConceptsRequest.newBuilder()
        .build()
);

if (listConceptsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List concepts failed, status: " + listConceptsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/concepts`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Update

### Update Concept Name

The code below showcases how to update a concept's name given its id by using the "overwrite" action. You can also patch multiple concepts by sending a list of concepts.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "concepts": [
    {
      "id": "charlie",
      "name": "Charlie Name"
    }
  ],
  "action": "overwrite"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/concepts", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

