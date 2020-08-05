# Training Data

AI requires high quality training data. Training data is used to "teach" AI models how to understand the world. Models

## Quality and quantity



## Organize your data in a way that AI can understand

A training set refers to the data that is used as inputs for concepts in a model. A “good” training set will set the model to make predictions as closely to the world as the user sees it as possible.  

Data quality

1) Visually adheres to concept descriptions laid out in a taxonomy.
2) Reflects the expected user’s data for model’s intended use case.

Data quantity

More data means more examples from your model to learn from.



### A cautionary tale: The importance of representative data

An international beer company wanted to build a “Perfect Pint” model as part of a promotional campaign. The model was meant to analyze a photo of a pint of beer, and judge how well it had been poured and presented (this particular brand puts a strong emphasis on the importance of pouring beer with the ideal amount of "head", or foam, on top).

The client had a few thousand images of professionally photographed pints of beer to use as training data. The images represented their beer in different stages of pour appearance on bar tops, taken in daylight and/or professional lighting.  

The initial version of their model struggled to perform effectively in production. Even though their training data provided many examples of the object that they wanted to analyze, the qualitative appearance of their training data did not capture the appearance of their beer in diverse real-world environments.

They needed to provide training data that captured:
1) The breadth of real world scenarios
2) The quality of user generated images

After applying these changes, the model performance improved.
