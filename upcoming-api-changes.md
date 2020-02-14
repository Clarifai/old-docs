## Upcoming API Changes for Clarifai

Here is a list of changes to the API that we want you to be aware of well in advance as they may
affect how you use Clarifai's platform. These changes include scheduled downtime and other
improvements in stability, performance or functionality of the Clarifai
platform in order to better serve you as a customer. Some of these changes may not be backward
compatible and thus require you to update how you call our APIs. We created this page with the
mindset of being as transparent as possible so you can plan any corresponding changes in advance and
minimize any interruptions to your usage of Clarifai.

The dates listed in the following tables are the date we plan to make the change. We may actually
make the change in the days following the specified date. However, to be safe, your client-side code
needs updating before that date to minimize any downtime to your applications.

We will continue to update this page regularly, so a good way to always stay up to date is to
watch our [documentation repo on GitHub](https://github.com/Clarifai/docs).


### Upcoming Changes

| Date | Change |
| ------ | ---- |
| Feb 27, 2020. 9:00am ET | **Deprecation of Face object from API**<br><br>The Face object in our API responses will be deprecated in favor of a list of Concepts that other model types return. This should only effect users of the Celebrity, Demographics, or custom face recognition models where the `data.face` attributes like `data.face.identity`, `data.face.age_appearance`, `data.face.gender_appearance`, and `data.face.multicultural_appearance` will now be returned in the list of `data.concepts` Concept object. The API will return both for a while during the transition to give you time to update your code away from using the `data.face` objects altogether. We are doing this to simplify the API interface and make it more easily compatible for advanced functionality that is coming soon in workflows! The custom face recognition and celebrity models are a simple change to just access the new `data.concepts` field, but the demographics model is a more fundamental change away from having three distinct lists of concept to a single list. In order to cope with this we have introduced a `vocab_id` field in each `data.concepts` entry that is returned by the demographics model so that you can distinguish `age_appearance`, `gender_appearance` and `multicultural_appearance`.<br><br>For example, the previous demographics model prediction output format was:<br>
```
{
    "status": {
        "code": 10000,
        "description": "Ok",
        "req_id": "5f896aac18e1477d9e8127f9451bbd7e"
    },
    "outputs": [
        {
            "id": "5d94ed68546c4503962dba69826b6f28",
            "status": {
                "code": 10000,
                "description": "Ok"
            },
            "created_at": "2020-02-13T16:00:32.850133015Z",
            "model": {
                "id": "c0c0ac362b03416da06ab3fa36fb58e3",
                "name": "demographics",
                "created_at": "2016-12-26T13:45:40.620652Z",
                "app_id": "main",
                "output_info": {
                    "message": "Show output_info with: GET /models/{model_id}/output_info",
                    "type": "detect-concept",
                    "type_ext": "detect-concept"
                },
                "model_version": {
                    "id": "f783f0807c52474c8c6ad20c8cf45fc0",
                    "created_at": "2016-12-26T13:45:40.620652Z",
                    "status": {
                        "code": 21100,
                        "description": "Model is trained and ready"
                    },
                    "worker_id": "8ced24ba0fb849c5bb3764ce62e88f60"
                },
                "display_name": "Demographics"
            },
            "input": {
                "id": "9b9a09f2a33c4dc58afbbc699c4fa149",
                "data": {
                    "image": {
                        "url": "..."
                    }
                }
            },
            "data": {
                "regions": [
                    {
                        "id": "3tdmf0ao9zgn",
                        "region_info": {
                            "bounding_box": {
                                "top_row": 0.19993289,
                                "left_col": 0.51557815,
                                "bottom_row": 0.5489441,
                                "right_col": 0.71368855
                            }
                        },
                        "data": {
                            "face": {
                                "age_appearance": {
                                    "concepts": [
                                        {
                                            "id": "ai_fbRxTRbd",
                                            "name": "46",
                                            "value": 0.5995513,
                                            "app_id": "main",
                                            "vocab_id": "age_appearance"
                                        },
                                        {
                                            "id": "ai_4w8KM6Rd",
                                            "name": "45",
                                            "value": 0.5868488,
                                            "app_id": "main",
                                            "vocab_id": "age_appearance"
                                        },
                                        ... // Usually top-k defaults to 20 here. 
                                    ]
                                },
                                "gender_appearance": {
                                    "concepts": [
                                        {
                                            "id": "ai_zgR2BBt0",
                                            "name": "masculine",
                                            "value": 0.97551966,
                                            "app_id": "main",
                                            "vocab_id": "gender_appearance"
                                        },
                                        {
                                            "id": "ai_cVWr8NK5",
                                            "name": "feminine",
                                            "value": 0.02448032,
                                            "app_id": "main",
                                            "vocab_id": "gender_appearance"
                                        }
                                    ]
                                },
                                "multicultural_appearance": {
                                    "concepts": [
                                        {
                                            "id": "ai_r5F00Gqn",
                                            "name": "white",
                                            "value": 0.5075468,
                                            "app_id": "main",
                                            "vocab_id": "multicultural_appearance"
                                        },
                                        {
                                            "id": "ai_l9ngrR28",
                                            "name": "hispanic, latino, or spanish origin",
                                            "value": 0.113882765,
                                            "app_id": "main",
                                            "vocab_id": "multicultural_appearance"
                                        },
                                        {
                                            "id": "ai_WWxnB3mw",
                                            "name": "american indian or alaska native",
                                            "value": 0.08919552,
                                            "app_id": "main",
                                            "vocab_id": "multicultural_appearance"
                                        },
                                        {
                                            "id": "ai_bZft5m0H",
                                            "name": "middle eastern or north african",
                                            "value": 0.020790711,
                                            "app_id": "main",
                                            "vocab_id": "multicultural_appearance"
                                        },
                                        {
                                            "id": "ai_659b6V0v",
                                            "name": "asian",
                                            "value": 0.015248744,
                                            "app_id": "main",
                                            "vocab_id": "multicultural_appearance"
                                        },
                                        {
                                            "id": "ai_wScNwk9Z",
                                            "name": "black or african american",
                                            "value": 0.0024879198,
                                            "app_id": "main",
                                            "vocab_id": "multicultural_appearance"
                                        },
                                        {
                                            "id": "ai_1qp01psl",
                                            "name": "native hawaiian or pacific islander",
                                            "value": 0.0018966927,
                                            "app_id": "main",
                                            "vocab_id": "multicultural_appearance"
                                        }
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "id": "2v3m24zsp6p3",
                        "region_info": {
                            "bounding_box": {
                                "top_row": 0.2792136,
                                "left_col": 0.23538604,
                                "bottom_row": 0.6306359,
                                "right_col": 0.4349089
                            }
                        },
                        "data": {
                            ...
                        }
                    }
                ]
            }
        }
    ]
}
```
<br>The new demographics model prediction output format as a list of concepts with `vocab_id` in each `concept` object:<br>
```
{
    "status": {
        "code": 10000,
        "description": "Ok",
        "req_id": "5f896aac18e1477d9e8127f9451bbd7e"
    },
    "outputs": [
        {
            "id": "5d94ed68546c4503962dba69826b6f28",
            "status": {
                "code": 10000,
                "description": "Ok"
            },
            "created_at": "2020-02-13T16:00:32.850133015Z",
            "model": {
                "id": "c0c0ac362b03416da06ab3fa36fb58e3",
                "name": "demographics",
                "created_at": "2016-12-26T13:45:40.620652Z",
                "app_id": "main",
                "output_info": {
                    "message": "Show output_info with: GET /models/{model_id}/output_info",
                    "type": "detect-concept",
                    "type_ext": "detect-concept"
                },
                "model_version": {
                    "id": "f783f0807c52474c8c6ad20c8cf45fc0",
                    "created_at": "2016-12-26T13:45:40.620652Z",
                    "status": {
                        "code": 21100,
                        "description": "Model is trained and ready"
                    },
                    "worker_id": "8ced24ba0fb849c5bb3764ce62e88f60"
                },
                "display_name": "Demographics"
            },
            "input": {
                "id": "9b9a09f2a33c4dc58afbbc699c4fa149",
                "data": {
                    "image": {
                        "url": "..."
                    }
                }
            },
            "data": {
                "regions": [
                    {
                        "id": "3tdmf0ao9zgn",
                        "region_info": {
                            "bounding_box": {
                                "top_row": 0.19993289,
                                "left_col": 0.51557815,
                                "bottom_row": 0.5489441,
                                "right_col": 0.71368855
                            }
                        },
                        "data": {
                            "concepts": [
                                {
                                    "id": "ai_fbRxTRbd",
                                    "name": "46",
                                    "value": 0.5995513,
                                    "app_id": "main",
                                    "vocab_id": "age_appearance"
                                },
                                {
                                    "id": "ai_4w8KM6Rd",
                                    "name": "45",
                                    "value": 0.5868488,
                                    "app_id": "main",
                                    "vocab_id": "age_appearance"
                                },
                                ... // typically up to 20 age_appearance concepts will be returned by default.
                                {
                                    "id": "ai_zgR2BBt0",
                                    "name": "masculine",
                                    "value": 0.97551966,
                                    "app_id": "main",
                                    "vocab_id": "gender_appearance"
                                },
                                {
                                    "id": "ai_cVWr8NK5",
                                    "name": "feminine",
                                    "value": 0.02448032,
                                    "app_id": "main",
                                    "vocab_id": "gender_appearance"
                                },
                                {
                                    "id": "ai_r5F00Gqn",
                                    "name": "white",
                                    "value": 0.5075468,
                                    "app_id": "main",
                                    "vocab_id": "multicultural_appearance"
                                },
                                {
                                    "id": "ai_l9ngrR28",
                                    "name": "hispanic, latino, or spanish origin",
                                    "value": 0.113882765,
                                    "app_id": "main",
                                    "vocab_id": "multicultural_appearance"
                                },
                                {
                                    "id": "ai_WWxnB3mw",
                                    "name": "american indian or alaska native",
                                    "value": 0.08919552,
                                    "app_id": "main",
                                    "vocab_id": "multicultural_appearance"
                                },
                                {
                                    "id": "ai_bZft5m0H",
                                    "name": "middle eastern or north african",
                                    "value": 0.020790711,
                                    "app_id": "main",
                                    "vocab_id": "multicultural_appearance"
                                },
                                {
                                    "id": "ai_659b6V0v",
                                    "name": "asian",
                                    "value": 0.015248744,
                                    "app_id": "main",
                                    "vocab_id": "multicultural_appearance"
                                },
                                {
                                    "id": "ai_wScNwk9Z",
                                    "name": "black or african american",
                                    "value": 0.0024879198,
                                    "app_id": "main",
                                    "vocab_id": "multicultural_appearance"
                                },
                                {
                                    "id": "ai_1qp01psl",
                                    "name": "native hawaiian or pacific islander",
                                    "value": 0.0018966927,
                                    "app_id": "main",
                                    "vocab_id": "multicultural_appearance"
                                }
                            ],
                        }
                    },
                    {
                        "id": "2v3m24zsp6p3",
                        "region_info": {
                            "bounding_box": {
                                "top_row": 0.2792136,
                                "left_col": 0.23538604,
                                "bottom_row": 0.6306359,
                                "right_col": 0.4349089
                            }
                        },
                        "data": {
                        }
                    }
                ]
            }
        }
    ]
}
```
<br>In order to convert from the new format to something similar the old format where you have a dictionary keyed by `age_appearance`, `gender_appearance` and `multicultural_appearance` you could do something like the following as an example in the Python programming language:<br>
```
buckets = {}
for c in outputs[0].data.regions[0].data:
  buckets.setdefault(c.vocab_id, [])
  buckets[c.vocab_id].append(c)
```
Similar examples could be made for all other langauge. If you need help in the conversion feel free to reach out to support@clarifai.com. 

|


### Completed Changes

| Date | Change |
| ------ | ---- |
| September 11, 2019. 9:00am ET | **Scheduled Database Downtime**<br><br>We plan to upgrade our database to make it faster and provide more space for your applications. We expect a few minutes of downtime during this upgrade but you should plan for up to an hour of downtime in case things don't go as expected. This will primarily affect the following uses of our platform: POST/GET/PATCH/DELETE inputs, Search, Custom Training, Model Evaluation |
| September 24, 2019. 5:00pm ET | **`POST /inputs` will only operate asynchronously**<br><br>We are cleaning up some inconsistent behavior in the API where a single image added with `POST /inputs` was a synchronous operation, but a batch of images was asynchronous. We are making both asynchronous. This allows us to provide more advanced functionality with workflows that index your inputs.<br><br>What this means for your code is if you application relies on added inputs having already been indexed when the `POST /inputs` call returns, you now need to add a second call to `GET /inputs/{input_id}` in order to check the status of the input you just added to look for 30000 (INPUT_IMAGE_DOWNLOAD_SUCCESS) status code.  |
| September 30, 2019. 5:00pm ET | **`DELETE /inputs` will only operate asynchronously**<br><br>Along the same lines as `POST /inputs` becoming completely asynchronous, we are cleaning up some inconsistent behavior in the API for deleting inputs. Previously, when a single image is deleted with `DELETE /inputs` or `DELETE /inputs/{input_id}` it was a synchronous operation, but when a batch of images were deleted it was asynchronous. We are making both asynchronous. This allows us to provide more advanced functionality with workflows that index your inputs.<br><br>What this means for your code is if you application relies on the input having been deleted when the `DELETE /inputs` or `DELETE /inputs/{input_id}` calls return, you now need to add a second call to `GET /inputs/{input_id}` in order to check that it fails with a not found error.  |
| November 20, 2019 | **`image.crop` argument will be deprecated**<br><br>In some requests we used to allow cropping of images during the request using the `image.crop` field. This was for convenience only, but in reality is was rarely ever used and significantly complicates the processing pipelines under the hood. Therefore, we will no longer support the `image.crop` field in any requests that used to accept it. <br><br>If you want to have similar behaviour please crop the images on the client side and send the cropped bytes as base64 encoded image data. |
| Feb 1, 2020 | **Deprecation of Focus Model**<br><br>The Focus model will no longer be supported and will be removed from our API after this point in time. If you have requests for recognizing focus and blurry regions within images please contact sales@clarifai.com so that we can help you directly. |
| Feb 3, 2020 | **`PATCH /inputs` overwrite action change**<br><br>The overwrite action when patching inputs currently has some inconsistent behavior. If you patch `input.data.metadata` or `input.data.geo` fields on an input that has `input.data.concepts` already added to it, these concepts will remain after the patch even though the patch action was `overwrite`.<br><br>Going forward, the overwrite behavior will overwrite the entire `data` object with what is included in the `PATCH /inputs` API call. Therefore if concepts are not provided in the patch call, but were originally on that input, they will be erased (overwritten with an empty list of concepts). You can maintain the current behvaiour by always sending back the complete `data` object from `GET /input/{input_id}` along with any modification to it if you are using the `overwrite` action. <br><br>Update: this change has become more complicated than originally expected and we may not undergo it after all, more to come in future. Still a good idea to update your PATCH calls to use the `merge` or `remove` actions instead of `overwrite` due to `overwrite`'s inconsistency. |
| Feb 12, 2020. 9:00am ET | **Deprecation of Face model type names**<br><br>The `facedetect*` model types will be deprecated in favor of their more general `detect*` counterparts. For example these would be the changes of model type:<br>`facedetect` -> `detect`<br>`facedetect-identity` -> `detect-concept`<br>`facedetect-demographics` -> `detect-concept`<br>`facedetect-embed` -> `detect-embed`<br>This change is to unify the APIs around face products and object detection products so that they are compatible everywhere either is used. |



