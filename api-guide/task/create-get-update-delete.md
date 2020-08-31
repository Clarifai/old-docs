# Create, Get, Update, Delete

The tasks are a powerful tool which can help your team to annotate inputs from your application.

## Create

To create a new task in your app you `POST` the task information to `v2/task` endpoint.

### Non-Assigned Task

A task should be assigned to a list of users, but it's not required. The following code will create a non-assigned task.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
      "tasks": [
          {
              "type": "CONCEPTS_CLASSIFICATION",
              "name": "Annotate {{concept_id}}",
              "worker": {
              	"strategy": "FULL"
              },
          	"concept_ids": [
          		"{{concept_id}}"
          	],
          	"input_source": {
          		"type": "ALL_INPUTS"
          	},
          	"sample_ms": 1000,
          	"review": {
          		"strategy": "NONE"
          	}
          }
      ]
  }'\
  https://api.clarifai.com/v2/tasks
```
{% endtab %}
{% endtabs %}

### Assigned Task

A task should be assigned to a list of users. These users will do the work, so they're also called workers. A task may also be assigned to a list of users for review.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
    {
        "tasks": [
            {
                "type": "CONCEPTS_CLASSIFICATION",
                "name": "Annotate {{concept_id}}",
                "worker": {
                    "strategy": "FULL",
                    "user_ids": [
                        "{{worker_user_id}}"
                    ]
                },
                "concept_ids": [
                    "{{concept_id}}"
                ],
                "input_source": {
                    "type": "ALL_INPUTS"
                },
                "sample_ms": 1000,
                "review": {
                    "strategy": "MANUAL",
                    "manual_strategy_info": {
                        "sample_percentage": 0.5
                    },
                    "user_ids": [
                        "{{reviewer_user_id}}"
                    ]
                }
            }
        ]
    }'\
  https://api.clarifai.com/v2/tasks
```
{% endtab %}
{% endtabs %}


## Task with Partitioned Worker Strategy

The previous tasks were created with full worker strategy.
```json
{
    "strategy": "FULL"
}
```

In case of `FULL` worker strategy, each worker will work on all inputs selected in the input source.

If you wish the work to be distributed between workers, then you can select the `PARTITIONED` worker strategy.

In the following example:
* there are two workers
* `workers_per_input`: each input will be assigned to 1 worker
* `weights.{{user_id1}}`: the first worker will get 90% of inputs
* `weights.{{user_id2}}`: the second worker will get 10% of inputs

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
    {
        "tasks": [
            {
                "type": "CONCEPTS_CLASSIFICATION",
                "name": "Annotate {{concept_id}}",
                "worker": {
                    "strategy": "PARTITIONED",
                    "user_ids": ["{{user_id1}}", "{{user_id2}}"],
                    "partitioned_strategy_info": {
                        "type": "WEIGHTED",
                        "workers_per_input": 1,
                        "weights": {
                            "{{user_id1}}": 90,
                            "{{user_id2}}": 10
                        }
                    }
                },
                "concept_ids": [
                    "{{concept_id}}"
                ],
                "input_source": {
                    "type": "ALL_INPUTS"
                },
                "sample_ms": 1000,
                "review": {
                    "strategy": "NONE"
                }
            }
        ]
    }'\
  https://api.clarifai.com/v2/tasks
```
{% endtab %}
{% endtabs %}

Notes:
* It is not required for the weights to add up to 100. For example, the weights [9, 1] are equivalent with weights [90, 10].
* The partitioning is approximate. This means that the number of assigned inputs to each worker may have a small error margin, but it will be close to the assigned weight percentage.

## Task with Consensus Review

The previous tasks were created with no review or manual review strategy.
```json
{
  "strategy": "MANUAL"
}
```

We recommend to create tasks with `CONSENSUS` review strategy. When enough workers label an input in the same way, it will automatically be approved, with no need for the reviewer to spend time to check. In this way, the reviewer will be able to focus on the inputs where the workers don't agree.

Note that an approval threshold must be set. For example, in case of 3 workers and `approval_threshold` set to 2, if an input is labeled in the same way by 2 workers, they form a majority and the group reaches a consensus.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
    {
        "tasks": [
            {
                "type": "CONCEPTS_CLASSIFICATION",
                "name": "Annotate {{concept_id}}",
                "worker": {
                    "strategy": "PARTITIONED",
                    "user_ids": ["{{user_id1}}", "{{user_id2}}", "{{user_id3}}"],
                    "partitioned_strategy_info": {
                        "type": "WEIGHTED",
                        "workers_per_input": 1,
                        "weights": {
                            "{{user_id1}}": 1,
                            "{{user_id2}}": 1,
                            "{{user_id3}}": 1
                        }
                    }
                },
                "concept_ids": [
                    "{{concept_id}}"
                ],
                "input_source": {
                    "type": "ALL_INPUTS"
                },
                "sample_ms": 1000,
                "review": {
                    "strategy": "CONSENSUS",
                    "consensus_strategy_info": {
                        "approval_threshold": 2
                    },
                    "user_ids": [
                        "{{user_id4}}"
                    ]
                }
            }
        ]
    }'\
  https://api.clarifai.com/v2/tasks
```
{% endtab %}
{% endtabs %}

## Get

### Get Task by ID

You can get a singular task by its ID. The ID was automatically generated when it was created.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/tasks/{task_id}
```
{% endtab %}
{% endtabs %}

### List All Tasks

You can get a list of tasks within your app with a `GET` call. This call supports [pagination](../../api-guide/api-overview/pagination.md).

{% tabs %}
{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/tasks
```
{% endtab %}
{% endtabs %}

### List Tasks Assigned to User

Get only the tasks assigned to a specific user for work.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/tasks?worker_user_ids={{user_id}}
```
{% endtab %}
{% endtabs %}

### List Tasks Assigned to User for Review

Get only the tasks assigned to a specific user for review.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/tasks?review_user_ids={{user_id}}
```
{% endtab %}
{% endtabs %}


## Update

Currently, we only support updating a task by providing all information at once.

### Update Task

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
    {
        "action": "overwrite",
        "tasks": [
            {
                "id": "{{task_id}}",
                "type": "CONCEPTS_CLASSIFICATION",
                "name": "Annotate {{concept_id}}",
                "worker": {
                    "strategy": "PARTITIONED",
                    "user_ids": ["{{user_id1}}", "{{user_id2}}"],
                    "partitioned_strategy_info": {
                        "type": "WEIGHTED",
                        "workers_per_input": 1,
                        "weights": {
                            "{{user_id1}}": 1,
                            "{{user_id2}}": 1
                        }
                    }
                },
                "concept_ids": [
                    "{{concept_id}}"
                ],
                "input_source": {
                    "type": "ALL_INPUTS"
                },
                "sample_ms": 1000,
                "review": {
                    "strategy": "CONSENSUS",
                    "consensus_strategy_info": {
                        "approval_threshold": 2
                    },
                    "user_ids": [
                        "{{user_id3}}"
                    ]
                },
                "status": {
                    "code": "TASK_DONE"
                }
            }
        ]
    }'\
  https://api.clarifai.com/v2/tasks
```
{% endtab %}
{% endtabs %}

## Delete

### Delete Multiple Tasks

You can delete tasks using their IDs.

{% tabs %}
{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
    {
        "ids":["{{task_id}}"]
    }'\
  https://api.clarifai.com/v2/tasks
```
{% endtab %}
{% endtabs %}
