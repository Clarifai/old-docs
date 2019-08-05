# Predict

### Predict

The Predict API analyzes your images or videos and tells you what's inside of them.

The API will return a list of concepts with corresponding probabilities of how likely it is these concepts are contained within the image or video.

When you make a prediction through the API, you tell it what model to use. This can be one Clarifai's pre-built models or a custom one trained by you. A model contains a group of concepts. A model will only 'see' the concepts it contains. You can also specify more parameters for predictions.

We recommend specifying the `version id` parameter in your predict calls. If no `version id` is specified, predictions will occur on the most recent version of the model. More information can be found in the [Advanced Predictions section](advanced-predict.md#by-model-version-id).

#### Images

**Via URL**

To get predictions for an input, you need to supply an image and the model you'd like to get predictions from. You can supply an image either with a publicly accessible URL or by directly sending bytes. You can send up to 128 images in one API call. You specify the model you'd like to use with the `{model-id}` parameter.

Below is an example of how you would send image URLs and receive back predictions from the `general` model.

You can learn all about the different [public models](public-models.md) available later in the guide.

```javascript
app.models.initModel({id: Clarifai.GENERAL_MODEL, version: "aa7f35c01e0642fda5cf400f543e7c40"})
      .then(generalModel => {
        return generalModel.predict("@@sampleTrain");
      })
      .then(response => {
        var concepts = response['outputs'][0]['data']['concepts']
      })
```

```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')
model = app.public_models.general_model
response = model.predict_by_url('@@sampleTrain')
```

```java
ConceptModel model = client.getDefaultModels().generalModel();
    ModelVersion modelVersion = model.getVersionByID("the-version").executeSync().get();

    ClarifaiResponse<List<ClarifaiOutput<Prediction>>> response = client.predict(model.id())
        .withInputs(ClarifaiInput.forImage("@@sampleTrain"))
        .withVersion("aa7f35c01e0642fda5cf400f543e7c40")
        .executeSync();
```

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

```objectivec
ClarifaiImage *image = [[ClarifaiImage alloc] initWithURL:@"@@sampleTrain"];
[_app getModelByName:@"general-v1.3" completion:^(ClarifaiModel *model, NSError *error) {
    [model predictOnImages:@[image]
                completion:^(NSArray<ClarifaiSearchResult *> *outputs, NSError *error) {
                    NSLog(@"outputs: %@", outputs);
                }];
}];
```

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

```bash
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

**Via Bytes**

Below is an example of how you would send the bytes of an image and receive back predictions from the `general` model.

```text

```

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

```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.public_models.general_model
response = model.predict_by_filename('/home/user/image.jpeg')
# You could also use model.predict_by_bytes or model.predict_by_base64
```

```java
client.getDefaultModels().generalModel().predict()
    .withInputs(ClarifaiInput.forImage(new File("/home/user/image.jpeg")))
    .executeSync();
```

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
  https://api.clarifai.com/v2/models/@@generalModelId/outputs

// Larger Files (Greater than 195 KB)

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- https://api.clarifai.com/v2/models/@@generalModelId/outputs << FILEIN
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

```text

```

```text
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

#### Videos

With a video input, the Predict API response will return a list of predicted concepts for every frame of a video. Video is processed at 1 frame per second. This means you will receive a list of concepts for every second of your video.

You can run Predict on your video using a select number of [public models](/models). The models that are currently supported are: Apparel, Food, General, NSFW, Travel, and Wedding. You make an API call by providing the `{model-id}` parameter and your data parameter is `video` instead of `image`.

**Video Limits**

The Predict API has limits to the length and size it can support. A video, uploaded through URL, can be anywhere up to 80MB in size or 10mins in length. When a video is sent through by bytes, the Predict API can support 10MB in size.

If your video exceeds the limits, please follow our [tutorial](https://docs.google.com/document/d/1mL1q5CIrgOauNlTe-PwokOiaDZ_4yyEzBjapl9BZbJc/edit?usp=sharing) on how to break up a large video into smaller components, and send those into the Video API. Otherwise, the processing will time out and you will receive an error response.

**Via URL**

Below is an example of how you would send video URLs and receive back predictions from the `general` model.

```text

```

```javascript
const Clarifai = require('clarifai');

const app = new Clarifai.App({apiKey: 'YOUR_API_KEY'});

app.models.predict(
    Clarifai.GENERAL_MODEL,
    'https://samples.clarifai.com/beer.mp4',
    {video: true, sampleMs: 1000})
  .then(response => {
    let frames = response['outputs'][0]['data']['frames'];
    frames.forEach(frame => {
      console.log('Concepts in frame at time: ' + frame['frame_info']['time'] + 'ms');
      frame['data']['concepts'].forEach(concept => {
        console.log(' ' + concept['name'] + ' ' + concept['value']);
      });
    });
  })
  .catch(error => {
    console.log('Error status code: ' + error.data['status']['code']);
    console.log('Error description: ' + error.data['status']['description']);
    if (error.data['status']['details'])
    {
      console.log('Error details: ' + error.data['status']['details']);
    }
  });
```

```python
from clarifai.errors import ApiError
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')

m = app.public_models.general_model

try:
    response = m.predict_by_url('https://samples.clarifai.com/beer.mp4',
                                is_video=True,
                                sample_ms=1000)
except ApiError as e:
    print('Error status code: %d' % e.error_code)
    print('Error description: %s' % e.error_desc)
    if e.error_details:
        print('Error details: %s' % e.error_details)
    exit(1)

frames = response['outputs'][0]['data']['frames']
for frame in frames:
    print('Concepts in frame at time: %d ms' % frame['frame_info']['time'])
    for concept in frame['data']['concepts']:
        print(' %s %f' % (concept['name'], concept['value']))
```

```java
import clarifai2.api.ClarifaiBuilder;
import clarifai2.api.ClarifaiClient;
import clarifai2.api.ClarifaiResponse;
import clarifai2.dto.input.ClarifaiInput;
import clarifai2.dto.model.VideoModel;
import clarifai2.dto.model.output.ClarifaiOutput;
import clarifai2.dto.prediction.Concept;
import clarifai2.dto.prediction.Frame;

import java.util.List;

public class YourClassName {
    public static void main(String[] args) {

        ClarifaiClient client = new ClarifaiBuilder("YOUR_API_KEY")
                .buildSync();

        VideoModel model = client .getDefaultModels().generalVideoModel();
        ClarifaiResponse<List<ClarifaiOutput<Frame>>> response = model.predict()
                .withInputs(ClarifaiInput.forVideo("https://samples.clarifai.com/beer.mp4"))
                .withSampleMs(1000)
                .executeSync();

        if (response.isSuccessful()) {
            List<Frame> frames = response.get().get(0).data();
            for (Frame frame : frames) {
                System.out.println("Concepts in frame at time: " + frame.time() + " ms");
                for (Concept concept : frame.concepts()) {
                    System.out.println(" " + concept.name() + " " + concept.value());
                }
            }

        } else {
            System.out.println("Error status code: " + response.getStatus().statusCode());
            System.out.println("Error description: " + response.getStatus().description());
            if (response.getStatus().errorDetails() != null) {
                System.out.println("Error details: " + response.getStatus().errorDetails());
            }
        }
    }
}
```

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.API.Responses;
using Clarifai.DTOs.Inputs;
using Clarifai.DTOs.Models;
using Clarifai.DTOs.Models.Outputs;
using Clarifai.DTOs.Predictions;

namespace YourPackageName
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            VideoModel model = client.PublicModels.GeneralVideoModel;

            ClarifaiResponse<ClarifaiOutput<Frame>> response = await model
                .Predict(
                    input: new ClarifaiURLVideo("https://samples.clarifai.com/beer.mp4"),
                    sampleMs: 1000
                )
                .ExecuteAsync();

            if (response.IsSuccessful)
            {
                List<Frame> frames = response.Get().Data;
                foreach (Frame frame in frames)
                {
                    Console.WriteLine($"Concepts in frame at time {frame.Time}:");
                    foreach (Concept concept in frame.Concepts)
                    {
                        Console.WriteLine($" {concept.Name} {concept.Value}");
                    }
                }
            }
            else
            {
                Console.WriteLine($"Error status code: {response.Status.StatusCode}");
                Console.WriteLine($"Error description: {response.Status.Description}");
                if (response.Status.ErrorDetails != null)
                {
                    Console.WriteLine($"Error details: {response.Status.ErrorDetails}");
                }
            }
        }
    }
}
```

```text
Objective-C client details coming soon
```

```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLVideo;
use Clarifai\DTOs\Models\VideoModel;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;
use Clarifai\DTOs\Predictions\Frame;

