---
description: Connect the knowledge gained by different models.
---

# Knowledge Graph



![](../../.gitbook/assets/kg6.png)

The Knowledge Graph uses Clarifai's concept mapping model to establish a hierarchical relationship between your concepts. and to uses three different _predicates_ to organize your concepts: hypernyms, hyponyms, and synonyms.

**Hyponym** represents an 'is a kind of' relation. The following relationship: 'honey' \(subject\), 'hyponym' \(predicate\), 'food' \(object\) is more easily be read as 'honey' 'is a kind of' 'food'.

**Hypernym** is the opposite of 'hyponym'. When you add one of the relationships the opposite will automatically appear for you in queries. The 'hypernym' can be read as 'is a parent of' so: 'food' \(subject\), 'hypernym' \(predicate\), 'honey' \(object\) can more easily be read as:'food' is a parent of 'honey'.

**Synonym** The 'synonym' relation defines two concepts that essential mean the same thing. This is more like a "is" relationship. So for example a 'synonym' relationship could be: "puppy" is "pup" The reverse is also true once the former is added so: "pup" is "puppy" will appear in queries as well.

## Create

To create a relation between two concepts, you first have to create them in your custom model. See [the Concepts page](https://docs.clarifai.com/api-guide/concepts/concepts) on how to do that programatically.

Each relation has to have specified a predicate, which can be _hyponym_, _hypernym_, or _synonym_.

{% tabs %}
{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_concept_relation_response = stub.PostConceptRelations(
    service_pb2.PostConceptRelationsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        concept_id="{YOUR_SUBJECT_CONCEPT_ID}",
        concept_relations=[
            resources_pb2.ConceptRelation(
                object_concept=resources_pb2.Concept(id="{YOUR_OBJECT_CONCEPT_ID}"),
                predicate="hypernym" # This can be hypernym, hyponym, or synonym.
            )
        ]
    ),
    metadata=metadata
)

if post_concept_relation_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_concept_relation_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_concept_relation_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_concept_relation_response.outputs[0].status.details))
    raise Exception("Post concept relation failed, status: " + post_concept_relation_response.status.description)
```
{% endtab %}

{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptRelationResponse postConceptRelationsResponse = stub.postConceptRelations(
    PostConceptRelationsRequest.newBuilder()
        .setUserAppId(
            UserAppIDSet.newBuilder()
                .setAppId("{YOUR_APP_ID}")
                .build()
        )
        .setConceptId("{YOUR_SUBJECT_CONCEPT_ID}")
        .addConceptRelations(
            ConceptRelation.newBuilder()
                .setObjectConcept(Concept.newBuilder().setId("{YOUR_OBJECT_CONCEPT_ID}").build())
                .setPredicate("hypernym").build()) // This can be hypernym, hypnonym, or synonym.
        .build()
);

if (postConceptRelationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post concept relations failed, status: " + postConceptRelationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostConceptRelations(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        concept_id: "{YOUR_SUBJECT_CONCEPT_ID}",
        concept_relations: [
            {
                object_concept: {
                    id: "{YOUR_OBJECT_CONCEPT_ID}",
                },
                predicate: "hypernym" // This can be hypernym, hyponym, or synonym.
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Create concept relations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{YOUR_APP_ID}/concepts/{YOUR_SUBJECT_CONCEPT_ID}/relations' \
    -H 'Authorization: Key {YOUR_PERSONAL_ACCESS_TOKEN}' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "concept_relations": [
            {
                "object_concept": {
                    "id": "{YOUR_OBJECT_CONCEPT_ID}"
                },
                "predicate": "hypernym"
            }
        ]
    }'
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const subjectConceptId = '{YOUR_SUBJECT_CONCEPT_ID}'

const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "concept_relations": [
      {
          "object_concept": {
              "id": "{YOUR_OBJECT_CONCEPT_ID}"
          },
          "predicate": "hypernym"
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

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/concepts/${subjectConceptId}/relations`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## List existing relations

{% tabs %}
{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_concept_relation_response = stub.ListConceptRelations(
    service_pb2.ListConceptRelationsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        concept_id="{YOUR_CONCEPT_ID}",
        predicate="hypernym"  # This is optional. If skipped, all concept's relations will be returned.
    ),
    metadata=metadata
)

