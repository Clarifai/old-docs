# Authentication

Note: API Keys have replaced Access Tokens/Client ID & Secret

API Keys will now be used to authorize your Clarifai applications. You can go to an [Application's detail page](https://portal.clarifai.com/apps) to create a new key . This change will not break existing applications - Access Tokens will be supported until late 2017. You can find more information on our [blog](http://blog.clarifai.com/introducing-api-keys-a-safer-way-to-authenticate-your-applications).

Authentication to the API is handled through API Keys. You can limit the scope of an API Key, which enables the key to perform very specific operations on a given app, keeping your app secure.

To create an API Key, you can head over to the [Application details page](https://portal.clarifai.com/apps), and specify what scopes you want the key to have.

![api keys](/images/apikey-screen.png)

**Authorize Applications**

Select the application that you want to authorize using this key. An API Key cannot be used across multiple apps.

**Key Description**

Use this field to create a descriptive name for your API Key. As you start to create a lot of keys, you would need this field to keep track of what key is for what purpose. Note: this field is not used for any identification purposes.

**Scopes**

You will see a list of scopes that you can add on to your API Key for the app that was selected. We recommend generating different keys for very specific purposes - this is the best approach to keep your app secure from malicious attacks. Do **NOT** share your API Key with other users. Here's a list of scopes that your key can have:

![scope](/images/keys.png)

Note: API Keys do not expire. In case your API Key gets compromised, you should delete that key, and create a new one with the same scopes.

**Authorize API Calls**

After creating your `API Key`, you are ready to make API calls. If you are using a client, authentication will be handled for you. If you are using the REST API, you will need to add the `Authorization` header as described in the cURL example.

{% code-tabs %}
{% code-tabs-item title="js" %}
```js
const app = new Clarifai.App({apiKey: 'YOUR_API_KEY'});
```
{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')
```
{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
new ClarifaiBuilder("YOUR_API_KEY").buildSync();
```
{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp
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
```
{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
ClarifaiApp *app = [[ClarifaiApp alloc] initWithApiKey:@"YOUR_API_KEY"];

```
{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');
```
{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL
curl -X POST \
  -H 'Authorization: Key YOUR_API_KEY' \
  -H "Content-Type: application/json" \
  -d '
```
{% endcode-tabs-item %}
{% endcode-tabs %}



If the API Key does not have the required scope\(s\), you will receive one of the following responses: 1. Rejected Request: if a large portion of the response requires a scope that is missing 2. Redacted Response: if majority of the response has the required scope\(s\), a small portion of the response will be redacted to not reveal unwarranted information
