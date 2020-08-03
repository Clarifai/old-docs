# Create, Get, Update, Delete

## Create

To create a new custom workflow, specify a list of model IDs that are to be included in the workflow. Each model ID also requires a specific model version ID, since a model can have several versions.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiWorkflowResponse postWorkflowsResponse = stub.postWorkflows(
    PostWorkflowsRequest.newBuilder().addWorkflows(
        Workflow.newBuilder()
            .setId("my-custom-workflow")
            .addNodes(
                WorkflowNode.newBuilder()
                    .setId("food-concepts")
                    .setModel(
                        Model.newBuilder()
                            .setId("bd367be194cf45149e75f01d59f77ba7")
                            .setModelVersion(ModelVersion.newBuilder().setId("dfebc169854e429086aceb8368662641"))
                    )
            )
            .addNodes(
                WorkflowNode.newBuilder()
                    .setId("general-concepts")
                    .setModel(
                        Model.newBuilder()
                            .setId("aaa03c23b3724a16a56b629203edc62c")
                            .setModelVersion(ModelVersion.newBuilder().setId("aa9ca48295b37401f8af92ad1af0d91d"))
                    )
            )
    ).build()
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
        workflows: [
            {
                id: "my-custom-workflow",
                nodes: [
                    {
                        id: "food-concepts",
                        model: {
                            id: "bd367be194cf45149e75f01d59f77ba7",
                            model_version: {
                                id: "dfebc169854e429086aceb8368662641"
                            }
                        }
                    },
                    {
                        id: "general-concepts",
                        model: {
                            id: "aaa03c23b3724a16a56b629203edc62c",
                            model_version: {
                                id: "aa9ca48295b37401f8af92ad1af0d91d"
                            }
                        }
                    },
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
            throw new Error("Post workflows failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_workflows_response = stub.PostWorkflows(
    service_pb2.PostWorkflowsRequest(
      workflows=[
        resources_pb2.Workflow(
          id="my-custom-workflow",
          nodes=[
            resources_pb2.WorkflowNode(
              id="food-concepts",
              model=resources_pb2.Model(
                id="bd367be194cf45149e75f01d59f77ba7",
                model_version=resources_pb2.ModelVersion(
                  id="dfebc169854e429086aceb8368662641"
                )
              )
            ),
            resources_pb2.WorkflowNode(
              id="general-concepts",
              model=resources_pb2.Model(
                id="aaa03c23b3724a16a56b629203edc62c",
                model_version=resources_pb2.ModelVersion(
                  id="aa9ca48295b37401f8af92ad1af0d91d"
                )
              )
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

{% tab title="cURL" %}
```text
# The first model is the Clarifai's Food model, and the second the Clarifai's General model.

curl -X POST 'https://api.clarifai.com/v2/workflows' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Key YOUR_API_KEY' \
    --data-raw '{
      "workflows": [{
        "id": "my-custom-workflow",
        "nodes": [
          {
            "id": "food-concepts",
            "model": {
              "id": "bd367be194cf45149e75f01d59f77ba7",
              "model_version": {
                "id": "dfebc169854e429086aceb8368662641"
              }
            }
          },
          {
            "id": "general-concepts",
            "model": {
              "id": "aaa03c23b3724a16a56b629203edc62c",
              "model_version": {
                "id": "aa9ca48295b37401f8af92ad1af0d91d"
              }
            }
          }
        ]
      }]
    }'
```
{% endtab %}
{% endtabs %}

## Workflow Predict

Predict using a workflow. The response will contain the predictions each model in the workflow returns for the input.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

PostWorkflowResultsResponse postWorkflowResultsResponse = stub.postWorkflowResults(
    PostWorkflowResultsRequest.newBuilder()
        .setWorkflowId("my-custom-workflow")
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder()
                        .setUrl("https://portal.clarifai.com/cms-assets/20180320212157/food-001.jpg")
                )
            )
        ).build()
);

if (postWorkflowResultsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post workflow results failed, status: " + postWorkflowResultsResponse.getStatus());
}

// Since we have one input, one output will exist here.
WorkflowResult results = postWorkflowResultsResponse.getResults(0);

// One output is present for each model in the workflow.
for (Output output : results.getOutputsList()) {
    System.out.println("Predicted concepts for model: " + output.getModel().getName());
    for (Concept concept : output.getData().getConceptsList()) {
        System.out.printf("%s %.2f%n", concept.getName(), concept.getValue());
    }
    System.out.println();
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostWorkflowResults(
    {
        workflow_id: "my-custom-workflow",
        inputs: [
            {
                data: {
                    image: {
                        url: "https://portal.clarifai.com/cms-assets/20180320212157/food-001.jpg"
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
            throw new Error("Post workflow results failed, status: " + response.status.description);
        }

        // Since we have one input, one output will exist here.
        const result = response.results[0]

        // One output is present for each model in the workflow.
        for (const output of result.outputs) {
            console.log("Predicted concepts for model: " + output.model.name);
            for (const concept of output.data.concepts) {
                console.log("\t" + concept.name + " " + concept.value);
            }
            console.log();
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_workflow_results_response = stub.PostWorkflowResults(
    service_pb2.PostWorkflowResultsRequest(
      workflow_id="my-custom-workflow",
      inputs=[
        resources_pb2.Input(
          data=resources_pb2.Data(
            image=resources_pb2.Image(
              url="https://portal.clarifai.com/cms-assets/20180320212157/food-001.jpg"
            )
          )
        )
      ]
    ),
    metadata=metadata
)

if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post workflow results failed, status: " + post_workflow_results_response.status.description)

# Since we have one input, one output will exist here.
result = post_workflow_results_response.results[0]

# One output is present for each model in the workflow.
for output in result.outputs:
  print("Predicted concepts for model: " + output.model.name)
  for concept in output.data.concepts:
    print("\t%s %.2f" % (concept.name, concept.value))
  print()
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/workflows/my-custom-workflow/results' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Key YOUR_API_KEY' \
    --data-raw '{
        "inputs": [
            {
                "data": {
                    "image": {
                        "url": "https://portal.clarifai.com/cms-assets/20180320212157/food-001.jpg"
                    }
                }
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

## Get

### Get all workflows in an app

Return all custom workflows in your app.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiWorkflowResponse listWorkflowsResponse = stub.listWorkflows(ListWorkflowsRequest.newBuilder().build());

if (listWorkflowsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List workflows failed, status: " + listWorkflowsResponse.getStatus());
}

for (Workflow workflow : listWorkflowsResponse.getWorkflowsList()) {
    System.out.println("The workflow " + workflow.getId() + " consists of these models:");
    for (WorkflowNode workflowNode : workflow.getNodesList()) {
        Model model = workflowNode.getModel();
        System.out.println(model.getId());
    }
    System.out.println();
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListWorkflows(
    {},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List workflows failed, status: " + response.status.description);
        }

        for (const workflow of response.workflows) {
            console.log("The workflow " + workflow.id + " consists of these models:");
            for (const workflowNode of workflow.nodes) {
                const model = workflowNode.model;
                console.log(model.id);
            }
            console.log();
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_workflows_response = stub.ListWorkflows(
    service_pb2.ListWorkflowsRequest(),
    metadata=metadata
)

if list_workflows_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List workflows failed, status: " + list_workflows_response.status.description)

for workflow in list_workflows_response.workflows:
    print(f"The workflow {workflow.id} consists of these models:")
    for workflow_node in workflow.nodes:
        model = workflow_node.model
        print(model.id)
    print()
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET 'https://api.clarifai.com/v2/workflows' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Key YOUR_API_KEY'
```
{% endtab %}
{% endtabs %}

### Get a workflow by a specific ID

Returns information about a specific workflow.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

SingleWorkflowResponse getWorkflowResponse = stub.getWorkflow(
    GetWorkflowRequest.newBuilder()
        .setWorkflowId("food-and-general")
        .build()
);

if (getWorkflowResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get workflow failed, status: " + getWorkflowResponse.getStatus());
}

Workflow workflow = getWorkflowResponse.getWorkflow();

System.out.println("The workflow consists of these models:");
for (WorkflowNode workflowNode : workflow.getNodesList()) {
    Model model = workflowNode.getModel();
    System.out.println(model.getId());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.GetWorkflow(
    {
        workflow_id: "my-custom-workflow"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get workflow failed, status: " + response.status.description);
        }

        const workflow = response.workflow;

        console.log("The workflow consists of these models:");
        for (const workflowNode of workflow.nodes) {
            const model = workflowNode.model;
            console.log(model.id);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_workflow_response = stub.GetWorkflow(
    service_pb2.GetWorkflowRequest(
        workflow_id="my-custom-workflow"
    ),
    metadata=metadata
)

if get_workflow_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Get workflow failed, status: " + get_workflow_response.status.description)

workflow = get_workflow_response.workflow
print(f"The workflow consists of these models:")
for workflow_node in workflow.nodes:
    model = workflow_node.model
    print(model.id)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET 'https://api.clarifai.com/v2/workflows/my-custom-workflow' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Key YOUR_API_KEY'
```
{% endtab %}
{% endtabs %}

## Update

### Patch workflow

Ability to change the workflow, that is to change the models of which the workflow consists.

Possible actions are "overwrite", "merge" and "remove".

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiWorkflowResponse patchWorkflowsResponse = stub.patchWorkflows(
    PatchWorkflowsRequest.newBuilder()
        .setAction("overwrite")
        .addWorkflows(
            Workflow.newBuilder()
                .setId("my-custom-workflow")
                .addNodes(
                    WorkflowNode.newBuilder()
                        .setId("travel-concepts")
                        .setModel(
                            Model.newBuilder()
                                .setId("ccc28c313d69466f836ab83287a54ed9")
                                .setModelVersion(ModelVersion.newBuilder().setId("cce28c313d69466f836ab83287a54ed9"))
                        )
                )
                .addNodes(
                    WorkflowNode.newBuilder()
                        .setId("nsfw-concepts")
                        .setModel(
                            Model.newBuilder()
                                .setId("ccc76d86d2004ed1a38ba0cf39ecb4b1")
                                .setModelVersion(ModelVersion.newBuilder().setId("cc76a92beaeb4d8495a58ba197998158"))
                        )
                )
                .addNodes(
                    WorkflowNode.newBuilder()
                        .setId("wedding-concepts")
                        .setModel(
                            Model.newBuilder()
                                .setId("c386b7a870114f4a87477c0824499348")
                                .setModelVersion(ModelVersion.newBuilder().setId("787cc9a002164250800598d36b072384"))
                        )
                )
        ).build()
);

if (patchWorkflowsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch workflows failed, status: " + patchWorkflowsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchWorkflows(
    {
        action: "overwrite",
        workflows: [
            {
                id: "my-custom-workflow",
                nodes: [
                    {
                        id: "travel-concepts",
                        model: {
                            id: "ccc28c313d69466f836ab83287a54ed9",
                            model_version: {
                                id: "cce28c313d69466f836ab83287a54ed9"
                            }
                        }
                    },
                    {
                        id: "nsfw-concepts",
                        model: {
                            id: "ccc76d86d2004ed1a38ba0cf39ecb4b1",
                            model_version: {
                                id: "cc76a92beaeb4d8495a58ba197998158"
                            }
                        }
                    },
                    {
                        id: "wedding-concepts",
                        model: {
                            id: "c386b7a870114f4a87477c0824499348",
                            model_version: {
                                id: "787cc9a002164250800598d36b072384"
                            }
                        }
                    },
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
            throw new Error("Patch workflows failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_workflows_response = stub.PatchWorkflows(
    service_pb2.PatchWorkflowsRequest(
      action="overwrite",
      workflows=[
        resources_pb2.Workflow(
          id="my-custom-workflow",
          nodes=[
            resources_pb2.WorkflowNode(
              id="travel-concepts",
              model=resources_pb2.Model(
                id="ccc28c313d69466f836ab83287a54ed9",
                model_version=resources_pb2.ModelVersion(
                  id="cce28c313d69466f836ab83287a54ed9"
                )
              )
            ),
            resources_pb2.WorkflowNode(
              id="nsfw-concepts",
              model=resources_pb2.Model(
                id="ccc76d86d2004ed1a38ba0cf39ecb4b1",
                model_version=resources_pb2.ModelVersion(
                  id="cc76a92beaeb4d8495a58ba197998158"
                )
              )
            ),
            resources_pb2.WorkflowNode(
              id="wedding-concepts",
              model=resources_pb2.Model(
                id="c386b7a870114f4a87477c0824499348",
                model_version=resources_pb2.ModelVersion(
                  id="787cc9a002164250800598d36b072384"
                )
              )
            ),
          ]
        )
      ]
    ),
    metadata=metadata
)

if patch_workflows_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch workflows failed, status: " + patch_workflows_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
# Supported actions are: overwrite, merge, remove.

curl -X PATCH 'https://api.clarifai.com/v2/workflows' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Key YOUR_API_KEY' \
    --data-raw '{
        "action": "overwrite",
        "workflows": [
            {
                "id": "my-custom-workflow",
                "nodes": [
                    {
                        "id": "travel-concepts",
                        "model": {
                            "id": "ccc28c313d69466f836ab83287a54ed9",
                            "model_version": {
                                "id": "cce28c313d69466f836ab83287a54ed9"
                            }
                        }
                    },
                    {
                        "id": "nsfw-concepts",
                        "model": {
                            "id": "ccc76d86d2004ed1a38ba0cf39ecb4b1",
                            "model_version": {
                                "id": "cc76a92beaeb4d8495a58ba197998158"
                            }
                        }
                    },
                    {
                        "id": "wedding-concepts",
                        "model": {
                            "id": "c386b7a870114f4a87477c0824499348",
                            "model_version": {
                                "id": "787cc9a002164250800598d36b072384"
                            }
                        }
                    }
                ]
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}

## Delete

### Delete workflow by ID

Delete a specific workflow.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteWorkflowResponse = stub.deleteWorkflow(
    DeleteWorkflowRequest.newBuilder()
        .setWorkflowId("my-custom-workflow")
        .build()
);

if (deleteWorkflowResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete workflow failed, status: " + deleteWorkflowResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteWorkflow(
    {
        workflow_id: "my-custom-workflow",
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete workflow failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_workflow_response = stub.DeleteWorkflow(
    service_pb2.DeleteWorkflowRequest(
      workflow_id="my-custom-workflow"
    ),
    metadata=metadata
)

if delete_workflow_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete workflow failed, status: " + delete_workflow_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE 'https://api.clarifai.com/v2/workflows/my-custom-workflow \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Key YOUR_API_KEY'
```
{% endtab %}
{% endtabs %}

### Delete all workflows

Deletes all custom workflows.

> Note: instead of "delete\_all" it's possible to specify a list of workflow IDs to be deleted, using the `ids` field.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteWorkflowsResponse = stub.deleteWorkflows(
    DeleteWorkflowsRequest.newBuilder()
        .setDeleteAll(true)
        .build()
);

if (deleteWorkflowsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete workflows failed, status: " + deleteWorkflowsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteWorkflows(
    {
        delete_all: true
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete workflows failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_workflows_response = stub.DeleteWorkflows(
    service_pb2.DeleteWorkflowsRequest(
      delete_all=True
    ),
    metadata=metadata
)

if delete_workflows_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete workflows failed, status: " + delete_workflows_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE 'https://api.clarifai.com/v2/workflows' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Key YOUR_API_KEY' \
    --data-raw '{
        "delete_all": true
    }'
```
{% endtab %}
{% endtabs %}