if list_concept_relation_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(list_concept_relation_response.outputs[0].status.code))
    print("\tDescription: {}".format(list_concept_relation_response.outputs[0].status.description))
    print("\tDetails: {}".format(list_concept_relation_response.outputs[0].status.details))
    raise Exception("List concept relation failed, status: " + list_concept_relation_response.status.description)

for relation in list_concept_relation_response.concept_relations:
    print(relation)
```
{% endtab %}

{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptRelationResponse listConceptRelationsResponse = stub.listConceptRelations(
    ListConceptRelationsRequest.newBuilder()
        .setUserAppId(
            UserAppIDSet.newBuilder()
                .setAppId("{YOUR_APP_ID}")
                .build()
        )
        .setConceptId("{YOUR_CONCEPT_ID}")
        .setPredicate("hypernym")  // This is optional. If skipped, all concept's relations will be returned.
        .build()
);


if (listConceptRelationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List concept relations failed, status: " + listConceptRelationsResponse.getStatus());
}

for (ConceptRelation relation : listConceptRelationsResponse.getConceptRelationsList()) {
    System.out.println(relation);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListConceptRelations(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        concept_id: "{YOUR_CONCEPT_ID}",
        predicate: "hypernym" // This is optional. If skipped, all concept's relations will be returned.
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List concept relations failed, status: " + response.status.description);
        }

        for (const relation of response.concept_relations) {
            console.log(relation);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
# Setting the predicate GET parameter is optional. If skipped, all concept's relations will be returned.
curl -X GET 'https://api.clarifai.com/v2/users/me/apps/{YOUR_APP_ID}/concepts/{YOUR_CONCEPT_ID}/relations?predicate=hypernym' \
    -H 'Authorization: Key {YOUR_PERSONAL_ACCESS_TOKEN}' \
    -H 'Content-Type: application/json'
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const conceptId = '{YOUR_CONCEPT_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

// Setting the predicate GET parameter is optional. If skipped, all concept's relations will be returned
fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/concepts/${conceptId}/relations?predicate=hypernym`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Delete

{% tabs %}
{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_concept_relation_response = stub.DeleteConceptRelations(
    service_pb2.DeleteConceptRelationsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        concept_id="{YOUR_OBJECT_CONCEPT_ID}",
        ids=["{YOUR_CONCEPT_RELATION_ID}"]
    ),
    metadata=metadata
)

if delete_concept_relation_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(delete_concept_relation_response.outputs[0].status.code))
    print("\tDescription: {}".format(delete_concept_relation_response.outputs[0].status.description))
    print("\tDetails: {}".format(delete_concept_relation_response.outputs[0].status.details))
    raise Exception("Delete concept relation failed, status: " + delete_concept_relation_response.status.description)
```
{% endtab %}

{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteConceptRelationsResponse = stub.deleteConceptRelations(
    DeleteConceptRelationsRequest.newBuilder()
        .setUserAppId(
            UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}").build()
        )
        .addIds("{YOUR_CONCEPT_RELATION_ID}")
        .setConceptId("{YOUR_OBJECT_CONCEPT_ID}")
        .build()
);

if (deleteConceptRelationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete concept relations failed, status: " + deleteConceptRelationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteConceptRelations(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        concept_id: "{YOUR_OBJECT_CONCEPT_ID}",
        ids: [
            "{YOUR_CONCEPT_RELATION_ID}"
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete concept relations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE 'https://api.clarifai.com/v2/users/me/apps/{YOUR_APP_ID}/concepts/{YOUR_OBJECT_CONCEPT_ID}/relations' \
    -H 'Authorization: Key {YOUR_PERSONAL_ACCESS_TOKEN}' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "ids": [
            "{YOUR_CONCEPT_RELATION_ID}"
        ]
    }'
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const conceptId = '{YOUR_CONCEPT_ID}'

const raw = JSON.stringify({
	"ids": [
	  "{YOUR_CONCEPT_RELATION_ID}"
  ]
})

const requestOptions = {
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/concepts/${conceptId}/relations`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

