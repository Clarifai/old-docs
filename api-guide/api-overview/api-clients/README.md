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
# Initialize client
##############################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2

channel = ClarifaiChannel.get_grpc_channel()

# Note: You can also use a secure (encrypted) ClarifaiChannel.get_grpc_channel() however
# it is currently not possible to use it with the latest gRPC version

stub = service_pb2_grpc.V2Stub(channel)

# This will be used by every Clarifai endpoint call.
metadata = (('authorization', 'Key {YOUR_CLARIFAI_API_KEY}'),)
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
//////////////////////////////////////////////////////////////////////////////
// Installation
//     - gRPC for PHP is required to use the Clarifai API
//////////////////////////////////////////////////////////////////////////////




//////////////////////////////////////////////////////////////////////////////
// Set Clarifai Namespace
//     - A variety of standard objects are provided in the Clarifai namespace
//       from the client library.  Which ones that are necessary depend on the
//       specific RPC call being made.  All namespaces used in the example
//       code are included below for reference, although you likely won't need
//       all of these in your application. 
//////////////////////////////////////////////////////////////////////////////

// Various data structures that are used in the RPC calls to the Clarifai Platform
// These operate as standardization wrappers for various types of data.

//    Data Types
use Clarifai\Api\Image;
use Clarifai\Api\Text;
use Clarifai\Api\Video;

//    ML Structures
use Clarifai\Api\Concept;
use Clarifai\Api\Model;

//    Wrapper Types
use Clarifai\Api\Data;
use Clarifai\Api\Input;

// Various Request objects.  These specify the structure of the actual RPC request between
// the client and the platform.
use Clarifai\Api\PostModelOutputsRequest;
use Clarifai\Api\PostConceptsSearchesRequest;


use Clarifai\Api\ConceptQuery;

// Output configuration objects
use Clarifai\Api\OutputInfo;
use Clarifai\Api\OutputConfig;

// The request status code object.  This contains information on the success or failure of
// the API operation.
use Clarifai\Api\Status\StatusCode;



//////////////////////////////////////////////////////////////////////////////
// Initialize client
//     - This initializes the gRPC based client to communicate with the 
//       Clarifai platform. 
//////////////////////////////////////////////////////////////////////////////

// The Clarifai PHP Client repository includes an autoload.php helper file that needs to be included
require 'vendor/autoload.php';

// Enable use of the ClarifaiClient object from the Clarifai namespace
use Clarifai\ClarifaiClient;  

// Construct the actual gRPC client object
$client = ClarifaiClient::grpc();



//////////////////////////////////////////////////////////////////////////////
// Set up Personal Access Token and Access information
//     - This will be used by every Clarifai API call 
//////////////////////////////////////////////////////////////////////////////

// Specify the Authorization key.  This should be changed to your Personal Access Token.
// Example: $metadata = ['Authorization' => ['Key 123456789123456789']]; 
$metadata = ['Authorization' => ['Key {YOUR PERSONAL ACCESS TOKEN HERE}']]; // Using the PAT in these examples

//
// A UserAppIDSet object is needed for most rpc calls.  This object cotnains
// two pieces of information: the user id and the app id.  Both of these are
// specified as string values.
//

use Clarifai\Api\UserAppIDSet;  // Specify the namespace for the UserAppIDSet object

$userDataObject = new UserAppIDSet([
    'user_id' => '{YOUR USER NAME HERE}', // This is your user id
    'app_id' => '{YOUR APPLICATION ID HERE}' // This is the app id which contains the model of interest
]);

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

