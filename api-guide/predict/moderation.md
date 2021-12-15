---
description: Build moderation models from text inputs
---

# Text

## Via raw

To generate a moderation model on a text input, provide the text to be moderated and enter the model to generate the moderation model from. An API call can generate the moderation model from either a publicly accessible URL to a text file or a raw text string. The string length is restricted to 4,294,967,295 characters. The model must be specified along `{model-id}` parameter.

The following example shows how you can generate moderation model from a raw text string:

{% tabs %}
{% tab title="Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# This is how you authenticate.
metadata = (('authorization', f'Key {Your_API_Key}'),)

request = service_pb2.PostModelOutputsRequest(
    # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
    model_id='{Your_Model_ID}',
    inputs=[
      resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(raw='burninhellyounarcissistsonofabitchmotherfuckeriatiredofyourshit')))
    ])
response = stub.PostModelOutputs(request, metadata=metadata)

if response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(response.outputs[0].status.code))
    print("\tDescription: {}".format(response.outputs[0].status.description))
    print("\tDetails: {}".format(response.outputs[0].status.details))
    raise Exception("Request failed, status code: " + str(response.status.code))

for concept in response.outputs[0].data.concepts:
    print('%12s: %.2f' % (concept.name, concept.value))```
{% endtab %}

