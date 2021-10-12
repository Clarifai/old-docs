# Collectors

## What are Collectors and why are they useful

> Collectors are available with Professional and Enterprise plans to help you manage data ingestion at scale.

An AI model is only as good as the data that it is trained on. However, it is not always possible to have enough data, or data with proper rights to train such a good model. It is here that Collectors become extremely useful.

Collectors capture input data for your app. They enable you to pipe in data from production models automatically, and you can use this data to further refine your models. You can create app-level collectors to monitor specific models and specify sampling rules for triggering data ingestion. Collectors can only collect data from apps where you are the app owner.

Collectors are available with Essential and Enterprise plans


### Creating a new collector

Collectors help you to feed your models with real-world training data. This data can be taken from models that you have already deployed to production. Just create a collector within your app and set it up to ingest data from another model when new inputs are "posted" to this model.


### Step 1: Create a sampler model and put it in a workflow
The first thing to do here is to create a Random sampler. The purpose of this model is to collect (sample) data based on the fraction or proportion that
we set. This would be a custom model and you can find it under **Create Custom Model** tab of Model Mode. The model type for this would be **Random Sampler**

Give this model a name and choose what percentage (fraction) of data you want to collect. The range runs from 0 to 1.0. 0 means that no data will be collected
and 1.0 means that any images sent for prediction to your custom model in production will be collected.

Creating the model in Model would the involve
1. Picking the Random Sampler Model Type.
2. Giving it the percentage of images to collect.

![model model screen showing random sampler](images/random_sampler_model_mode.png)

![creating a random sampler with args](../../images/random_sample_args.png)

### Step 2: Put the sampler in a workflow

Once the model is created you will just put that model in a workflow. In the Model Mode screen, use the Create Workflow tab. Under your user you should be able to see the sampler model you created. Add that model to the workflow, give the workflow a descriptive name and hit **Create Workflow**

![image showing a pre-queue workflow being created](images/random_sampler_preQ.png)

### Step 3: Create a Collector
Under Data Mode, at the bottom you should see the option to create new collectors. When you are creating a new screen you will see a screen like this
![](../../../.gitbook/assets/create_new_collector.jpg)


#### Collector ID

Give your collector a useful and descriptive name.

#### Description

Provide additional details about your collector.

#### Pre-queue workflow

We will use the workflow we created in step 2 as the pre-queue workflow

#### Post Inputs key

Select the API key that you would like to use to allow new inputs to be posted to your app. This is the post-queue workflow ID of the workflow to run to after the collector is processing the queued input. This API key must have the PostInputs scope, since it grants the collector the authority to POST inputs to your app.

This workflow uses the original input to the model as input to the workflow so that you can run additional models as well on that input to decide whether to queue the model or not. If the workflow output has any field that is non-empty then it will be passed on to POST /inputs to the destination app. At least one \(pre-queue or post-queue\) workflow ID is required.

#### Caller
**Any Caller** means that any API call from any user made to your model will get collected. You could also specify a specific user id you want to collect against.

#### Source

Select the model that you would like to collect from, and the collector will automatically post the new inputs to your app. Simply enter your model name, or model ID number. You can select the model that you would like to collect from in the drop down menu. When the user predicts an input against this model, the input is going to be collected.

The app ID and user ID where the model is located. If using a publicly available model, the model user and app ID should be `clarifai` and `main`, respectively. Otherwise the IDs should belong to the user who created the model. An API key ID using which the inputs are is going to be added.
