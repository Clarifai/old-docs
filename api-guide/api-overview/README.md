# API overview

Our API enables you to build AI applications with capabilities like prediction, search and custom training.

Access our API over HTTPS via `https://api.clarifai.com`. In the examples throughout our documentation, we use single brackets `{variable}` to indicate variables that you should replace with a real value.

We recommend using a client library to access the API. We offer official clients in a variety of languages.
To access the Clarifai API in other languages, use the REST API directly. For REST documentation
please see the cURL examples.

## gRPC Clients

For new projects, we recommend using one of the auto-generated clients built using [gRPC](https://grpc.io/). These
clients may offer better performance since they use a gRPC channel where the network transfer of the
data is optimized. The data is serialized with [Protocol Buffers](https://developers.google.com/protocol-buffers/).

Since the gRPC clients are auto-generated and will always have the latest available Clarifai API
feature-set.

It's possible to make these clients use the standard HTTP+JSON channel, while enjoying a better
auto-completion support in most IDEs (compared to building and parsing JSON directly), and easily
being able to switch to using a gRPC channel when/if desired.

The gRPC clients below are currently available and we'll be adding more as time goes on.

| Available gRPC Clients |
| ----------------- |
| [Clarifai gRPC Java](https://github.com/Clarifai/clarifai-java-grpc/) |
| [Clarifai gRPC NodeJS](https://github.com/Clarifai/clarifai-javascript-grpc) |
| [Clarifai gRPC Python](https://github.com/Clarifai/clarifai-python-grpc/) |

## Manually-built Clients

| Available Clients |
| ----------------- |
| [Clarifai C#](https://github.com/Clarifai/clarifai-csharp) |
| [Clarifai Java](https://github.com/Clarifai/clarifai-java) |
| [Clarifai JavaScript](https://github.com/Clarifai/clarifai-javascript) ([Reference Docs](https://sdk.clarifai.com/js/latest/index.html)) |
| [Clarifai PHP](https://github.com/Clarifai/clarifai-php) |
| [Clarifai Python](https://github.com/Clarifai/clarifai-python) ([Reference Docs](https://clarifai-python.readthedocs.io/en/latest/index.html)) |

## Client Installation Instructions

{% tabs %}
{% tab title="gRPC Java" %}
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
import io.grpc.Channel;

...

// Construct one of the channels you want to use
Channel channel = ClarifaiChannel.INSTANCE.getJsonChannel();
Channel channel = ClarifaiChannel.INSTANCE.getInsecureGrpcChannel();

// Note: You can also use a secure (encrypted) ClarifaiChannel.INSTANCE.getGrpcChannel() however
// it is currently not supported in the latest gRPC version.
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
///////////////////////////////////////////////////////////////////////////////
// Installation
///////////////////////////////////////////////////////////////////////////////

npm install clarifai-nodejs-grpc

///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

// Construct one of the stubs you want to use
const stub = ClarifaiStub.json();
const stub = ClarifaiStub.insecureGrpc();
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
///////////////////////////////////////////////////////////////////////////////
// Installation
///////////////////////////////////////////////////////////////////////////////

pip install clarifai-grpc

///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel

# Construct one of the channels you want to use
channel = ClarifaiChannel.get_json_channel()
channel = ClarifaiChannel.get_insecure_grpc_channel()

# Note: You can also use a secure (encrypted) ClarifaiChannel.get_grpc_channel() however
# it is currently not possible to use it with the latest gRPC version
```
{% endtab %}

{% tab title="javascript" %}
```javascript
// The JavaScript client works in both Node.js and the browser.
// From browser use see: http://browserify.org/

///////////////////////////////////////////////////////////////////////////////
// Installation
///////////////////////////////////////////////////////////////////////////////

npm install clarifai

// You can also use the SDK by adding this script to your HTML:
<script type="text/javascript" src="https://sdk.clarifai.com/js/clarifai-latest.js"></script>


///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

const Clarifai = require('clarifai');

const app = new Clarifai.App({
 apiKey: 'YOUR_API_KEY'
});
```
{% endtab %}

{% tab title="python" %}
```python
##############################################################################
# Installation
##############################################################################

pip install clarifai


##############################################################################
# Initialize client
##############################################################################

from clarifai.rest import ClarifaiApp

# Skip the argument to fetch the key from the CLARIFAI_API_KEY environment variable.
app = ClarifaiApp(api_key='YOUR_API_KEY')
```
{% endtab %}

{% tab title="java" %}
```java
///////////////////////////////////////////////////////////////////////////////
// Installation - via Gradle (recommended)
///////////////////////////////////////////////////////////////////////////////

// Add the client to your dependencies:
dependencies {
    compile 'com.clarifai.clarifai-api2:core:INSERT_VERSION'
}

// Make sure you have the Maven Central Repository in your Gradle File.
// Note: our Java API client is hosted on jCenter, Maven Central, and JitPack.
repositories {
    mavenCentral()
}


///////////////////////////////////////////////////////////////////////////////
// Installation - via Maven
///////////////////////////////////////////////////////////////////////////////

<!-- Add the client to your dependencies: -->
<dependency>
  <groupId>com.clarifai.clarifai-api2</groupId>
  <artifactId>core</artifactId>
  <version>INSERT_VERSION</version>
</dependency>


///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

import clarifai2.api.ClarifaiBuilder;
import clarifai2.api.ClarifaiClient;

public class Main {
    public static void main(String[] args) {
        // Skip the argument to fetch the key from the CLARIFAI_API_KEY environment variable.
        ClarifaiBuilder builder = new ClarifaiBuilder("YOUR_CLARIFAI_API_KEY");
        ClarifaiClient client = builder.buildSync();
    }
}
```
{% endtab %}

{% tab title="csharp" %}
```csharp
///////////////////////////////////////////////////////////////////////////////
// Installation
///////////////////////////////////////////////////////////////////////////////

// Within Visual Studio IDE:
Install-Package Clarifai

// With the dotnet command line tool:
dotnet add package Clarifai


///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

using System.Threading.Tasks;
using Clarifai.API;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            // Skip the argument to fetch the key from the CLARIFAI_API_KEY environment variable.
            var client = new ClarifaiClient("YOUR_API_KEY");
        }
    }
}

// Note: For C# <=7.0, see this StackOverflow answer on using async/await from the Main method:
// https://stackoverflow.com/a/24601591
// Set `<LangVersion>7.1</LangVersion>` in your .csproj under `<PropertyGroup/>`
```
{% endtab %}

{% tab title="objective-c" %}
```text
// Installation via CocoaPods - https://cocoapods.org

// 1. Create a new XCode project, or use a current one.

// 2. Add the following to your Podfile:

//  pod 'Clarifai'

// 3. Install dependencies and generate workspace.

//  pod install

// 4. Open the workspace in Xcode

//  open YOUR_PROJECT_NAME.xcworkspace

// 5. You are now able to import ClarifaiApp.h and any other classes you need!

  #import ClarifaiApp.h

// Note: if you are using Swift in your project, make sure to include use_frameworks! in your Podfile. Then import Clarifai as a module.

  import Clarifai
```
{% endtab %}

{% tab title="php" %}
```php
///////////////////////////////////////////////////////////////////////////////
// Installation
///////////////////////////////////////////////////////////////////////////////

composer require clarifai/clarifai-php


///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

use Clarifai\API\ClarifaiClient;

// Skip the argument to fetch the key from the CLARIFAI_API_KEY environment variable.
$client = new ClarifaiClient('YOUR_API_KEY');
```
{% endtab %}

{% tab title="bash" %}
```text
// Your system may already have curl installed. Test by running `curl --help` from your terminal.
// Otherwise, install cURL: https://curl.haxx.se/download.html
```
{% endtab %}
{% endtabs %}
