### Interpreting Results
![model eval results](/images/eval-results-new.png)
Once the Model Evaluation is complete, you’ll be able to view the evaluation results in the <a href="https://clarifai.com/apps" target="_blank">
  Portal here <span class="icon icon-link-out"></span>
</a>

We suggest that you start by looking at the Concept by Concept Probabilities Results and the Summary Table to get a sense of the overall model prediction performance and identify the high-performing and low-performing concepts. Afterwards, hone in on the Selection Details of the False Positives and False Negatives to identify any biases, if any, in how the model is predicting, and to correct any inputs that are mislabeled 
 
Generally, you’ll be looking at results that represent either a) the average across K splits, or b) the test set of a single split, which is about 1/K of your original training set. Note that a single split will be capped at 1,000 inputs. 
 

#### Model Analysis
##### Model Accuracy Score
![model eval results](/images/model-score-new.png) 
Model Accuracy Score is the highest level metric for your model’s prediction performance. It is defined as the macro average of the areas under the receiver operating characteristic curve for every concept. This metric does not depend on the Prediction Threshold. This metric is an average across K splits. 
 
A score of 1 represents a perfect model; a score of .5 represents a worthless model. As a general rule of thumb, a score above .9 is considered good. 
 
Note that we discourage users from making a final assessment of the model accuracy based on the Model Accuracy Score only.

#### Concept Analysis
##### Prediction Threshold
![prediction threshold](/images/prediction-threshold-new.png)
Probability threshold determines the model’s predictions. The default threshold is .5. The input is predicted as (i.e. “counts” as) as a concept, such as “dog”, only if the prediction probability for “dog” is higher than the set threshold, for example, 0.5. You can adjust the threshold depending on how ‘strict’ you want your classification to be. 
 
All prediction binary metrics, such as True Positives, False Negatives, and False Positives, and Total Predicted, Recall Rate, Precision Rate, depend on this threshold. 

##### Evaluation Summary
![model eval summary](/images/eval-summary-table.png)
This table summarizes the numerical evaluation results for every concept. For every concept, it calculates:

**K-Split Average**

1. **ROC AUC (Concept Accuracy Score):** concept’s prediction performance score, defined the area under the receiver operating characteristic curve. A score of 1 represents a perfect model; a score of .5 represents a worthless model. As a general rule of thumb, a score above .9 is considered good. Note: ROC AUC is not dependent on the prediction threshold.

**1-Split**

1. **Total Labeled:** Total number of inputs that were originally labeled as the concept in the test set. Total Labeled is the sum of True Positives (correct) and False Negatives (incorrect). Note: Total Labeled is not dependent on the prediction threshold.
2. **Total Predicted:** Total number of inputs that were predicted as the concept in the test set. This means these inputs were predicted as a concept with probability greater than the prediction threshold value. Total Predicted is the sum of True Positives (correct) and False Positives (incorrect).
3. **True Positives (TP):** Number of inputs that were correctly predicted as the concept they were actually labeled. Also known as “hits”. (E.g. These are the images that were labeled as “dog” and were predicted as “dog”) 
4. **False Negatives (FN):** Number of inputs that were not predicted as the concept they were actually labeled. Also known as “misses”. (E.g. These are the images that were labeled as “dog” but were not predicted as “dog”)
5. **False Positives (FP):** Number of inputs that were predicted as the concept, but they were not labeled as the concept. Also known as “false alarms”. (E.g. These are the images that were predicted as “dog” but were not labeled as “dog”)
6. **Recall Rate:** proportion of the images labeled as the concept that were predicted as the concept. It is calculated as True Positives divided by Total Labeled. Also known as “sensitivity” or “true positive rate”. 
7. **Precision Rate:** proportion of the images predicted as a concept that had been actually labeled as the concept. It is calculated as True Positives divided by Total Predicted. Also known as “positive predictive value”.

##### Concept by Concept Results (Advanced)
This section has a concept by concept matrix. Note that this is not a confusion matrix; we recommend that you read this through before interpreting the data.

In general, the matrix is meant to be read by fixing each row. Each row represents a subset of the test set that was actually labeled as a particular concept. For this subset, each cell across the row represents either

1. The number of inputs that were predicted as a concept (i.e. “counts”), or 
2. The average prediction probability for each concept, noted by the column name, for all inputs in this subset, across all K splits  (i.e. “probabilities”). 
 
Concepts that co-occur, or are similar, may form a visual cluster on the matrix. On the other hand, exclusive or dissimilar concepts should not form a cluster.

