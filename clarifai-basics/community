---
description: We make our platform open for community to discover, test, use and share models and workflow (apps and datasets are coming soon) with Clarifai community.
---

# Clarifai Community Quick Start

Access to our “AI lake” of pre-trained models and workflows including high quality models built by Clarifai, Hugging Face, Google and other top contributors.
Use community resources as building blocks as you develop amazing things with our no code/low code end-to-end AI platform

You can still use current portal as development GUI-based IDE and use community as "GitHub" on top of the IDE (models & workflows are synced with community profile)

## Step 1: Browse and Search (No Login Needed)

On the community page, click on “Featured” in the top left corner. This will present the main page of the community, where you can view the news and featured models at the top of the page.

## Step 2: Check Model Card and Test Predictions (Test Requires Login - Give Yourself A Cool User Id)

Select a model from the “Featured Models”. In the video, we selected “clarifai/main/general”, which is a general purpose classifier that will work on a huge range of subject matters.

* The default photo shown in the video is of a group of people, and you can view the predictions and their probabilities on the right.
* To try your own photo, click the “Try Your Own Input” button under the predictions.
* Select your own photo to upload; in the video we see a happy couple and all the concepts identified in the photo.
* You can click “View JSON” underneath the “Try Your Own Input”  button to view the JSON returned by the model for programmatic use.
* Click on the “Community” link and select “Models” underneath it to view published models on the platform. On the right side of the screen there are a number of checkboxes under “Filters” that allow filtering by model INPUT TYPE. Select image.
* Below INPUT TYPE is a section for MODEL TYPE filters. In the video we filter this to a Visual Detector.
* Click on “Models” in the top left of the screen again, and in the search box type “face” to filter the models for face detection.
* Select the model “clarifai/main/Face”. This will open the same default photo of a group of people, and will have bounding boxes around the detected faces. On the right side of the screen you will see the probabilities that the detection is correct, and a preview of the image inside each bounding box.
* Again, as before, you can click on “Try Your Own Input” to upload your own photo to see how the same process works for your own content.

## Step 3: Use Model in API or Add to Workflow

Now we’re going to try to use one of the models we’ve been playing with. Click on “Community” in the top left, then select the “clarifai/main/general” model again.

* Click the “Use Model” button in the top right corner.
* A window will open with our API code that can be used in a program. We’re going to create our own workflow instead, so at the top of this window, where you see “Call by API” and “Use in a Workflow”, select “Use in a Workflow.”
* While the video does have some pre-existing applications in the “Select App” dropdown, you may only have the “my-first-application” if you are using a new account. Select an app, and then select the “Create new workflow” button, and give your workflow a name. In the video we use “general-test2”, but you can name it whatever you want.
* Now that you’ve created a workflow, click on your profile icon in the very top right of the screen. This is a small circle, which will either be your initials or a photo if you’ve uploaded one. This will open your profile page, where you can select “Workflows” and click the workflow you just created.
* You will now be presented with the visual graph, where you can drag and connect components of your workflow.


## Step 4: Check Apps/Models/Workflows under My Profile, and Publish Models

This section shows the relationship between the Clarifai portal and the Clarifai Community.  Think of the portal is being like an IDE where you develop your models, and community as a type of git-like repository where you can publish them.

* The video first checks the Applications page on Portal, where it has a model called “text-moderation-test”.
* Then it switches to Community, and clicks into the Profile link in the top left corner. Notice how the same application, text-moderation-test, is listed under the use profile.
* We then click back into Portal and click on the 4 squares icon on the left, which enters Model Mode.
* Using the dropdown under the Models tab, you can choose either “clarifai” or your username. The “clarifai” option contains all of Clarifai’s pre-trained models, so select your username instead.
* In this case, we select the model “bert-base-uncased-hatexplain”, which is a BERT-based model for NLP classification. It is inside the “text-moderation-test” application.
* We then go back to the Community view, and show that “text-moderation-test” is under the Apps tab, and “bert-base-uncased-hatexplain” under the Models tab.
* Clicking into the “bert-base-uncased-hatexplain” model, we can test it using “Try Your Own Text”. We select “Add Raw Text” so that we can type it in.
* As we see in the results, “you are fine” is classified as normal with a 0.669 probability, and “he is a moron” is classified as offensive with a 0.573 probability.
* Scrolling down, we click the Edit link on the notes, and paste a description of the model in.
* We then use the tags on the right to tag it as “text moderation” under Use Case, and “HuggingFace” under Toolkit.

## Step 5: Checkout Your First Published Model!

We’re ready to publish! Click on “Make Model Public in the top right corner of the model view in Community. You will be presented with a dialog box, where you can change the model visibility to PUBLIC.

* When you set the model to public, your user-id will be set to public, your app-id will be set to public, and all app notes, tags, and descriptions will be made public.
* Choose a version of the model to make public using the dropdown box.
* Switching to the Models view of the Community, you can now search for your model in the text box, or simply refresh the browser to see your model is now listed in the public Models tab.
