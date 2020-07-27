# Model Types

This page describes some important model types that you should know when working with the Clarifai platform. Please keep in mind that this is an overview of the general categories of models available to you. New models are created all the time. For the most up-to-date list of available models, visit Model Mode in Portal.

## Classification

Classification models help you answer the question "What" or "Who" is in your data. Classification models understand the world in terms of [concepts](https://docs.clarifai.com/api-guide/concepts). Models can come pre-trained to recognize concepts, or you can create your own custom models to recognize custom concepts.

Example use case:

A large retailer looking to find and remove listings for illegal objects and substances across thousands of listings that include user-generated data. A classification model allows the retailer to quickly find listings that are in violation of their community rules, and remove them from the site.

## Detection

Detection models answer the question "Where" are objects in your data. Detectors can come pre-trained to detect specific objects, or you can train your own custom detectors to detect your own custom list of objects.

Example use case:



## Embedding

Embedding models don't answer a specific question. Instead, embedding models contain the

The "learnings" from machine learning models can be saved and transferred to new models, or used for other forms of visual analysis. This is what the Embedding model type is all about. Embeddings can provide the foundations for new custom models, or can be used to power visual search.



## Deep Trained Models

Use deep trained models when you want to build models that have their own custom embeddings, concepts and/or detections.


## Models that modify, connect or extend other models

### Context-Based Classifier

The context-based classifier

### Cluster

Allows a user to detect an object or subject in different scenarios and settings, and then define the object. DST is not required for training these kinds of models because they are built by our Field Engineering and Backend teams. | “I will use this image of a giraffe to find other giraffes”



### Fixed-Function Operators
