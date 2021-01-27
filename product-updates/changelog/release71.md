---
description: Changelog for Clarifai Release 7.1
---

# Release 7.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%2819%29.jpg) |

## API

|Status     |Details                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Add apps and keys scopes so they can be created with personal access tokens.                                                                            |
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Change /keys to work with PATs                                                                                                                          |
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Change /apps to work with personal access tokens                                                                                                        |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Split java proto files into multiple and add package name.                                                                                              |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Write script to prune the proto files into public only rpcs and messages                                                                                |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Mark the appropriate fields in protos as cl_private_rpc to release grpc clients.                                                                        |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |copy app count and last_inputs added in app duplication                                                                                                 |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Rewrite input counting in the API to be more scalable and robust.                                                                                       |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Fix collector scopes so that predict keys don't need Collectors:Get                                                                                     |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Check the GetInputsKey of collectors has access to userA's information.                                                                                 |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Return “All” scopes when listing available scopes so that you have that option when creating new keys.                                                  |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |properly return err if `AddAssets` failed to insert into DB                                                                                             |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |POST inputs wasn’t using batch model optimizations correctly.                                                                                           |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |created_at field in sharing table is incorrect                                                                                                          |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Missing Apps_Get scope in session token auth caused creation of keys to fail temporarily.                                                               |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |API services do not function once Queue goes down and comes back up has been fixed. This makes on premise deployments more resilient to power failures. |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |List of missing scopes is not correct in error messages                                                                                                 |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Fix node ID validation logic in Bug in workflows                                                                                                        |


## Armada

|Status     |Details                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Create endpoint for taking down a spire                                                                                                                 |
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Create endpoint to deploy deep training models                                                                                                          |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Calculate detection pr and roc curves using score buckets                                                                                               |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Support for pytorch inference in spire                                                                                                                  |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |able to overwrite default max conn for Citus                                                                                                            |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Upgrade to go version for performance boost.                                                                                                            |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Make runtime config to remote the extra round trip to storage in predict pathway.                                                                       |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Improve JSON serialization performance in our servers by using an optimized third party library.                                                        |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Fix the WorkflowInput field name in proto to workflow_input                                                                                             |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |When reaching the final page, network request responds with 500 internal service error. Fixed                                                           |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Spire fails to launch in local-k8s-USER with error "persistentvolumeclaim not found". Fixed                                                             |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Video processing fails with 'caseids' error. Fixed                                                                                                      |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Fix a connection issue from Golang backend service to media processing service                                                                          |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Allocated resources for faster model performance                                                                                                        |

## Enlight

|Status     |Details                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Return deep training evals through the API                                                                                                              |
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |OCR Model                                                                                                                                               |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Update templates to have more straightforward names and more friendly defaults                                                                          |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Add 'Face' Default workflow to `https://api-dev.clarifai.com'                                                                                           |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Make custom/transfer training evaluations for large models stable.                                                                                      |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |training progress is saved too frequently, causing very slow training                                                                                   |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Return friendlier errors for incorrect parameters passed to templates                                                                                   |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Fix a bug in tracing setup for custom trainer and evaluator                                                                                             |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Accellerated training for specific cases                                                                                                                |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Training System failed to train some layers                                                                                                             |


## Mesh

|Status     |Details                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Implement image crop model                                                                                                                              |
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Implement RandomSample model type                                                                                                                       |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models.          |


## Portal

|Status     |Details                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |make UI for personal access token                                                                                                                       |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Send event to Hubspot when a user signs up on portal                                                                                                    |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Change HTML tag of ImagePile component from '<span>' to '<img>'                                                                                         |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Optimize Video Detection Frame Rate on Front end                                                                                                        |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Remove classification/detection toggle in image details view                                                                                            |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Add colors to differentiate region results                                                                                                              |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Scroll active thumb into view in image details carousel                                                                                                 |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Unable to upload same file(s) through browse files. Fixed                                                                                               |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Added a favicon for Portal                                                                                                                              |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Can’t create a new API key or edit the information of API key. Fixed                                                                                    |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Delete input while having other inputs selected deselects everything. Fixed                                                                             |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Cannot view workflow results in a face app. Fixed                                                                                                       |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Setting useCustomConfig isn't checked at login. Fixed                                                                                                   |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |ffmpeg can produce no frames for very short videos. Fixed                                                                                               |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Video spire tests are not running correctly. Fixed                                                                                                      |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Verify your email                                                                                                                                       |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Last concept used for bounding boxes is retained between apps. Fixed                                                                                    |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Intercom links to old community site (and maybe old FAQ page). Fixed                                                                                    |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Add Inputs/View Explorer does not display in new app anymore                                                                                            |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Clicking video thumbs in detail view does not reload a video                                                                                            |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |The Add Positives / Add Negatives buttons on a Concept details view breaks portal                                                                       |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Collaboration apps have race condition where wrong user id is used                                                                                      |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Don't load collaborations for search demo/logged-out users                                                                                              |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Keyboard navigation in image details view highlights incorrect thumb                                                                                    |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Render Video Assets in Search Bar                                                                                                                       |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |AppDetailsPanel add inputs/view in explorer no longer displays in devel                                                                                 |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Editing geo/json search items no longer work after adding the search bar tooltip                                                                        |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |TypeError: Cannot read 'get' of undefined when clicking image thumbnails in explorer search bar                                                         |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Explorer Visibility in small resolution screen                                                                                                          |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |No Prompt when uploading an image to explorer through url                                                                                               |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |CFR rectangles on grid view do not correlate                                                                                                            |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Prevent users from evaluating models that are not trainable.                                                                                            |


## Scribe

|Status     |Details                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Mark the /annotation endpoints with cl_private_rpc                                                                                                      |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |No longer able to copy an app that has been shared with you via Collaborators. Fixed                                                                    |
|![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) |Collaborators can not see workers                                                                                                                       |


## Spacetime

|Status     |Details                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Implement visual search in another app as a model type you can add to a workflow.                                                                       |
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Add click to search metadata attributes in image details sidebar                                                                                        |
|![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) |Ability to keep concepts sorted by alpha.                                                                                                               |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Refactor search                                                                                                                                         |
|![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) |Add metadata to collector added inputs so that you can filter by collector ID                                                                           |
