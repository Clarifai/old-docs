---
description: Clarifai API provides clients in the most popular languages.
---

# Clarifai API Clients

## Clarifai Clients

You can access the Clarifai API through clients in many of the most popular programming languages. Our clients are built on [gRPC](https://grpc.io/) and are accessible through HTTP+JSON channels as well as gRPC channels. 

| Official Clients |
| :--- |
| [Clarifai Python](https://github.com/Clarifai/clarifai-python-grpc/) |
| [Clarifai Java](https://github.com/Clarifai/clarifai-java-grpc/) |
| [Clarifai NodeJS](https://github.com/Clarifai/clarifai-nodejs-grpc) |
| [Clarifai C\#](https://github.com/Clarifai/clarifai-csharp-grpc/) |
| [Clarifai PHP](https://github.com/Clarifai/clarifai-php-grpc/) |
| [Clarifai Swift](https://github.com/Clarifai/clarifai-swift-grpc) |
| [Clarifai Rust](https://github.com/Clarifai/clarifai-rust-grpc) |
| [Clarifai Go](https://github.com/Clarifai/clarifai-go-grpc) |
| [Clarifai C++](https://github.com/Clarifai/clarifai-cpp-grpc) |

## Manually-built Clients \(deprecated\)

| Available Clients |
| :--- |
| [C\#](https://github.com/Clarifai/clarifai-csharp) |
| [Java](https://github.com/Clarifai/clarifai-java) |
| [JavaScript](https://github.com/Clarifai/clarifai-javascript) \([Reference Docs](https://sdk.clarifai.com/js/latest/index.html)\) |
| [PHP](https://github.com/Clarifai/clarifai-php) |
| [Python](https://github.com/Clarifai/clarifai-python) \([Reference Docs](https://clarifai-python.readthedocs.io/en/latest/index.html)\) |

## Client Installation Instructions

Here are installation instructions for three of our most commonly used clients. For information on installing our other clients, please follow the links above.

### Authorization keys

The key to be used as authorization can be either:

* An API key, which is tied to a certain application, or
* A Personal Access Token \(PAT\), which is tied to a user.

Since a user can own multiple applications, using a PAT is more powerful. However, using a PAT also means that you need to specify the application ID to which the request should be applied.

With most endpoints you can freely choose whether to use an API key or a PAT. In this documentation, some code examples use one and some the other. But certain endpoints support only PAT \(e.g. creating a new application or a new API key\).

{% tabs %}
{% tab title="Python" %}
```python
##############################################################################
# Installation
##############################################################################

pip install clarifai-grpc

##############################################################################
## Initialize client
##     - This initializes the gRPC based client to communicate with the 
##       Clarifai platform. 
##############################################################################
## Import in the Clarifai gRPC based objects needed
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2

## Construct the communications channel and the object stub to call requests on.
# Note: You can also use a secure (encrypted) ClarifaiChannel.get_grpc_channel() however
# it is currently not possible to use it with the latest gRPC version
channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)


################################################################################
## Set up Personal Access Token and Access information
##     - This will be used by every Clarifai API call 
################################################################################
## Specify the Authorization key.  This should be changed to your Personal Access Token.
## Example: metadata = (('authorization', 'Key 123457612345678'),) 
metadata = (('authorization', 'Key {YOUR_CLARIFAI_API_KEY}'),)

##
## A UserAppIDSet object is needed for most rpc calls.  This object contains
## two pieces of information: the user id and the app id.  Both of these are
## specified as string values.
##
##     'user_id' : This is your user id
##     'app_id'  : This is the app id which contains the model of interest
userDataObject = UserAppIDSet(user_id='{YOUR USER NAME HERE}', app_id='{YOUR APPLICATION ID HERE}')
```
{% endtab %}

{% tab title="Java" %}
```java
///////////////////////////////////////////////////////////////////////////////
// Installation (build.gradle)
///////////////////////////////////////////////////////////////////////////////

repositories {
    jcenter()
}

dependencies {
    implementation 'com.clarifai:clarifai-grpc:LATEST_VERSION'
}

///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

import com.clarifai.channel.ClarifaiChannel;
import com.clarifai.credentials.ClarifaiCallCredentials;
import com.clarifai.grpc.api.*;
import io.grpc.Channel;


Channel channel = ClarifaiChannel.INSTANCE.getGrpcChannel();

// Note: You can also use a secure (encrypted) ClarifaiChannel.INSTANCE.getGrpcChannel() however
// it is currently not supported in the latest gRPC version.

V2Grpc.V2BlockingStub stub = V2Grpc.newBlockingStub(channel)
    .withCallCredentials(new ClarifaiCallCredentials("{YOUR_CLARIFAI_API_KEY}"));
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
///////////////////////////////////////////////////////////////////////////////
// Installation
///////////////////////////////////////////////////////////////////////////////

npm install clarifai-nodejs-grpc

///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

const {ClarifaiStub, grpc} = require("clarifai-nodejs-grpc");

const stub = ClarifaiStub.grpc();

// This will be used by every Clarifai endpoint call.
const metadata = new grpc.Metadata();
metadata.set("authorization", "Key {YOUR_CLARIFAI_API_KEY}");
```
{% endtab %}
{% endtabs %}

