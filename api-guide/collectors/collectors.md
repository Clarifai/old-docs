# Collectors

The collector takes several parameters:
- The collector's ID and description are of your own choosing.
- The pre-queue workflow ID of the workflow to run inline in model predict calls.
  It should only have very fast and light-weight models in it as it will effect the speed of the predictions being made.
  This workflow's purpose is to filter down the inputs to queue for the collector to process.
  The input to this workflow is going to be the OUTPUT of the model.
  Optional, but at least one (pre-queue or post-queue) workflow ID is required.
- The post-queue workflow ID of the workflow to run to after the collector is processing the queued input.
  This workflow uses the original input to the model as input to the workflow so that you can run additional models as well on that input to decide whether to queue the model or not.
  If the workflow output has any field that is non-empty then it will be passed on to POST /inputs to the destination app.
  Optional, but at least one (pre-queue or post-queue) workflow ID is required.
- The model ID, and its model version ID, should belong to the model from where you want to collect. When the user predicts an input against that model, the input is going to be collected.
- The app ID and user ID where the model is located. If using a publicly available model, the model user and app ID should be `clarifai` and `main`, respectively. Otherwise the IDs should belong to the user who created the model.
- An API key ID using which the inputs are is going to be added.

A possible pre-queue workflow would be one that does:
1. random sampling (i.e. it collects a random subset of predicted inputs), then
2. knowledge graph mapping from public General model concepts to a custom model, then
2. concept thresholding.

