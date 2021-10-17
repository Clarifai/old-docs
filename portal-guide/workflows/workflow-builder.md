Workflow Builder

The workflow builder is designed to make it easy for you to create, modify and experiment with AI workflows.
You can create the skeleton of a workflow by connecting one or more models, and then configuring each model-type as a node in your workflow.  Non-trainable models (also known as "model operators") can be added to workflows on-the-fly, without the need to pre-configure these models ahead of time. You can even view and edit the output settings of any model in a workflow, directly in the graph editor.

Model Types
Filter
Filtering helps you to remove unwanted data from your workflow. This data might take the form of inputs (like images, video and text), or it might be an output from another model, like a predicted concept. One very common use of filters in workflows is to eliminate predictions that fall below a certain confidence threshold.

Edit
Edit models help you to transform and/or augment your data. Edit models can be used to crop out regions of an image, align an image based on the pose of a face, or even map predictions from one model to another.

Action
Action models help you to automate processes. You can trigger a wide variety of actions based on predictions made by models in your workflow. You can automatically send an SMS message when a certain object is detected, you can add a label to an image based on predicted concepts, and you can even trigger aws-lambda functions.

Aggregate
Aggregation models consolidate multiple model outputs into a single output. Aggregation is important for a wide variety of image, video and text use cases, and can help you count objects, connect individually detected words into sentences, or connect objects across multiple frames of video.

Predict
Prediction models are the "intelligent" part of your AI workflows. Predictions help you to understand, classify and organize your data. Predictions can be used to drive behaviors in other nodes in your workflow. Predictions take specific input types and then return predictions about things like the concepts, regions, poses, characters, words, and the abstract visual characteristics of your inputs.

Building Workflows
To build a workflow, just grab a model from the lefthand sidebar and drag it onto your workspace. This model will automatically be configured as a node in your workflow. Once a node is added to your workflow you can configure the model parameters in the righthand sidebar.

The models in your workflow will automatically connect when they are placed near each other. You can also grab the node connectors on each model and configure your workflow nodes manually.