**Counts (1-Split)**
![concept by concept results](/images/cxc-result.png)
Each row represents the subset of the test set that were actually labeled as a concept, e.g. “dog”. As you go across the row, each cell shows the number of times those images were predicted as each concept, noted by the column name. 
 
The diagonal cells represent True Positives, i.e. correctly predicted inputs. You’d want this number to be as close to the Total Labeled as possible. 
 
Depending on how your model was trained, the off-diagonal cells could include both correct and incorrect predictions. In a non-mutually exclusive concepts environment, you can label an image with more than 1 concept. For example, an image is labeled as both “dog” and “cat”, this image would be counted in both “dog” row and “cat” row. If the model correctly predicts this image to be both “dog” and “cat”, then this input will be counted in both on and off-diagonal cells. 
 
Few things to note:

1. Remember that the prediction counts depend on the threshold. This means the images are counted toward a predicted concept only if the prediction probability for this concept is higher than the threshold. 
2. This means the sum of the row may be less or greater than the # of total labeled inputs that were labeled as the concept. 
3. You can click on each cell to view the actual prediction results for every input that was counted in this cell. 
4. This represents the test set data of a single split.
 
**Probabilities (K-Split Average)**
![concept by concept five split results](/images/cxc-5split.png)
Each row represents the subset of the test set that were actually labeled as a concept, e.g. “dog”. As you go across the row, each cell shows the average prediction probability for each concept, noted by the column name, for all inputs in this subset. In short, the cell shows the average prediction probability for a concept given the images labeled as a concept.
 
Few things to note:

1. This matrix does not depend on the Prediction Threshold. 
2. You can click on each cell to view the actual prediction results for every input that were used to calculate this cell. 
3. This represents the average across all K splits. 

#### Input Analysis

##### Selection Details
![not expanded](/images/not-expanded-new.png)
This Selection Details table shows the input-level details of the selection you made on the Summary Table or Concept by Concept Results. It shows the image input and prediction probabilities for a specific concept. 
 
Note: the prediction probabilities on this table may seem different from your actual model’s probabilities. The reason is that all the evaluation results are based on the new model that was built for evaluation purposes during the cross validation process.  

##### Expanded Selection Details
![expanded](/images/expanded-new.png)
You can click on the expand button to view the prediction probabilities for every concept for each image. The blue dot denotes the concept(s) the input was actually labeled, i.e. true positives. The red dot denotes the concept(s) that the input was not labeled. 


### Improving your Model
The evaluation metrics are meant to help you diagnose the quality of your model. Your model may belong to one or more of many categories, including, but not limited to: 

1. Good model with all great concepts. 
2. OK model with a few bad concepts.
3. Bad model: with all bad concepts. 
4. Biased model: the model is consistently picking up certain visual cues other than what you’d like to pick up. This is sometimes obvious to pick up in the <a href="https://clarifai.com/apps" target="_blank">
  Portal here <span class="icon icon-link-out"></span>
</a>. 
5. Model with Variance: there is no consistency in the way the model is predicting on inputs. 
 
#### Possible Areas of Improvement
The performance of your model depends on the performance of each concept, which is trained on a set of inputs. We’d recommend that you look at both inputs and concepts when diagnosing areas of improvement.

**Inputs**

1. Diversity: try to include all perspectives of the concept, e.g. include all angles of a “dog”, if you’re building a “dog” concept. 
2. Strong positives: Images that are the true representation of your concept.
3. Training data should be representative of the real world data -- avoid making models where the data is too ‘easy’, i.e. unrealistic set of data. 
4. Number: minimum 50 inputs per concept; more inputs the better. 
5. File dimensions: minimum 512px x 512px. 


**Concepts**

1. Concepts: avoid concepts that do not rely on visual cues within the image. Also, current custom training does not perform well on training to identify faces.
2. Labels: check to see if any inputs are labeled with wrong concepts. 

#### Tips
When improving your model, there is no one-size-fits-all answer. Here are some tips to keep in mind:

1. Although we use ROC AUC as a general top-level ‘score’ for both concept and model, we do not recommend that you rely on 1 metric only to draw your final conclusion on your model performance. 
2. Refer to both Concepts by Concepts Results as well as Selection Details to get a better grasp of your model. 
3. When interpreting the evaluation results, keep in mind the nature of your model. Specifically, pay attention to whether or not you have labeled the inputs with more than 1 concept (i.e. non-mutually exclusive concepts environment), vs. only 1 concept per image. 
4. Remember, the rule of diminishing returns may also apply to training models. After a certain point, the changes may not make a big difference in the model quality.

