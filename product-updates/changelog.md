# Changelog

## Change log 5.11

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement%20%2822%29.jpg) | ![](../.gitbook/assets/bug%20%2875%29.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%289%29.jpg) | Create a UI for personal access tokens making it easier for users to access their own apps and any apps where they have been added as collaborators |
| ![](../.gitbook/assets/new_feature%20%2810%29.jpg) | Updated /keys to work with PATs so that app-specific keys can be created programmatically. |
| ![](../.gitbook/assets/bug%20%2895%29.jpg) | Login \(user/PW\) has no rate limit/max attempts. Fixed |
| ![](../.gitbook/assets/bug%20%2883%29.jpg) | Remove all instances of worker\_id from explorer |
| ![](../.gitbook/assets/bug%20%2827%29.jpg) | When email link to verify my email address clicked, still see "verify your email" banner. Fixed |
| ![](../.gitbook/assets/bug%20%2836%29.jpg) ![](../.gitbook/assets/enterprise%20%281%29.jpg) | API services do not function once Queue goes down and comes back up. Fixed. This makes on premise deployments more resilient to power failures. |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2815%29.jpg) | Add apps and keys scopes so they can be created with personal access tokens |
| ![](../.gitbook/assets/improvement%20%283%29.jpg) ![](../.gitbook/assets/enterprise%20%283%29.jpg) | Copy app count and last\_inputs added in app duplication |
| ![](../.gitbook/assets/bug%20%2887%29.jpg) | Fixed demo font syntax |
| ![](../.gitbook/assets/bug%20%2816%29.jpg) | Fixed details page header missing description |
| ![](../.gitbook/assets/bug%20%2846%29.jpg) | Added favicon for Portal |
| ![](../.gitbook/assets/bug%20%2850%29.jpg) | Unable to copy an app that has been shared via Collaborators. Fixed |
| ![](../.gitbook/assets/bug%20%2857%29.jpg) | Setting useCustomConfig isn't checked at login. Fixed |
| ![](../.gitbook/assets/bug%20%2884%29.jpg) | Collaboration apps have race condition where wrong user id is used |
| ![](../.gitbook/assets/bug%20%2894%29.jpg) | Stopped loading of collaborations for search demo/logged-out users |
| ![](../.gitbook/assets/bug%20%2897%29.jpg) | Return “All” scopes when listing available scopes so that you have that option when creating new keys. |
| ![](../.gitbook/assets/bug%20%2822%29.jpg) | Collaborators can not see workers. Fixed |
| ![](../.gitbook/assets/bug%20%2843%29.jpg) | Missing `Apps_Get` scope in session token auth caused creation of keys to fail temporarily. Fixed |
| ![](../.gitbook/assets/bug%20%2873%29.jpg) | List of missing scopes is not correct in error messages. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%285%29.jpg) | Optimize video detection frame rate on Front end |
| ![](../.gitbook/assets/improvement%20%289%29.jpg) | Improve JSON serialization performance in our servers by using an optimized third party library |
| ![](../.gitbook/assets/improvement%20%2810%29.jpg) | Able to overwrite default max conn for Citus |
| ![](../.gitbook/assets/improvement%20%287%29.jpg) | Rewrite input counting in the API to be more scalable and robust |
| ![](../.gitbook/assets/bug%20%287%29.jpg) | Allow RegionInfo from SpireDetectEmbedResponse to contain Point when saving to DB |
| ![](../.gitbook/assets/bug%20%28103%29.jpg) | Unable to upload same file\(s\) through browse files. Fixed |
| ![](../.gitbook/assets/bug%20%2878%29.jpg) | ffmpeg can produce no frames for very short videos |
| ![](../.gitbook/assets/bug%20%2834%29.jpg) | Add Inputs/View Explorer does not display in new app anymore. Fixed |
| ![](../.gitbook/assets/bug%20%28100%29.jpg) | Clicking video thumbs in detail view does not reload a video. Fixed |
| ![](../.gitbook/assets/bug%20%2886%29.jpg) | Keyboard navigation in image details view highlights incorrect thumb |
| ![](../.gitbook/assets/bug%20%2838%29.jpg) | No Prompt when uploading an image to Explorer through URL. Fixed |
| ![](../.gitbook/assets/bug%20%2825%29.jpg) | Properly return error if `AddAssets` failed to insert into database |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2824%29.jpg) | Remove classification/detection toggle in image details view |
| ![](../.gitbook/assets/bug%20%2844%29.jpg) | Improved adding negatives to regions |
| ![](../.gitbook/assets/bug%20%2881%29.jpg) | Create one annotation for each bbox |
| ![](../.gitbook/assets/bug%20%285%29.jpg) | Log capability added for annotation/search request/response |
| ![](../.gitbook/assets/bug%20%2849%29.jpg) | Eliminated error if no annotation to be deleted |
| ![](../.gitbook/assets/bug%20%2888%29.jpg) | Last concept used for bounding boxes is retained between apps. Fixed |
| ![](../.gitbook/assets/bug%20%2829%29.jpg) | The Add Positives / Add Negatives buttons on a Concept details view breaks portal |
| ![](../.gitbook/assets/bug%20%2853%29.jpg) | CFR rectangles on grid view do not correlate. Fixed |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2817%29.jpg) | Ability to keep concepts sorted by alpha in Portal |
| ![](../.gitbook/assets/new_feature%20%2812%29.jpg) | Implement image crop model to make it possible to work in subregions of an image |
| ![](../.gitbook/assets/new_feature%20%2819%29.jpg) | Implement random sample model type, adding to fixed function feature set |
| ![](../.gitbook/assets/improvement%20%2825%29.jpg) | Update training templates to have more straightforward names and more friendly defaults |
| ![](../.gitbook/assets/improvement%20%2826%29.jpg) | Fix the WorkflowInput field name in proto to workflow\_input |
| ![](../.gitbook/assets/improvement%20%2811%29.jpg) | Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models |
| ![](../.gitbook/assets/bug%20%2860%29.jpg) | Confusion matrix predicted/true are swapped in evaluation results. Fixed |
| ![](../.gitbook/assets/bug%20%2859%29.jpg) | Fixed generalModel imports and optimize video click handlers with useCallback hooks |
| ![](../.gitbook/assets/bug%20%2898%29.jpg) | Fix for selectEmbedModelVersionId in detection apps |
| ![](../.gitbook/assets/bug%20%2830%29.jpg) | Drawing annotations: wrong embed model version id |
| ![](../.gitbook/assets/bug%20%2815%29.jpg) | Made custom training evaluations for large models stable. |
| ![](../.gitbook/assets/bug.jpg) | Training progress is saved too frequently, causing very slow training |
| ![](../.gitbook/assets/bug%20%284%29.jpg) | Return friendlier errors for incorrect parameters passed to templates |
| ![](../.gitbook/assets/bug%20%2879%29.jpg) | Fixed a bug in tracing setup for custom trainer and evaluator |
| ![](../.gitbook/assets/bug%20%2874%29.jpg) | Some models were operating slowly because of lack of resources. Fixed |
| ![](../.gitbook/assets/bug%20%2833%29.jpg) | Training System failed to train some layers. Fixed |
| ![](../.gitbook/assets/bug%20%2848%29.jpg) | Prevent users from evaluating models that are not trainable |
| ![](../.gitbook/assets/bug%20%2852%29.jpg) | Fixed node ID validation logic in Bug in workflows |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%288%29.jpg) | Add colors to differentiate region results |
| ![](../.gitbook/assets/bug%20%2817%29.jpg) | Cannot view workflow results in a face app. Fixed |
| ![](../.gitbook/assets/bug%20%2867%29.jpg) | Video spire tests are not running correctly. Fixed |
| ![](../.gitbook/assets/bug%20%28104%29.jpg) | Video processing fails with 'caseids' error. fixed |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%282%29.jpg) | Add click to search metadata attributes in image details sidebar |
| ![](../.gitbook/assets/new_feature%20%2813%29.jpg) | Implement visual search in another app as a model type you can add to a workflow |
| ![](../.gitbook/assets/bug%20%2872%29.jpg) | Search bar missing in some cases. Fixed |
| ![](../.gitbook/assets/bug%20%2891%29.jpg) | Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed |
| ![](../.gitbook/assets/bug%20%2824%29.jpg) | Click Search button icons on Thumbs not working for localized search. Fixed |
| ![](../.gitbook/assets/bug%20%2813%29.jpg) | Disable all search by click handlers in Portal for Text Apps |
| ![](../.gitbook/assets/bug%20%2828%29.jpg) | Disable "hide all positively labeled" inputs button for NLP until search works |
| ![](../.gitbook/assets/bug%20%289%29.jpg) | Scroll active thumb into view in image details carousel |
| ![](../.gitbook/assets/bug%20%2845%29.jpg) | Render Video Assets in Search Bar |
| ![](../.gitbook/assets/bug%20%2889%29.jpg) | Editing geo/json search items no longer work after adding the search bar tooltip. Fixed |
| ![](../.gitbook/assets/bug%20%2812%29.jpg) | TypeError: Cannot read 'get' of undefined when clicking image thumbnails in Explorer search bar. Fixed |
| ![](../.gitbook/assets/bug%20%2861%29.jpg) | Explorer Visibility in small resolution screen improved |

