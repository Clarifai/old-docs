# Deep Training

Clarifai offers a variety of prebuilt models that are designed to help you build AI solutions quickly and efficiently. Clarifai Models are the recommended starting point for many users because they offer incredibly fast training times when you customize them using the "Context-Based Classifier" type in Portal's Model Mode.

But there are many cases where accuracy and the ability to carefully target solutions takes priority over speed and ease of use. Additionally, your may need a model to learn new features not recognized by existing Clarifai Models. For these cases, it is possible to "deep train" your custom models and integrate them directly within your workflows.

You might consider deep training if you have:

* **A custom tailored dataset**
* **Accurate labels**
* **Expertise and time to fine tune models**

{% hint style="info" %}
Deep training is in early access preview. To request you access, [contact us](https://www.clarifai.com/contact).
{% endhint %}

## Template types

You can take advantage of a variety of templates when building your deep trained models. Templates give you the control to choose the specific architecture used by your neural network, and also define a set of hyperparameters that you can use to fine-tune the way that your model learns.

#### Visual Classifier

Classification templates let you classify what is in your images or videos.

#### Visual Detector

Detection templates make it easy to build models that can identify objects within a region of your images or videos. Detection models return concepts and bounding boxes.

#### Visual Embedder

Embedding models can be useful in their own right \(for applications like clustering and visual search\), or as an input to a machine learning model for a supervised task. In effect, embedding templates enable you to create your own "base models" that you can then use in your workflows.

## Hyperparameters

Deep training gives you the power to tune the hyperparameters that affect “how” your model learns. Model Mode dynamically changes the available hyperparameters based on the template selected.

* **average\_horizontal\_flips** Provides basic data augmentation for your dataset. If set to true, there is a 0.5 probability that current image and associated ground truth will flip horizontally.
* **base\_gradient\_multiplier** This sets the learning rate of the pre-initialized base \(also sometimes called "backbone"\) model that generates embeddings. Learning rate controls how the weights of our network are adjusted with respect to the loss gradient. The lower the value, the slower the trip along the downward slope. A low learning rate can help ensure that local minima are not missed, but can take a long time to converge — especially if the model gets stuck on a plateau region.
* **batch\_size** The number of images used to make updates to the model. Increased batch size allows for a better approximation of gradient over those samples. Batches allow for stochastic gradient descent, by choosing a random set of X images for each training update. You may want to increase batch size if the model is large and taking a long time to train. You also may want to increase the batch size if your total number of model concepts is larger than the batch size \(you may want to increase to around 2x the category count\).
* **detection\_score\_threshold** Only bounding boxes with a detection score above this threshold will be returned.
* **image\_size** The size of images used for training. Images are scaled for efficient processing, and a lower number will take up less memory and run faster. A higher number will have more pixel information to train on and will increase accuracy.
* **init\_epochs** The initial number of epochs before the first step/change in the **lrate**.
* **logreg** Set to True to use **logistic regression**, set to False to use **softmax** \(for binary classification\).
* **lrate** The learning rate is a tuning parameter in an optimization algorithm that determines the step size at each iteration while moving toward a minimum of a loss function.
* **num\_epochs** An epoch is defined as one-pass over the entire dataset. If you increase it, it will take longer to train but it could make the model more robust.
* **num\_items\_per\_epoch** The number of training examples per "epoch". An epoch would be defined as one-pass over this amount of examples.
* **per\_128\_lrate** Total change in **lrate** after 128 images processed. This is calculated as lrate = per\_128\_lrate \* \(batch\_size / 128\).
* **per\_item\_lrate** The rate that model weights are changed per item.
* **step\_epochs** The number of epochs between applications of the step/change in **lrate** scheduler.
* **test\_freq** The number of epochs should you run before evaluation of the test set. Increased frequency can allow for more granular testing but will extend processing time.
* **use\_perclass\_regression** Enables box coordinate local regression on a per-class basis. When set to True there will be `num_classes` sets of regressors for each anchor location, when set to False, there will be one coordinate regressor for each anchor location.

## Create

### Create a Visual Classifier

Use a visual classifier model if you would like to classify images and videos frames into set of concepts.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder trainInfoParams = Struct.newBuilder()
    .putFields(
        "num_epochs", Value.newBuilder().setNumberValue(2).build()

    )
    .putFields(
        "template", Value.newBuilder().setStringValue("classification_cifar10_v1").build()
    );

SingleModelResponse postModelsResponse = stub.postModels(
    PostModelsRequest.newBuilder()
        .addModels(
            Model.newBuilder()
                .setId("lawrence-1591638385")
                .setModelTypeId("visual-classifier")
                .setTrainInfo(TrainInfo.newBuilder().setParams(trainInfoParams))
                .setOutputInfo(
                    OutputInfo.newBuilder()
                        .setData(
                            Data.newBuilder()
                                .addConcepts(Concept.newBuilder().setId("ferrari23"))
                                .addConcepts(Concept.newBuilder().setId("outdoors23"))
                        )
                        .setOutputConfig(
                            OutputConfig.newBuilder()
                                .setClosedEnvironment(true)
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
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostModels(
    {
        models: [
            {
                id: "lawrence-1591638385",
                model_type_id: "visual-classifier",
                train_info: {
                    params: {
                        num_epoch: 2,
                        template: "classification_cifar10_v1"
                    }
                },
                output_info: {
                    data: {
                        concepts: [
                            {id: "ferrari23"},
                            {id: "outdoors23"}
                        ]
                    },
                    output_config: {
                        closed_environment: true
                    }
                }
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            done(err);
            return;
        }

        if (response.status.code !== 10000) {
            done(new Error("Received status: " + response.status.description + "\n" + response.status.details));
        }

        done();
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

train_params = Struct()
train_params.update(
{
  "template": "classification_cifar10_v1",
  "num_epochs": 2
}
)

post_models_response = stub.PostModels(
service_pb2.PostModelsRequest(
  models=[
    resources_pb2.Model(
      id="lawrence-1591638385",
      model_type_id="visual-classifier",
      train_info=resources_pb2.TrainInfo(params=train_params),
      output_info=resources_pb2.OutputInfo(
        data=resources_pb2.Data(
          concepts=[
            resources_pb2.Concept(id="ferrari23"),
            resources_pb2.Concept(id="outdoors23")
          ]
        ),
        output_config=resources_pb2.OutputConfig(closed_environment=True)
      )
    )
  ]
),
metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/models' \
    -H 'Authorization: Key YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "model": {
            "id": "lawrence-1591638385",
            "model_type_id": "visual-classifier",
            "train_info": {
                "params": {
                    "template": "classification_cifar10_v1",
                    "num_epochs": 2
                }
            },
            "output_info": {
                "data": {
                    "concepts": [
                        {"id":"ferrari23"},
                        {"id":"outdoors23"}
                    ]
                },
                "output_config": {
                  "closed_environment" : true
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create a Visual Detector

Create a visual detector to detect bounding box regions in images or video frames and then classify the detected images. You can also send the image regions to an image cropper model to create a new cropped image.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder trainInfoParams = Struct.newBuilder()
    .putFields(
        "num_epochs", Value.newBuilder().setNumberValue(2).build()

    )
    .putFields(
        "template", Value.newBuilder().setStringValue("Clarifai-InceptionV2").build()
    );

SingleModelResponse postModelsResponse = stub.postModels(
    PostModelsRequest.newBuilder()
        .addModels(
            Model.newBuilder()
                .setId("detection-test-1591638385")
                .setModelTypeId("visual-detector")
                .setTrainInfo(TrainInfo.newBuilder().setParams(trainInfoParams))
                .setOutputInfo(
                    OutputInfo.newBuilder()
                        .setData(
                            Data.newBuilder()
                                .addConcepts(Concept.newBuilder().setId("ferrari23"))
                                .addConcepts(Concept.newBuilder().setId("outdoors23"))
                        )
                        .setOutputConfig(
                            OutputConfig.newBuilder()
                                .setClosedEnvironment(true)
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
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostModels(
    {
        models: [
            {
                id: "detection-test-1591638385",
                model_type_id: "visual-detector",
                train_info: {
                    params: {
                        num_epoch: 2,
                        template: "Clarifai-InceptionV2"
                    }
                },
                output_info: {
                    data: {
                        concepts: [
                            {id: "ferrari23"},
                            {id: "outdoors23"}
                        ]
                    },
                    output_config: {
                        closed_environment: true
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
            throw new Error("Received status: " + response.status.description + "\n" + response.status.details);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

train_params = Struct()
train_params.update(
    {
        "template": "Clarifai-InceptionV2",
        "num_epochs": 2
    }
)

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        models=[
            resources_pb2.Model(
                id="detection-test-1591638385",
                model_type_id="visual-detector",
                train_info=resources_pb2.TrainInfo(params=train_params),
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="ferrari23"),
                            resources_pb2.Concept(id="outdoors23")
                        ]
                    ),
                    output_config=resources_pb2.OutputConfig(closed_environment=True)
                )
            )
        ]
    ),
    metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
  raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/models' \
    -H 'Authorization: Key YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "model": {
            "id": "detection-test-1591638385",
            "model_type_id": "visual-detector",
            "train_info": {
                "params": {
                    "template": "Clarifai-InceptionV2",
                    "num_epochs": 2
                }
            },
            "output_info": {
                "data": {
                    "concepts": [
                        {"id":"ferrari23"},
                        {"id":"outdoors23"}
                    ]
                },
                "output_config": {
                  "closed_environment" : true
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create a Visual Embedder

Create a visual embedding model to transform images and videos frames into "high level" vector representation understood by our AI models. These embeddings enable visual search and can be used as base models to train other models.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

Struct.Builder trainInfoParams = Struct.newBuilder()
    .putFields(
        "num_epochs", Value.newBuilder().setNumberValue(2).build()

    )
    .putFields(
        "template", Value.newBuilder().setStringValue("classification_basemodel_v1_embed").build()
    );

SingleModelResponse postModelsResponse = stub.postModels(
    PostModelsRequest.newBuilder()
        .addModels(
            Model.newBuilder()
                .setId("embed-test-1591638385")
                .setModelTypeId("visual-embedder")
                .setTrainInfo(TrainInfo.newBuilder().setParams(trainInfoParams))
                .setOutputInfo(
                    OutputInfo.newBuilder()
                        .setData(
                            Data.newBuilder()
                                .addConcepts(Concept.newBuilder().setId("ferrari23"))
                                .addConcepts(Concept.newBuilder().setId("outdoors23"))
                        )
                        .setOutputConfig(
                            OutputConfig.newBuilder()
                                .setClosedEnvironment(true)
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
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostModels(
    {
        models: [
            {
                id: "embed-test-1591638385",
                model_type_id: "visual-embedder",
                train_info: {
                    params: {
                        num_epoch: 2,
                        template: "classification_basemodel_v1_embed"
                    }
                },
                output_info: {
                    data: {
                        concepts: [
                            {id: "ferrari23"},
                            {id: "outdoors23"}
                        ]
                    },
                    output_config: {
                        closed_environment: true
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
            throw new Error("Received status: " + response.status.description + "\n" + response.status.details);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

from google.protobuf.struct_pb2 import Struct

train_params = Struct()
train_params.update(
    {
        "template": "classification_basemodel_v1_embed",
        "num_epochs": 2
    }
)

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        models=[
            resources_pb2.Model(
                id="embed-test-1591638385",
                model_type_id="visual-embedder",
                train_info=resources_pb2.TrainInfo(params=train_params),
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="ferrari23"),
                            resources_pb2.Concept(id="outdoors23")
                        ]
                    ),
                    output_config=resources_pb2.OutputConfig(closed_environment=True)
                )
            )
        ]
      ),
      metadata=metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post models failed, status: " + post_models_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/models' \
    -H 'Authorization: Key YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "model": {
            "id": "embed-test-1591638385",
            "model_type_id": "visual-embedder",
            "train_info": {
                "params": {
                    "template": "classification_basemodel_v1_embed",
                    "num_epochs": 2
                }
            },
            "output_info": {
                "data": {
                    "concepts": [
                        {"id":"ferrari23"},
                        {"id":"outdoors23"}
                    ]
                },
                "output_config": {
                  "closed_environment" : true
                }
            }
        }
    }'
```
{% endtab %}
{% endtabs %}

### Create a Workflow with a Deep Trained Model

Put your new deep-trained model to work by adding it to a workflow.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiWorkflowResponse postWorkflowsResponse = stub.postWorkflows(
  PostWorkflowsRequest.newBuilder()
      .addWorkflows(
          Workflow.newBuilder()
              .setId("my-new-workflow-id")
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("embed")
                      .setModel(
                          Model.newBuilder()
                              .setId("{YOUR_EMBED_MODEL_ID}")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("{YOUR_EMBED_MODEL_VERSION_ID}")
                              )
                      )
              )
              .addNodes(
                  WorkflowNode.newBuilder()
                      .setId("my-custom-model")
                      .setModel(
                          Model.newBuilder()
                              .setId("{YOUR_CUSTOM_MODEL_ID}")
                              .setModelVersion(
                                  ModelVersion.newBuilder()
                                      .setId("{YOUR_CUSTOM_MODEL_MODEL_VERSION_ID}")
                              )
                      )
                      .addNodeInputs(NodeInput.newBuilder().setNodeId("embed"))
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
// https://docs.clarifai.com/api-guide/api-overview

stub.PostWorkflows(
    {
        workflows: [
            {
                id: "my-new-workflow-id",
                nodes: [
                    {
                        id: "embed",
                        model: {
                            id: "{YOUR_EMBED_MODEL_ID}",
                            model_version: {
                                id: "{YOUR_EMBED_MODEL_VERSION_ID}"
                            }
                        }
                    },
                    {
                        id: "my-custom-model",
                        model: {
                            id: "{YOUR_CUSTOM_MODEL_ID}",
                            model_version: {
                                id: "{YOUR_CUSTOM_MODEL_VERSION_ID}"
                            }
                        },
                        node_inputs: [
                            {node_id: "embed"}
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_workflows_response = stub.PostWorkflows(
    service_pb2.PostWorkflowsRequest(
        workflows=[
            resources_pb2.Workflow(
                id="my-new-workflow-id",
                nodes=[
                    resources_pb2.WorkflowNode(
                        id="embed",
                        model=resources_pb2.Model(
                            id="{YOUR_EMBED_MODEL_ID}",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_EMBED_MODEL_VERSION_ID}"
                            )
                        )
                    ),
                    resources_pb2.WorkflowNode(
                        id="my-custom-model",
                        model=resources_pb2.Model(
                            id="{YOUR_CUSTOM_MODEL_ID}",
                            model_version=resources_pb2.ModelVersion(
                                id="{YOUR_CUSTOM_MODEL_VERSION_ID}"
                            )
                        ),
                        node_inputs=[
                            resources_pb2.NodeInput(node_id="embed")
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

{% tab title="cURL" %}
```text
curl -X POST 'https://api.clarifai.com/v2/workflows' \
    -H 'Authorization: Key YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "workflows": [
            {
                "id": "my-new-workflow-id",
                "nodes": [
                    {
                        "id": "embed",
                        "model": {
                            "id": "{YOUR_EMBED_MODEL_ID}",
                            "model_version": {
                                "id": "{YOUR_EMBED_MODEL_VERSION_ID}"
                            }
                        }
                    },
                    {
                        "id": "my-custom-model",
                        "model": {
                            "id": "{YOUR_CUSTOM_MODEL_ID}",
                            "model_version": {
                                "id": "{YOUR_CUSTOM_MODEL_VERSION_ID}"
                            }
                        },
                        "node_inputs": [
                            {
                                "node_id": "embed"
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

### Update your Default Workflow with your Deep Trained Model

Index your inputs with your deep trained model by updating your default workflow. You can also use your deep trained embeddings as the basis for clustering and search.

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
```javascript
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

