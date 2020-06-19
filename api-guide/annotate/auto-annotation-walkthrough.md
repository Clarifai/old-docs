# Active Learning Auto Annotation Walkthrough

This tutorial demonstrates how auto-annotation workflows can be configured in the Clarifai API. Inputs are automatically annotated with concepts and assigned `SUCCESS` status by leveraging the high confidence predictions of a model, and when the model is unsure, the annotation is going to be written as you with `PENDING` status. This enables you to scale up your annotation process while ensuring quality standards by including a backstop of human reveiw.


### Create concepts

Create the concepts that we'll be using in our model. In this tutorial we'll create the following concepts: `people`, `man` and `adult`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
    raise Exception("Post concepts failed, status: " + post_concepts_response.status.description)
```
{% endtab %}

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

### Link the concepts

Link the newly created concepts with concepts in the Clarifai/Main General model.

Run the code below three times, once for each concept created previously. The concept IDs of the clarifai/main General models are the following:
- `ai_l8TKp2h5` - the people concept,
- `ai_dxSG2s86` - the man concept,
- `ai_VPmHr5bm` - the adult concept.

Your model's concept IDs are the ones you created in the previous step: `peopleID`, `manID`, and `adultID`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
    raise Exception("Post concept relations failed, status: " + post_concept_relations_response.status.description)
```
{% endtab %}

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

### Create a mapper model

We're going to create a mapper model that translates the concepts from the General model to our new concepts. The model will map the concepts as synonyms. Hypernyms and hyponyms are supported as well.

We'll be setting the `knowledge_graph_id` value to be empty.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

model_metadata = Struct()
model_metadata.update({
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
                output_info=resources_pb2.OutputInfo(
                    type="concept-synonym-mapper",
                    output_config=resources_pb2.OutputConfig(
                        model_metadata=model_metadata
                    )
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

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

const model_metadata = {
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
                output_info: {
                    type: "concept-synonym-mapper",
                    output_config: {
                        model_metadata: model_metadata
                    }
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

### Create a "greater than" Concept Thresholder model

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

model_metadata = Struct()
model_metadata.update({
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
                output_info=resources_pb2.OutputInfo(
                    type="concept-threshold",
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="peopleID", value=0.5),
                            resources_pb2.Concept(id="manID", value=0.5),
                            resources_pb2.Concept(id="adultID", value=0.95),
                        ]
                    ),
                    output_config=resources_pb2.OutputConfig(
                        model_metadata=model_metadata
                    )
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

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

const model_metadata = {
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
                output_info: {
                    type: "concept-threshold",
                    data: {
                        concepts: [
                            {id: "peopleID", value: 0.5},
                            {id: "manID", value: 0.5},
                            {id: "adultID", value: 0.95}
                        ]
                    },
                    output_config: {
                        model_metadata: model_metadata
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


### Create a "less than" Concept Thresholder model

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

model_metadata = Struct()
model_metadata.update({
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
                output_info=resources_pb2.OutputInfo(
                    type="concept-threshold",
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="peopleID", value=0.5),
                            resources_pb2.Concept(id="manID", value=0.5),
                            resources_pb2.Concept(id="adultID", value=0.95),
                        ]
                    ),
                    output_config=resources_pb2.OutputConfig(
                        model_metadata=model_metadata
                    )
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

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

const model_metadata = {
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
                output_info: {
                    type: "concept-threshold",
                    data: {
                        concepts: [
                            {id: "peopleID", value: 0.5},
                            {id: "manID", value: 0.5},
                            {id: "adultID", value: 0.95}
                        ]
                    },
                    output_config: {
                        model_metadata: model_metadata
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

### Create a "write success as me" Annotation Writer model

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

model_metadata = Struct()
model_metadata.update({
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
                output_info=resources_pb2.OutputInfo(
                    type="annotation-writer",
                    output_config=resources_pb2.OutputConfig(
                        model_metadata=model_metadata
                    )
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

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

const model_metadata = {
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
                output_info: {
                    type: "annotation-writer",
                    output_config: {
                        model_metadata: model_metadata
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

### Create a "write pending as me" Annotation Writer model

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

model_metadata = Struct()
model_metadata.update({
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
                output_info=resources_pb2.OutputInfo(
                    type="annotation-writer",
                    output_config=resources_pb2.OutputConfig(
                        model_metadata=model_metadata
                    )
                )
            ),
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

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

Every input will be predicted by General Embed model to generate embedding. The output of the embed model (embeddings) will be sent to general concept to predict concept and cluster model. Then the concept model's output (a list of concepts) will be sent to concept mapper model which maps Clarifai concept to your concept, `people`, `man` and `adult` in this case. Then the mapped concepts will be sent to both concept thresholds models (`GREATER THAN` and `LESS THAN`). `GREATER THAN` model will filter out the concept if it lower than corresponding value you defined in model and send the final concept list to `write success as me` model which labels the input with these concepts (your app concepts only) as you with `success` status. You can train or search on these concepts immediately. The `LESS THAN` model will filter out the concept if it is higher than the corresponding value you defined and send the final concept list to `write pending as me` model which labels the input with these concepts (your app concepts only) as you with `pending` status.

The model IDs and model version IDs from the public `clarifai/main` application are fixed, so they are already hard-coded in the code examples below. It's possible to use other public model or model version IDs.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
    raise Exception("Post workflows failed, status: " + post_workflows_response.status.description)
```
{% endtab %}

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

### Make the new workflow your app's default

Make this the default workflow in the app, so it will run every time we add an input and execute the auto annotation process.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
    raise Exception("Patch apps failed, status: " + patch_apps_response.status.description)
```
{% endtab %}

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

### Add an image

Adding the image will trigger the default workflow.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

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

### List annotations

Now you can list annotations with your user id to see the annotations created by your workflow.

{% tabs %}
{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
