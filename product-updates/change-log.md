# Change log 5.11

## Accounts
* Create a UI for personal access tokens making it easier for users to access their own apps and any apps where they have been added as collaborators
* Updated /keys to work with PATs
* Login (user/PW) has no rate limit/max attempts. Fixed
* Remove all instances of worker_id from explorer
* When email link to verify my email address clicked, still see "verify your email" banner. Fixed
* API services do not function once Queue goes down and comes back up. Fixed. This makes on premise deployments more resilient to power failures.

## Applications
* Add apps and keys scopes so they can be created with personal access tokens
* copy app count and last_inputs added in app duplication
* Fixed demo font syntax
* Fixed details page header missing description
* Added favicon for Portal
* Unable to copy an app that has been shared via Collaborators. Fixed
* Setting useCustomConfig isn't checked at login. Fixed
* Collaboration apps have race condition where wrong user id is used
* Stopped loading of collaborations for search demo/logged-out users
* Check the GetInputsKey of collectors has access to user's information
* Return “All” scopes when listing available scopes so that you have that option when creating new keys.
* `created_at` field in sharing table is incorrect. Fixed
* Collaborators can not see workers. Fixed
* Missing `Apps_Get` scope in session token auth caused creation of keys to fail temporarily. Fixed
* List of missing scopes is not correct in error messages. Fixed

## Data Management
* Optimize video detection frame rate on Front end
* Improve JSON serialization performance in our servers by using an optimized third party library
* able to overwrite default max conn for Citus
* Rewrite input counting in the API to be more scalable and robust
* Allow RegionInfo from SpireDetectEmbedResponse to contain Point when saving to DB
* grant select permission to clarifairead
* Unable to upload same file(s) through browse files. Fixed
* ffmpeg can produce no frames for very short videos
* Add Inputs/View Explorer does not display in new app anymore. Fixed
* Clicking video thumbs in detail view does not reload a video. Fixed
* Keyboard navigation in image details view highlights incorrect thumb
* No Prompt when uploading an image to Explorer through URL. Fixed
* Fix collector scopes so that predict keys don't need Collectors:Get
* Properly return error if `AddAssets` failed to insert into database

## Annotate
* Remove classification/detection toggle in image details view
* Mark /annotation endpoints with cl_private_rpc
* Improved adding negatives to regions
* Create one annotation for each bbox
* Log capability added for annotation/search request/response
* Eliminated error if no annotation to be deleted
* Last concept used for bounding boxes is retained between apps. Fixed
* The Add Positives / Add Negatives buttons on a Concept details view breaks portal
* CFR rectangles on grid view do not correlate. Fixed

## Model
* Return deep training evals through the API to automate evaluation process
* Update templates to have more straightforward names and more friendly defaults
* Ability to keep concepts sorted by alpha
* Implement image crop model to make it possible to work in subregions of an image
* Implement RandomSample model type, adding to fixed function feature set
* Fix the WorkflowInput field name in proto to workflow_input
* Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models
* Confusion matrix predicted/true are swapped in evaluation results. Fixed
* Explore Image/Text Joint embedding
* Fixed generalModel imports and optimize video click handlers with useCallback hooks
* Fix for selectEmbedModelVersionId in detection apps
* NLP bug fixes for non text apps
* Drawing annotations: wrong embed model version id
* ConfigRunner Test  test_tf_trainer_progress_status unreliable
* Made custom/transfer training evaluations for large models stable.
* Training progress is saved too frequently, causing very slow training
* Return friendlier errors for incorrect parameters passed to templates
* Fixed a bug in tracing setup for custom trainer and evaluator
* Some models were operating slowly because of lack of resources. Fixed
* Training System failed to train some layers. Fixed
* Prevent users from evaluating models that are not trainable
* Fixed node ID validation logic in Bug in workflows

## Predict
* Add colors to differentiate region results
* Cannot view workflow results in a face app. Fixed
* Video spire tests are not running correctly. Fixed
* Video processing fails with 'caseids' error. fixed

## Search
* Add click to search metadata attributes in image details sidebar
* Implement visual search in another app as a model type you can add to a workflow
* Add metadata to collector added inputs so that you can filter by collector ID
* Search bar missing. Fixed   
* Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed
* Click Search button icons on Thumbs not working for localized search. Fixed
* Disable all search by click handlers in Portal for Text Apps
* Disable "hide all positively labeled" inputs button for NLP until search works
* Scroll active thumb into view in image details carousel
* Render Video Assets in Search Bar
* Editing geo/json search items no longer work after adding the search bar tooltip. Fixed
* TypeError: Cannot read 'get' of undefined when clicking image thumbnails in Explorer search bar. Fixed
* Explorer Visibility in small resolution screen improved


# Change Log 5.10

## New Feature

