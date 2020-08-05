# Training Data

AI requires high quality training data. Training data is used to "teach" AI models how to understand the world. Models

## Organize your data in a way that AI can understand

A training set refers to the data that is used as inputs for concepts in a model. A “good” training set will set the model to make predictions as closely to the world as the user sees it as possible.

### Data quality

* Visually adheres to concept descriptions laid out in a taxonomy
* Inputs are representative of the expected data for your model’s intended use case

### Data quantity

* More data means more examples from your model to learn from

{% hint style="info" %}
### A cautionary tale: The importance of representative data

[img]

An international beer company wanted to build a “Perfect Pint” model as part of a promotional campaign. The model was meant to analyze a photo of a pint of beer, and judge how well it had been poured and presented (this particular brand puts a strong emphasis on the importance of pouring beer with the ideal amount of "head", or foam, on top).

The client had a few thousand images of professionally photographed pints of beer to use as training data. The images represented their beer in different stages of pour appearance on bar tops, taken in daylight and/or professional lighting.  

The initial version of their model struggled to perform effectively in production. Even though their training data provided many examples of the object that they wanted to analyze, the qualitative appearance of their training data did not capture the appearance of their beer in diverse real-world environments.

They needed to provide training data that captured:
1) The breadth of real world scenarios
2) The quality of user generated images

After applying these changes, the model performance improved.
{% endhint %}

## Training Data Checklist


Visually Distinct

Look for visually noticeable qualities - trying to recognize something that is not too subtle for humans to pick up on AND something that can be picked up through the noise of a photo. Also look for whether or not those noticeable qualities are distinct enough to be repeatable across inputs.

Ideal/Not Ideal inputs defined

Create a visual dictionary of what each concept’s training data will and will not be trained for.  Determine resolution and image size for optimal data
Remember to set aside Evaluation data at the start of each project. A split of 80% Training Data to 20% Evaluation data should be good to start.

Semantically clear

Make sure the labels for concepts reflect what the photo is of, not just what is in the photo.

UGC Optimized

UGC stands for “User Generated Content”. We need to make sure the training and test data matches the reality of the use-case. Your evaluation test set should be a reflection of this.

Assets

Have model versions and API Keys on-hand for testing and for running scripts, if applicable

Labels

Keep track of the number of images labeled, either via JIRA or docs.


## Common Problems in Model Performance

Bias occurs when the scope of your training data is too narrow. If you only see green apples, you’ll assume that all apples are green and think red apples were another kind of fruit. If the training data contains only a small number of examples, it’ll react accordingly, taking it as truth. Small datasets make for a smaller worldview.

Variance, on the other hand, occurs when your training set is cast too wide. If you train a concept of too many different kinds of images, and they are all visually different, the training set will become noisy. This will make it difficult for the model to find the visually distinct qualities to learn from.







## Gathering and cleaning data

## Building a visual dictionary
