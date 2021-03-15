---
description: Learn the basics of setting up a new workflow.
---

# Setting Up a Mesh Workflow

Workflows are a graph of computation that encompass one or more Clarifai or Custom model\(s\). Every workflow is attached to one of your applications. Under each workflow, you will see a list of the Clarifai Models and all custom models in that application when selecting models to add to your workflow. With Workflow Predict, you will be able to run your business logic on one efficient tool.

{% hint style="info" %}
This won't have any impact on the price you are charged per call. You will still be charged for the same operation if it were separate calls to the API. When you do a predict with a workflow you're charged for the prediction of each model in the workflow as if they were separate calls.
{% endhint %}

## Workflow Setup

To set up a workflow, you will need to head over to the [Applications page](https://portal.clarifai.com/apps) through your account. From there, you will need to select which application you want to create the workflow under.

![AI Applications](../../.gitbook/assets/application-screen-new%20%282%29%20%281%29.png)

Then click on the model mode icon in the lefthand sidebar. From here, click the "Create Workflow" button at the top righthand corner of the screen.

![AI model gallery](../../.gitbook/assets/create-workflow-new%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%284%29%20%285%29%20%285%29%20%282%29.png)

### Create a Workflow

To create a custom workflow, just click the "ADD" button next you the model you would like to add. You will see the model displayed in the "Selected Models" section below. You can use the dropdown menu on the left hand side of the screen to filter through your available models:

_Workflow ID_ - Provide a descriptive name for your workflow. This ID will be used to make the API call, so make sure to give it something URL-friendly.

_User_ - Filter your models by user ID. Be sure to select "Clarifai" if you would like to choose a Clarifai Model.

_APP_ - Filter your models based on their app.

_Inputs_ - Filter your models based on the type if input that they accept.

_Outputs_ - Filter your models based on the type of output that they return.

Once added you can configure your input nodes for each model. Model outputs vary based on the type of model that you are working with.

{% hint style="info" %}
For Clarifai Models, you will be able to use the latest version. For your custom models, you can select the version of your model.
{% endhint %}

You can add up to 20 models to a single workflow. Once you have finished adding everything, press the "Save Workflow" button and that will save the state of your workflow. Now you are ready to predict using your brand new workflow. You can edit a workflow at any time.

![Create a workflow](../../.gitbook/assets/my-workflow-new%20%282%29%20%282%29%20%282%29%20%282%29%20%281%29.png)