See also the [Auto Annotation walkthrough](https://docs.clarifai.com/api-guide/walkthroughs/auto-annotation-walkthrough).

## Add Collector

Add a new collector to your application.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiCollectorResponse postCollectorsResponse = stub.postCollectors(
    PostCollectorsRequest.newBuilder()
        .addCollectors(
            Collector.newBuilder()
                .setId("{YOUR_COLLECTOR_ID}")
                .setDescription("{YOUR_COLLECTOR_DESCRIPTION}")
                .setPreQueueWorkflowId("{YOUR_PRE_QUEUE_WORKFLOW_ID}")
                .setPostQueueWorkflowId("{YOUR_POST_QUEUE_WORKFLOW_ID}")
                .setCollectorSource(
                    CollectorSource.newBuilder()
                        .setApiPostModelOutputsCollectorSource(
                            APIPostModelOutputsCollectorSource.newBuilder()
                                .setModelUserId("{YOUR_MODEL_USER_ID}")
                                .setModelAppId("{YOUR_MODEL_APP_ID}")
                                .setModelId("{YOUR_MODEL_ID}")
                                .setModelVersionId("{YOUR_MODEL_VERSION_ID}")
                                .setPostInputsKeyId("{YOUR_API_KEY}")
                        )
                )
        )
        .build()
);

if (postCollectorsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post collectors failed, status: " + postCollectorsResponse.getStatus());
}
```
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostCollectors(
    {
        collectors: [
            {
                id: "{YOUR_COLLECTOR_ID}",
                description: "{YOUR_COLLECTOR_DESCRIPTION}",
                pre_queue_workflow_id: "{YOUR_PRE_QUEUE_WORKFLOW_ID}",
                post_queue_workflow_id: "{YOUR_POST_QUEUE_WORKFLOW_ID}",
                collector_source: {
                    api_post_model_outputs_collector_source: {
                        model_user_id: "{YOUR_MODEL_USER_ID}",
                        model_app_id: "{YOUR_MODEL_APP_ID}",
                        model_id: "{YOUR_MODEL_ID}",
                        model_version_id: "{YOUR_MODEL_VERSION_ID}",
                        post_inputs_key_id: "{YOUR_API_KEY}"
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
            throw new Error("Post collectors failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_collectors_response = stub.PostCollectors(
    service_pb2.PostCollectorsRequest(
        collectors=[
            resources_pb2.Collector(
                id="{YOUR_COLLECTOR_ID}",
                description="{YOUR_COLLECTOR_DESCRIPTION}",
                pre_queue_workflow_id="{YOUR_PRE_QUEUE_WORKFLOW_ID}",
                post_queue_workflow_id="{YOUR_POST_QUEUE_WORKFLOW_ID}",
                collector_source=resources_pb2.CollectorSource(
                    api_post_model_outputs_collector_source=resources_pb2.APIPostModelOutputsCollectorSource(
                        model_user_id="{YOUR_MODEL_USER_ID}",
                        model_app_id="{YOUR_MODEL_APP_ID}",
                        model_id="{YOUR_MODEL_ID}",
                        model_version_id="{YOUR_MODEL_VERSION_ID}",
                        post_inputs_key_id="{YOUR_API_KEY}"
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_collectors_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post collectors failed, status: " + post_collectors_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/collectors' \
  -H 'Authorization: Key YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "collectors": [
        {
            "id": "{YOUR_COLLECTOR_ID}",
            "description": "{YOUR_COLLECTOR_DESCRIPTION}",
            "pre_queue_workflow_id": "{YOUR_PRE_QUEUE_WORKFLOW_ID}",
            "post_queue_workflow_id": "{YOUR_POST_QUEUE_WORKFLOW_ID}",
            "collector_source": {
                "api_post_model_outputs_collector_source": {
                    "model_user_id": "{YOUR_MODEL_USER_ID]",
                    "model_app_id": "{YOUR_MODEL_APP_ID}",
                    "model_id": "{YOUR_MODEL_ID}",
                    "model_version_id": "{YOUR_MODEL_VERSION_ID}",
                    "post_inputs_key_id": "{YOUR_API_KEY}"
                }
            }
       }
    ]
}'
```
{% endtab %}
{% endtabs %}


## Update Collector

Update an existing collector.


{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiCollectorResponse patchCollectorsResponse = stub.patchCollectors(
    PatchCollectorsRequest.newBuilder()
        .addCollectors(
            Collector.newBuilder()
                .setId("{YOUR_COLLECTOR_ID}")
                .setDescription("{A_NEW_DESCRIPTION}")
                .setPreQueueWorkflowId("{A_NEW_WORKFLOW_ID}")
        )
        .build()
);

if (patchCollectorsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch collectors failed, status: " + patchCollectorsResponse.getStatus());
}
```
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PatchCollectors(
    {
        collectors: [
            {
                id: "{YOUR_COLLECTOR_ID}",
                description: "{A_NEW_DESCRIPTION}",
                pre_queue_workflow_id: "{A_NEW_WORKFLOW_ID}",
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
            throw new Error("Patch collectors failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

patch_collectors_response = stub.PatchCollectors(
    service_pb2.PatchCollectorsRequest(
        collectors=[
            resources_pb2.Collector(
                id="{YOUR_COLLECTOR_ID}",
                description="{A_NEW_DESCRIPTION}",
                pre_queue_workflow_id="{A_NEW_WORKFLOW_ID}",
            )
        ]
    ),
    metadata=metadata
)

if patch_collectors_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch collectors failed, status: " + patch_collectors_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X PATCH 'https://api-dev.clarifai.com/v2/collectors' \
  -H 'Authorization: Key YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "action": "overwrite",
    "collectors": [
        {
            "id": "{YOUR_COLLECTOR_ID}",
            "description": "{A_NEW_DESCRIPTION}",
            "pre_queue_workflow_id": "{A_NEW_WORKFLOW_ID}"
       }
    ]
}'
```
{% endtab %}
{% endtabs %}


## List Collectors

List all the collectors. See [Pagination](https://docs.clarifai.com/api-guide/api-overview/pagination) on how to control which page gets displayed.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiCollectorResponse listCollectorsResponse = stub.listCollectors(
    ListCollectorsRequest.newBuilder()
        .build()
);

if (listCollectorsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List collectors failed, status: " + listCollectorsResponse.getStatus());
}

for (Collector collector : listCollectorsResponse.getCollectorsList()) {
    System.out.println(collector);
}
```
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.ListCollectors(
    {},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            console.log(response.status);
            throw new Error("List collectors failed, status: " + response.status.description);
        }

        for (const collector of response.collectors) {
            console.log(collector);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

list_collectors_response = stub.ListCollectors(
    service_pb2.ListCollectorsRequest(),
    metadata=metadata
)

if list_collectors_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List collectors failed, status: " + list_collectors_response.status.description)

for collector in list_collectors_response.collectors:
    print(collector)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET 'https://api.clarifai.com/v2/collectors' \
  -H 'Authorization: Key YOUR_API_KEY' \
  -H 'Content-Type: application/json'
```
{% endtab %}
{% endtabs %}


## Get Collector

Return details of a certain collector.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

SingleCollectorResponse getCollectorResponse = stub.getCollector(
    GetCollectorRequest.newBuilder()
        .setCollectorId("{YOUR_COLLECTOR_ID}")
        .build()
);

if (getCollectorResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get collector failed, status: " + getCollectorResponse.getStatus());
}

System.out.println(getCollectorResponse.getCollector());
```
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.GetCollector(
    {
        collector_id: "{YOUR_COLLECTOR_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            console.log(response.status);
            throw new Error("Get collector failed, status: " + response.status.description);
        }

        console.log(response.collector);
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

get_collector_response = stub.GetCollector(
    service_pb2.GetCollectorRequest(
        collector_id="{YOUR_COLLECTOR_ID}"
    ),
    metadata=metadata
)

if get_collector_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get collector failed, status: " + get_collector_response.status.description)

print(get_collector_response.collector)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET 'https://api.clarifai.com/v2/collectors/{YOUR_COLLECTOR_ID}' \
  -H 'Authorization: Key YOUR_API_KEY' \
  -H 'Content-Type: application/json'
```
{% endtab %}
{% endtabs %}


## Delete Collector

Delete a collector.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

BaseResponse deleteCollectorsResponse = stub.deleteCollectors(
    DeleteCollectorsRequest.newBuilder()
        .addIds("{YOUR_COLLECTOR_ID}")
        .build()
);

if (deleteCollectorsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete collectors failed, status: " + deleteCollectorsResponse.getStatus());
}
```
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.DeleteCollectors(
    {
        ids: ["{YOUR_COLLECTOR_ID}"]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            console.log(response.status);
            throw new Error("Delete collectors failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

delete_collectors_response = stub.DeleteCollectors(
    service_pb2.DeleteCollectorsRequest(
        ids=["{YOUR_COLLECTOR_ID}"]
    ),
    metadata=metadata
)

if delete_collectors_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete collectors failed, status: " + delete_collectors_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE 'https://api-dev.clarifai.com/v2/collectors' \
  -H 'Authorization: Key YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "ids": ["{YOUR_COLLECTOR_ID}"]
}'
```
{% endtab %}
{% endtabs %}