## Change Log 5.10

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%281%29.jpg) | ![](../.gitbook/assets/improvement%20%284%29.jpg) | ![](../.gitbook/assets/bug%20%2837%29.jpg) | ![](../.gitbook/assets/enterprise%20%282%29.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2811%29.jpg) | Create delete email endpoints in v2 to finally get off old internal endpoints to streamline operations |
| ![](../.gitbook/assets/new_feature%20%2814%29.jpg) | Create Patch, Delete, Get CreditCards endpoint in v2 APIs to finally get off old internal endpoints to streamline operations |
| ![](../.gitbook/assets/improvement%20%2814%29.jpg) | Improved billing for collaborators |
| ![](../.gitbook/assets/bug%20%2842%29.jpg) | PostVerifyEmail error causing some issues not being able to verify their email addresses upon sign-up. Fixed |
| ![](../.gitbook/assets/bug%20%2868%29.jpg) | Fixed flaky email verification integration test to provide more stability to sign-up process |
| ![](../.gitbook/assets/bug%20%2885%29.jpg) | Fixed a link to a non-public version of our API used for development purposes which led to a lot of login issues for users who landed there |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%287%29.jpg) | Created display for scopes on collaborator invitations, allowing users to easily understand and control the scope of access allowed for app collaborators |
| ![](../.gitbook/assets/new_feature%20%284%29.jpg) | Introduced Collaborators and Collaborations endpoints in API and UIs in Portal |
| ![](../.gitbook/assets/new_feature%20%283%29.jpg) | Add ability to upload inputs from App Details screen in Portal |
| ![](../.gitbook/assets/improvement%20%2815%29.jpg) | Created collaboration tab in Portal, making it easy to add collaborators to apps |
| ![](../.gitbook/assets/improvement%20%282%29.jpg) | Created display to show the user who invited you to collaborate on an app |
| ![](../.gitbook/assets/improvement%20%2816%29.jpg) | Update email phrases for collaborator invitations. After successful sign-up, the user is now redirected to the app's dashboard in Portal |
| ![](../.gitbook/assets/bug%20%2814%29.jpg) | Fixed issue with concept counts in some apps |
| ![](../.gitbook/assets/bug%20%2855%29.jpg) | Clicking pencil icon to edit an API Key in Portal crashed apps. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2821%29.jpg) | PATCH /inputs needs to check status of asset before patching |
| ![](../.gitbook/assets/improvement%20%2813%29.jpg) | Removed sync DELETE /inputs after runtime config tested |
| ![](../.gitbook/assets/improvement%20%2812%29.jpg) | Changed POST /inputs to be async always to simplify processing of workflows after API client tests updated |
| ![](../.gitbook/assets/improvement%20%2827%29.jpg) | Added pagination to clusters making for easier data management |
| ![](../.gitbook/assets/bug%20%2892%29.jpg) | Sporadic inability to delete any inputs via Portal or in bulk via the API |
| ![](../.gitbook/assets/bug%20%2851%29.jpg) | Numerous third party security fixes under the hood during ongoing upgrades |
| ![](../.gitbook/assets/bug%20%281%29.jpg) | Fix 40012 status caused by parallel deletes and adds having a race condition |
| ![](../.gitbook/assets/bug%20%2876%29.jpg) | Update status\_changed\_at when deleting inputs so we can better track changes |
| ![](../.gitbook/assets/bug%20%2818%29.jpg) | Cache the input counts so that apps can display them in Portal efficiently |
| ![](../.gitbook/assets/bug%20%2862%29.jpg) | Handle killing URL downloading if it is processing for more than 60s. This will make URL processing much more reliable |
| ![](../.gitbook/assets/bug%20%2854%29.jpg) | Return an error if a user sends YouTube video URL as that is not a valid URL to a video we can download |
| ![](../.gitbook/assets/bug%20%2866%29.jpg) | Prevent PostInputs from creating inputs with a user-provided Input.ID that contains a colon |
| ![](../.gitbook/assets/bug%20%28107%29.jpg) | Video calls failed if URLs contain parameters after the file type. Fixed |
| ![](../.gitbook/assets/bug%20%2870%29.jpg) | Failed to resolve DNS MX record in URL down-loader which effected some downloads. Fixed |
| ![](../.gitbook/assets/bug%20%2869%29.jpg) | Investigate why some re-hosted s3 links are no longer working |
| ![](../.gitbook/assets/bug%20%2896%29.jpg) | Getting input counts was broken in some apps, reporting zero, which caused Portal to add an input view to display always |
| ![](../.gitbook/assets/bug%20%2810%29.jpg) | Debug UnicodeErrors in URL downloading to fix URLs with Unicode characters |
| ![](../.gitbook/assets/bug%20%2864%29.jpg) | Fix the poor handling of video too large error message |
| ![](../.gitbook/assets/bug%20%2831%29.jpg) | Unable to batch delete inputs from time to time has been fixed |
| ![](../.gitbook/assets/bug%20%2871%29.jpg) | Media processor video handling was having errors with decoding some videos |
| ![](../.gitbook/assets/bug%20%2880%29.jpg) | Delete Image Button doesn't work in some scenarios |
| ![](../.gitbook/assets/bug%20%2819%29.jpg) | Fixed support for webp image format so it is available again |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%285%29.jpg) | Deploy General Detection Beta Model to recognize multiple objects with bounding boxes. |
| ![](../.gitbook/assets/new_feature%20%2818%29.jpg) | Deployed new face detector for improved face detection performance over images and video |
| ![](../.gitbook/assets/new_feature%20%286%29.jpg) | Created custom training enhancements that handle negatives better for improved model performance |
| ![](../.gitbook/assets/new_feature%20%2816%29.jpg) | Created evaluation metrics for custom facial recognition in backend for improved facial recognition performance |
| ![](../.gitbook/assets/improvement%20%2817%29.jpg) | Topological sort for workflows for scheduling a sequence based on dependencies |
| ![](../.gitbook/assets/improvement%20%2820%29.jpg) | Cleaned up duplicate models in workflow model list |
| ![](../.gitbook/assets/improvement%20%286%29.jpg) | Deployed public general v1.5 in concept model |
| ![](../.gitbook/assets/improvement%20%2819%29.jpg) | Create Pixel Training Hyperparameter Help Guide |
| ![](../.gitbook/assets/improvement.jpg) | Improved accuracy of annotation counts, improving the user experience when annotating inputs |
| ![](../.gitbook/assets/bug%20%2882%29.jpg) | If an image is tagged with a concept that is not in the model, training fails due to KeyError, this is fixed |
| ![](../.gitbook/assets/bug%20%2865%29.jpg) | Fix detection labeling bug where previous images image ratio is used which would cause display issues |
| ![](../.gitbook/assets/bug%20%2893%29.jpg) | We have updated Portal to scale to a large number of concepts with much lower resource usage |
| ![](../.gitbook/assets/bug%20%2811%29.jpg) | Investigate face bounding box probabilities consistency to improve user experience |
| ![](../.gitbook/assets/bug%20%2826%29.jpg) | Bounding box creation canvas in Portal was breaking on resize of the window |
| ![](../.gitbook/assets/bug%20%286%29.jpg) | Model |
| ![](../.gitbook/assets/bug%20%288%29.jpg) | Cleaned up duplicate models in the workflow model list, so that you no longer see two General models |
| ![](../.gitbook/assets/bug%20%283%29.jpg) | Unintended behavior for private model version IDs for certain customers has been fixed |
| ![](../.gitbook/assets/bug%20%2856%29.jpg) | Models referencing deleted backends should be marked as deleted |
| ![](../.gitbook/assets/bug%20%2840%29.jpg) | The latest version of our general model wasn't always default, now it is |
| ![](../.gitbook/assets/bug%20%28105%29.jpg) | Fixed a bug with face recognition evaluations. |
| ![](../.gitbook/assets/bug%20%2820%29.jpg) | Deleted Concepts Persisted in face recognition models. Not anymore! |
| ![](../.gitbook/assets/bug%20%28102%29.jpg) | Inability to see whether a large model is training and making progress, or hung has been addressed to better support our customers |
| ![](../.gitbook/assets/bug%20%2832%29.jpg) | Model won't train in some apps with no positive examples issue has been resolved |
| ![](../.gitbook/assets/bug%20%2839%29.jpg) | Fixed issues with color models failing for a short period of time |
| ![](../.gitbook/assets/bug%20%2835%29.jpg) | Fixed list of models available to workflows to only show a single General model |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%288%29.jpg) | Return custom detection evaluations through the GO API |
| ![](../.gitbook/assets/improvement%20%2823%29.jpg) | Improved cluster page performance |
| ![](../.gitbook/assets/bug%20%2858%29.jpg) | Investigate health checks killing a prediction backend service, which could affect some predictions in the API |
| ![](../.gitbook/assets/bug%20%2847%29.jpg) | Workflow predict sometimes was failing with 98012 status code. Many fixes here should reduce that |
| ![](../.gitbook/assets/bug%20%2821%29.jpg) | Workflow Predict called the wrong model sometimes. Not any more! |
| ![](../.gitbook/assets/bug%20%2863%29.jpg) | Video playback out of sync with detections in our demos |
| ![](../.gitbook/assets/bug%20%282%29.jpg) | Fixed issues with regions predicted on inputs would be carried over between inputs in Portal |
| ![](../.gitbook/assets/bug%20%2877%29.jpg) | Fixed the flaky face recognition tests to ensure stability of our face recognition product |
| ![](../.gitbook/assets/bug%20%28106%29.jpg) | Face Detection backends were running out of memory for some predictions, this has been resolved |
| ![](../.gitbook/assets/bug%20%2890%29.jpg) | Return more descriptive error msg for post metric endpoint |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%281%29.jpg) | Added helper text/suggestions to improve Portal user experience |
| ![](../.gitbook/assets/improvement%20%2818%29.jpg) | Header Search return app\_owner's user info in collaboration endpoints |
| ![](../.gitbook/assets/bug%20%2841%29.jpg) | Explorer Search Bar - Clicking the green/red circle icons didn't reliably detect click, now it does! |
| ![](../.gitbook/assets/bug%20%2823%29.jpg) | Portal not showing the correct number of results in concept search. Fixed. |
| ![](../.gitbook/assets/bug%20%2899%29.jpg) | Left/right arrows in single image view don't switch between images with regions. Fixed |
| ![](../.gitbook/assets/bug%20%28101%29.jpg) | Fixed carousel thumbnail clicks wiping query params / trigger new search |