* Deploy General Detection Beta Model to recognize multiple objects with bounding boxes.
* Create delete email endpoints in v2 to finally get off old internal endpoints to streamline operations.
* Create Patch, Delete, Get CreditCards endpoint in v2 APIs to finally get off old internal endpoints to streamline operations.
* Created display for scopes on collaborator invitations, allowing users to easily understand and control the scope of access allowed for app collaborators
* Deployed new face detector for improved face detection performance over images and video
* Created custom training enhancements that handle negatives better for improved model performance
* Created evaluation metrics for custom facial recognition in backend for improved facial recognition performance
* Introduced Collaborators and Collaborations endpoints in API and UIs in Portal
* Return custom detection evaluations through the GO API
* Custom detection training with new data-dump
* Add ability to upload inputs from App Details screen in Portal

## Improvement

* Improved accuracy of annotation counts, improving the user experience when annotating inputs
* Topological sort for workflows
* Added helper text/suggestions to improve Portal user experience
* Header Search return app\_owner's user info in collaboration endpoints
* Improved billing for collaborators
* Created collaboration tab in Portal, making it easy to add collaborators to apps
* Created display to show the user who invited you to collaborate on an app
* Update email phrases for collaborator invitations
* Cleaned up duplicate models in workflow model list
* PATCH /inputs needs to check status of asset before patching
* Removed sync DELETE /inputs after runtime config tested
* Changed POST /inputs to be async always to simplify processing of workflows after API client tests updated
* Deployed public general v1.5 in concept model
* Create Pixel Training Hyperparameter Help Guide
* Improved cluster page performance
* Added pagination to clusters making for easier data management

## Bug Fixes

* Cleaned up duplicate models in the workflow model list, so that you no longer see two General models
* Unintended behavior for private model version IDs for certain customers has been fixed
* Sporadic inability to delete any inputs via Portal or in bulk via the API
* Numerous third party security fixes under the hood during ongoing upgrades
* Fix 40012 status caused by parallel deletes and adds having a race condition
* Investigate health checks killing a prediction backend service, which could affect some predictions in the API
* Update status\_changed\_at when deleting inputs so we can better track changes
* Workflow predict sometimes was failing with 98012 status code. Many fixes here should reduce that
* Models referencing deleted backends should be marked as deleted
* Cache the input counts so that apps can display them in Portal efficiently
* Handle killing URL downloading if it is processing for more than 60s. This will make URL processing much more reliable
* Return an error if a user sends YouTube video URL as that is not a valid URL to a video we can download
* Workflow Predict called the wrong model sometimes. Not any more!
* The latest version of our general model wasn't always default, now it is
* If an image is tagged with a concept that is not in the model, training fails due to KeyError, this is fixed
* Video playback out of sync with detections in our demos
* Fix detection labeling bug where previous images image ratio is used which would cause display issues
* After successful sign-up, the user is not redirected to the app's dashboard in Portal
* Explorer Search Bar - Clicking the green/red circle icons didn't reliably detect click, now it does!
* We have updated Portal to scale to a large number of concepts with much lower resource usage
* Fixed issues with regions predicted on inputs would be carried over between inputs in Portal
* Fixed the flaky face recognition tests to ensure stability of our face recognition product
* Face Detection backends were running out of memory for some predictions, this has been resolved
* Investigate face bounding box probabilities consistency to improve user experience
* Fixed a bug with face recognition evaluations.
* Deleted Concepts Persisted in face recognition models
* Prevent PostInputs from creating inputs with a user-provided Input.ID that contains a colon
* Fixed issue with concept counts in some apps
* Video calls failed if URLs contain parameters after the file type
* Portal not showing the correct number of results in concept search
* Failed to resolve DNS MX record in URL down-loader which effected some downloads
* Investigate why some re-hosted s3 links are no longer working
* Inability to see whether a large model is training and making progress, or hung has been addressed to better support our customers
* Getting input counts was broken in some apps, reporting zero, which caused Portal to add an input view to display always
* Debug UnicodeErrors in URL downloading to fix URLs with Unicode characters
* Return more descriptive error msg for post metric endpoint
* Fix the poor handling of video too large error message
* PostVerifyEmail error causing some issues not being able to verify their email addresses upon sign-up
* Fixed flaky email verification integration test to provide more stability to sign-up process
* Unable to batch delete inputs from time to time has been fixed
* Media processor video handling was having errors with decoding some videos
* Bounding box creation canvas in Portal was breaking on resize of the window
* Delete Image Button doesn't work in some scenarios
* Left/right arrows in single image view don't switch between images with regions
* Issues with properly consenting to GDPR not being visible in Portal and preventing usage have been fixed
* Model won't train in some apps with no positive examples issue has been resolved
* Fixed a link to a non-public version of our API used for development purposes which led to a lot of login issues for users who landed there
* Fixed issues with color models failing for a short period of time
* Fixed list of models available to workflows to only show a single General model
* Fixed support for webp image format so it is available again
* Clicking pencil icon to edit an API Key in Portal crashed your app
* Fixed carousel thumbnail clicks wiping query params / trigger new search
