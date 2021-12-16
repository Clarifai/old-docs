# Text

## Make predictions on text inputs

You can make predictions on passages of written text and analyze their emotional and language tones. You need to provide a text and a model you'd like to get predictions from.

You can supply the text either by specifying a `raw` text string or a `url` to a text file. You also need to specify the model to use with the `{model-id}` parameter.

Here is an example of how you to use the `moderation-english` model to analyze a `raw` text input and receive predictions.

```python

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# This is how you authenticate.
metadata = (('authorization', f'Key {"YOUR_CLARIFAI_API_KEY"}'),)

request = service_pb2.PostModelOutputsRequest(
    # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
    model_id='THE_MODEL_ID',
    inputs=[
      resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(raw='YOUR_TEXT_HERE')))
    ])
response = stub.PostModelOutputs(request, metadata=metadata)

if response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(response.outputs[0].status.code))
    print("\tDescription: {}".format(response.outputs[0].status.description))
    print("\tDetails: {}".format(response.outputs[0].status.details))
    raise Exception("Request failed, status code: " + str(response.status.code))

for concept in response.outputs[0].data.concepts:
    print('%12s: %.2f' % (concept.name, concept.value))
```
