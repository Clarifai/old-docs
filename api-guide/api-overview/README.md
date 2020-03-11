# API overview

Our API enables you to build AI applications with capabilities like prediction, search and custom training.

Access our API over HTTPS via `https://api.clarifai.com`. In the examples throughout our documentation, we use single brackets `{variable}` to indicate variables that you should replace with a real value.

We recommend using a client library to access the API. We offer official clients in a variety of languages.

| Available Clients |
| ----------------- |
| [Clarifai C#](https://github.com/Clarifai/clarifai-csharp) |
| [Clarifai Java](https://github.com/Clarifai/clarifai-java) |
| [Clarifai JavaScript](https://github.com/Clarifai/clarifai-javascript) ([Reference Docs](https://sdk.clarifai.com/js/latest/index.html)) |
| [Clarifai PHP](https://github.com/Clarifai/clarifai-php) |
| [Clarifai Python](https://github.com/Clarifai/clarifai-python) ([Reference Docs](https://clarifai-python.readthedocs.io/en/latest/index.html)) |

To access the Clarifai API in other languages, use the REST API directly. For REST documentation
please see the cURL examples.

## Client Installation Instructions

{% tabs %}
{% tab title="javascript" %}
```javascript
// The JavaScript client works in both Node.js and the browser.


// Install the client from NPM

npm install clarifai

// Require the client

const Clarifai = require('clarifai');

// initialize with your api key. This will also work in your browser via http://browserify.org/

const app = new Clarifai.App({
 apiKey: 'YOUR_API_KEY'
});

// You can also use the SDK by adding this script to your HTML:

<script type="text/javascript" src="https://sdk.clarifai.com/js/clarifai-latest.js"></script>
```
{% endtab %}

{% tab title="python" %}
```python
# Pip install the client:
# pip install clarifai

from clarifai.rest import ClarifaiApp

# Create your API key in your account's Application details page:
# https://clarifai.com/apps

app = ClarifaiApp(api_key='YOUR_API_KEY')

# You can also create an environment variable called `CLARIFAI_API_KEY`
# and set its value to your API key.
# In this case, the construction of the object requires no `api_key` argument.

app = ClarifaiApp()
```
{% endtab %}

{% tab title="java" %}
```java
// Our API client is hosted on jCenter, Maven Central, and JitPack.

///////////////////////////////////////////////////////////////////////////////
// Installation - via Gradle (recommended)
///////////////////////////////////////////////////////////////////////////////

// Add the client to your dependencies:
dependencies {
    compile 'com.clarifai.clarifai-api2:core:2.3.0'
}

// Make sure you have the Maven Central Repository in your Gradle File
repositories {
    mavenCentral()
}

///////////////////////////////////////////////////////////////////////////////
// Installation - via Maven
///////////////////////////////////////////////////////////////////////////////

/*
<!-- Add the client to your dependencies: -->
<dependency>
  <groupId>com.clarifai.clarifai-api2</groupId>
  <artifactId>core</artifactId>
  <version>2.3.0</version>
</dependency>
*/

///////////////////////////////////////////////////////////////////////////////
// Initialize client
///////////////////////////////////////////////////////////////////////////////

new ClarifaiBuilder("YOUR_API_KEY")
    .client(new OkHttpClient()) // OPTIONAL. Allows customization of OkHttp by the user
    .buildSync(); // or use .build() to get a Future<ClarifaiClient>
```
{% endtab %}

{% tab title="csharp" %}
```csharp
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
            var client = new ClarifaiClient("YOUR_API_KEY");
        }
    }
}

// Note: See the StackOverflow answer below on how to use async/await from the Main method in C# < 7.1:
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
composer require clarifai/clarifai-php
```
{% endtab %}

{% tab title="bash" %}
```text
// Install cURL: https://curl.haxx.se/download.html
```
{% endtab %}
{% endtabs %}


##### gRPC Clients (alpha)

We are in the process of building auto-generated clients using [gRPC](https://grpc.io/). These
clients may offer higher performance since they use the more optimized gRPC channel to transfer the
data over the network. The data is serialized with
[Protocol Buffers](https://developers.google.com/protocol-buffers/).

These clients are auto-generated and will always have the latest available Clarifai API
feature-set.

It's even possible to make these clients use the standard HTTP+JSON channel, while enjoying a better
auto-completion support in most IDEs (compared to building and parsing JSON directly), and easily
being able to switch to using a gRPC channel when/if desired.

The gRPC clients below are currently available and we'll be adding more as time goes on.

| Available gRPC Clients |
| ----------------- |
| [Clarifai gRPC Java](https://github.com/Clarifai/clarifai-java-grpc/) |
| [Clarifai gRPC NodeJS](https://github.com/Clarifai/clarifai-javascript-grpc) |
| [Clarifai gRPC Python](https://github.com/Clarifai/clarifai-python-grpc/) |
