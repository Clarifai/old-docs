### Authorize API Calls

After creating your `API Key`, you are ready to make API calls. If you are using a client, authentication will be handled for you. If you are using the REST API, you will need to add the `Authorization` header as described in the cURL example.

{% tabs %}
{% tab title="js" %}
```javascript
const app = new Clarifai.App({apiKey: 'YOUR_API_KEY'});
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')
```
{% endtab %}

{% tab title="java" %}
```java
new ClarifaiBuilder("YOUR_API_KEY").buildSync();
```
{% endtab %}

{% tab title="csharp" %}
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
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiApp *app = [[ClarifaiApp alloc] initWithApiKey:@"YOUR_API_KEY"];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient('YOUR_API_KEY');
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H 'Authorization: Key YOUR_API_KEY' \
  -H "Content-Type: application/json" \
  -d '
```
{% endtab %}
{% endtabs %}

If the API Key does not have the required scope\(s\) to execute a given request, you will get an error message reporting the missing scopes and/or endpoints that your key needs to execute this request.
