# Authorize

After creating your `API Key`, you are ready to make API calls. Most
clients set up authentication when initilizing the client, it can be
changed for particular requests if needed. If you are using the REST
API, you will need to add the `Authorization` header as described in
the cURL example.

{% tabs %}
{% tab title="js" %}
```javascript
// Authentication done at grpc stub initialization time see:
//
https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions
metadata.set("authorization", "Key YOUR_CLARIFAI_API_KEY");
```
{% endtab %}

{% tab title="python" %}
```python
metadata = (('authorization', 'Key YOUR_API_KEY'),)
# Yes the word 'Key' appears in addition to the alphanumeric API_KEY

```
{% endtab %}

{% tab title="java" %}
```java
// Authentication done at grpc stub initialization time see:
//
https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions
V2Grpc.V2BlockingStub stub = V2Grpc.newBlockingStub(ClarifaiChannel.INSTANCE.getGrpcChannel())
    .withCallCredentials(new ClarifaiCallCredentials("YOUR_CLARIFAI_API_KEY"));
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

If the API Key does not have the required scope\(s\) to execute a
given request, you will get an error message reporting the missing
scopes and/or endpoints that your key needs to execute this
request. An invalid key may be reported as 'API key not
found'. Failure to include a required key may result simple in
'Invalid request'.

