# Pagination

Many API calls are paginated. You can provide `page` and `per_page` params to the API. In the example below we are getting all inputs and specifying to start at page 2 and get back 20 results per page.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

...

MultiInputResponse listInputsResponse = stub.listInputs(
    ListInputsRequest.newBuilder()
        .setPage(2)
        .setPerPage(20)
        .build()
);

if (listInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List inputs failed, status: " + listInputsResponse.getStatus());
}

for (Input input : listInputsResponse.getInputsList()) {
    System.out.println(input);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
stub.ListInputs(
    {page: 2, per_page: 20},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List inputs failed, status: " + response.status.description);
        }

        for (const input of response.inputs) {
            console.log(JSON.stringify(input, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

...

list_inputs_response = stub.ListInputs(
    service_pb2.ListInputsRequest(page=2, per_page=20),
    metadata=metadata
)

if list_inputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List inputs failed, status: " + list_inputs_response.status.description)

for input_object in list_inputs_response.inputs:
    print(input_object)
```
{% endtab %}

{% tab title="js" %}
```javascript
app.inputs.list({page: 2, perPage: 20});
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.inputs.get_by_page(page=2, per_page=20)
```
{% endtab %}

{% tab title="java" %}
```java
client.getInputs()
    .perPage(20) // OPTIONAL, to specify how many results should be on one page
    .getPage(2)
    .executeSync();
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

            await client.GetInputs()
                .PerPage(20) // OPTIONAL, to specify how many results should be on one page
                .Page(2)
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
[app getInputsOnPage:2 pageSize:20 completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiInput;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->getInputs()
    ->withPerPage(20)  // OPTIONAL, to specify how many results should be on one page
    ->withPage(2)
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    /** @var ClarifaiInput[] $inputs */
    $inputs = $response->get();
    foreach ($inputs as $input) {
        echo $input->id() . "\n";
    }
} else {
    echo "Response is not successful. Reason: \n";
    echo $response->status()->description() . "\n";
    echo $response->status()->errorDetails() . "\n";
    echo "Status code: " . $response->status()->statusCode();
}
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs?page=2&per_page=20
```
{% endtab %}
{% endtabs %}

