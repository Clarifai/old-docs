# Images

## Via URL

To get predictions for an input, you need to supply an image and the model you'd like to get predictions from. You can supply an image either with a publicly accessible URL or by directly sending bytes. You can send up to 128 images in one API call. You specify the model you'd like to use with the `{model-id}` parameter.

Below is an example of how you would send image URLs and receive back predictions from the `general` model.

You can learn all about the different [Clarifai Models](images.md) available later in the guide.

{% tabs %}
{% tab title="js" %}
```javascript
app.models.initModel({id: Clarifai.GENERAL_MODEL, version: "aa7f35c01e0642fda5cf400f543e7c40"})
      .then(generalModel => {
        return generalModel.predict("@@sampleTrain");
      })
      .then(response => {
        var concepts = response['outputs'][0]['data']['concepts']
      })
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')
model = app.public_models.general_model
response = model.predict_by_url('@@sampleTrain')
```
{% endtab %}

{% tab title="java" %}
```java
ConceptModel model = client.getDefaultModels().generalModel();
    ModelVersion modelVersion = model.getVersionByID("the-version").executeSync().get();

    ClarifaiResponse<List<ClarifaiOutput<Prediction>>> response = client.predict(model.id())
        .withInputs(ClarifaiInput.forImage("@@sampleTrain"))
        .withVersion("aa7f35c01e0642fda5cf400f543e7c40")
        .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var Client = new ClarifaiClient("YOUR_API_KEY");

             var response = await Client.Predict<Concept>(
                    Client.PublicModels.GeneralModel.ModelID,
                    new List<IClarifaiInput>
                    {
                        new ClarifaiURLImage("@@sampleTrain"),
                        new ClarifaiURLImage("the-url-2")
                    },
                    "aa7f35c01e0642fda5cf400f543e7c40")
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="objective-c" %}
```text
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"@@sampleTrain"];
[_app getModelByName:@"general-v1.3" completion:^(ClarifaiModel *model, NSError *error) {
    [model predictOnImages:@[image]
                completion:^(NSArray<ClarifaiSearchResult *> *outputs, NSError *error) {
                    NSLog(@"outputs: %@", outputs);
                }];
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$model = $client->publicModels()->generalModel();

$input = new ClarifaiURLImage("@@sampleTrain");
$response = $model->predict($input)
    ->withModelVersionID("aa7f35c01e0642fda5cf400f543e7c40")
    ->executeSync();

if ($response->isSuccessful()) {
    /** @var ClarifaiOutput $output */
    $output = $response->get();

    echo "Predicted concepts:\n";
    /** @var Concept $concept */
    foreach ($output->data() as $concept) {
        echo $concept->name() . ': ' . $concept->value() . "\n";
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
curl -X POST
    -H 'Authorization: Key YOUR_API_KEY'
    -H "Content-Type: application/json"
    -d '
    {
      "inputs": [
        {
          "data": {
            "image": {
              "url": "https://samples.clarifai.com/metro-north.jpg"
            }
          }
        }
      ]
    }'
    https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/versions/aa7f35c01e0642fda5cf400f543e7c40/outputs
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Response JSON" %}
```javascript
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "outputs": [
    {
      "id": "ea68cac87c304b28a8046557062f34a0",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2016-11-22T16:50:25Z",
      "model": {
        "name": "general-v1.3",
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "created_at": "2016-03-09T17:11:39Z",
        "app_id": null,
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T01:19:12Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "ea68cac87c304b28a8046557062f34a0",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "ai_HLmqFqBf",
            "name": "train",
            "app_id": null,
            "value": 0.9989112
          },
          {
            "id": "ai_fvlBqXZR",
            "name": "railway",
            "app_id": null,
            "value": 0.9975532
          },
          {
            "id": "ai_Xxjc3MhT",
            "name": "transportation system",
            "app_id": null,
            "value": 0.9959158
          },
          {
            "id": "ai_6kTjGfF6",
            "name": "station",
            "app_id": null,
            "value": 0.992573
          },
          {
            "id": "ai_RRXLczch",
            "name": "locomotive",
            "app_id": null,
            "value": 0.992556
          },
          {
            "id": "ai_VRmbGVWh",
            "name": "travel",
            "app_id": null,
            "value": 0.98789215
          },
          {
            "id": "ai_SHNDcmJ3",
            "name": "subway system",
            "app_id": null,
            "value": 0.9816359
          },
          {
            "id": "ai_jlb9q33b",
            "name": "commuter",
            "app_id": null,
            "value": 0.9712483
          },
          {
            "id": "ai_46lGZ4Gm",
            "name": "railroad track",
            "app_id": null,
            "value": 0.9690325
          },
          {
            "id": "ai_tr0MBp64",
            "name": "traffic",
            "app_id": null,
            "value": 0.9687052
          },
          {
            "id": "ai_l4WckcJN",
            "name": "blur",
            "app_id": null,
            "value": 0.9667078
          },
          {
            "id": "ai_2gkfMDsM",
            "name": "platform",
            "app_id": null,
            "value": 0.9624243
          },
          {
            "id": "ai_CpFBRWzD",
            "name": "urban",
            "app_id": null,
            "value": 0.960752
          },
          {
            "id": "ai_786Zr311",
            "name": "no person",
            "app_id": null,
            "value": 0.95864904
          },
          {
            "id": "ai_6lhccv44",
            "name": "business",
            "app_id": null,
            "value": 0.95720303
          },
          {
            "id": "ai_971KsJkn",
            "name": "track",
            "app_id": null,
            "value": 0.9494642
          },
          {
            "id": "ai_WBQfVV0p",
            "name": "city",
            "app_id": null,
            "value": 0.94089437
          },
          {
            "id": "ai_dSCKh8xv",
            "name": "fast",
            "app_id": null,
            "value": 0.9399334
          },
          {
            "id": "ai_TZ3C79C6",
            "name": "road",
            "app_id": null,
            "value": 0.93121606
          },
          {
            "id": "ai_VSVscs9k",
            "name": "terminal",
            "app_id": null,
            "value": 0.9230834
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Via bytes

Below is an example of how you would send the bytes of an image and receive back predictions from the `general` model.

{% tabs %}
{% tab title="js" %}
```javascript
app.models.predict(Clarifai.GENERAL_MODEL, {base64: "G7p3m95uAl..."}).then(
  function(response) {
    // do something with response
  },
  function(err) {
    // there was an error
  }
);
```
{% endtab %}

{% tab title="python" %}
```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.public_models.general_model
response = model.predict_by_filename('/home/user/image.jpeg')
# You could also use model.predict_by_bytes or model.predict_by_base64
```
{% endtab %}

{% tab title="java" %}
```java
client.getDefaultModels().generalModel().predict()
    .withInputs(ClarifaiInput.forImage(new File("/home/user/image.jpeg")))
    .executeSync();
```
{% endtab %}

{% tab title="csharp" %}
```csharp
using System.IO;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.PublicModels.GeneralModel.Predict(
                    new ClarifaiFileImage(File.ReadAllBytes("/home/user/image.jpeg")))
                .ExecuteAsync();
        }
    }
}
```
{% endtab %}

{% tab title="obj-c" %}
```text
UIImage *image = [UIImage imageNamed:@"dress.jpg"];
ClarifaiImage *clarifaiImage = [[ClarifaiImage alloc] initWithImage:image];
[_app getModelByName:@"general-v1.3" completion:^(ClarifaiModel *model, NSError *error) {
    [model predictOnImages:@[clarifaiImage]
                completion:^(NSArray<ClarifaiSearchResult *> *outputs, NSError *error) {
                    NSLog(@"outputs: %@", outputs);
                }];
}];
```
{% endtab %}

{% tab title="php" %}
```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiFileImage;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->publicModels()->generalModel()->predict(
        new ClarifaiFileImage(file_get_contents('/home/user/image.jpeg')))
    ->executeSync();

if ($response->isSuccessful()) {
    /** @var ClarifaiOutput $output */
    $output = $response->get();

    echo "Predicted concepts:\n";
    /** @var Concept $concept */
    foreach ($output->data() as $concept) {
        echo $concept->name() . ': ' . $concept->value() . "\n";
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
// Smaller files (195 KB or less)

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "image": {
            "base64": "'"$(base64 /home/user/image.jpeg)"'"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/{model-id}/outputs

// Larger Files (Greater than 195 KB)

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- https://api.clarifai.com/v2/models/{model-id}/outputs << FILEIN
  {
    "inputs": [
      {
        "data": {
          "image": {
            "base64": "$(base64 /home/user/image.png)"
          }
        }
      }
    ]
  }
FILEIN
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Response JSON" %}
```javascript
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "outputs": [
    {
      "id": "e1cf385843b94c6791bbd9f2654db5c0",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2016-11-22T16:59:23Z",
      "model": {
        "name": "general-v1.3",
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "created_at": "2016-03-09T17:11:39Z",
        "app_id": null,
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T01:19:12Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "e1cf385843b94c6791bbd9f2654db5c0",
        "data": {
          "image": {
            "url": "https://s3.amazonaws.com/clarifai-api/img/prod/b749af061d564b829fb816215f6dc832/e11c81745d6d42a78ef712236023df1c.jpeg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "ai_l4WckcJN",
            "name": "blur",
            "app_id": null,
            "value": 0.9973569
          },
          {
            "id": "ai_786Zr311",
            "name": "no person",
            "app_id": null,
            "value": 0.98865616
          },
          {
            "id": "ai_JBPqff8z",
            "name": "art",
            "app_id": null,
            "value": 0.986006
          },
          {
            "id": "ai_5rD7vW4j",
            "name": "wallpaper",
            "app_id": null,
            "value": 0.9722556
          },
          {
            "id": "ai_sTjX6dqC",
            "name": "abstract",
            "app_id": null,
            "value": 0.96476805
          },
          {
            "id": "ai_Dm5GLXnB",
            "name": "illustration",
            "app_id": null,
            "value": 0.922542
          },
          {
            "id": "ai_5xjvC0Tj",
            "name": "background",
            "app_id": null,
            "value": 0.8775655
          },
          {
            "id": "ai_tBcWlsCp",
            "name": "nature",
            "app_id": null,
            "value": 0.87474406
          },
          {
            "id": "ai_rJGvwlP0",
            "name": "insubstantial",
            "app_id": null,
            "value": 0.8196385
          },
          {
            "id": "ai_2Bh4VMrb",
            "name": "artistic",
            "app_id": null,
            "value": 0.8142488
          },
          {
            "id": "ai_mKzmkKDG",
            "name": "Christmas",
            "app_id": null,
            "value": 0.7996079
          },
          {
            "id": "ai_RQccV41p",
            "name": "woman",
            "app_id": null,
            "value": 0.7955615
          },
          {
            "id": "ai_20SCBBZ0",
            "name": "vector",
            "app_id": null,
            "value": 0.7775099
          },
          {
            "id": "ai_4sJLn6nX",
            "name": "dark",
            "app_id": null,
            "value": 0.7715479
          },
          {
            "id": "ai_5Kp5FMJw",
            "name": "still life",
            "app_id": null,
            "value": 0.7657637
          },
          {
            "id": "ai_LM64MDHs",
            "name": "shining",
            "app_id": null,
            "value": 0.7542407
          },
          {
            "id": "ai_swtdphX8",
            "name": "love",
            "app_id": null,
            "value": 0.74926054
          },
          {
            "id": "ai_h45ZTxZl",
            "name": "square",
            "app_id": null,
            "value": 0.7449074
          },
          {
            "id": "ai_cMfj16kJ",
            "name": "design",
            "app_id": null,
            "value": 0.73926914
          },
          {
            "id": "ai_LxrzLJmf",
            "name": "bright",
            "app_id": null,
            "value": 0.73790145
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

