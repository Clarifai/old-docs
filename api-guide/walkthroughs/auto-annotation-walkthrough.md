# Auto Annotation

This tutorial demonstrates how auto-annotation workflows can be configured in the Clarifai API. With auto-annotation, you can use model predictions to label your inputs. Auto-annotation can help you to prepare training data, or assign other useful labels and metadata to your inputs. Since models are doing most of the work of annotating your data, this enables you to speed-up and scale-up your annotation process while ensuring quality standards, typically reducing human effort of labelling data by orders of magnitude. And since this is built into our APIs it seamlessly integrates with all the search, training and prediction functionality of the Clarifai platform.

When a concept is predicted by a model, it is predicted with a confidence score between 0 and 1. In this walkthrough we will leverage that score in our workflow so that when your model predictions are confident \(close to 1\), you can have your data automatically labeled with that concept. When your predictions are less-than-confident, you can have your input sent to a human being for review.

## Create Concepts

Create the concepts that we'll be using in our model. In this tutorial we'll create the following concepts: `people`, `man` and `adult`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_concepts_response = stub.PostConcepts(
    service_pb2.PostConceptsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        concepts=[
            resources_pb2.Concept(id="peopleID", name="people"),
            resources_pb2.Concept(id="manID", name="man"),
            resources_pb2.Concept(id="adultID", name="adult"),
        ]
    ),
    metadata=metadata
)

if post_concepts_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_concepts_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_concepts_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_concepts_response.outputs[0].status.details))
    raise Exception("Post concepts failed, status: " + post_concepts_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptResponse postConceptsResponse = stub.postConcepts(
    PostConceptsRequest.newBuilder()
        .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
        .addConcepts(
            Concept.newBuilder()
                .setId("peopleID")
                .setName("people")
        )
        .addConcepts(
            Concept.newBuilder()
                .setId("manID")
                .setName("man")
        )
        .addConcepts(
            Concept.newBuilder()
                .setId("adultID")
                .setName("adult")
        )
        .build()
);

if (postConceptsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post concepts failed, status: " + postConceptsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostConcepts(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        concepts: [
            {
                id: "peopleID",
                name: "people"
            },
            {
                id: "manID",
                name: "man"
            },
            {
                id: "adultID",
                name: "adult"
            },
        ]
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

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/concepts' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "concepts": [
            {
                "id": "peopleID",
                "name": "people"
            },
            {
                "id": "manID",
                "name": "man"
            },
            {
                "id": "adultID",
                "name": "adult"
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

## Link Concepts

Link the newly created concepts with concepts in the Clarifai/Main General model.

Run the code below three times, once for each concept created previously. The concept IDs of the clarifai/main General models are the following:

* `ai_l8TKp2h5` - the people concept,
* `ai_dxSG2s86` - the man concept,
* `ai_VPmHr5bm` - the adult concept.

Your model's concept IDs are the ones you created in the previous step: `peopleID`, `manID`, and `adultID`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_concept_relations_response = stub.PostConceptRelations(
    service_pb2.PostConceptRelationsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        concept_id="{YOUR_MODEL_CONCEPT_ID}",
        concept_relations=[
            resources_pb2.ConceptRelation(
                object_concept=resources_pb2.Concept(id="{GENERAL_MODEL_CONCEPT_ID}", app_id="main"),
                predicate="synonym"
            )
        ]
    ),
    metadata=metadata
)

