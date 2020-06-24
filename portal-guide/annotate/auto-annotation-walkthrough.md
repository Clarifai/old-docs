# Auto Annotation Walkthrough

This tutorial demonstrates how auto-annotation workflows can be configured within Clarifai Portal.

Inputs are automatically annotated with concepts and assigned `SUCCESS` status by leveraging the high confidence predictions of a model, and when the model is unsure, the annotation is going to be written as you with `PENDING` status. This enables you to scale up your annotation process while ensuring quality standards by including a backstop of human review.


### Create Concepts, Label and Train a Custom Model

To begin, create your application and upload your inputs.

![](../../images/create_auto_annotation_demo.jpg)

![](../../images/auto_annotation_app_details.jpg)

Upload files from your computer, or add image and video URLs.

![](../../images/add_inputs_auto_demo.jpg)

Create the concepts that we'll be using in our model, by clicking create new concept in the lefthand sidebar. In this tutorial we'll create concepts that describe people based on activities they do in the park: `walker`, `runner`, `bike_rider`, `rollerblader` and `stroller`.

![](../../images/create_concepts_auto_a.jpg)

Label your inputs with the appropriate concepts by clicking the checkmark box.

![](../../images/label_inputs_aa.jpg)

### Navigate to the Model Gallery

Now it is time to create some custom models.

![](../../images/model_gallery.jpg)

### Create a Context-Based Classifier

![](../../images/create_cbc_aa.jpg)

### Create a "greater than" Concept Thresholder model

![](../../images/train_cbc_aa.jpg)


### Create a "less than" Concept Thresholder model

![](../../images/concept_thresholder.jpg)


### Create a "write success as me" Annotation Writer model

![](../../images/annotation_writer.jpg)



### Create the workflow

We will now join all the models together into a single workflow.

Every input will be predicted by General Embed model to generate embedding. The output of the embed model (embeddings) will be sent to general concept to predict concept and cluster model. Then the concept model's output (a list of concepts) will be sent to concept mapper model which maps Clarifai concept to your concept, `people`, `man` and `adult` in this case. Then the mapped concepts will be sent to both concept thresholds models (`GREATER THAN` and `LESS THAN`). `GREATER THAN` model will filter out the concept if it lower than corresponding value you defined in model and send the final concept list to `write success as me` model which labels the input with these concepts (your app concepts only) as you with `success` status. You can train or search on these concepts immediately. The `LESS THAN` model will filter out the concept if it is higher than the corresponding value you defined and send the final concept list to `write pending as me` model which labels the input with these concepts (your app concepts only) as you with `pending` status.

The model IDs and model version IDs from the public `clarifai/main` application are fixed, so they are already hard-coded in the code examples below. It's possible to use other public model or model version IDs.

![](../../images/create_workflow_aa.jpg)

![](../../images/connect_nodes_aa.jpg)



### Make the new workflow your app's default

Make this the default workflow in the app, so it will run every time we add an input and execute the auto annotation process.

![](../../images/set_as_default.jpg)


### Add an image

Adding the image will trigger the default workflow.

![](../../images/add_additional_inputs.jpg)


### View Annotations in Explorer

Now you can view your annotations in Explorer. Just drag your mouse over the "tag" icon to see annotations associated with the image.

![](../../images/aa_inputs.jpg)