$client = new ClarifaiClient('YOUR_API_KEY');

/** @var VideoModel $model */
$model = $client->publicModels()->generalVideoModel();

$response = $model->predict(
        new ClarifaiURLVideo('https://samples.clarifai.com/beer.mp4'))
    ->withSampleMs(1000)
    ->executeSync();

if ($response->isSuccessful()) {
    /** @var ClarifaiOutput $output */
    $output = $response->get();
    /** @var Frame[] $frames */
    $frames = $output->data();

    foreach ($frames as $frame) {
        echo "Concepts in frame at time: {$frame->time()}\n";
        /** @var Concept $concept */
        foreach ($frame->concepts() as $concept) {
            echo " {$concept->name()} {$concept->value()}\n";
        }
    }
} else {
    echo "Error status code: {$response->status()->statusCode()}";
    echo "Error description: {$response->status()->description()}";
    if ($response->status()->errorDetails()) {
        echo "Error details: {$response->status()->errorDetails()}";
    }
}
```

```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "video": {
            "url": "https://samples.clarifai.com/beer.mp4"
          }
        }
      }
    ],
    "model": {
      "output_info": {
        "output_config": {
          "sample_ms": 1000
        }
      }
    }
  }'\
  https://api.clarifai.com/v2/models/@@generalModelId/outputs
