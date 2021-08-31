# Collectors

> Collectors are available with Professional and Enterprise plans to help you manage data ingestion at scale.

Collectors capture input data for your app. They enable you to pipe in data from production models automatically, and are the key to unlocking many platform training capabilities like active learning. 

You can create app-level collectors to monitor specific models and specify sampling rules for triggering data ingestion. Collectors can only collect data from apps where you are the app owner.

## Collector Parameters

### Collector ID

Give your collector a useful and descriptive name.

### Description

Provide additional details about your collector.

### Pre-queue workflow

In many scenarios, you will only want to ingest a sample, or subset of a given data source into your app. Pre-queue workflows allow you to pre-process your inputs so that you can sample and filter your new data before it is ever added to your app. Pre-queue workflows allow you to specify sampling rules for triggering data ingestion. Common pre-queue workflows are designed to:

* Randomly sample inputs
* Filter inputs by metadata
* Filter inputs with a maximum probability below a given threshold
* Filter inputs with a minimum probability above a given threshold
* Filter specific concept probabilities above a given threshold
* Knowledge graph mapping from public General model concepts to a custom model

At least one \(pre-queue or post-queue\) workflow ID is required. The input to this workflow is going to be the OUTPUT of the model. We recommend that you use fast and light-weight models in it as it will effect the speed of the predictions being made.

### Post Inputs key

Select the API key that you would like to use to allow new inputs to be posted to your app. This is the post-queue workflow ID of the workflow to run to after the collector is processing the queued input. This API key must have the PostInputs scope, since it grants the collector the authority to POST inputs to your app.

This workflow uses the original input to the model as input to the workflow so that you can run additional models as well on that input to decide whether to queue the model or not. If the workflow output has any field that is non-empty then it will be passed on to POST /inputs to the destination app. At least one \(pre-queue or post-queue\) workflow ID is required.

### Source

Select the model that you would like to collect from, and the collector will automatically post the new inputs to your app. Simply enter your model name, or model ID number. When the user predicts an input against this model, the input is going to be collected.

The app ID and user ID where the model is located. If using a publicly available model, the model user and app ID should be `clarifai` and `main`, respectively. Otherwise the IDs should belong to the user who created the model. An API key ID using which the inputs are is going to be added.

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
```javascript
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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
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
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/collectors", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
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
```javascript
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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "action": "overwrite",
  "collectors": [
      {
          "id": "{YOUR_COLLECTOR_ID}",
          "description": "{A_NEW_DESCRIPTION}",
          "pre_queue_workflow_id": "{A_NEW_WORKFLOW_ID}"
     }
  ]
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/collectors", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
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
```javascript
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

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/collectors`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
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
```javascript
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

{% tab title="Javascript (REST)" %}
```javascript
const collectorId = '{YOUR_COLLECTOR_ID}'
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/collectors/${collectorId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
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
```javascript
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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "ids": [
    "collector2"
  ]
});

var requestOptions = {
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/collectors", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

