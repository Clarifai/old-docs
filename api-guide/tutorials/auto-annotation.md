## Auto Annotation Tutorial (WIP)


Let's create a process where inputs are going to be automatically annotated with some concepts and success status as you by a model when the confidence is high, and when the model is unsure, the annotation is going to be writen as you with `Pending` status .

### Create concepts

Create the concepts that we'll be using in our model. In this tutorial we'll create the following concepts: `people`, `man` and `adult`.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

### Link the concepts

Link the newly created concepts with the ones from the clarifai/main General model.

Run the code below three times, once for each concept created previously. The concept IDs of the clarifai/main General models are the following:
- `ai_l8TKp2h5` - the people concept,
- `ai_dxSG2s86` - the man concept,
- `ai_VPmHr5bm` - the adult concept

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

### Create a mapper model

We're going to create a mapper model that translates the concepts from the General model to our new concepts. The model will map the concepts as synonyms. Hypernyms and hyponyms are supported as well.

We'll be setting the `knowledge_graph_id` value to be empty, to declare search should not be done to any spe

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder modelMetadata = Struct.newBuilder()
    .putFields("knowledge_graph_id", Value.newBuilder().setStringValue("").build());

SingleModelResponse postModelsResponse = stub.postModels(
  PostModelsRequest.newBuilder()
      .setUserAppId(UserAppIDSet.newBuilder().setAppId("{YOUR_APP_ID}"))
      .addModels(
          Model.newBuilder()
              .setId("synonym-model-id")
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setType("concept-synonym-mapper")
                      .setOutputConfig(
                          OutputConfig.newBuilder().setModelMetadata(modelMetadata)
                      )
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
            "output_info": {
                "type": "concept-synonym-mapper",
                "output_config": {
                    "model_metadata": {
                        "knowledge_graph_id": ""
                    }
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create a "greater than" model

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder modelMetadata = Struct.newBuilder()
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
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setType("concept-threshold")
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
                      .setOutputConfig(
                          OutputConfig.newBuilder().setModelMetadata(modelMetadata)
                      )
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
            "output_info": {
                "type": "concept-threshold",
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
                "output_config": {
                    "model_metadata": {
                        "concept_threshold_type": 1
                    }
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create a "less than" model

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder modelMetadata = Struct.newBuilder()
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
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setType("concept-threshold")
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
                      .setOutputConfig(
                          OutputConfig.newBuilder().setModelMetadata(modelMetadata)
                      )
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
            "output_info": {
                "type": "concept-threshold",
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
                "output_config": {
                    "model_metadata": {
                        "concept_threshold_type": 3
                    }
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create a "write success as me" model

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder modelMetadata = Struct.newBuilder()
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
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setType("annotation-writer")
                      .setOutputConfig(
                          OutputConfig.newBuilder().setModelMetadata(modelMetadata)
                      )
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
            "output_info": {
                "type": "annotation-writer",
                "output_config": {
                    "model_metadata": {
                        "annotation_status": 24150,
                        "annotation_user_id": "{YOUR_USER_ID}"
                    }
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create a "write pending as me" model

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder modelMetadata = Struct.newBuilder()
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
              .setOutputInfo(
                  OutputInfo.newBuilder()
                      .setType("annotation-writer")
                      .setOutputConfig(
                          OutputConfig.newBuilder().setModelMetadata(modelMetadata)
                      )
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
            "output_info": {
                "type": "annotation-writer",
                "output_config": {
                    "model_metadata": {
                        "annotation_status": 24151,
                        "annotation_user_id": "{YOUR_USER_ID}"
                    }
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create the workflow

We will now joint all the models together into a single workflow.
Every input will be predicted by general embed model to generate embedding. The output of the embed model (embeddins) will be sent to general concept to predict concept and cluster model. Then the concept model's output (a list of concepts) will be sent to concept mapper model which maps clarifai concept to your concept, `people`, `man` and `adult` in this case. Then the mapped concepts will be sent to both concept thresholds models (`GREATER THAN` and `LESS THAN`). `GREATER THAN` model will filter out the concept if it lower than corresponding value you defined in model and send the final concept list to `write success as me` model which labels the input with these concepts (your app concepts only) as you with `success` stauts. You can train or search on these concepts immediately. At the mean time, `LESS THAN` model will filter out the concept if it higher than ccorresponding valud you defined in model and send the final concept list to `write pending as me` model which labels the input with these concepts (your app concepts only) as you with `pending` status.

The model IDs and model version IDs from the public `clarifai/main` application are fixed, so they are already hard-coded in the code examples below. It's possible to use some other public model / model version IDs.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

### Make the new workflow app's default

Make this the default workflow in the app, so it will every time we add an input.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

### Add an image

Adding the image will trigger the default workflow.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

### List annotations

Now you can list annotations with your user id to see the annotations created by model.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
