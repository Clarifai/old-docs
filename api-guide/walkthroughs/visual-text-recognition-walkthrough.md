# Visual Text Recognition Walkthrough

Visual text recognition helps you understand text in images and videos.

Visual text detection and recognition models need to be configured in a workflow so that you can understand text in your images. You will add these three models to your workflow:

* **Visual Text Detection**
* **1.0 Cropper**
* **Visual Text Recognition**

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
                id="visual-text-recognition-id",
                nodes=[
                    resources_pb2.WorkflowNode(
                        id="detect-concept",
                        model=resources_pb2.Model(
                            id="2419e2eae04d04f820e5cf3aba42d0c7",
                            model_version=resources_pb2.ModelVersion(
                                id="75a5b92a0dec436a891b5ad224ac9170"
                            )
                        )
                    ),
                    resources_pb2.WorkflowNode(
                        id="image-crop",
                        model=resources_pb2.Model(
                            id="ce3f5832af7a4e56ae310d696cbbefd8",
                            model_version=resources_pb2.ModelVersion(
                                id="a78efb13f7774433aa2fd4864f41f0e6"
                                )
                            ),
                            node_inputs=[
                                resources_pb2.NodeInput(node_id="detect-concept")
                            ]
                        ),
                    resources_pb2.WorkflowNode(
                        id="image-to-text",
                        model=resources_pb2.Model(
                            id="9fe78b4150a52794f86f237770141b33",
                            model_version=resources_pb2.ModelVersion(
                                id="d94413e582f341f68884cac72dbd2c7b"
                                )
                            ),
                            node_inputs=[
                                resources_pb2.NodeInput(node_id="image-crop")
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
              .setId("visual-text-recognition-id")
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("detect-concept")
                      .setModel(
                          Model.newBuilder()
                              .setId("2419e2eae04d04f820e5cf3aba42d0c7")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("75a5b92a0dec436a891b5ad224ac9170")
                              )
                      )
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("image-crop")
                      .setModel(
                          Model.newBuilder()
                              .setId("ce3f5832af7a4e56ae310d696cbbefd8")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("a78efb13f7774433aa2fd4864f41f0e6")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("detect-concept"))
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("image-to-text")
                      .setModel(
                          Model.newBuilder()
                              .setId("9fe78b4150a52794f86f237770141b33")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("d94413e582f341f68884cac72dbd2c7b")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("image-crop"))
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
                id: "visual-text-recognition-id",
                nodes: [
                    {
                        id: "detect-concept",
                        model: {
                            id: "2419e2eae04d04f820e5cf3aba42d0c7",
                            model_version: {
                                id: "75a5b92a0dec436a891b5ad224ac9170"
                            }
                        }
                    },
                    {
                        id: "image-crop",
                        model: {
                            id: "ce3f5832af7a4e56ae310d696cbbefd8",
                            model_version: {
                                id: "a78efb13f7774433aa2fd4864f41f0e6"
                            }
                        },
                        node_inputs: [
                            {node_id: "detect-concept"}
                        ]
                    },
                    {
                        id: "image-to-text",
                        model: {
                            id: "9fe78b4150a52794f86f237770141b33",
                            model_version: {
                                id: "d94413e582f341f68884cac72dbd2c7b"
                            }
                        },
                        node_inputs: [
                            {node_id: "image-crop"}
                        ]
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
                "id": "visual-text-recognition-id",
                "nodes": [
                    {
                        "id": "detect-concept",
                        "model": {
                            "id": "2419e2eae04d04f820e5cf3aba42d0c7",
                            "model_version": {
                                "id": "75a5b92a0dec436a891b5ad224ac9170"
                            }
                        }
                    },
                    {
                        "id": "image-crop",
                        "model": {
                            "id": "ce3f5832af7a4e56ae310d696cbbefd8",
                            "model_version": {
                                "id": "a78efb13f7774433aa2fd4864f41f0e6"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "general-concept"
                            }
                        ]
                    },
                    {
                        "id": "image-to-text",
                        "model": {
                            "id": "9fe78b4150a52794f86f237770141b33",
                            "model_version": {
                                "id": "d94413e582f341f68884cac72dbd2c7b"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "image-crop"
                            }
                        ]
                    },
                ]
            }
        ]
    }'
```
{% endtab %}
{% endtabs %}
