---
description: Changelog for Clarifai Release 5.11
---

# Release 5.11

## Changelog 5.11

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Create a UI for personal access tokens making it easier for users to access their own apps and any apps where they have been added as collaborators |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Updated /keys to work with PATs so that app-specific keys can be created programmatically. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Login \(user/PW\) has no rate limit/max attempts. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Remove all instances of worker\_id from explorer |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | When email link to verify my email address clicked, still see "verify your email" banner. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) | API services do not function once Queue goes down and comes back up. Fixed. This makes on premise deployments more resilient to power failures. |

### Applications

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Add apps and keys scopes so they can be created with personal access tokens |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) | Copy app count and last\_inputs added in app duplication |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed demo font syntax |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed details page header missing description |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Added favicon for Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Unable to copy an app that has been shared via Collaborators. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Setting useCustomConfig isn't checked at login. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Collaboration apps have race condition where wrong user id is used |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Stopped loading of collaborations for search demo/logged-out users |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Return “All” scopes when listing available scopes so that you have that option when creating new keys. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Collaborators can not see workers. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Missing `Apps_Get` scope in session token auth caused creation of keys to fail temporarily. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | List of missing scopes is not correct in error messages. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Optimize video detection frame rate on Front end |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Improve JSON serialization performance in our servers by using an optimized third party library |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Able to overwrite default max conn for Citus |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Rewrite input counting in the API to be more scalable and robust |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Allow RegionInfo from SpireDetectEmbedResponse to contain Point when saving to DB |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Unable to upload same file\(s\) through browse files. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ffmpeg can produce no frames for very short videos |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Add Inputs/View Explorer does not display in new app anymore. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Clicking video thumbs in detail view does not reload a video. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Keyboard navigation in image details view highlights incorrect thumb |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | No Prompt when uploading an image to Explorer through URL. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Properly return error if `AddAssets` failed to insert into database |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove classification/detection toggle in image details view |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Improved adding negatives to regions |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Create one annotation for each bbox |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Log capability added for annotation/search request/response |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Eliminated error if no annotation to be deleted |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Last concept used for bounding boxes is retained between apps. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | The Add Positives / Add Negatives buttons on a Concept details view breaks portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Custom facial recognition bboxes on grid view do not correlate. Fixed |

### Model

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Ability to keep concepts sorted by alpha in Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Implement image crop model to make it possible to work in subregions of an image |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Implement random sample model type, adding to fixed function feature set |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update training templates to have more straightforward names and more friendly defaults |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Fix the WorkflowInput field name in proto to workflow\_input |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Confusion matrix predicted/true are swapped in evaluation results. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed generalModel imports and optimize video click handlers with useCallback hooks |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix for selectEmbedModelVersionId in detection apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Drawing annotations: wrong embed model version id |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Made custom training evaluations for large models stable. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Training progress is saved too frequently, causing very slow training |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Return friendlier errors for incorrect parameters passed to templates |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed a bug in tracing setup for custom trainer and evaluator |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Some models were operating slowly because of lack of resources. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Training System failed to train some layers. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Prevent users from evaluating models that are not trainable |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed node ID validation logic in Bug in workflows |

### Predict

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add colors to differentiate region results |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Cannot view workflow results in a face app. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video spire tests are not running correctly. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video processing fails with 'caseids' error. fixed |

### Search

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Add click to search metadata attributes in image details sidebar |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Implement visual search in another app as a model type you can add to a workflow |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Search bar missing in some cases. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Click Search button icons on Thumbs not working for localized search. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Disable all search by click handlers in Portal for Text Apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Disable "hide all positively labeled" inputs button for NLP until search works |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Scroll active thumb into view in image details carousel |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Render Video Assets in Search Bar |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Editing geo/json search items no longer work after adding the search bar tooltip. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | TypeError: Cannot read 'get' of undefined when clicking image thumbnails in Explorer search bar. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Explorer Visibility in small resolution screen improved |
