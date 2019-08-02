## Video

The *Video API* analyzes video and predicts what's inside of it.

The Video API will return a list of predicted concepts for every frame of video. Video is processed at 1
frame per second. This means you will receive a list of concepts for every second of your video.

You can run Predict on your video using a select number of <a href="https://clarifai.com/models" target="_self">Public Models</a>. The models
that are currently supported are: Apparel, Food, General, NSFW, Travel, and Wedding. You make an API call
by providing the `ModelId` parameter as outlined in the [Predict API](predict.md).

### Input by URL



```js
app.models.predict(Clarifai.GENERAL_MODEL, 'https://samples.clarifai.com/beer.mp4', {video: true})
  .then(response => {
    // There was a successful response
  })
  .catch(error => {
    // There was an error
  });
```

```python
from clarifai.rest import Video as ClVideo

model = app.models.get('general-v1.3')
video = ClVideo(url='https://samples.clarifai.com/beer.mp4')
model.predict([video])
```

```java
ClarifaiResponse<List<ClarifaiOutput<Frame>>> frames = client.getDefaultModels().generalVideoModel().predict()
       .withInputs(
             ClarifaiInput.forImage(ClarifaiImage.ofVideo("https://samples.clarifai.com/beer.mp4"))
        )
       .executeSync();
```

```objective-c
Objective-C client details coming soon
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
          "video": {
            "url": "https://samples.clarifai.com/beer.mp4"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs
```




### Input by base64



```js
app.models.predict(Clarifai.GENERAL_MODEL, {base64: 'AAAAIGZ...'}, {video: true})
  .then(response => {
    // There was a successful response
  })
  .catch(error => {
    // There was an error
  });
```

```python
from clarifai.rest import Video as ClVideo

model = app.models.get('general-v1.3')
video = ClVideo(filename='/home/user/video.mp4')
model.predict([video])
```

```java
ClarifaiResponse<List<ClarifaiOutput<Frame>>> frames = client.getDefaultModels().generalVideoModel().predict()
       .withInputs(
             ClarifaiInput.forImage(ClarifaiImage.ofBase64Video("/home/user/video.mp4"))
        )
       .executeSync();
```

```objective-c
Objective-C client details coming soon
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
          "video": {
            "base64": "'"$(base64 /home/user/video.mp4)"'"
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs
```



### Video Format

The Video API currently accepts videos in the following formats: .avi, .mp4, .wmv, .mov, .gif, and .3gpp.

### Video Limits

There are certain limits imposed on you when using the Video API. Some of these are technical in nature,
and others are based on your plan. If you need to increase your limits, you may do so by
<a href="https://clarifai.com/developer/support/" target="_self">contacting support</a>. Please familiarize yourself with the limits below.

#### Data Limits

The Video API currently supports videos of up to 80MB in size or 10min in length (whichever comes first) if you are uploading through URL, and videos of up to 10MB in size, if you are uploading through video bytes (base 64).
If the video input exceeds the limits, the processing will time out and you will receive a response error.

If your video exceeds the above limits, please follow our <a href="http://help.clarifai.com/videos/how-to-split-video-files-into-smaller-pieces" target="_self">tutorial</a> on how to break up a large
video into smaller components, and send those components into the Video API.

