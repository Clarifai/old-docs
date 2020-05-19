Tasks enable you delegate labeling jobs to your team.

## Task types

Choose the type of label that you would like your worker to add to your images or video. You can choose classification, bounding box detection, polygon detection label types.

Please note that if you want to create a detection labeling task, you will need to select a detection model as the base workflow in your app.


## Input sources

You can choose "All inputs", which will include all inputs from your dataset, or you can choose any one of your [Saved Searches](https://docs.clarifai.com/v/v6.1/portal-guide/psearch/psaved_searches).

By saving your searches, you can slice and dice your dataset, and configure dynamic and static types of datasets. You can also create highly customized filters to your data, by adding metadata and searching by metadata filtering.

## Applicable concepts

Concepts are the words that you are labeling your data with. Concepts can be anything you can think of, and can be written in the language of your choice. You can create concepts in Portal, or you can create them when assigning tasks.


## Worker strategy

Manually assign work to a specific person, or have work randomly assigned to a group of collaborators. 

## Workers

You can assign work to a worker, or group of workers. Simply add the worker's email address and the worker will receive an email notification, and will see a new Task under the "assigned to me" tab.

## Review strategy
### None

All labels will be automatically marked with a "Success" status and can be immediately used to train your new model.

### Manual

Labels will be marked with a "Pending Review" status until the assigned reviewer approves them. These labels cannot be used to train new models until approved.

### Consensus

Consensus review will mark labels with "Success" status in cases where multiple reviewers provide the same label.

## Sample size to select for manual review

You can choose to review all or part of a workers labels. Simply adjust the slider, and you will review a random subset of their labeled images. For example, if a worker is labeling 10,000 images, you might choose to review 1% of them as a quality control  measure.

## Reviewers

You assign reviewers by adding their email. Assigned review tasks will show up in the "For Review" tab.

## Enable workflow predictions

Enable AI-assisted workflow predictions in your labeling project. You must first create a workflow with a custom model to enable predictions.

## Video FPS

Select your preferred video sample rate.