if post_concept_relations_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_concept_relations_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_concept_relations_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_concept_relations_response.outputs[0].status.details))
    raise Exception("Post concept relations failed, status: " + post_concept_relations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptRelationResponse postConceptRelationsResponse = stub.postConceptRelations(
    PostConceptRelationsRequest.newBuilder()
        .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
        .setConceptId("{YOUR_MODEL_CONCEPT_ID}")
        .addConceptRelations(
            ConceptRelation.newBuilder()
                .setObjectConcept(
                    Concept.newBuilder()
                        .setId("{GENERAL_MODEL_CONCEPT_ID}")
                        .setAppId("main")
                )
                .setPredicate("synonym").build())
        .build()
);

if (postConceptRelationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post concept relations failed, status: " + postConceptRelationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostConceptRelations(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        concept_id: "{YOUR_MODEL_CONCEPT_ID}",
        concept_relations: [
            {
                object_concept: {
                    id: "{GENERAL_MODEL_CONCEPT_ID}",
                    app_id: "main"
                },
                predicate: "synonym"
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post concept relations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/concepts/{YOUR_MODEL_CONCEPT_ID}/relations' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "concept_relations": [
            {

                "object_concept": {
                    "id": "{GENERAL_MODEL_CONCEPT_ID}",
                    "app_id": "main"
                },
                "predicate": "synonym"
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

## Create a Concept Mapper Model

We're going to create a concept mapper model that translates the concepts from the General model to our new concepts. The model will map the concepts as synonyms. Hypernyms and hyponyms are supported as well.

We'll be setting the `knowledge_graph_id` value to be empty. If you wanted to define a subset of relationships in your app to be related to each other you can provide the `knowledge_graph_id` to each concept relation and then provide that `knowledge_graph_id` as input to this model as well which will only follow relationships in that subset of your app's knowledge graph.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

params = Struct()
params.update({
    "knowledge_graph_id": ""
})

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        models=[
            resources_pb2.Model(
                id="synonym-model-id",
                model_type_id="concept-synonym-mapper",
                output_info=resources_pb2.OutputInfo(
                    params=params,
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_models_response.outputs[0].status.details))
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

Struct.Builder params = Struct.newBuilder()
    .putFields("knowledge_graph_id", Value.newBuilder().setStringValue("").build());

SingleModelResponse postModelsResponse = stub.postModels(
  PostModelsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addModels(
          Model.newBuilder()
              .setId("synonym-model-id")
              .setModelTypeId("concept-synonym-mapper")
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setParams(params)
              )
      )
      .build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

const params = {
    knowledge_graph_id: ""
}

stub.PostModels(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        models: [
            {
                id: "synonym-model-id",
                model_type_id: "concept-synonym-mapper"
                output_info: {
                    params: params,
                }
            },
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/models' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "model": {
            "id": "synonym-model-id",
            "model_type_id": "concept-synonym-mapper",
            "output_info": {
                "params": {
                    "knowledge_graph_id": ""
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

## Create a "Greater Than" Concept Thresholder Model

This model will allow any predictions &gt;= the concept values defined in the model to be output from this model.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

params = Struct()
params.update({
    "concept_threshold_type": resources_pb2.GREATER_THAN
})

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        models=[
            resources_pb2.Model(
                id="greater-than-model-id",
                model_type_id="concept-threshold",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="peopleID", value=0.5),
                            resources_pb2.Concept(id="manID", value=0.5),
                            resources_pb2.Concept(id="adultID", value=0.95),
                        ]
                    ),
                    params=params
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_models_response.outputs[0].status.details))
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

Struct.Builder params = Struct.newBuilder()
  .putFields(
      "concept_threshold_type",
      Value.newBuilder().setNumberValue(ValueComparator.GREATER_THAN_VALUE).build()
  );

SingleModelResponse postModelsResponse = stub.postModels(
  PostModelsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addModels(
          Model.newBuilder()
              .setId("greater-than-model-id")
              .setModelTypeId("concept-threshold")
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setData(
                          Data.newBuilder()
                              .addConcepts(
                                  Concept.newBuilder()
                                      .setId("peopleID")
                                      .setValue(0.5f)
                              )
                              .addConcepts(
                                  Concept.newBuilder()
                                      .setId("manID")
                                      .setValue(0.5f)
                              )
                              .addConcepts(
                                  Concept.newBuilder()
                                      .setId("adultID")
                                      .setValue(0.95f)
                              )
                      )
                      .setParams(params)
              )
      )
      .build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

const params = {
    concept_threshold_type: "GREATER_THAN"
}

stub.PostModels(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        models: [
            {
                id: "greater-than-model-id",
                model_type_id: "concept-threshold",
                output_info: {
                    data: {
                        concepts: [
                            {id: "peopleID", value: 0.5},
                            {id: "manID", value: 0.5},
                            {id: "adultID", value: 0.95}
                        ]
                    },
                },
                params: params
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/models' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "model": {
            "id": "greater-than-model-id",
            "model_type_id": "concept-threshold",
            "output_info": {
                "data": {
                    "concepts": [
                        {
                            "id": "peopleID",
                            "value": 0.5
                        },
                        {
                            "id": "manID",
                            "value": 0.5
                        },
                        {
                            "id": "adultID",
                            "value": 0.95
                        }
                    ]
                },
                "params": {
                    "concept_threshold_type": 1
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

## Create a "Less Than" Concept Thresholder Model

This model will allow any predictions &lt; the concept values defined in the model to be output from this model.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

params = Struct()
params.update({
    "concept_threshold_type": resources_pb2.LESS_THAN
})

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        models=[
            resources_pb2.Model(
                id="less-than-model-id",
                model_type_id="concept-threshold",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="peopleID", value=0.5),
                            resources_pb2.Concept(id="manID", value=0.5),
                            resources_pb2.Concept(id="adultID", value=0.95),
                        ]
                    ),
                    params=params
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_models_response.outputs[0].status.details))
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

Struct.Builder params = Struct.newBuilder()
    .putFields(
        "concept_threshold_type",
        Value.newBuilder().setNumberValue(ValueComparator.LESS_THAN_VALUE).build()
    );

SingleModelResponse postModelsResponse = stub.postModels(
  PostModelsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addModels(
          Model.newBuilder()
              .setId("less-than-model-id")
              .setModelTypeId("concept-threshold")
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setData(
                          Data.newBuilder()
                              .addConcepts(
                                  Concept.newBuilder()
                                      .setId("peopleID")
                                      .setValue(0.5f)
                              )
                              .addConcepts(
                                  Concept.newBuilder()
                                      .setId("manID")
                                      .setValue(0.5f)
                              )
                              .addConcepts(
                                  Concept.newBuilder()
                                      .setId("adultID")
                                      .setValue(0.95f)
                              )
                      )
                      .setParams(params)
              )
      )
      .build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

const params = {
    concept_threshold_type: "LESS_THAN"
}

stub.PostModels(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        models: [
            {
                id: "less-than-model-id",
                model_type_id: "concept-threshold",
                output_info: {
                    data: {
                        concepts: [
                            {id: "peopleID", value: 0.5},
                            {id: "manID", value: 0.5},
                            {id: "adultID", value: 0.95}
                        ]
                    },
                    params: params
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
            throw new Error("Post models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/models' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "model": {
            "id": "less-than-model-id",
            "model_type_id": "concept-threshold",
            "output_info": {
                "data": {
                    "concepts": [
                        {
                            "id": "peopleID",
                            "value": 0.5
                        },
                        {
                            "id": "manID",
                            "value": 0.5
                        },
                        {
                            "id": "adultID",
                            "value": 0.95
                        }
                    ]
                },
                "params": {
                    "concept_threshold_type": 3
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

## Create a "Write Success as Me" Annotation Writer Model

Any incoming Data object full of concepts, regions, etc. will be writtent by this model to the database as an annotation with ANNOTATION\_SUCCESS status as if the app owner did the work themself.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

params = Struct()
params.update({
    "annotation_status": status_code_pb2.ANNOTATION_SUCCESS,
    "annotation_user_id": "{YOUR_USER_ID}"
})

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        models=[
            resources_pb2.Model(
                id="write-success-model-id",
                model_type_id="annotation-writer",
                output_info=resources_pb2.OutputInfo(
                    params=params
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_models_response.outputs[0].status.details))
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

Struct.Builder params = Struct.newBuilder()
    .putFields(
        "annotation_status", Value.newBuilder().setNumberValue(StatusCode.ANNOTATION_SUCCESS_VALUE).build()
    )
    .putFields(
        "annotation_user_id",
        Value.newBuilder().setStringValue("{YOUR_USER_ID}").build()
    );

SingleModelResponse postModelsResponse = stub.postModels(
  PostModelsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addModels(
          Model.newBuilder()
              .setId("write-success-as-me-id")
              .setModelTypeId("annotation-writer")
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setParams(params)
              )
      )
      .build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

const params = {
    annotation_status: "ANNOTATION_SUCCESS",
    annotation_user_id: "{YOUR_USER_ID}"
}

stub.PostModels(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        models: [
            {
                id: "write-success-model-id",
                model_type_id: "annotation-writer",
                output_info: {
                    params: params
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
            throw new Error("Post models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/models' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "model": {
            "id": "write-success-as-me",
            "model_type_id": "annotation-writer",
            "output_info": {
                "params": {
                    "annotation_status": 24150,
                    "annotation_user_id": "{YOUR_USER_ID}"
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

## Create a "Write Pending as Me" Annotation Writer Model

Any incoming Data object full of concepts, regions, etc. will be written by this model to the database as an annotation with ANNOTATION\_PENDING status as if the app owner did the work themself but needs further review so is marked pending.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

params = Struct()
params.update({
    "annotation_status": status_code_pb2.ANNOTATION_PENDING,
    "annotation_user_id": "{YOUR_USER_ID}"
})

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        models=[
            resources_pb2.Model(
                id="write-pending-model-id",
                model_type_id="annotation-writer",
                output_info=resources_pb2.OutputInfo(
                    params=params
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_models_response.outputs[0].status.details))
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

Struct.Builder params = Struct.newBuilder()
    .putFields(
        "annotation_status", Value.newBuilder().setNumberValue(StatusCode.ANNOTATION_PENDING_VALUE).build()
    )
    .putFields(
        "annotation_user_id",
        Value.newBuilder().setStringValue("{YOUR_USER_ID}").build()
    );

SingleModelResponse postModelsResponse = stub.postModels(
  PostModelsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addModels(
          Model.newBuilder()
              .setId("write-pending-as-me-id")
              .setModelTypeId("annotation-writer")
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setParams(params)
              )
      )
      .build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/models' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "model": {
            "id": "write-pending-as-me",
            "model_type_id": "annotation-writer",
            "output_info": {
                "params": {
                    "annotation_status": 24151,
                    "annotation_user_id": "{YOUR_USER_ID}"
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

## Create the Workflow

We will now connect all the models together into a single workflow.

Every input will be predicted by General Embed model to generate embeddings. The output of the embed model \(embeddings\) will be sent to general concept to predict concept and cluster model. Then the concept model's output \(a list of concepts with prediction values\) will be sent to concept mapper model which maps Clarifai concepts to your concepts within your app, `people`, `man` and `adult` in this case. Then the mapped concepts will be sent to both concept thresholds models \(`GREATER THAN` and `LESS THAN`\). `GREATER THAN` model will filter out the concepts that are lower than corresponding value you defined in model and send the remaining concept list to `write success as me` model which labels the input with these concepts \(your app concepts only\) as you with `success` status. You can train or search on these concepts immediately. The `LESS THAN` model will filter out concepts that are higher than the corresponding value you defined in the model and send the remaining concept list to `write pending as me` model which labels the input with these concepts \(your app concepts only\) as you with `pending` status.

The model IDs and model version IDs from the public `clarifai/main` application are fixed to the latest version at the time of this writing \(check GET /models for an always up to date list of available models\), so they are already hard-coded in the code examples below. It's possible to use other public model or model version IDs.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_workflows_response = stub.PostWorkflows(
    service_pb2.PostWorkflowsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="cdd79189eb6f44049b6c5b58f14a87e6"
        ),
        workflows=[
            resources_pb2.Workflow(
                id="auto-annotation-workflow-id",
                nodes=[
                    resources_pb2.WorkflowNode(
                        id="general-embed",
                        model=resources_pb2.Model(
                            id="bbb5f41425b8468d9b7a554ff10f8581",
                            model_version=resources_pb2.ModelVersion(
                                id="bb186755eda04f9cbb6fe32e816be104"
                            )
                        )
                    ),
                    resources_pb2.WorkflowNode(
                        id="general-concept",
                        model=resources_pb2.Model(
                            id="aaa03c23b3724a16a56b629203edc62c",
                            model_version=resources_pb2.ModelVersion(
                                id="aa7f35c01e0642fda5cf400f543e7c40"
                            )
                        )
                    ),
                    resources_pb2.WorkflowNode(
                        id="general-cluster",
                        model=resources_pb2.Model(
                            id="cccbe437d6e54e2bb911c6aa292fb072",
                            model_version=resources_pb2.ModelVersion(
                                id="cc2074cff6dc4c02b6f4e1b8606dcb54"
                            )
                        ),
                    ),
                    resources_pb2.WorkflowNode(
                        id="mapper",
                        model=resources_pb2.Model(
                            id="synonym-model-id",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_SYNONYM_MODEL_VERSION_ID}"
                            )
                        ),
                        node_inputs=[
                            resources_pb2.NodeInput(node_id="general-concept")
                        ]
                    ),
                    resources_pb2.WorkflowNode(
                        id="greater-than",
                        model=resources_pb2.Model(
                            id="greater-than-model-id",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_GREATER_THAN_MODEL_VERSION_ID}"
                            )
                        ),
                        node_inputs=[
                            resources_pb2.NodeInput(node_id="mapper")
                        ]
                    ),
                    resources_pb2.WorkflowNode(
                        id="write-success",
                        model=resources_pb2.Model(
                            id="write-success-model-id",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_WRITE_SUCCESS_MODEL_VERSION_ID}"
                            )
                        ),
                        node_inputs=[
                            resources_pb2.NodeInput(node_id="greater-than")
                        ]
                    ),
                    resources_pb2.WorkflowNode(
                        id="less-than",
                        model=resources_pb2.Model(
                            id="less-than-model-id",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_LESS_THAN_MODEL_VERSION_ID}"
                            )
                        ),
                        node_inputs=[
                            resources_pb2.NodeInput(node_id="mapper")
                        ]
                    ),
                    resources_pb2.WorkflowNode(
                        id="write-pending",
                        model=resources_pb2.Model(
                            id="write-pending-model-id",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_WRITE_PENDING_MODEL_VERSION_ID}"
                            )
                        ),
                        node_inputs=[
                            resources_pb2.NodeInput(node_id="less-than")
                        ]
                    ),
                ]
            )
        ]
    ),
    metadata=metadata
)

if post_workflows_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_workflows_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_workflows_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_workflows_response.outputs[0].status.details))
    raise Exception("Post workflows failed, status: " + post_workflows_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiWorkflowResponse postWorkflowsResponse = stub.postWorkflows(
  PostWorkflowsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addWorkflows(
          Workflow.newBuilder()
              .setId("auto-annotation-workflow-id")
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("general-embed")
                      .setModel(
                          Model.newBuilder()
                              .setId("bbb5f41425b8468d9b7a554ff10f8581")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("bb186755eda04f9cbb6fe32e816be104")
                              )
                      )
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("general-concept")
                      .setModel(
                          Model.newBuilder()
                              .setId("aaa03c23b3724a16a56b629203edc62c")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("aa7f35c01e0642fda5cf400f543e7c40")
                              )
                      )
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("general-cluster")
                      .setModel(
                          Model.newBuilder()
                              .setId("cccbe437d6e54e2bb911c6aa292fb072")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("cc2074cff6dc4c02b6f4e1b8606dcb54")
                              )
                      )
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("mapper")
                      .setModel(
                          Model.newBuilder()
                              .setId("synonym-model-id")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("{YOUR_SYNONYM_MODEL_VERSION_ID}")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("general-concept"))
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("greater-than")
                      .setModel(
                          Model.newBuilder()
                              .setId("greater-than-model-id")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("{YOUR_GREATER_THAN_MODEL_VERSION_ID}")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("mapper"))
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("write-as-success-as-me")
                      .setModel(
                          Model.newBuilder()
                              .setId("write-success-as-me-id")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("{YOUR_WRITE_SUCCESS_AS_ME_MODEL_VERSION_ID}")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("greater-than"))
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("less-than")
                      .setModel(
                          Model.newBuilder()
                              .setId("less-than-model-id")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("{YOUR_LESS_THAN_MODEL_VERSION_ID}")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("mapper"))
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("write-pending")
                      .setModel(
                          Model.newBuilder()
                              .setId("write-pending-as-me-id")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("{YOUR_WRITE_PENDING_AS_ME_MODEL_VERSION_ID}")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("less-than"))
              )
      )
      .build()
);

if (postWorkflowsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post workflows failed, status: " + postWorkflowsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostWorkflows(
    {
        user_app_id: {
            app_id: "e83440590d104cee97ef84af1856837d"
        },
        workflows: [
            {
                id: "auto-annotation-workflow-id",
                nodes: [
                    {
                        id: "general-embed",
                        model: {
                            id: "bbb5f41425b8468d9b7a554ff10f8581",
                            model_version: {
                                id: "bb186755eda04f9cbb6fe32e816be104"
                            }
                        }
                    },
                    {
                        id: "general-concept",
                        model: {
                            id: "aaa03c23b3724a16a56b629203edc62c",
                            model_version: {
                                id: "aa7f35c01e0642fda5cf400f543e7c40"
                            }
                        }
                    },
                    {
                        id: "general-cluster",
                        model: {
                            id: "cccbe437d6e54e2bb911c6aa292fb072",
                            model_version: {
                                id: "cc2074cff6dc4c02b6f4e1b8606dcb54"
                            }
                        }
                    },
                    {
                        id: "mapper",
                        model: {
                            id: "synonym-model-id",
                            model_version: {
                                id: "{YOUR_SYNONYM_MODEL_VERSION_ID}"
                            }
                        },
                        node_inputs: [
                            {node_id: "general-concept"}
                        ]
                    },
                    {
                        id: "greater-than",
                        model: {
                            id: "greater-than-model-id",
                            model_version: {
                                id: "{YOUR_GREATER_THAN_MODEL_VERSION_ID}"
                            }
                        },
                        node_inputs: [
                            {node_id: "mapper"}
                        ]
                    },
                    {
                        id: "write-success",
                        model: {
                            id: "write-success-model-id",
                            model_version: {
                                id: "{YOUR_WRITE_SUCCESS_MODEL_VERSION_ID}"
                            }
                        },
                        node_inputs: [
                            {node_id: "greater-than"}
                        ]
                    },
                    {
                        id: "less-than",
                        model: {
                            id: "less-than-model-id",
                            model_version: {
                                id: "{YOUR_LESS_THAN_MODEL_VERSION_ID}"
                            }
                        },
                        node_inputs: [
                            {node_id: "mapper"}
                        ]
                    },
                    {
                        id: "write-pending",
                        model: {
                            id: "write-pending-model-id",
                            model_version: {
                                id: "{YOUR_WRITE_PENDING_MODEL_VERSION_ID}"
                            }
                        },
                        node_inputs: [
                            {node_id: "less-than"}
                        ]
                    }
                ]
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            console.log(response.status);
            throw new Error("Post workflows failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/workflows' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "workflows": [
            {
                "id": "auto-annotation-workflow-id",
                "nodes": [
                    {
                        "id": "general-embed",
                        "model": {
                            "id": "{YOUR_GENERAL_EMBED_MODEL_ID}",
                            "model_version": {
                                "id": "{YOUR_GENERAL_EMBED_MODEL_VERSION_ID}"
                            }
                        }
                    },
                    {
                        "id": "general-concept",
                        "model": {
                            "id": "{YOUR_GENERAL_CONCEPT_MODEL_ID}",
                            "model_version": {
                                "id": "{YOUR_GENERAL_CONCEPT_MODEL_VERSION_ID}"
                            }
                        }
                    },
                    {
                        "id": "general-cluster",
                        "model": {
                            "id": "{YOUR_GENERAL_CLUSTER_MODEL_ID}",
                            "model_version": {
                                "id": "{YOUR_GENERAL_CLUSTER_MODEL_VERSION_ID}"
                            }
                        }
                    },
                    {
                        "id": "mapper",
                        "model": {
                            "id": "synonym-model-id",
                            "model_version": {
                                "id": "{YOUR_MAPPER_MODEL_VERSION_ID}"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "general-concept"
                            }
                        ]
                    },
                    {
                        "id": "greater-than",
                        "model": {
                            "id": "greater-than-model-id",
                            "model_version": {
                                "id": "{YOUR_GREATER_THAN_MODEL_VERSION_ID}"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "mapper"
                            }
                        ]
                    },
                    {
                        "id": "write-success",
                        "model": {
                            "id": "write-success-as-me",
                            "model_version": {
                                "id": "{YOUR_WRITE_AS_ME_MODEL_VERSION_ID}"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "greater-than"
                            }
                        ]
                    },
                    {
                        "id": "less-than",
                        "model": {
                            "id": "less-than-model-id",
                            "model_version": {
                                "id": "{YOUR_LESS_THAN_MODEL_VERSION_ID}"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "mapper"
                            }
                        ]
                    },
                    {
                        "id": "write-pending",
                        "model": {
                            "id": "write-pending-as-me",
                            "model_version": {
                                "id": "{YOUR_WRITE_AS_COLLABORATOR_MODEL_VERSION_ID}"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "less-than"
                            }
                        ]
                    }
                ]
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

## Make the New Workflow your App's Default

Make this the default workflow in the app, so it will run every time we add an input and execute the auto annotation process. If the workflow is not the default workflow of your app you can still use PostWorkflowResults on new inputs to check that you configured the workflow graph and your models properly but the data will not be written to the DB. This is recommended before making it your default workflow and adding inputs to you app.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_apps_response = stub.PatchApps(
    service_pb2.PatchAppsRequest(
        action="overwrite",
        apps=[
            resources_pb2.App(
                id="{YOUR_APP_ID}",
                default_workflow_id="auto-annotation-workflow-id"
            )
        ]
    ),
    metadata=metadata
)

if patch_apps_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(patch_apps_response.outputs[0].status.code))
    print("\tDescription: {}".format(patch_apps_response.outputs[0].status.description))
    print("\tDetails: {}".format(patch_apps_response.outputs[0].status.details))
    raise Exception("Patch apps failed, status: " + patch_apps_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAppResponse patchAppsResponse = stub.patchApps(
    PatchAppsRequest.newBuilder()
        .setAction("overwrite")
        .addApps(
            App.newBuilder()
                .setId("{YOUR_APP_ID}")
                .setDefaultWorkflowId("auto-annotation-workflow-id")
        ).build()
);

if (patchAppsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch apps failed, status: " + patchAppsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchApps(
    {
        action: "overwrite",
        apps: [
            {
                id: "{YOUR_APP_ID}",
                default_workflow_id: "auto-annotation-workflow-id"
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            console.log(response.status);
            throw new Error("Patch apps failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X PATCH 'https://api.clarifai.com/v2/users/me/apps' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "action": "overwrite",
        "apps": [
            {
                "id": "{{app}}",
                "default_workflow_id": "auto-annotation-workflow-ID"
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

## Add an Image

Adding the image will trigger the default workflow.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="{YOUR_IMAGE_URL}"
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_inputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_inputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_inputs_response.outputs[0].status.details))
    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder()
        .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
        .addInputs(
            Input.newBuilder()
                .setData(
                    Data.newBuilder()
                        .setImage(
                            Image.newBuilder()
                                .setUrl("{YOUR_IMAGE_URL}")
                        )
                )
        )
        .build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostInputs(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        inputs: [
            {
                data: {
                    image: {
                        url: "{YOUR_IMAGE_URL}"
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
            console.log(response.status);
            throw new Error("Post inputs failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/inputs' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "inputs": [
            {
                "data": {
                    "image": {
                        "url": "{YOUR_IMAGE_URL}"
                    }
                }
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

## List Annotations

Now you can list annotations with your user id to see the annotations created by your workflow.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(
        user_app_id=resources_pb2.UserAppIDSet(
            app_id="{YOUR_APP_ID}"
        ),
        user_ids=["{YOUR_USER_ID}"],
        list_all_annotations=True,
    ),
    metadata=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(list_annotations_response.outputs[0].status.code))
    print("\tDescription: {}".format(list_annotations_response.outputs[0].status.description))
    print("\tDetails: {}".format(list_annotations_response.outputs[0].status.details))
    raise Exception("List annotations failed, status: " + list_annotations_response.status.description)

for annotation in list_annotations_response.annotations:
    print(annotation)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
  ListAnnotationsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addUserIds("{YOUR_USER_ID}")
      .setListAllAnnotations(true)
      .build()
);

if (listAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("List annotations failed, status: " + listAnnotationsResponse.getStatus());
}

for (Annotation annotation : listAnnotationsResponse.getAnnotationsList()) {
    System.out.println(annotation);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListAnnotations(
    {
        user_app_id: {
            app_id: "{YOUR_APP_ID}"
        },
        user_ids: ["{YOUR_USER_ID}"],
        list_all_annotations: true
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List annotations failed, status: " + response.status.description);
        }

        for (const annotation of response.annotations) {
            console.log(annotation);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?user_ids={YOUR_USER_ID}
```
{% endtab %}
{% endtabs %}

