### Languages

The Clarifai API supports many languages in addition to English. When making a
[predict api request](predict.md), you can pass in the language you would like the
concepts returned in.

#### Supported Languages

Language | Code
--- | ---
Aravic (ar) | ar

#### Supported Models

The only public model which supports languages other than English is the
[General model](https://www.clarifai.com/models/general-image-recognition-model-aaa03c23b3724a16a56b629203edc62c). If you make a predict request using a language other
than English on a public model other than General, you will receive an error.

#### Default Language

When you create a new Application, you must specify a default language. This will be the default language
concepts are returned in when you do not explicitly set a language in an API request. You cannot change the
default language. You can however change languages per request.

![create new app](/images/create-new-app-new.png)

#### Example Predict API Request

You can predict concepts in a language other then the Application's default, by explicitly passing in the
language. Here is how you predict concepts in Chinese:



```js

app.models.predict(Clarifai.GENERAL_MODEL, "https://samples.clarifai.com/metro-north.jpg", {language: 'zh'}).then(
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

m = app.models.get('general-v1.3')

# predict labels in simplified Chinese
m.predict_by_url('https://samples.clarifai.com/metro-north.jpg', lang='zh')

# predict labels in Japanese
m.predict_by_url('https://samples.clarifai.com/metro-north.jpg', lang='ja')

```

```java

client.predict(client.getDefaultModels().generalModel().id())
    .withInputs(ClarifaiInput.forImage("https://samples.clarifai.com/metro-north.jpg"))
    .withLanguage("zh")
    .executeSync();

```

```csharp

using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Inputs;
using Clarifai.DTOs.Predictions;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.Predict<Concept>(
                    client.PublicModels.GeneralModel.ModelID,
                    input: new ClarifaiURLImage("https://samples.clarifai.com/metro-north.jpg"),
                    language: "zh")
                .ExecuteAsync();
        }
    }
}

```

```objective-c

// first get the general model.
[app getModelByName:@"general-v1.3" completion:^(ClarifaiModel *model, NSError *error) {
  // create input to predict on.
  ClarifaiImage *input = [[ClarifaiImage alloc] initWithURL:@"https://samples.clarifai.com/metro-north.jpg"];

  // predict with the general model in Chinese.
  [model predictOnImages:@[input] withLanguage:@"zh" completion:^(NSArray<ClarifaiOutput *> *outputs, NSError *error) {
    for (ClarifaiConcept *concept in outputs[0].concepts) {
      NSLog(@"tag: %@", concept.conceptName);
      NSLog(@"probability: %f", concept.score);
    }
  }];
}];

```

```php

use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Inputs\ClarifaiURLImage;
use Clarifai\DTOs\Models\ModelType;
use Clarifai\DTOs\Outputs\ClarifaiOutput;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient();

$response = $client->predict(ModelType::concept(),
        $client->publicModels()->generalModel()->modelID(),
        new ClarifaiURLImage('https://samples.clarifai.com/metro-north.jpg'))
    ->withLanguage('zh')
    ->executeSync();

if ($response-> isSuccessful()) {
    $output = $response->get();

    echo "Predicted concepts:\n";
    
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

```cURL

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
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
  ],
  "model":{
    "output_info":{
      "output_config":{
        "language":"zh"
      }
    }
  }
}'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs

```



```response
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "outputs": [
    {
      "id": "b9f3c12f1534440fa984dc463e491780",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-01-31T20:59:27Z",
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
        "id": "b9f3c12f1534440fa984dc463e491780",
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
            "name": "铁路列车",
            "app_id": null,
            "value": 0.9989112
          },
          {
            "id": "ai_fvlBqXZR",
            "name": "铁路",
            "app_id": null,
            "value": 0.9975532
          },
          {
            "id": "ai_Xxjc3MhT",
            "name": "运输系统",
            "app_id": null,
            "value": 0.9959158
          },
          {
            "id": "ai_6kTjGfF6",
            "name": "站",
            "app_id": null,
            "value": 0.992573
          },
          {
            "id": "ai_RRXLczch",
            "name": "火车",
            "app_id": null,
            "value": 0.992556
          },
          {
            "id": "ai_VRmbGVWh",
            "name": "旅游",
            "app_id": null,
            "value": 0.98789215
          },
          {
            "id": "ai_SHNDcmJ3",
            "name": "地铁",
            "app_id": null,
            "value": 0.9816359
          },
          {
            "id": "ai_jlb9q33b",
            "name": "通勤",
            "app_id": null,
            "value": 0.9712483
          },
          {
            "id": "ai_46lGZ4Gm",
            "name": "铁路",
            "app_id": null,
            "value": 0.9690325
          },
          {
            "id": "ai_tr0MBp64",
            "name": "交通",
            "app_id": null,
            "value": 0.9687052
          },
          {
            "id": "ai_l4WckcJN",
            "name": "模煳",
            "app_id": null,
            "value": 0.9667078
          },
          {
            "id": "ai_2gkfMDsM",
            "name": "平台",
            "app_id": null,
            "value": 0.9624243
          },
          {
            "id": "ai_CpFBRWzD",
            "name": "城市的",
            "app_id": null,
            "value": 0.960752
          },
          {
            "id": "ai_786Zr311",
            "name": "沒有人",
            "app_id": null,
            "value": 0.95864904
          },
          {
            "id": "ai_6lhccv44",
            "name": "商业",
            "app_id": null,
            "value": 0.95720303
          },
          {
            "id": "ai_971KsJkn",
            "name": "跑道",
            "app_id": null,
            "value": 0.9494642
          },
          {
            "id": "ai_WBQfVV0p",
            "name": "城市",
            "app_id": null,
            "value": 0.94089437
          },
          {
            "id": "ai_dSCKh8xv",
            "name": "快速的",
            "app_id": null,
            "value": 0.9399334
          },
          {
            "id": "ai_TZ3C79C6",
            "name": "马路",
            "app_id": null,
            "value": 0.93121606
          },
          {
            "id": "ai_VSVscs9k",
            "name": "终点站",
            "app_id": null,
            "value": 0.9230834
          }
        ]
      }
    }
  ]
}
```

#### Example Search By Tag API Request

You can search for concepts in other languages even if the default language of your application is English.
When you add inputs to your application, concepts are predicted for every language. Here is an example of
searching for '人' which is simplified Chinese for 'people'.



```js

