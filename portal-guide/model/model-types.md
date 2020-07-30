# Model Types

This page describes some important model types that you should know when working with the Clarifai platform. Please keep in mind that this is an overview of the general categories of models available to you. New models are created all the time. For the most up-to-date list of available models, visit Model Mode in Portal.

## Trainable Models

### Classification

Classification models help you answer the question "What" or "Who" is in your data. Classification models understand the world in terms of [concepts](https://docs.clarifai.com/api-guide/concepts). Models can come pre-trained to recognize concepts, or you can create your own custom models to recognize custom concepts.

Example use case:

A large retailer looking to find and remove listings for illegal objects and substances across thousands of listings that include user-generated data. A classification model allows the retailer to quickly find listings that are in violation of their community rules, and remove them from the site.

### Detection

Detection models answer the question "Where" are objects in your data. Detectors can come pre-trained to detect specific objects, or you can train your own custom detectors to detect your own custom list of objects.

Example use case:

A roofing company wants to provide insurance companies and customers with a consistent way of evaluating roof damage. This company captures images of roofs with a drone, and then feeds the images into a detection model. The detection model can then locate and classify specific areas of damage on the roofs.

### Embedding

Embedding models don't answer a specific question. Instead, they help you work with something that is a little more abstract: the underlying *structure* of a classification or detection model. In fact, you can think of an embedding model as a classification or detection model with the concepts removed, because in many cases this is exactly what an embedding model is. Embedding models are important because they help you transfer the learnings from existing models to your own custom models. This means that you can come up with your own set of custom concepts and quickly train a new model with relatively few training samples.

{% hint style="info" %}
Embeddings also can be combined with cluster models to provide a fast and efficient way to search your data based on *visual similarity*.
{% endhint %}

Example use case:

A security company wants to use face verification as part of their two-factor identification system. They would begin by using Clarifai's face embedding model, and then training this model to recognize the identities of permitted individuals. They would simply upload images of the people that want to identify, add individual names as concepts, and train the new model using a *Context-Based Classifier*.

### Deep Trained Models

Use deep trained models when you are working with highly specialized data, or you want to push the accuracy of your model to its limits for a specific use case. Deep training builds a custom neural network for your application from the ground-up. This means that your model can become an expert in recognizing the unique set of visual features that is important in your data set.

Example use case:

A radiology laboratory is training a model to detect COVID-19 in patients based on their chest x-rays. They need to push model accuracy to its absolute limit to reduce false positives. Their dataset is also highly specialized and technical in nature. They would typically choose to a deep trained model to get the best results.

## Models that modify, connect or extend other models

### Context-Based Classifier

The Context-Based Classifier is the key to transfer learning and custom model building on the Clarifai platform. The context based classifier can learn new concepts and create new custom models out of existing models.

Example use case:

A retailer wants to train a model that can recognize their apparel in use on social media. They would use a context-based classifier in conjunction with Clarifai's apparel model to train a new custom model that will recognize clothing items produced by their brand.

### Cluster

Cluster models work with Embedding models so that you can perform visual searches. Cluster models are able to use the mathematical structure of a model's embedding to determine which images are "clustered together" in the embedding space. This means that you can search for visually similar people or objects in your dataset quickly and easily, without the need for labeling and training custom concepts.

Example use case:

An online retailer wants to suggest relevant products based on visual similarity to products that customers have previously purchased. They would use a cluster model together with an embedding model, and perform a "visual search" on their catalog to identify similar items.

### Fixed-Function Operators

Fixed-Function Operators are "non-trainable models" that help you connect, direct, and network your models in a workflow. Some of our most popular operators are used for random sampling, routing based on predictions and image cropping. 

Example use case:

A customer wants to automatically tag images based on AI predictions. They would might connect a classification model with a "Concept Thresholder" model to determine which images are labeled and which ones are not.
