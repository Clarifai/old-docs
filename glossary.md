### Application 
An application is a kind of self-contained workspace for your search indexes and custom models. A search performed in one application will return results from images within that same application, but will be blind to those in other applications. You can create as many applications as you like, and can divide your use among them to segment data into collections and manage access accordingly.
### Concept 
A concept is something that describes an input, similar to a “tag” or “keyword.” There are two types of concepts - those that you specify to train a model, and those that a model assigns as a prediction.
### Embeddings 
A low-dimensional representation of a model’s input that has rich semantic information.
### Portal 
Portal is a web application that allows you to preview your Clarifai apps. You can view all the inputs you have added, perform searches, and train new models.
### Input 
An input, usually an image, is the thing you’re trying to learn about. You send inputs to a given model, and Clarifai returns predictions. You can “save” inputs and their predictions to search against later. You can also add your own concepts to inputs to use when training your own model.
### Model 
Models convert inputs to predictions. Clarifai provides many different models that each ‘see’ the world differently - with a unique group of concepts. Clarifai has built some great models for you use, but there are times when you wish you had a model that sees the world the way you see it, with your own concepts. You can use your own model by adding images with concepts, training it, and then specifying it when making predictions.
### Operation 
An Operation is an action that is performed via our API or User Interface. It can include actions such as predictions, searches, input uploads, training custom models, model evaluations and more.
### Prediction 
A prediction is Clarifai’s answer to the question “What can you tell me about this input?”. When you call predict on an image, you will receive one or more predictions of different concepts that apply to that image. Predictions vary by model, which you can learn more about in this glossary.
### Search 
All of the images in your app are indexed by both the concepts applied by the app’s default model, and by their own visual properties. Search, in the context of Clarifai, refers to finding relevant images in your app by text (match concepts), reverse image search (similar-looking images), or both.
### Train 
Train is when you update a model to “learn” from all the image concepts you have provided in your app. Any time you add or update image concepts, you can use train again to create a new model version, fit to the latest information.
### Workflow 
Workflows enables users to make predictions on one or more public/custom models, with a single API call.
