---
description: Dynamic AI model orchestration and inference scaling
---

# Making Predictions

The Predict API analyzes your images or videos and tells you what's inside of them. The API will return a list of concepts with corresponding probabilities of how likely it is these concepts are contained within the image.

![](../../.gitbook/assets/armada.svg)


We recommend specifying the `version_id` parameter in your predict calls. If no `version_id` is specified, predictions will occur on the most recent version of the model. This helps when you want to run a specific version of your model in production while building future versions of your model. This is also true with Clarifai's pre-trained models, as we will update them to have new versions from time to time. Therefore using a specific version\_id keeps your production environment stable.


![](../../.gitbook/assets/predict.jpg)

