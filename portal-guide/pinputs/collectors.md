Collectors enable you to capture input data for an app.
collect data into your app automatically from production models

a way of piping data into your app



When a selected caller makes predictions with a specified model version, this collector will post the inputs to your app.

Pre-queue workflow
This should be set to the ID of a workflow to pre-process the input. For example, a random sampling workflow to sample a fraction of the matched inputs.

Post inputs key
This API key must have the PostInputs scope, since it grants the collector the authority to POST inputs to your app.


Caller
Any caller
Caller user ID

Source
When the selected caller makes predictions with the following model version, this collector will post the inputs to your app.

user
app
model name
