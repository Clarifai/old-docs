## Evaluate
Now that you've successfully trained the model, you may want to test its performance before using it in the production environment. The Model Evaluation tool allows you to perform a cross validation on a specified model version. Once the evaluation is complete, you’ll be able to view various metrics that will inform the model’s performance.  
 
This evaluate operation is asynchronous and is currently available on the <a href="https://clarifai.com/apps" target="_blank">
  Portal <span class="icon icon-link-out"></span>
</a> only. 

### How It Works
Model Evaluation performs a K-split cross validation on data you used to train your custom model. 
![cross validation](/images/eval-metrics-1.0@2x.png)
In the cross validation process, it will:
1. Set aside a random 1/K subset of the training data and designate as a test set,
2. Train a new model with the remaining training data, 
3. Pass the test set data through this new model to make predictions,
4. Compare the predictions against the test set’s actual labels, and
5. Repeat steps 1) through 4) across K splits to average out the evaluation results
 
For a refresher on custom training, please refer to our [training documentation](train.md).

### Requirements
To run the evaluation on your custom model, it will need the meet the following criteria:



- A custom trained model model version with:
  1. At least 2 concepts
  2. At least 10 training inputs per concept (At least 50 inputs per concept is recommended)

### Running Evaluation
You can run the evaluation on a specific model version of your custom model in the <a href="https://clarifai.com/apps" target="_blank">
  Portal<span class="icon icon-link-out"></span></a>. Go to your Application, click on your model of interest, and select the Versions tab. Simply click on the Evaluate button for the specific model version. 

![model-eval-versions](/images/previewui-versions-new.png)
![model eval](/images/preview-evaluate-new.png)

The evaluation may take up to 30 minutes. Once it is complete, the Evaluate button will become View button. Click on the View button to see the evaluation results.

![model eval results](/images/preview-view-new.png)

Note that the evaluation may result in an error if the model version doesn’t satisfy the requirements above.

For more information on how to interpret the evaluation results and to improve your model, check out the [Evaluation](advanced-model-eval-2.md) corner under the “Advanced” section below.
