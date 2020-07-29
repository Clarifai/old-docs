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
Embeddings also provide a fast and efficient way to search your data based on *visual similarity*.
{% endhint %}

Example use case:




### Deep Trained Models

Use deep trained models when you are working with highly specialized data, or you want to push the accuracy of your model to its limits for a specific use case. Deep training builds a custom neural network for your application from the ground-up. This means that your model can become an expert in recognizing the unique set of visual features that is important in your data set.




## Models that modify, connect or extend other models

### Context-Based Classifier

The Context-Based Classifier is the key to transfer learning and custom model building on the Clarifai platform. The context based classifier can learn new concepts and create new custom models out of existing models.

### Cluster

Allows a user to detect an object or subject in different scenarios and settings, and then define the object. DST is not required for training these kinds of models because they are built by our Field Engineering and Backend teams. | “I will use this image of a giraffe to find other giraffes”


### Fixed-Function Operators

Fixed-Function Operators are "non-trainable models" that help you connect, direct, and network your models when they are connected in a workflow.
