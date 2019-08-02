## Feedback
The feedback endpoint allows you to send feedback on your prediction and search responses. Currently, you can send feedback on 3 types of responses: 1. predictions without regions, 2. predictions with regions, and 3. searches. The request bodies are slightly different but all share the `feedback_info` component. Note that sending feedback will not result in immediate changes to your predictions or searches, but you may see accuracy improvements to them over time as we aggregate the feedback for evaluation and improvement of your models.

We highly encourage integrating feedback into your application as this dramatically improves accuracy of models over time. You or users of your application can correct errors, such as: if the system returned cat for an image of a dog, you can send feedback with add_tags="dog", remove_tags="cat". You can also use feedback to further enhance the models by suggesting a new concept or region, such as: if the model returned "dog", you can add a new concept called "laborador_retriever".

The feedback endpoint does not count towards your usage limits. Please use it as much as you can.

### Feedback Info
The feedback info object allows for specific information to be recorded
from your application and your end users. All fields are optional unless noted.

  * • `event_type` [required] - Use `'annotation'` for prediction feedback, and use `'search_click'` for search feedback.
  * • `output_id`/`search_id` [required] - the id associated with the output or search received
  from a given API call. With this, the API can traceback the response.
  * • `end_user_id` - the id associated with your end user. If you want to be able
  to understand which user was producing this feedback, you can associate it with this field.
  * • `session_id` - the id associated with your user's interface. This is allows you
  to understand what the user was doing during that time and allows you an avenue
  to investigate more.

### Prediction Feedback
To send feedback on predictions, you can use `POST /v2/models/{model_id}/feedback`.

Please use this request to send feedback on the model prediction responses without any region data. This includes any feedback on concept models such as General, Food, and Travel models.

In each request body, you can send

  * • concept `id`: either the correct concept name that you defined or the id that Clarifai defined in the predict response
  * • concept `value`: `true` if the concept is present in the input, or `false` if it is not present in the input

This allows for our model to re-evaluate the concept and improve the accuracy of our predictions.

Note that the `event_type` should be set to `annotation`.




```js
app.models.feedback(Clarifai.GENERAL_MODEL, 'https://samples.clarifai.com/dog.tiff', {
  id: '{input_id}',
  data: {
    concepts: [
      {'id': 'ai_8S2Vq3cR', 'value': true },
      {'id': 'ai_mFqxrph2', 'value': false }
    ]
  },
  info: {
    'eventType':  'annotation',
    'outputId':   '{output_id}',
    'endUserId':  '{end_user_id}',
    'sessionId':  '{session_id}'
  }
})
  .then(response => {
    // There was a successful response
  })
  .catch(error => {
    // There was an error
  });
```

```python
from clarifai.rest import ClarifaiApp, FeedbackInfo
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('general-v1.3')

model.send_concept_feedback(
    input_id='{input_id}', 
    url='https://samples.clarifai.com/dog.tiff', 
    concepts=['ai_8S2Vq3cR'], 
    not_concepts=['ai_mFqxrph2'], 
    feedback_info=FeedbackInfo(event_type='annotation', 
                               output_id='{output_id}', 
                               end_user_id='{end_user_id}', 
                               session_id='{session_id}'))
```

```java
ModelFeedbackRequest request =
    client.modelFeedback(client.getDefaultModels().generalModel().id())
       .withInputId("{input_id}")
       .withImageUrl("https://samples.clarifai.com/dog.tiff")
       .withConcepts(
           ConceptFeedback.forIdAndValue("ai_8S2Vq3cR", true),
           ConceptFeedback.forIdAndValue("ai_mFqxrph2", false)
       )
       .withEventType("annotation")
       .withOutputId("{output_id}")
       .withEndUserId("{end_user_id}")
       .withSessionId("{session_id}");
```

```csharp

using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs.Feedbacks;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModelFeedback(
                    client.PublicModels.GeneralModel.ModelID,
                    imageUrl: "https://samples.clarifai.com/dog.tiff",
                    inputID: "inputID",
                    outputID: "{output_id}",
                    endUserID: "{end_user_id}",
                    sessionID: "{session_id}",
                    concepts: new List<ConceptFeedback>
                    {
                        new ConceptFeedback("ai_8S2Vq3cR", true),
                        new ConceptFeedback("ai_mFqxrph2", false)
                    }
                )
                .ExecuteAsync();
        }
    }
}

```

```objective-c
// Coming Soon
```

