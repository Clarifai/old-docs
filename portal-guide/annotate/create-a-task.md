---
description: Manage and delegate your labeling work with tasks.
---

# Create a Task

{% embed url="https://youtu.be/7AQLsVq5RLQ" caption="Clarifai Scribe: Creating Tasks" %}

Tasks enable you delegate labeling jobs to your team.

![](../../.gitbook/assets/task_overview%20%281%29%20%281%29.jpg)

## Task Name and Instructions

Provide your task with a descriptive name and provide instructions for your labelers. You can even provide you labelers with a "visual dictionary" by including sample image URLs.

## Task Types

Choose the type of label that you would like your worker to add to your images or video. You can choose classification, bounding box detection, polygon detection label types.

Please note that if you want to create a detection labeling task, you will need to select a detection model as the base workflow in your app.

## Applicable Concepts

Concepts are the words that you are labeling your data with. Concepts can be anything you can think of, and can be written in the language of your choice. You can create concepts in Portal, or you can create them when assigning tasks. Check the "Select all concepts" box to automatically add all available concepts to your app.

## Input Sources

You can choose "All inputs", which will include all inputs from your dataset, or you can choose any one of your [Saved Searches](../psearch/psaved_searches.md).

By saving your searches, you can slice and dice your dataset, and configure dynamic and static types of datasets. You can also create highly customized filters to your data, by adding metadata and searching by metadata filtering.

## Workers

You can assign work to a worker, or group of workers. Simply add the worker email addresses and workers will receive an email notification and a new task will be added to their "Assigned to Me" tab.

## Worker Strategy

Manually assign work to a specific person, or have work randomly assigned to workers from a group of collaborators. By selecting "Full", all inputs will be assigned to each worker. By selecting "Partition" you will be able to break up your labeling task amongst your workers.

## Review Strategy

### None

All labels will be automatically marked with a "Success" status and can be immediately used to train your new model.

### Manual

Labels will be marked with a "Pending Review" status until the assigned reviewer approves them. These labels cannot be used to train new models until approved.

### Consensus \(Coming soon!\)

Consensus review will mark labels with "Success" status in cases where multiple reviewers provide the same label.

## Sample Size to Select for Manual Review

You can choose to review all or part of a workers labels. Simply adjust the slider, and you will review a random subset of their labeled images. For example, if a worker is labeling 10,000 images, you might choose to review 1% of them for quality control.

## Reviewers

You assign reviewers by adding their email. Assigned review tasks will show up in the "For Review" tab.

## Enable AI Assist

Enable AI-assisted workflow predictions in your labeling project. You must first create a workflow with a custom model to enable predictions.

## Video FPS

Select your preferred video sample rate. This is the integer value that represents the number of frames that we can capture per second. We do not currently sample video at fractional frame rates.

