## Text

### Make predictions on text input

--------

### Via Raw Text Input

To get predictions for a text input, you need to supply a text and the model you'd like to get predictions from. You can supply a text either with a publicly accessible URL or by directly by using the `raw` attribute and attaching a `string` value of the text input you're like to get predictions for. You would also specify the model you'd like to use with the `model-id` parameter.

Below is an example of how you would send `raw` text inputs and receive back predictions from the moderation_model.

```python

# Initialization of Clarifai
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# This is how you authenticate.
metadata = (('authorization', f'Key {YOUR_CLARIFAI_API_KEY}'),)

request = service_pb2.PostModelOutputsRequest(
    # This is the model ID of custom model or a publicly available model.
    model_id= {'THE_MODEL_ID'},
    inputs=[
      resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(raw="Gas emissions are depleting our natural resouurces")))
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