```php

use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Feedbacks\ConceptFeedback;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modelFeedback(
        $client->publicModels()->generalModel()->modelID(),
        'https://samples.clarifai.com/dog.tiff',
        '{input-id}',
        '{output-id}',
        '{end-user-id}',
        '{session-id}')
        ->withConceptFeedbacks([
            new ConceptFeedback('ai_8S2Vq3cR', true),
            new ConceptFeedback('ai_mFqxrph2', false),
        ])
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";
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
    "input": {
      "id": "{input_id}",
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/dog.tiff"
        },
        "concepts":[
          {"id": "ai_8S2Vq3cR", "value": true },
          {"id": "ai_mFqxrph2", "value": false }
        ]
      },
      "feedback_info":{
        "event_type":   "annotation",
        "output_id":    "{output_id}",
        "end_user_id":  "{end_user_id}",
        "session_id":   "{session_id}"
      }
    }
  }'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/feedback
```



```response
{
    "status": {
        "code": 10000,
        "description": "Ok"
    }
}
```

### Prediction with Regions Feedback
To send feedback on predictions, you can use `POST /v2/models/{model_id}/feedback`.

Please use this request to send feedback on the model prediction responses with region data. This includes any feedback on detection models such as Face Detection, Demographic, Celebrity, and Logo models. These models return a list of `region` objects, each of which contains local coordinates and detected concepts.

In the request body for the feedback for predictions with regions, you can send each `region` object with:

  * • correct `bounding_box` coordinates of the region
  * • `feedback` for the originally predicted region: `accurate` if it's correct, `misplaced` if the coordinates should be modified, `not_detected` if the region was not originally detected by the model, or `false_positive` if the region should not have been detected by the model
  * • concept `id`: either the correct concept name that you defined or the id that Clarifai defined in the predict response
  * • concept `value`: `true` if the concept is present in the input, or `false` if it is not present in the input

Note that the `event_type` should be set to `annotation`.



```js
app.models.feedback(Clarifai.LOGO_MODEL, 'https://clarifai.com/images/model-samples/logo-002.jpg', {
  id: '{input_id}',
  data: {
    'regions': [
       {
         'region_info': {
           'bounding_box': {
             'top_row': 0.3,
             'left_col': 0.2,
             'bottom_row': 0.7,
             'right_col': 0.8
           },
           'feedback': 'accurate'
         },
         'data': {
           'concepts': [
             {"id": "ai_TG4GHlnf", "value": true }
           ]
         }
       }
     ]
   },
  info: {
    'eventType':  'annotation',
    'outputId':   '{output_id}',
    'endUserId':  '{end_user_id}',
    'sessionId':  '{session_id}'
   }
 })
  .then(response => {
    // There was a successful response
  })
  .catch(error => {
    // There was an error
  });
```

```python
from clarifai.rest import ClarifaiApp, Region, RegionInfo, BoundingBox, Concept, FeedbackInfo
app = ClarifaiApp(api_key='YOUR_API_KEY')

model = app.models.get('logo')

model.send_region_feedback(
    input_id='{input_id}',
    url='https://clarifai.com/images/model-samples/logo-002.jpg',
    regions=[Region(
        region_info=RegionInfo(
            bbox=BoundingBox(top_row=0.3, left_col=0.2, bottom_row=0.7, right_col=0.8),
            feedback_type='accurate'),
        concepts=[Concept(concept_id='ai_TG4GHlnf', value=True)])],
    feedback_info=FeedbackInfo(event_type='annotation',
                               output_id='{output_id}',
                               end_user_id='{end_user_id}',
                               session_id='{session_id}'))
```

```java
ModelFeedbackRequest request =
    client.modelFeedback(client.getDefaultModels().logoModel().id())
        .withInputId("{input_id}")
        .withImageUrl("https://clarifai.com/images/model-samples/logo-002.jpg")
        .withRegions(
            RegionFeedback.make(
                Crop.create().top(0.3f).left(0.2f).bottom(0.7f).right(0.8f),
                Feedback.ACCURATE
            )
              .withConceptFeedbacks(ConceptFeedback.forIdAndValue("ai_TG4GHlnf", true)))
        .withEventType("annotation")
        .withOutputId("{output_id}")
        .withEndUserId("{end_user_id}")
        .withSessionId("{session_id}");
```

```csharp

using System.Collections.Generic;
using System.Threading.Tasks;
using Clarifai.API;
using Clarifai.DTOs;
using Clarifai.DTOs.Feedbacks;

namespace YourNamespace
{
    public class YourClassName
    {
        public static async Task Main()
        {
            var client = new ClarifaiClient("YOUR_API_KEY");

            await client.ModelFeedback(
                    client.PublicModels.GeneralModel.ModelID,
                    imageUrl: "https://samples.clarifai.com/dog.tiff",
                    inputID: "inputID",
                    outputID: "{output_id}",
                    endUserID: "{end_user_id}",
                    sessionID: "{session_id}",
                    regions: new List<RegionFeedback>
                    {
                        new RegionFeedback(
                            new Crop(top: 0.3m, left: 0.2m, bottom: 0.7m, right: 0.8m),
                            Feedback.Accurate,
                            new List<ConceptFeedback>
                            {
                                new ConceptFeedback("ai_8S2Vq3cR", true),
                                new ConceptFeedback("ai_mFqxrph2", false)
                            })
                    })
                .ExecuteAsync();
        }
    }
}

```

