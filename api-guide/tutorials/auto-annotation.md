## Auto Annotation Tutorial (WIP)


Let's create a process where inputs are going to be automatically annotated by a model when the confidence is high, and when the model is unsure, the annotation is going to be sent into human review.


### Add a collaborator

Add a collaborator to whom we are later going to assign the task of reviewing annotations.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/collaborators' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "collaborators": [
            {
                "id": "my-collaborator-1",
                "user": {
                    "id": "{YOUR_COLLABORATOR_USER_ID}"
                },
                "scopes": [],
                "endpoints": []
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}


### Create concepts

Create the concepts that we'll be using in our model. In this tutorial we'll create the following concepts: `people`, `man` and `adult`.

{% tabs %}
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


{% tabs %}
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

### Create a "write as me" model

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/models' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "model": {
            "id": "write-as-me",
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

### Create a "write as collaborator" model

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/models' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/javascript' \
    --data-raw '{
        "model": {
            "id": "write-as-collaborator",
            "output_info": {
                "type": "annotation-writer",
                "output_config": {
                    "model_metadata": {
                        "annotation_status": 24151,
                        "annotation_user_id": "{YOUR_COLLABORATOR_USER_ID}",
                        "annotation_info": {
                            "task_id": "{YOUR_TASK_ID}"
                        }
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

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/users/me/apps/{{app}}/workflows' \
    -H 'Authorization: Key {{PAT}}' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "workflows": [
            {
                "id": "mapper-threshold-testID",
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
                        "id": "write-as-me",
                        "model": {
                            "id": "write-as-me",
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
                        "id": "write-as-collaborator",
                        "model": {
                            "id": "write-as-collaborator",
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
                "default_workflow_id": "mapper-threshold-testID"
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

### Add an image

Adding the image will trigger the default workflow.

{% tabs %}
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