```response
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "outputs": [
    {
      "id": "f1da7044eb0349cba858d2750e5369a7",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-05-12T22:51:01.954979448Z",
      "model": {
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "name": "general-v1.3",
        "created_at": "2016-03-09T17:11:39.608845Z",
        "app_id": "",
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
        "id": "ef524c1e486d42299624227e4d8aaf5c",
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
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": ""
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.9783862,
                  "app_id": ""
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.97157896,
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.96628696,
                  "app_id": ""
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.95581007,
                  "app_id": ""
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.92861253,
                  "app_id": ""
                },
                {
                  "id": "ai_7vR9zv7l",
                  "name": "bubble",
                  "value": 0.9082134,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9020835,
                  "app_id": ""
                },
                {
                  "id": "ai_7Xg5SQRW",
                  "name": "luxury",
                  "value": 0.8990605,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.89708906,
                  "app_id": ""
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": ""
                },
                {
                  "id": "ai_7qwGxLch",
                  "name": "gold",
                  "value": 0.8892093,
                  "app_id": ""
                },
                {
                  "id": "ai_wmbvr5TG",
                  "name": "celebration",
                  "value": 0.88606626,
                  "app_id": ""
                },
                {
                  "id": "ai_4lvjn8qv",
                  "name": "closeup",
                  "value": 0.881963,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": ""
                },
                {
                  "id": "ai_12dz73B9",
                  "name": "bottle",
                  "value": 0.86288416,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.86252767,
                  "app_id": ""
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.86069393,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": ""
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.9783862,
                  "app_id": ""
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.97157896,
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.96628696,
                  "app_id": ""
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.95581007,
                  "app_id": ""
                },
                {
                  "id": "ai_7vR9zv7l",
                  "name": "bubble",
                  "value": 0.9082134,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9020835,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.89708906,
                  "app_id": ""
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": ""
                },
                {
                  "id": "ai_7qwGxLch",
                  "name": "gold",
                  "value": 0.8834515,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": ""
                },
                {
                  "id": "ai_b01mhdxB",
                  "name": "party",
                  "value": 0.8603341,
                  "app_id": ""
                },
                {
                  "id": "ai_XNmzgDnF",
                  "name": "pub",
                  "value": 0.85809004,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.85319245,
                  "app_id": ""
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.8506696,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.84634554,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": ""
                },
                {
                  "id": "ai_wmbvr5TG",
                  "name": "celebration",
                  "value": 0.8383831,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.97975093,
                  "app_id": ""
                },
                {
                  "id": "ai_8XGJjH7R",
                  "name": "foam",
                  "value": 0.9755833,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9733174,
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.969543,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.94170487,
                  "app_id": ""
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.92778283,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9227257,
                  "app_id": ""
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": ""
                },
                {
                  "id": "ai_drK6ClJR",
                  "name": "alcohol",
                  "value": 0.90887475,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": ""
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8938055,
                  "app_id": ""
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.87420183,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.8699659,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.8674431,
                  "app_id": ""
                },
                {
                  "id": "ai_XNmzgDnF",
                  "name": "pub",
                  "value": 0.85809004,
                  "app_id": ""
                },
                {
                  "id": "ai_Lq00FggW",
                  "name": "desktop",
                  "value": 0.8506696,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": ""
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": ""
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.8397074,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9794438,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9733174,
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.9645849,
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.94761443,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.92864025,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9227257,
                  "app_id": ""
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.91797745,
                  "app_id": ""
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": ""
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.889248,
                  "app_id": ""
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.8689867,
                  "app_id": ""
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.86591685,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8546975,
                  "app_id": ""
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8544879,
                  "app_id": ""
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.852397,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8446485,
                  "app_id": ""
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": ""
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.837438,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9748836,
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.9645849,
                  "app_id": ""
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.96217895,
                  "app_id": ""
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9179274,
                  "app_id": ""
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9045203,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9030821,
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.8983356,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.894987,
                  "app_id": ""
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.889248,
                  "app_id": ""
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8860091,
                  "app_id": ""
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.8837219,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8712319,
                  "app_id": ""
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.8695712,
                  "app_id": ""
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.8664293,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8546975,
                  "app_id": ""
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.852397,
                  "app_id": ""
                },
                {
                  "id": "ai_qNxqNBWN",
                  "name": "cream",
                  "value": 0.844169,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97719705,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.9748836,
                  "app_id": ""
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.96217895,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9210669,
                  "app_id": ""
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9124408,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.90667903,
                  "app_id": ""
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.904904,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9046865,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.9030821,
                  "app_id": ""
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.8983356,
                  "app_id": ""
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.8947689,
                  "app_id": ""
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.8852426,
                  "app_id": ""
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.8789175,
                  "app_id": ""
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.8762902,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.87279737,
                  "app_id": ""
                },
                {
                  "id": "ai_mZ2tl6cW",
                  "name": "health",
                  "value": 0.8544879,
                  "app_id": ""
                },
                {
                  "id": "ai_cHsR7RS8",
                  "name": "milk",
                  "value": 0.849733,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": ""
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9273318,
                  "app_id": ""
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": ""
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": ""
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": ""
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": ""
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.892028,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.88797945,
                  "app_id": ""
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": ""
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": ""
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": ""
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": ""
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9273318,
                  "app_id": ""
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": ""
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": ""
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": ""
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": ""
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.892028,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.8913312,
                  "app_id": ""
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": ""
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": ""
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": ""
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": ""
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
                  "app_id": ""
                },
                {
                  "id": "ai_TBlp0Pt3",
                  "name": "beer",
                  "value": 0.97817445,
                  "app_id": ""
                },
                {
                  "id": "ai_786Zr311",
                  "name": "no person",
                  "value": 0.97463626,
                  "app_id": ""
                },
                {
                  "id": "ai_zJx6RbxW",
                  "name": "drink",
                  "value": 0.9659773,
                  "app_id": ""
                },
                {
                  "id": "ai_4sJLn6nX",
                  "name": "dark",
                  "value": 0.9219268,
                  "app_id": ""
                },
                {
                  "id": "ai_pkvDRSJ1",
                  "name": "mug",
                  "value": 0.9210669,
                  "app_id": ""
                },
                {
                  "id": "ai_B3MXt5Ng",
                  "name": "refreshment",
                  "value": 0.9185593,
                  "app_id": ""
                },
                {
                  "id": "ai_2gmKZLxp",
                  "name": "cold",
                  "value": 0.91295856,
                  "app_id": ""
                },
                {
                  "id": "ai_3PlgVmlN",
                  "name": "food",
                  "value": 0.9119204,
                  "app_id": ""
                },
                {
                  "id": "ai_54zxXFGL",
                  "name": "full",
                  "value": 0.91089505,
                  "app_id": ""
                },
                {
                  "id": "ai_SsmKLB4z",
                  "name": "bar",
                  "value": 0.9056676,
                  "app_id": ""
                },
                {
                  "id": "ai_BrnHNkt0",
                  "name": "coffee",
                  "value": 0.90262496,
                  "app_id": ""
                },
                {
                  "id": "ai_mCpQg89c",
                  "name": "glass",
                  "value": 0.89882934,
                  "app_id": ""
                },
                {
                  "id": "ai_7D0mdp1W",
                  "name": "delicious",
                  "value": 0.894392,
                  "app_id": ""
                },
                {
                  "id": "ai_WbwL0pPL",
                  "name": "breakfast",
                  "value": 0.8932399,
                  "app_id": ""
                },
                {
                  "id": "ai_zFnPQdgB",
                  "name": "wood",
                  "value": 0.88797945,
                  "app_id": ""
                },
                {
                  "id": "ai_3R5pJ6hB",
                  "name": "lager",
                  "value": 0.88745904,
                  "app_id": ""
                },
                {
                  "id": "ai_8LWlDfFD",
                  "name": "table",
                  "value": 0.87949455,
                  "app_id": ""
                },
                {
                  "id": "ai_MmRdqDFp",
                  "name": "soap",
                  "value": 0.87376094,
                  "app_id": ""
                },
                {
                  "id": "ai_5VHsZr8N",
                  "name": "liquid",
                  "value": 0.8715329,
                  "app_id": ""
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
