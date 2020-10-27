# Changelog

## Changelog 5.11

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Create a UI for personal access tokens making it easier for users to access their own apps and any apps where they have been added as collaborators |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Updated /keys to work with PATs so that app-specific keys can be created programmatically. |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Login \(user/PW\) has no rate limit/max attempts. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Remove all instances of worker\_id from explorer |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | When email link to verify my email address clicked, still see "verify your email" banner. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) ![](../.gitbook/assets/enterprise%20%2810%29.jpg) | API services do not function once Queue goes down and comes back up. Fixed. This makes on premise deployments more resilient to power failures. |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Add apps and keys scopes so they can be created with personal access tokens |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) ![](../.gitbook/assets/enterprise%20%2810%29.jpg) | Copy app count and last\_inputs added in app duplication |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed demo font syntax |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed details page header missing description |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Added favicon for Portal |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Unable to copy an app that has been shared via Collaborators. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Setting useCustomConfig isn't checked at login. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Collaboration apps have race condition where wrong user id is used |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Stopped loading of collaborations for search demo/logged-out users |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Return “All” scopes when listing available scopes so that you have that option when creating new keys. |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Collaborators can not see workers. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Missing `Apps_Get` scope in session token auth caused creation of keys to fail temporarily. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | List of missing scopes is not correct in error messages. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Optimize video detection frame rate on Front end |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Improve JSON serialization performance in our servers by using an optimized third party library |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Able to overwrite default max conn for Citus |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Rewrite input counting in the API to be more scalable and robust |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Allow RegionInfo from SpireDetectEmbedResponse to contain Point when saving to DB |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Unable to upload same file\(s\) through browse files. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | ffmpeg can produce no frames for very short videos |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Add Inputs/View Explorer does not display in new app anymore. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Clicking video thumbs in detail view does not reload a video. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Keyboard navigation in image details view highlights incorrect thumb |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | No Prompt when uploading an image to Explorer through URL. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Properly return error if `AddAssets` failed to insert into database |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove classification/detection toggle in image details view |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Improved adding negatives to regions |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Create one annotation for each bbox |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Log capability added for annotation/search request/response |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Eliminated error if no annotation to be deleted |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Last concept used for bounding boxes is retained between apps. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | The Add Positives / Add Negatives buttons on a Concept details view breaks portal |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Custom facial recognition bboxes on grid view do not correlate. Fixed |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Ability to keep concepts sorted by alpha in Portal |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Implement image crop model to make it possible to work in subregions of an image |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Implement random sample model type, adding to fixed function feature set |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Update training templates to have more straightforward names and more friendly defaults |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Fix the WorkflowInput field name in proto to workflow\_input |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Confusion matrix predicted/true are swapped in evaluation results. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed generalModel imports and optimize video click handlers with useCallback hooks |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix for selectEmbedModelVersionId in detection apps |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Drawing annotations: wrong embed model version id |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Made custom training evaluations for large models stable. |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Training progress is saved too frequently, causing very slow training |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Return friendlier errors for incorrect parameters passed to templates |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed a bug in tracing setup for custom trainer and evaluator |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Some models were operating slowly because of lack of resources. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Training System failed to train some layers. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Prevent users from evaluating models that are not trainable |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed node ID validation logic in Bug in workflows |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add colors to differentiate region results |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Cannot view workflow results in a face app. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Video spire tests are not running correctly. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Video processing fails with 'caseids' error. fixed |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Add click to search metadata attributes in image details sidebar |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Implement visual search in another app as a model type you can add to a workflow |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Search bar missing in some cases. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Click Search button icons on Thumbs not working for localized search. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Disable all search by click handlers in Portal for Text Apps |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Disable "hide all positively labeled" inputs button for NLP until search works |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Scroll active thumb into view in image details carousel |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Render Video Assets in Search Bar |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Editing geo/json search items no longer work after adding the search bar tooltip. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | TypeError: Cannot read 'get' of undefined when clicking image thumbnails in Explorer search bar. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Explorer Visibility in small resolution screen improved |
