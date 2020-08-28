# AWS Lambda Functions with Clarifai

AWS Lambda

## Accessing the clarifai_grpc package

We need to setup some initial helper functions for users to get easy access to our clarifai_grpc package.


{% tabs %}
{% tab title="gRPC Python" %}
```python

pip install clarifai-grpc
cd ~/
mkdir -p temp_python_folder/python/google
cp -r ~/virtualenv/v1/lib/python3.7/site-packages/clarifai_grpc temp_python_folder/python/
cp -r ~/virtualenv/v1/lib/python3.7/site-packages/google/protobuf temp_python_folder/python/google/
cd temp_python_folder
zip -r lambda_function.zip python
cd ..
rm -rf temp_python_folder

```
{% endtab %}
{% endtabs %}

Then in AWS console, upload that .zip file as a new Layer here https://console.aws.amazon.com/lambda/home?region=us-east-1#/layers



## Helpful articles

Setting up lambda layers with your python package: https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d

Invoking from python: https://www.sqlshack.com/calling-an-aws-lambda-function-from-another-lambda-function/

Permissions: https://aws.amazon.com/blogs/compute/easy-authorization-of-aws-lambda-functions/

Calling lambda from golang: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/lambda-go-example-run-function.html

## Opening up permission for other users to use our lambda layer

(called clarifaiGRPCWithPythonFolder version 4):

{% tabs %}
{% tab title="gRPC Python" %}
```python

aws lambda add-layer-version-permission --layer-name clarifaiGRPCWithPythonFolder  --version-number 4  --statement-id allAccountsExample --principal="*"   --action lambda:GetLayerVersion

```
{% endtab %}
{% endtabs %}


## Instructions for Python Users

Create an AWS lambda function (we will call it `MyFunction` in the below examples) using the blank template.

Give it a name `MyFunction` and select python 3.8

Add the `arn:aws:lambda:us-east-1:282244745782:layer:clarifaiGRPCWithPythonFolder:4` layer to your function.

Use this as a template to do something in your function:

{% tabs %}
{% tab title="gRPC Python" %}
```python

import json
from google.protobuf import json_format

from clarifai_grpc.grpc.api import resources_pb2, service_pb2
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2

def lambda_handler(event, context):

    # We pass the request in "request" field so that the event can store other information in future if needed.
    request = json_format.ParseDict(event['request'], service_pb2.PostModelOutputsRequest(), ignore_unknown_fields=True)

    # do some work here.

    outputs = []
    for inp in request.inputs:
        output = resources_pb2.Output(data=inp.data)
        output.data.text.raw = "some text from lambda function"
        output.data.concepts.extend([resources_pb2.Concept(id="lamborghini23", value=0.75)])
        outputs.append(output)        

    # just echo the incoming data for now into the response.
    response = service_pb2.MultiOutputResponse(
        #status=status_pb2.Status(code=status_code_pb2.SUCCESS),
        outputs=outputs,
    )

    return {
        # Leave room for other fields above if needed in future.
        'response': json_format.MessageToDict(response),
    }
```
{% endtab %}
{% endtabs %}


Test out your function with some data:

{% tabs %}
{% tab title="gRPC Python" %}
```python
{
  "request": {
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
          }
        }
      }
    ]
  }
}

```
{% endtab %}
{% endtabs %}


Add the Clarifai AWS account to have permission to invoke your function:

{% tabs %}
{% tab title="gRPC Python" %}
```python

aws lambda add-permission \
  --function-name MyFunction \
  --region us-east-1 \
  --statement-id inviteClarifaiToInvoke \
  --action "lambda:InvokeFunction" \
  --principal 282244745782 \
  --profile adminuser


```
{% endtab %}
{% endtabs %}

We will send a `PostModelsOuptut` call to the lambda function and the data payload you should expect is `PostModelsOutputRequest` with the previous model's output in workflow. The response will look like this:

{% tabs %}
{% tab title="gRPC Python" %}
```

type AWSLambdaResponse struct {
	StatusCode int64                    `json:"statusCode"`
	Body       string                   `json:"body"`
	Response   *api.MultiOutputResponse `json:"response"`
}
```
{% endtab %}
{% endtabs %}

In the `statusCode` field you should expect a value of 200 if the lambda call is successful. In the `response` field you can expect a response in the form of a json object from `MultiOutputResponse`. We will then send the data returned from this object to the next model in your workflow.
