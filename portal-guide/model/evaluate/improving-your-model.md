# Improving your Model

The evaluation metrics are meant to help you diagnose the quality of your model. Your model may belong to one or more of many categories, including, but not limited to:

1. Good model with all great concepts.
2. OK model with a few bad concepts.
3. Bad model with all bad concepts.
4. Biased model: the model is consistently picking up certain visual cues other than what you’d like to pick up.
5. Model with Variance: there is no consistency in the way the model is predicting on inputs.

## Possible Areas of Improvement

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

## Tips

When improving your model, there is no one-size-fits-all answer. Here are some tips to keep in mind:

1. Although we use ROC AUC as a general top-level ‘score’ for both concept and model, we do not recommend that you rely on 1 metric only to draw your final conclusion on your model performance.
2. Refer to both Concepts by Concepts Results as well as Selection Details to get a better grasp of your model.
3. When interpreting the evaluation results, keep in mind the nature of your model. Specifically, pay attention to whether or not you have labeled the inputs with more than 1 concept \(i.e. non-mutually exclusive concepts environment\), vs. only 1 concept per image.
4. Remember, the rule of diminishing returns may also apply to training models. After a certain point, the changes may not make a big difference in the model quality.
