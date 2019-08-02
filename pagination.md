## Pagination

Many API calls are paginated. You can provide `page` and `per_page` params to the API. In the example below
we are getting all inputs and specifying to start at page 2 and get back 20 results per page.



```js

app.inputs.list({page: 2, perPage: 20});

```

```python
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.inputs.get_by_page(page=2, per_page=20)

```

```java

client.getInputs()
    .perPage(20) // OPTIONAL, to specify how many results should be on one page
    .getPage(2)
    .executeSync();

```

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

```objective-c

[app getInputsOnPage:2 pageSize:20 completion:^(NSArray<ClarifaiInput *> *inputs, NSError *error) {
    NSLog(@"inputs: %@", inputs);
}];

```

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

```cURL

curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs?page=2&per_page=20

```