app.inputs.search({
  concept: {
    name: '人'
  },
  language: 'ja'
}).then(
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

# search '人' in simplified Chinese
app.inputs.search_by_predicted_concepts(u'人', lang='zh')

```

```java

client.searchInputs(
    SearchClause.matchImageURL(ClarifaiImage.of("https://samples.clarifai.com/metro-north.jpg")))
    .withLanguage("zh")
    .getPage(1)
    .executeSync();

```

```csharp

using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Searches;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.SearchInputs(
                    new List<SearchBy>
                    {
                        SearchBy.ImageURL("https://samples.clarifai.com/metro-north.jpg")
                    },
                    language: "zh")
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

```objective-c

// create search term with concept you want to search predicted inputs with.
ClarifaiConcept *concept1 = [[ClarifaiConcept alloc] initWithConceptName:@"人"];
ClarifaiSearchTerm *searchTerm = [[ClarifaiSearchTerm alloc] initWithSearchItem:concept1 isInput:NO];

// search will find inputs predicted to be associated with the given concept.
[_app search:@[searchTerm] page:@1 perPage:@20 language:@"zh" completion:^(NSArray<ClarifaiSearchResult *> *results, NSError *error) {
  for (ClarifaiSearchResult *result in results) {
    NSLog(@"image url: %@", result.mediaURL);
    NSLog(@"probability: %f", [result.score floatValue]);
  }
}];


```

```php

use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Searches\SearchBy;
use Clarifai\DTOs\Searches\SearchInputsResult;

$client = new ClarifaiClient();

$response = $client->searchInputs(
        SearchBy::imageURL('https://samples.clarifai.com/metro-north.jpg'))
    ->withLanguage('zh')
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";

    /** @var SearchInputsResult $result */
    $result = $response->get();
    foreach ($result->searchHits() as $searchHit) {
        echo $searchHit->input()->id() . ' ' . $searchHit->score() . "\n";
    }
} else {
    echo "Response is not successful. Reason: \n";
    echo $response->status()->description() . "\n";
    echo $response->status()->errorDetails() . "\n";
    echo "Status code: " . $response->status()->statusCode();
}

```

```cURL

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "query": {
      "ands": [
        {
          "output": {
            "data": {
              "concepts": [
                {
                  "name": "人"
                }
              ]
            }
          }
        }
      ],
      "language": "zh"
    }
  }'\
  https://api.clarifai.com/v2/searches

```



#### Example Search Concepts API Request

You can also search for concepts in a different language:




```js

app.concepts.search('人*', 'zh').then(
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
app.concepts.search(u'人*', lang='zh')

```

```java

client.searchConcepts("人*")
    .withLanguage("zh")
    .getPage(1)
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

            await client.SearchConcepts(
                    "人*",
                    language: "zh")
                .Page(1)
                .ExecuteAsync();
        }
    }
}

```

```objective-c

// Search for all concept names in chinese, beginning with "人".
[_app searchForConceptsByName:@"人*" andLanguage:@"zh" completion:^(NSArray<ClarifaiConcept *> *concepts, NSError *error) {
  for (ClarifaiConcept *concept in concepts) {
    NSLog(@"tag name: %@", concept.conceptName);
  }
}];


```

```php

use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Predictions\Concept;

$client = new ClarifaiClient();

$response = $client->searchConcepts('人*')
    ->withLanguage('zh')
    ->executeSync();

if ($response->isSuccessful()) {
    echo "Response is successful.\n";

    $concepts = $response->get();

    foreach ($concepts as $concept) {
        echo $concept->name() . ' ' . $concept->value() . "\n";
    }
} else {
    echo "Response is not successful. Reason: \n";
    echo $response->status()->description() . "\n";
    echo $response->status()->errorDetails() . "\n";
    echo "Status code: " . $response->status()->statusCode();
}

```

```cURL

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "concept_query": {
      "name":"人*",
      "language": "zh"
    }
  }'\
  https://api.clarifai.com/v2/concepts/searches

```



```response
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "concepts": [
    {
      "id": "ai_l8TKp2h5",
      "name": "人",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_ZKJ48TFz",
      "name": "人",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_GlPlRlTZ",
      "name": "人为破坏",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_8ZsdCrVZ",
      "name": "人体模型",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_K1KL0zgk",
      "name": "人力的",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_Tm9d2BZ2",
      "name": "人口",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_NLF8h1fJ",
      "name": "人口",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_8bHdFtsg",
      "name": "人口",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_vLnr3Mcj",
      "name": "人孔",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_HRt4nfvL",
      "name": "人工智能",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_Qc3mqxTJ",
      "name": "人才",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_VFKQ0qD6",
      "name": "人物",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_Wz8JXXMB",
      "name": "人类免疫缺陷病毒",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_bzp3Lg81",
      "name": "人类的",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_dJ15S9s6",
      "name": "人群",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_MNCVrmml",
      "name": "人行天桥",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_CChWH41S",
      "name": "人行横道",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_4lbXrFgT",
      "name": "人造",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_277LRf4d",
      "name": "人造卫星",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_H3RDmvSn",
      "name": "人造奶油",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    }
  ]
}
```