```objective-c
// Coming Soon
```

```php

use Clarifai\API\ClarifaiClient;
use Clarifai\DTOs\Crop;
use Clarifai\DTOs\Feedbacks\ConceptFeedback;
use Clarifai\DTOs\Feedbacks\Feedback;
use Clarifai\DTOs\Feedbacks\RegionFeedback;

$client = new ClarifaiClient('YOUR_API_KEY');

$response = $client->modelFeedback(
        $client->publicModels()->generalModel()->modelID(),
        'https://samples.clarifai.com/dog.tiff',
        '{input-id}',
        '{output-id}',
        '{end-user-id}',
        '{session-id}')
        ->withRegionFeedbacks([
            (new RegionFeedback())
                ->withCrop(new Crop(0.3, 0.2, 0.7, 0.8))
                ->withFeedback(Feedback::accurate())
                ->withConceptFeedbacks([
                    new ConceptFeedback('ai_8S2Vq3cR', true),
                    new ConceptFeedback('ai_mFqxrph2', false),
                ])
        ])
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";
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
    "input": {
      "id": "{input_id}",
      "data": {
        "image": {
          "url": "https://clarifai.com/images/model-samples/logo-002.jpg"
        },
        "regions":
        [
          {   
            "region_info": {
              "bounding_box": {
                "top_row": 0.3,
                "left_col": 0.2,
                "bottom_row": 0.7,
                "right_col": 0.8
              },
              "feedback": "accurate"
            },
            "data": {
              "concepts":[
                {"id": "ai_TG4GHlnf", "value": true }
              ]
            }
          }
        ]
      },
      "feedback_info":{
        "event_type":   "annotation",
        "output_id":    "{output_id}",
        "end_user_id":  "{end_user_id}",
        "session_id":   "{session_id}",
      }
    }
  }'\
  https://api.clarifai.com/v2/models/c443119bf2ed4da98487520d01a0b1e3/feedback
```



```response
{
    "status": {
        "code": 10000,
        "description": "Ok"
    }
}
```

### Search Feedback
To send feedback on searches, you can use `POST /v2/searches/feedback`.

This request is meant to collect the correctly searched inputs, which is usually done by capturing your end user's clicks on the given search results. Your feedback will help us improve our search algorithm.

In the request body for search feedback, you can specify:

  * • input id of a correct image ('hit') from the search results
  * • `search_id` from the search API response

Note that the `event_type` should be set to `search_click`.




```js
app.inputs.searchFeedback('{input_id}', '{search_id}', '{end_user_id}', '{session_id}')
  .then(response => {
    // There was a successful response
  })
  .catch(error => {
    // There was an error
  });
```

```python
from clarifai.rest import ClarifaiApp, FeedbackInfo
app = ClarifaiApp(api_key='YOUR_API_KEY')

app.inputs.send_search_feedback(
    '{input_id}',
    FeedbackInfo('{end_user_id}', '{session_id}', 'search_click', search_id='{search_id}'))
```

```java
SearchesFeedbackRequest request = client.searchesFeedback()
    .withId("{input_id}")
    .withEndUserId("{end_user_id}")
    .withSessionId("{session_id}")
    .withEventType("search_click")
    .withSearchId("{search_id}");
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

            await client.SearchesFeedback(
                    inputID: "{input_id}",
                    endUserID: "{end_user_id}",
                    sessionID: "{session_id}",
                    searchID: "{search_id}")
                .ExecuteAsync();
        }
    }
}

```

```objective-c
// Coming Soon
```

```php

use Clarifai\API\ClarifaiClient;

$client = new ClarifaiClient();

$response = $client->searchesFeedback('{input_id}', '{end_user_id}', '{session_id}', '{search_id}')
    ->executeSync();

if ($response-> isSuccessful()) {
    echo "Response is successful.\n";
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
    "input": {
      "id": "{input_id}",
      "feedback_info": {
        "event_type":   "search_click",
        "search_id":    "{output_id}",
        "end_user_id":  "{end_user_id}",
        "session_id":   "{session_id}"
      }
    }
  }'\
  https://api.clarifai.com/v2/searches/feedback
```



```response
{
    "status": {
        "code": 10000,
        "description": "Ok"
    }
}
```
