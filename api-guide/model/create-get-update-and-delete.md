---
description: Manage your model training jobs.
---

# Create, Get, Update, Delete

### Create Model

To create a model, you need to specify the model's name and other required fields \(which depend on the model\). Specifying the ID is optional.

Below, we create a classifier model with one initial concept. You can always add and remove concepts later.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

SingleModelResponse postModelsResponse = stub.postModels(
    PostModelsRequest.newBuilder().addModels(
        Model.newBuilder()
            .setId("petsID")
            .setOutputInfo(
                OutputInfo.newBuilder().setData(
                    Data.newBuilder().addConcepts(Concept.newBuilder().setId("boscoe"))
                )
            )
    ).build()
);

if (postModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models failed, status: " + postModelsResponse.getStatus());
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModels(
    {
        models: [
            {
                id: "petsID",
                output_info: {
                    data: {concepts: [{id: "boscoe"}]},
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

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        models=[
            resources_pb2.Model(
                id="petsID",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[resources_pb2.Concept(id="boscoe", value=1)]
                    ),
                )
            )
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

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "model": {
      "id": "petsID",
      "output_info": {
        "data": {
          "concepts": [
            {
              "id": "boscoe",
              "value": 1
            }
          ]
        }
      }
    }
  }'\
  https://api.clarifai.com/v2/models
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "model": {
    "id": "petsID",
    "output_info": {
      "data": {
        "concepts": [
          {
            "id": "boscoe",
            "value": 1
          }
        ]
      }
    }
  }
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Add Concepts To A Model

You can add concepts to a model at any point. As you add concepts to inputs, you may want to add them to your model.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiModelResponse patchModelsResponse = stub.patchModels(
    PatchModelsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove
        .addModels(
            Model.newBuilder()
                .setId("petsID")
                .setOutputInfo(
                    OutputInfo.newBuilder().setData(
                        Data.newBuilder().addConcepts(Concept.newBuilder().setId("charlie"))
                    )
                )
        )
        .build()
);

if (patchModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch models failed, status: " + patchModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchModels(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove
        models: [
            {
                id: "petsID",
                output_info: {data: {concepts: [{id: "charlie"}]}}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_models_response = stub.PatchModels(
    service_pb2.PatchModelsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove
        models=[
            resources_pb2.Model(
                id="petsID",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[resources_pb2.Concept(id="charlie")]
                    ),
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(patch_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(patch_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(patch_models_response.outputs[0].status.details))
    raise Exception("Patch models failed, status: " + patch_models_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "models": [
      {
        "id": "petsID",
        "output_info": {
          "data": {
            "concepts": [
              {
                "id": "charlie"
              }
            ]
          }
        }
      }
    ],
    "action": "merge"
  }'\
  https://api.clarifai.com/v2/models/
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "models": [
    {
      "id": "petsID",
      "output_info": {
        "data": {
          "concepts": [
            {
              "id": "charlie"
            }
          ]
        }
      }
    }
  ],
  "action": "merge"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Remove Concepts From A Model

Conversely, if you'd like to remove concepts from a model, you can also do that.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiModelResponse patchModelsResponse = stub.patchModels(
    PatchModelsRequest.newBuilder()
        .setAction("remove")  // Supported actions: overwrite, merge, remove
        .addModels(
            Model.newBuilder()
                .setId("petsID")
                .setOutputInfo(
                    OutputInfo.newBuilder().setData(
                        Data.newBuilder().addConcepts(Concept.newBuilder().setId("charlie"))
                    )
                )
        )
        .build()
);

if (patchModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch models failed, status: " + patchModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchModels(
    {
        action: "remove",  // Supported actions: overwrite, merge, remove
        models: [
            {
                id: "petsID",
                output_info: {data: {concepts: [{id: "charlie"}]}}
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_models_response = stub.PatchModels(
    service_pb2.PatchModelsRequest(
        action="remove",  # Supported actions: overwrite, merge, remove
        models=[
            resources_pb2.Model(
                id="petsID",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[resources_pb2.Concept(id="charlie")]
                    ),
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(patch_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(patch_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(patch_models_response.outputs[0].status.details))
    raise Exception("Patch models failed, status: " + patch_models_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "models": [
      {
        "id": "petsID",
        "output_info": {
          "data": {
            "concepts": [
              {
                "id": "charlie"
              }
            ]
          }
        }
      }
    ],
    "action": "remove"
  }'\
  https://api.clarifai.com/v2/models/
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "models": [
    {
      "id": "petsID",
      "output_info": {
        "data": {
          "concepts": [
            {
              "id": "charlie"
            }
          ]
        }
      }
    }
  ],
  "action": "remove"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Update Model Name and Configuration

Here we will change the model name to 'newname' and the model's configuration to have concepts\_mutually\_exclusive=true and closed\_environment=true.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiModelResponse patchModelsResponse = stub.patchModels(
    PatchModelsRequest.newBuilder()
        .setAction("overwrite")
        .addModels(
            Model.newBuilder()
                .setId("petsID")
                .setName("newname")
                .setOutputInfo(
                    OutputInfo.newBuilder()
                        .setData(
                            Data.newBuilder()
                                .addConcepts(Concept.newBuilder().setId("birds"))
                                .addConcepts(Concept.newBuilder().setId("hurd"))
                        )
                        .setOutputConfig(
                            OutputConfig.newBuilder()
                                .setConceptsMutuallyExclusive(true)
                                .setClosedEnvironment(true)
                        )
                )
    ).build()
);

if (patchModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch models failed, status: " + patchModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchModels(
    {
        action: "overwrite",
        models: [
            {
                id: "petsID",
                name: "newname",
                output_info: {
                    data: {concepts: [{id: "birds"}, {id: "hurd"}]},
                    output_config: {concepts_mutually_exclusive: true, closed_environment: true}
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
            throw new Error("Patch models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_models_response = stub.PatchModels(
    service_pb2.PatchModelsRequest(
        action="overwrite",
        models=[
            resources_pb2.Model(
                id="petsID",
                name="newname",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="birds"),
                            resources_pb2.Concept(id="hurd")
                        ]
                    ),
                    output_config=resources_pb2.OutputConfig(
                        concepts_mutually_exclusive=True,
                        closed_environment=True,
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(patch_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(patch_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(patch_models_response.outputs[0].status.details))
    raise Exception("Patch models failed, status: " + patch_models_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "models": [
      {
        "id": "petsID",
        "name": "newname",
        "output_info": {
          "data": {"concepts": [{"id": "birds"}, {"id": "hurd"}]},
          "output_config": {
            "concepts_mutually_exclusive": true,
            "closed_environment": true
          }
        }
      }
    ],
    "action": "overwrite"
  }'\
  https://api.clarifai.com/v2/models/
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "models": [
    {
      "id": "petsID",
      "name": "newname",
      "output_info": {
        "data": {"concepts": [{"id": "birds"}, {"id": "hurd"}]},
        "output_config": {
          "concepts_mutually_exclusive": true,
          "closed_environment": true
        }
      }
    }
  ],
  "action": "overwrite"
});

const requestOptions = {
  method: 'PATCH',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Get

### List Model Types

Learn about available model types and their hyperparameters. This endpoint lists all the possible models that are creatable \(when creatable=true\), or in general in the platform \(the others ones have creatable=false\).

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiModelTypeResponse listModelTypesResponse = stub.listModelTypes(ListModelTypesRequest.newBuilder().build());

for (ModelType modelType : listModelTypesResponse.getModelTypesList()) {
    System.out.println(modelType);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListModelTypes(
    {
        page: 1,
        per_page: 500
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Received status: " + response.status.description + "\n" + response.status.details);
        }

        for (const model_type of response.model_types) {
            console.log(model_type)
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

response = stub.ListModelTypes(
    service_pb2.ListModelTypesRequest(), 
    metadata=metadata
    )

if response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(response.outputs[0].status.code))
    print("\tDescription: {}".format(response.outputs[0].status.description))
    print("\tDetails: {}".format(response.outputs[0].status.details))
    raise Exception("Patch models failed, status: " + response.status.description)

for model_type in response.model_types:
  print(model_type)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET 'https://api.clarifai.com/v2/models/types?per_page=20&page=1' \
    -H 'Authorization: Key YOUR_API_KEY'
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

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/types?per_page=20&page=1`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Get Models

To get a list of all models including models you've created as well as [Clarifai models](https://github.com/Clarifai/old-docs/tree/1c1d25cdd43190c38a2edb313297c0d566b3a0e3/api-guide/model/api-guide/model/public-models.md):

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiModelResponse listModelsResponse = stub.listModels(
    ListModelsRequest.newBuilder().build()
);

if (listModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List models failed, status: " + listModelsResponse.getStatus());
}

List<Model> models = listModelsResponse.getModelsList();
for (Model model : models) {
    System.out.println(model);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListModels(
    {},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List models failed, status: " + response.status.description);
        }

        for (const model of response.models) {
            console.log(JSON.stringify(model, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_models_response = stub.ListModels(
    service_pb2.ListModelsRequest(),
    metadata=metadata
)

if list_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(list_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(list_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(list_models_response.outputs[0].status.details))
    raise Exception("List models failed, status: " + list_models_response.status.description)

for model in list_models_response.models:
    print(model)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models
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

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Get Model By Id

All models have unique Ids. You can get a specific model by its id:

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

SingleModelResponse getModelResponse = stub.getModel(
    GetModelRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (getModelResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get model failed, status: " + getModelResponse.getStatus());
}

Model model = getModelResponse.getModel();
System.out.println(model);
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.GetModel(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List models failed, status: " + response.status.description);
        }

        const model = response.model;
        console.log(JSON.stringify(model, null, 2));
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_model_response = stub.GetModel(
    service_pb2.GetModelRequest(model_id="petsID"),
    metadata=metadata
)

if get_model_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(get_model_response.outputs[0].status.code))
    print("\tDescription: {}".format(get_model_response.outputs[0].status.description))
    print("\tDetails: {}".format(get_model_response.outputs[0].status.details))
    raise Exception("Get model failed, status: " + get_model_response.status.description)

model = get_model_response.model
print(model)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Get Model Output Info By Id

The output info of a model lists what concepts it contains.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

SingleModelResponse getModelOutputInfoResponse = stub.getModelOutputInfo(
    GetModelRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (getModelOutputInfoResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get model output info failed, status: " + getModelOutputInfoResponse.getStatus());
}

Model model = getModelOutputInfoResponse.getModel();
System.out.println(model);
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.GetModelOutputInfo(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List models failed, status: " + response.status.description);
        }

        const model = response.model;
        console.log(JSON.stringify(model, null, 2));
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_model_response = stub.GetModelOutputInfo(
    service_pb2.GetModelRequest(model_id="petsID"),
    metadata=metadata
)

if get_model_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(get_model_response.outputs[0].status.code))
    print("\tDescription: {}".format(get_model_response.outputs[0].status.description))
    print("\tDetails: {}".format(get_model_response.outputs[0].status.details))
    raise Exception("Get model failed, status: " + get_model_response.status.description)

model = get_model_response.model
print(model)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID/output_info
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}/output_info`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### List Model Versions

Every time you train a model, it creates a new version. You can list all the versions created.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiModelVersionResponse listModelVersionsResponse = stub.listModelVersions(
    ListModelVersionsRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (listModelVersionsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List model versions failed, status: " + listModelVersionsResponse.getStatus());
}

List<ModelVersion> modelVersions = listModelVersionsResponse.getModelVersionsList();
for (ModelVersion modelVersion : modelVersions) {
    System.out.println(modelVersion);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListModelVersions(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List model versions failed, status: " + response.status.description);
        }

        for (const model_version of response.model_versions) {
            console.log(JSON.stringify(model_version, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_model_versions_response = stub.ListModelVersions(
    service_pb2.ListModelVersionsRequest(
        model_id="petsID"
    ),
    metadata=metadata
)

if list_model_versions_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(list_model_versions_response.outputs[0].status.code))
    print("\tDescription: {}".format(list_model_versions_response.outputs[0].status.description))
    print("\tDetails: {}".format(list_model_versions_response.outputs[0].status.details))
    raise Exception("List model versions failed, status: " + list_model_versions_response.status.description)

for model_version in list_model_versions_response.model_versions:
    print(model_version)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID/versions
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}/versions`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Get Model Version By Id

To get a specific model version, you must provide the model\_id as well as the version\_id. You can inspect the model version status to determine if your model is trained or still training.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions


SingleModelVersionResponse getModelVersionResponse = stub.getModelVersion(
    GetModelVersionRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")
        .build()
);

if (getModelVersionResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Get model version failed, status: " + getModelVersionResponse.getStatus());
}

ModelVersion modelVersion = getModelVersionResponse.getModelVersion();
System.out.println(modelVersion);
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.GetModelVersion(
    {model_id: "petsID", version_id: "{YOUR_MODEL_VERSION_ID}"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Get model version failed, status: " + response.status.description);
        }

        const model_version = response.model_version;
        console.log(JSON.stringify(model_version, null, 2));
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

get_model_version_response = stub.GetModelVersion(
    service_pb2.GetModelVersionRequest(
        model_id="petsID",
        version_id="{YOUR_MODEL_VERSION_ID}"
    ),
    metadata=metadata
)

if get_model_version_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(get_model_version_response.outputs[0].status.code))
    print("\tDescription: {}".format(get_model_version_response.outputs[0].status.description))
    print("\tDetails: {}".format(get_model_version_response.outputs[0].status.details))
    raise Exception("Get model version failed, status: " + get_model_version_response.status.description)

model_version = get_model_version_response.model_version
print(model_version)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID/versions/{YOUR_MODEL_VERSION_ID}
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'
const modelVersionId = '{MODEL_VERSION_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}/versions/${modelVersionId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Get Model Training Inputs

You can list all the inputs that were used to train the model.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse listModelInputsResponse = stub.listModelInputs(
    ListModelInputsRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (listModelInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List model inputs failed, status: " + listModelInputsResponse.getStatus());
}

List<Input> inputs = listModelInputsResponse.getInputsList();
for (Input input : inputs) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListModelInputs(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List model inputs failed, status: " + response.status.description);
        }

        for (const input of response.inputs) {
            console.log(JSON.stringify(input, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_model_inputs_response = stub.ListModelInputs(
    service_pb2.ListModelInputsRequest(model_id="petsID"),
    metadata=metadata
)

if list_model_inputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(list_model_inputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(list_model_inputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(list_model_inputs_response.outputs[0].status.details))
    raise Exception("List model inputs failed, status: " + list_model_inputs_response.status.description)

for input_object in list_model_inputs_response.inputs:
    print(input_object)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}/inputs`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Get Model Training Inputs By Version

You can also list all the inputs that were used to train a specific model version.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiInputResponse listModelInputsResponse = stub.listModelInputs(
    ListModelInputsRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")
        .build()
);

if (listModelInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List model inputs failed, status: " + listModelInputsResponse.getStatus());
}

List<Input> inputs = listModelInputsResponse.getInputsList();
for (Input input : inputs) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListModelInputs(
    {
        model_id: "petsID",
        version_id: "{YOUR_MODEL_VERSION_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List model inputs failed, status: " + response.status.description);
        }

        for (const input of response.inputs) {
            console.log(JSON.stringify(input, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_model_inputs_response = stub.ListModelInputs(
    service_pb2.ListModelInputsRequest(
        model_id="petsID",
        version_id="{YOUR_MODEL_VERSION_ID}"
    ),
    metadata=metadata
)

if list_model_inputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(list_model_inputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(list_model_inputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(list_model_inputs_response.outputs[0].status.details))
    raise Exception("List model inputs failed, status: " + list_model_inputs_response.status.description)

for input_object in list_model_inputs_response.inputs:
    print(input_object)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID/versions/{YOUR_MODEL_VERSION_ID}/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'
const modelVersionId = '{MODEL_VERSION_ID}'

const requestOptions = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}/versions/${modelVersionId}/inputs`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Delete A Model

You can delete a model using the model\_id.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteModelResponse = stub.deleteModel(
    DeleteModelRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (deleteModelResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete model failed, status: " + deleteModelResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteModel(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete model failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_model_response = stub.DeleteModel(
    service_pb2.DeleteModelRequest(model_id="petsID"),
    metadata=metadata
)

if delete_model_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(delete_model_response.outputs[0].status.code))
    print("\tDescription: {}".format(delete_model_response.outputs[0].status.description))
    print("\tDetails: {}".format(delete_model_response.outputs[0].status.details))
    raise Exception("Delete model failed, status: " + delete_model_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'

const requestOptions = {
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Delete A Model Version

You can also delete a specific version of a model with the model\_id and version\_id.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteModelVersionResponse = stub.deleteModelVersion(
    DeleteModelVersionRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")
        .build()
);

if (deleteModelVersionResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete model version failed, status: " + deleteModelVersionResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteModelVersion(
    {
        model_id: "petsID",
        version_id: "{YOUR_MODEL_VERSION_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete model version failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_model_version_response = stub.DeleteModelVersion(
    service_pb2.DeleteModelVersionRequest(
        model_id="petsID",
        version_id="{YOUR_MODEL_VERSION_ID}"
    ),
    metadata=metadata
)

if delete_model_version_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(delete_model_version_response.outputs[0].status.code))
    print("\tDescription: {}".format(delete_model_version_response.outputs[0].status.description))
    print("\tDetails: {}".format(delete_model_version_response.outputs[0].status.details))
    raise Exception("Delete model version failed, status: " + delete_model_version_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/petsID/versions/{YOUR_MODEL_VERSION_ID}
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'
const modelVersionId = '{MODEL_VERSION_ID}'

const requestOptions = {
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}/versions/${modelVersionId}`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Delete All Models

If you would like to delete all models associated with an application, you can also do that. Please proceed with caution as these cannot be recovered.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteModelsResponse = stub.deleteModels(
    DeleteModelsRequest.newBuilder()
        .setDeleteAll(true)
        .build()
);

if (deleteModelsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete models failed, status: " + deleteModelsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteModels(
    {delete_all: true},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete models failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_models_response = stub.DeleteModels(
    service_pb2.DeleteModelsRequest(delete_all=True),
    metadata=metadata
)

if delete_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(delete_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(delete_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(delete_models_response.outputs[0].status.details))
    raise Exception("Delete models failed, status: " + delete_models_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/models/
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'

const requestOptions = {
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Train A Model

When you train a model, you are telling the system to look at successfully indexed images with concepts you've provided and learn from them. This train operation is asynchronous. It may take a few seconds for your model to be fully trained and ready.

_Note: you can repeat this operation as often as you like. By adding more images with concepts and training, you can get the model to predict exactly how you want it to._

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

SingleModelResponse postModelVersionsResponse = stub.postModelVersions(
    PostModelVersionsRequest.newBuilder()
        .setModelId("petsID")
        .build()
);

if (postModelVersionsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model versions failed, status: " + postModelVersionsResponse.getStatus());
}

String modelVersionId = postModelVersionsResponse.getModel().getModelVersion().getId();
System.out.println("New model version ID: " + modelVersionId);
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelVersions(
    {model_id: "petsID"},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model versions failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_versions = stub.PostModelVersions(
    service_pb2.PostModelVersionsRequest(
        model_id="petsID"
    ),
    metadata=metadata
)

if post_model_versions.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_model_versions.outputs[0].status.code))
    print("\tDescription: {}".format(post_model_versions.outputs[0].status.description))
    print("\tDetails: {}".format(post_model_versions.outputs[0].status.details))
    raise Exception("Post model versions failed, status: " + post_model_versions.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  https://api.clarifai.com/v2/models/petsID/versions
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const appId = '{YOUR_APP_ID}'
const modelId = '{MODEL_ID}'

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  }
};

fetch(`https://api.clarifai.com/v2/users/me/apps/${appId}/models/${modelId}/versions`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## Predict With A Model

Once you have trained a model you are ready to use your new model to get predictions. The predictions returned will only contain the concepts that you told it to see.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("petsID")
        .setVersionId("{YOUR_MODEL_VERSION_ID}")  // Optional. Defaults to the latest version.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder().setUrl("https://samples.clarifai.com/metro-north.jpg")
                )
            )
        )
        .build()
);

if (postModelOutputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model outputs failed, status: " + postModelOutputsResponse.getStatus());
}

// Since we have one input, one output will exist here.
Output output = postModelOutputsResponse.getOutputs(0);

System.out.println("Predicted concepts:");
for (Concept concept : output.getData().getConceptsList()) {
    System.out.printf("%s %.2f%n", concept.getName(), concept.getValue());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelOutputs(
    {
        model_id: "petsID",
        version_id: "{YOUR_MODEL_VERSION_ID}",  // This is optional. Defaults to the latest model version.
        inputs: [
            {data: {image: {url: "https://samples.clarifai.com/metro-north.jpg"}}}
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model outputs failed, status: " + response.status.description);
        }

        // Since we have one input, one output will exist here.
        const output = response.outputs[0];

        console.log("Predicted concepts:");
        for (const concept of output.data.concepts) {
            console.log(concept.name + " " + concept.value);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="petsID",
        version_id="{YOUR_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        ]
    ),
    metadata=metadata
)
if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_model_outputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_model_outputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_model_outputs_response.outputs[0].status.details))
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# Since we have one input, one output will exist here.
output = post_model_outputs_response.outputs[0]

print("Predicted concepts:")
for concept in output.data.concepts:
    print("%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/puppy.jpeg"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/petsID/outputs

# Model version defaults to latest. If you want to specify the model version, use this URL:
# https://api.clarifai.com/v2/models/petsID/versions/{YOUR_MODEL_VERSION_ID}/outputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/puppy.jpeg"
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

// NOTE: MODEL_VERSION_ID is optional, you can also call prediction with the MODEL_ID only
// https://api.clarifai.com/v2/models/{YOUR_MODEL_ID}/outputs
// this will default to the latest version_id

fetch("https://api.clarifai.com/v2/models/petsID/versions/{MODEL_VERSION_ID}/outputs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(JSON.parse(result, null, 2).outputs[0].data))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Search Models By Name And Type

You can search all your models by name and type of model.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import java.util.List;

// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiModelResponse postModelsSearchesResponse = stub.postModelsSearches(
    PostModelsSearchesRequest.newBuilder()
        .setModelQuery(
            ModelQuery.newBuilder()
                .setName("gen*")
                .setType("concept")
        )
        .build()
);

if (postModelsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post models searches failed, status: " + postModelsSearchesResponse.getStatus());
}

List<Model> models = postModelsSearchesResponse.getModelsList();
for (Model model : models) {
    System.out.println(model);
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelsSearches(
    {
        model_query: {
            name: "gen*",
            type: "concept"
        }
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model searches failed, status: " + response.status.description);
        }

        const models = response.models;
        for (const model of models) {
            console.log(JSON.stringify(model, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://old-docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_models_searches_response = stub.PostModelsSearches(
    service_pb2.PostModelsSearchesRequest(
        model_query=resources_pb2.ModelQuery(
            name="gen*",
            type="concept"
        )
    ),
    metadata=metadata
)

if post_models_searches_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_models_searches_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_models_searches_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_models_searches_response.outputs[0].status.details))
    raise Exception("Post models searches failed, status: " + post_models_searches_response.status.description)

for model in post_models_searches_response.models:
    print(model)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "model_query": {
      "name": "gen*",
      "type": "concept"
    }
  }'\
  https://api.clarifai.com/v2/models/searches
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "model_query": {
    "name": "gen*",
    "type": "concept"
  }
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
  body: raw
};

fetch("https://api.clarifai.com/v2/models/searches", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

