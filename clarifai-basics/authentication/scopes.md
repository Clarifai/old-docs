# Scopes

Scopes provide control over the set of functionality and features available when using our API. Modifying scopes allows for fine-grained control over the data that users have access to, and can help keep your app secure from malicious attacks.

You can control scopes for our apps at three different levels:

**App-Specific API Keys** Control access to resources used by a specific app and a specific user

**Personal Access Tokens** Control access to resources available to a specific user

**Collaboration** Control access to resources available to collaborators

## Combining Scopes

A variety of use cases can be address by selecting different combinations of scopes.

For example, you might want to create an app that only has access to the search endpoint, but for search to work properly it needs access to Predict at the operation level \(so that it can perform advanced visual searches like searching by an image crop, which first needs to be understood with a prediction before search is performed\).

By giving the combination of predict op-level but only search endpoint, you can create an app that can perform searches, but not model predictions \(like PostModelOutputs\).


Since collaborators need to create an API key to access the app they are invited to \(or use a PAT\), the scopes that are attached to the collaborator invite for an app will be intersected with the scopes attached to the API key or PAT. Therefore, the permissions allowed when making requests will be the minimum set of scopes from that intersection. This ensures that the app owner remains in full control of the permissions they want their collaborators to have.


## Operations and Endpoints

You have control over both operation and endpoint level scopes.

### Operation Level Scopes

Operation level scopes provide control over the ability to read, write, or delete a given resource type. To see the always up to date list of operation level scopes avilable in your plan create a key in Portal.

**Annotation**

* Annotations:Add \(Write Annotations\)
* Annotations:Delete \(Delete Annotations\)
* Annotations:Get \(Read Annotations\)

**Concept**

* Concepts:Add \(Write Concepts\)
* Concepts:Get \(Read Concepts\)

**Input**

* Inputs:Add \(Write Inputs\)
* Inputs:Delete \(Delete Inputs\)
* Inputs:Get \(Read Inputs\)

**Model**

* Models:Add \(Write Models\)
* Models:Delete \(Delete Models\)
* Models:Get \(Read Models\)
* Models:Train \(Train a Custom Model\)

**Predict**

* Predict \(Predict on Public and Custom Models\)

**Search**

* Search \(Search by Inputs and Concepts\)

**Workflow**

* Workflows:Add \(Write Workflows\)
* Workflows:Delete \(Delete Workflows\)
* Workflows:Get \(Read Workflows\)

### Endpoint level scopes

Endpoint level scopes give you control over access to specific endpoints. To see the always up to date list of endpoint level scopes available in your plan create a key in Portal.

**Concept**

* /clarifai.api.V2/GetConcept
* /clarifai.api.V2/GetConceptCounts
* /clarifai.api.V2/ListConcepts
* /clarifai.api.V2/PatchConcepts
* /clarifai.api.V2/PostConcepts
* /clarifai.api.V2/PostConceptsSearches

**Input**

* /clarifai.api.V2/DeleteInput
* /clarifai.api.V2/DeleteInputs
* /clarifai.api.V2/GetInput
* /clarifai.api.V2/GetInputCount
* /clarifai.api.V2/ListInputs
* /clarifai.api.V2/ListModelInputs
* /clarifai.api.V2/PatchInputs
* /clarifai.api.V2/PostInputs

**Model**

* /clarifai.api.V2/DeleteModel
* /clarifai.api.V2/DeleteModelVersion
* /clarifai.api.V2/DeleteModels
* /clarifai.api.V2/GetModel
* /clarifai.api.V2/GetModelOutputInfo
* /clarifai.api.V2/GetModelVersion
* /clarifai.api.V2/GetModelVersionMetrics
* /clarifai.api.V2/ListModelVersions
* /clarifai.api.V2/ListModels
* /clarifai.api.V2/PatchModels
* /clarifai.api.V2/PostModelVersionMetrics
* /clarifai.api.V2/PostModelVersions
* /clarifai.api.V2/PostModels
* /clarifai.api.V2/PostModelsSearches

**Predict**

* /clarifai.api.V2/PostModelOutputs
* /clarifai.api.V2/PostWorkflowResults

**Search**

* /clarifai.api.V2/PostSearches

**Workflows**

* /clarifai.api.V2/DeleteWorkflow
* /clarifai.api.V2/DeleteWorkflows
* /clarifai.api.V2/GetWorkflow
* /clarifai.api.V2/ListWorkflows
* /clarifai.api.V2/PatchWorkflows
* /clarifai.api.V2/PostWorkflows

