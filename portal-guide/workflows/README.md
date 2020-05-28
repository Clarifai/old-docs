# Workflows

Workflows are a graph of computation that encompass one or more Clarifai or Custom model\(s\). Every workflow is attached to one of your applications. Under each workflow, you will see a list of the Clarifai Models and all custom models in that application when selecting models to add to your workflow. With Workflow Predict, you will be able to run your business logic on one efficient tool.

{% hint style="info" %}
This won't have any impact on the price you are charged per call. You will still be charged for the same operation if it were separate calls to the API. When you do a predict with a workflow you're charged for the prediction of each model in the workflow as if they were separate calls.
{% endhint %}

## Workflow Setup

To set up a workflow, you will need to head over to the [Applications page](https://portal.clarifai.com/apps) through your account. From there, you will need to select which application you want to create the workflow under.

![Image showing the top-level Applications page on the Clarifai Developer website](../images/application-screen-new.png)

Then under that application, you will see a section labeled "App Workflows" and a button to "Create Workflow".

![Image showing My First Application and the Create Workflow button underneath the Create API Key](../images/create-workflow-new.png)

After that, the page will reveal a new workflow form to fill out. Fill out the Workflow ID field, this will be used to make the API call, so make sure to give it something URL friendly! Included there, you will also a list that consists of a model field and a version associated with it. For Clarifai Models, you will be mandated to use the latest version. For your custom models, you will be able to [select the version of your model](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/models.md#list-model-versions)&lt;/a&gt;. To add another model, you will just click underneath your latest addition on the "Add Model". The max limit of models associated with any given workflow is 5 models. If you would like to remove a model, there is a large X that will allow you to remove a model. Once you have finished adding everything, press the "Save Workflow" button and that will save the state of your workflow. Now you are ready to predict using your brand new workflow. You can edit a given workflow at any time, in case you don't like it.

![Image showing a list of models \(Moderation and General\) under a workflow with the name my-workflow](../images/my-workflow-new.png)
