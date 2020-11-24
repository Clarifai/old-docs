---
description: Evaluate model performance.
---

# Evaluate

Now that you've successfully trained the model, you may want to test its performance before using it in the production environment. The Model Evaluation tool allows you to perform a cross validation on a specified model version. Once the evaluation is complete, you’ll be able to view various metrics that will inform the model’s performance.

## How It Works

Model Evaluation performs a K-split cross validation on data you used to train your custom model.

![cross validation](../../../.gitbook/assets/cross_validation%20%282%29.jpg)

In the cross validation process, it will: 1. Set aside a random 1/K subset of the training data and designate as a test set, 2. Train a new model with the remaining training data, 3. Pass the test set data through this new model to make predictions, 4. Compare the predictions against the test set’s actual labels, and 5. Repeat steps 1\) through 4\) across K splits to average out the evaluation results.

## Requirements

To run the evaluation on your custom model, it will need the meet the following criteria:

* A custom trained model model version with:
  1. At least 2 concepts
  2. At least 10 training inputs per concept \(At least 50 inputs per concept is recommended\)

## Running Evaluation

You can run the evaluation on a specific model version of your custom model in the [Portal](https://clarifai.com/apps). Go to your Application, click on your model of interest, and select the Versions tab. Simply click on the Evaluate button for the specific model version.

![](../../../.gitbook/assets/previewui-versions-new%20%282%29.png)

![](../../../.gitbook/assets/preview-evaluate-new%20%282%29.png)

The evaluation may take up to 30 minutes. Once it is complete, the Evaluate button will become View button. Click on the View button to see the evaluation results.

![](../../../.gitbook/assets/preview-view-new%20%282%29.png)

Note that the evaluation may result in an error if the model version doesn’t satisfy the requirements above.

For more information on how to interpret the evaluation results and to improve your model, check out the [Evaluation](https://github.com/Clarifai/docs/tree/5882f46bd17affcd85ed3e2ec98f4d6f355b58a9/advanced-model-eval-2.md) corner under the “Advanced” section below.