```

```text

```

```text
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "outputs": [
    {
      "id": "d8234da5d1f04ca8a2e13e34d51f9b85",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-06-28T14:58:41.835370141Z",
      "model": {
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "name": "general-v1.3",
        "created_at": "2016-03-09T17:11:39.608845Z",
        "app_id": "main",
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept",
          "type_ext": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T01:19:12.147644Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "f0fc1a005f124d389da4d80823a3125b",
        "data": {
          "video": {
            "url": "https://samples.clarifai.com/beer.mp4"
          }
        }
      },
      "data": {
        "frames": [
          {
            "frame_info": {
              "index": 0,
              "time": 0
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.98658466,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": "main"
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.9783862,
                  "app_id": "main"
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.97157896,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.96628696,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.95581007,
                  "app_id": "main"
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.92861253,
                  "app_id": "main"
                },
                {
                  "id": "ai_7vR9zv7l",
                  "name": "bubble",
                  "value": 0.9082134,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9020835,
                  "app_id": "main"
                },
                {
                  "id": "ai_7Xg5SQRW",
                  "name": "luxury",
                  "value": 0.8990605,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.89708906,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": "main"
                },
                {
                  "id": "ai_7qwGxLch",
                  "name": "gold",
                  "value": 0.8892093,
                  "app_id": "main"
                },
                {
                  "id": "ai_wmbvr5TG",
                  "name": "celebration",
                  "value": 0.88606626,
                  "app_id": "main"
                },
                {
                  "id": "ai_4lvjn8qv",
                  "name": "closeup",
                  "value": 0.881963,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": "main"
                },
                {
                  "id": "ai_12dz73B9",
                  "name": "bottle",
                  "value": 0.86288416,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.86252767,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.86069393,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 1,
              "time": 1000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.98658466,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": "main"
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.9783862,
                  "app_id": "main"
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.97157896,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.96628696,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.95581007,
                  "app_id": "main"
                },
                {
                  "id": "ai_7vR9zv7l",
                  "name": "bubble",
                  "value": 0.9082134,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9020835,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.89708906,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": "main"
                },
                {
                  "id": "ai_7qwGxLch",
                  "name": "gold",
                  "value": 0.8834515,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": "main"
                },
                {
                  "id": "ai_b01mhdxB",
                  "name": "party",
                  "value": 0.8603341,
                  "app_id": "main"
                },
                {
                  "id": "ai_XNmzgDnF",
                  "name": "pub",
                  "value": 0.85809004,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.85319245,
                  "app_id": "main"
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.8506696,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.84634554,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": "main"
                },
                {
                  "id": "ai_wmbvr5TG",
                  "name": "celebration",
                  "value": 0.8383831,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 2,
              "time": 2000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9856042,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": "main"
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.9755833,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9733174,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.94170487,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.92778283,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9227257,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": "main"
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.90887475,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.87420183,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.8699659,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": "main"
                },
                {
                  "id": "ai_XNmzgDnF",
                  "name": "pub",
                  "value": 0.85809004,
                  "app_id": "main"
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.8506696,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": "main"
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.8397074,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 3,
              "time": 3000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.996614,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9794438,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9733174,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.9645849,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.94761443,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.92864025,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9227257,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.91797745,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.889248,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.8689867,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.86591685,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8546975,
                  "app_id": "main"
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8544879,
                  "app_id": "main"
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.852397,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": "main"
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.837438,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 4,
              "time": 4000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.996614,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9748836,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.9645849,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.96217895,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9030821,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.8983356,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.894987,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.889248,
                  "app_id": "main"
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8860091,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.8837219,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8712319,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.8695712,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.8664293,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8546975,
                  "app_id": "main"
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.852397,
                  "app_id": "main"
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 5,
              "time": 5000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.997158,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97719705,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9748836,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.96217895,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9210669,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9124408,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.90667903,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9046865,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9030821,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.8983356,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.8947689,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8852426,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8789175,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.8762902,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.87279737,
                  "app_id": "main"
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8544879,
                  "app_id": "main"
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.849733,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 6,
              "time": 6000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.99790645,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9273318,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.892028,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.88797945,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": "main"
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 7,
              "time": 7000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.99790645,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9273318,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.892028,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8913312,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": "main"
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": "main"
                }
              ]
            }
          },
          {
            "frame_info": {
              "index": 8,
              "time": 8000
            },
            "data": {
              "concepts": [
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.99790645,
                  "app_id": "main"
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": "main"
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": "main"
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": "main"
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": "main"
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9210669,
                  "app_id": "main"
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": "main"
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": "main"
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": "main"
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": "main"
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": "main"
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": "main"
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": "main"
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": "main"
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": "main"
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.88797945,
                  "app_id": "main"
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": "main"
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": "main"
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": "main"
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": "main"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
```

**Via Bytes**

Below is an example of how you would send the bytes of a video and receive back predictions from the general model.

```text

```

```javascript
const Clarifai = require('clarifai');

const app = new Clarifai.App({apiKey: 'YOUR_API_KEY'});

app.models.predict(
    Clarifai.GENERAL_MODEL,
    {base64: 'AAAAIGZ...'},
    {video: true, sampleMs: 1000})
  .then(response => {
    let frames = response['outputs'][0]['data']['frames'];
    frames.forEach(frame => {
      console.log('Concepts in frame at time: ' + frame['frame_info']['time'] + 'ms');
      frame['data']['concepts'].forEach(concept => {
        console.log(' ' + concept['name'] + ' ' + concept['value']);
      });
    });
  })
  .catch(error => {
    console.log('Error status code: ' + error.data['status']['code']);
    console.log('Error description: ' + error.data['status']['description']);
    if (error.data['status']['details']) {
      console.log('Error details: ' + error.data['status']['details']);
    }
  });
```

```python
from clarifai.errors import ApiError
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='YOUR_API_KEY')

m = app.public_models.general_model

try:
    # There are also methods m.predict_by_base64 and m.predict_by_bytes
    response = m.predict_by_filename('video_file_path.mp4',
                                     is_video=True,
                                     sample_ms=1000)
except ApiError as e:
    print('Error status code: %d' % e.error_code)
    print('Error description: %s' % e.error_desc)
    if e.error_details:
        print('Error details: %s' % e.error_details)
    exit(1)

frames = response['outputs'][0]['data']['frames']
for frame in frames:
    print('Concepts in frame at time: %d ms' % frame['frame_info']['time'])
    for concept in frame['data']['concepts']:
        print(' %s %f' % (concept['name'], concept['value']))
```

```java
import clarifai2.api.ClarifaiBuilder;
import clarifai2.api.ClarifaiClient;
import clarifai2.api.ClarifaiResponse;
import clarifai2.dto.input.ClarifaiInput;
import clarifai2.dto.model.VideoModel;
import clarifai2.dto.model.output.ClarifaiOutput;
import clarifai2.dto.prediction.Concept;
import clarifai2.dto.prediction.Frame;

import java.io.File;
import java.util.List;

public class YourClassName {
    public static void main(String[] args) {

        ClarifaiClient client = new ClarifaiBuilder("YOUR_API_KEY")
                .buildSync();

        VideoModel model = client .getDefaultModels().generalVideoModel();
        ClarifaiResponse<List<ClarifaiOutput<Frame>>> response = model.predict()
                .withInputs(ClarifaiInput.forVideo(new File("video_file_path.mp4")))
                .withSampleMs(1000)
                .executeSync();

        if (response.isSuccessful()) {
            List<Frame> frames = response.get().get(0).data();
            for (Frame frame : frames) {
                System.out.println("Concepts in frame at time: " + frame.time() + " ms");
                for (Concept concept : frame.concepts()) {
                    System.out.println(" " + concept.name() + " " + concept.value());
                }
            }

        } else {
            System.out.println("Error status code: " + response.getStatus().statusCode());
            System.out.println("Error description: " + response.getStatus().description());
            if (response.getStatus().errorDetails() != null) {
                System.out.println("Error details: " + response.getStatus().errorDetails());
            }
        }
    }
}
```

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.API.Responses;
using Clarifai.DTOs.Inputs;
using Clarifai.DTOs.Models;
using Clarifai.DTOs.Models.Outputs;
using Clarifai.DTOs.Predictions;

namespace YourPackageName
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            VideoModel model = client.PublicModels.GeneralVideoModel;

            ClarifaiResponse<ClarifaiOutput<Frame>> response = await model
                .Predict(
                    input: new ClarifaiFileVideo(File.ReadAllBytes("video_file_path.mp4")),
                    sampleMs: 1000
                )
                .ExecuteAsync();

            if (response.IsSuccessful)
            {
                List<Frame> frames = response.Get().Data;
                foreach (Frame frame in frames)
                {
                    Console.WriteLine($"Concepts in frame at time {frame.Time}:");
                    foreach (Concept concept in frame.Concepts)
                    {
                        Console.WriteLine($" {concept.Name} {concept.Value}");
                    }
                }
            }
            else
            {
                Console.WriteLine($"Error status code: {response.Status.StatusCode}");
                Console.WriteLine($"Error description: {response.Status.Description}");
                if (response.Status.ErrorDetails != null)
                {
                    Console.WriteLine($"Error details: {response.Status.ErrorDetails}");
                }
            }
        }
    }
}
```

```text
Objective-C client details coming soon
```

```php
use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiFileVideo;
use Clarifai\DTOs\Models\VideoModel;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;
use Clarifai\DTOs\Predictions\Frame;

$client = new ClarifaiClient('YOUR_API_KEY');

/** @var VideoModel $model */
$model = $client->publicModels()->generalVideoModel();

$response = $model->predict(
        new ClarifaiFileVideo(file_get_contents('video_file_path.mp4')))
    ->withSampleMs(1000)
    ->executeSync();

if ($response->isSuccessful()) {
    /** @var ClarifaiOutput $output */
    $output = $response->get();
    /** @var Frame[] $frames */
    $frames = $output->data();

    foreach ($frames as $frame) {
        echo "Concepts in frame at time: {$frame->time()}\n";
        /** @var Concept $concept */
        foreach ($frame->concepts() as $concept) {
            echo " {$concept->name()} {$concept->value()}\n";
        }
    }
} else {
    echo "Error status code: {$response->status()->statusCode()}\n";
    echo "Error description: {$response->status()->description()}\n";
    if ($response->status()->errorDetails()) {
        echo "Error details: {$response->status()->errorDetails()}\n";
    }
}
```

```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "video": {
            "base64": "'"$(base64 video_file_path.mp4)"'"
          }
        }
      }
    ],
    "model": {
      "output_info": {
        "output_config": {
          "sample_ms": 1000
        }
      }
    }
  }'\
  https://api.clarifai.com/v2/models/@@generalModelId/outputs
```

```text

```

```text
{
    "status": {
        "code": 10000,
        "description": "Ok"
    },
    "outputs": [
        {
            "id": "f6f9e1b007d742fb9d777f35cf3bffd0",
            "status": {
                "code": 10000,
                "description": "Ok"
            },
            "created_at": "2017-06-28T16:00:51.258194418Z",
            "model": {
                "id": "aaa03c23b3724a16a56b629203edc62c",
                "name": "general-v1.3",
                "created_at": "2016-03-09T17:11:39.608845Z",
                "app_id": "main",
                "output_info": {
                    "message": "Show output_info with: GET /models/{model_id}/output_info",
                    "type": "concept",
                    "type_ext": "concept"
                },
                "model_version": {
                    "id": "aa9ca48295b37401f8af92ad1af0d91d",
                    "created_at": "2016-07-13T01:19:12.147644Z",
                    "status": {
                        "code": 21100,
                        "description": "Model trained successfully"
                    }
                }
            },
            "input": {
                "id": "b17d29ad1b714869a8c729e510ab22d0",
                "data": {
                    "video": {
                        "url": "https://s3.amazonaws.com/clarifai-api/vid/prod/ib81c84d5b2341858b86da18a2bd21d2/e86fbf516521425098081dd42e157a12",
                        "base64": "true"
                    }
                }
            },
            "data": {
                "frames": [
                    {
                        "frame_info": {
                            "index": 0,
                            "time": 0
                        },
                        "data": {
                            "concepts": [
                                {
                                    "id": "ai_VTlCx2f2",
                                    "name": "window",
                                    "value": 0.99909437,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_l8TKp2h5",
                                    "name": "people",
                                    "value": 0.99610686,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_VPmHr5bm",
                                    "name": "adult",
                                    "value": 0.9958472,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_SVshtN54",
                                    "name": "one",
                                    "value": 0.9937376,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_TJ9wFfK5",
                                    "name": "portrait",
                                    "value": 0.9899301,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_ZrPNDjxN",
                                    "name": "daylight",
                                    "value": 0.9885398,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_dxSG2s86",
                                    "name": "man",
                                    "value": 0.9833108,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_86sS08Pw",
                                    "name": "wear",
                                    "value": 0.9807093,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_GxSDhQ34",
                                    "name": "facial expression",
                                    "value": 0.9769263,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_Pf2b7clG",
                                    "name": "indoors",
                                    "value": 0.96838474,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_VRmbGVWh",
                                    "name": "travel",
                                    "value": 0.96641624,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_XNzGRk0F",
                                    "name": "side view",
                                    "value": 0.9603646,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_Zmhsv0Ch",
                                    "name": "outdoors",
                                    "value": 0.9434113,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_n9vjC1jB",
                                    "name": "light",
                                    "value": 0.94182396,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_WcnFrjw1",
                                    "name": "backlit",
                                    "value": 0.9347838,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_QKqjh1CM",
                                    "name": "vehicle window",
                                    "value": 0.92699903,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_mlrv94tv",
                                    "name": "reflection",
                                    "value": 0.90993655,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_41s912fX",
                                    "name": "fair weather",
                                    "value": 0.90100014,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_rsX6XWc2",
                                    "name": "building",
                                    "value": 0.88111985,
                                    "app_id": "main"
                                },
                                {
                                    "id": "ai_L83krFdq",
                                    "name": "veil",
                                    "value": 0.8785704,
                                    "app_id": "main"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}
```

