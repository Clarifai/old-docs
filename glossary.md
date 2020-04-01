### Application 
An application is a kind of self-contained project for managing data, annotating, modeling, predicting and searching. An operation performed in one application will return results from data within that application but will be blind to data in other applications. You can create as many applications as you like and can divide your use among them to segment data into collections and manage access accordingly.
### Concept 
A concept is something that describes an entity in the physical world, similar to a “tag” or “keyword”. You can use a concept to annotate an input if that input has that entity. You can also add it to a model if you want that model to be able to recognize that entity. 
### Embeddings 
A low-dimensional representation of a model’s input that has rich semantic information.
### Portal 
Portal is a web application that allows you to preview your Clarifai apps. You can view all the inputs you have added, perform searches, and train new models.
### Input 
An input, usually an image or video, is the data you're providing into the platform. Inputs and their predictions are indexed so that they can be used for search. You can also add your own concepts to inputs to use when training your own model. 
### Output
On output, usually in the form of a prediction or predictions, is the data returned to you when you send an input into a model. Because of their close relationship, the terms "outputs" and "predictions" are sometimes used interchangeably. 
### Indexing
Indexing collects, parses, and stores your inputs to facilitate fast and accurate information retrieval. Indexing happens automatically every time you add new inputs to your app. Indexing enables responsive visual search, data clustering, concept search and model training.
### Model 
Models convert inputs to outputs. Clarifai provides many different models that each ‘see’ the world differently - with a unique group of concepts. Clarifai has built some great models for you use, but there are times when you wish you had a model that sees the world the way you see it, with your own concepts. You can use your own model by adding images with concepts, training it, and then specifying it when making predictions.
### Operation 
An Operation is an action that is performed via our API or User Interface. It can include actions such as predictions, searches, input uploads, training custom models, model evaluations and more.
### Prediction 
A prediction is an answer to the question “What can you tell me about this input?”. When you call predict on an input, you will receive one or more predictions of different concepts that apply to that image. Predictions vary based on the concepts included in a given model.
### Search 
All of the images in your app are indexed by both the concepts applied by the app’s default model, and by their own visual properties. Search, in the context of Clarifai, refers to finding relevant images in your app by text (match concepts), reverse image search (similar-looking images), or both.
### Train 
Train is when you update a model to “learn” from all the annotated concepts on your inputs. Any time you add or update image concepts, you can use train again to create a new model version, fit to the latest information.
### Workflow 
Workflows enables users to make predictions on one or more pre-trained or custom models, with a single API call.
