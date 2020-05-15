# Changelog 6.1

|New Feature|Improvement|Bug Fix|Enterprise Only
|:-:|:-:|:-:|:-:|
|![](/images/new_feature.jpg)|![](/images/improvement.jpg)|![](/images/bug.jpg)|![](/images/enterprise.jpg)


## Clients
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Remove Feedback endpoints from Python client                                                     |
|![](/images/improvement.jpg)|Remove Feedback endpoints from Java client                                                       |
|![](/images/improvement.jpg)|Remove Feedback endpoints from Javascript client                                                 |
|![](/images/improvement.jpg)|Remove Feedback endpoints from Portal/demo                                                       |
|![](/images/improvement.jpg)|Remove image.crop field from Python API client                                                   |
|![](/images/improvement.jpg)|Remove image.crop field from Java API client                                                     |
|![](/images/improvement.jpg)|Remove image.crop field from Javascript API client

## Model
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg) |Added detection evaluation in platform                                                                 |
|![](/images/new_feature.jpg)|Introduce concept mapping model that uses the knowledge graph relations, creating a path for users to eventually benefit from pool of networked data
|![](/images/bug.jpg)|Fix a bug that caused the new face predictions to have a huge performance drop                                   |
|![](/images/bug.jpg)|Train and eval worker didn't invalidate model related cache. Fixed                               |
|![](/images/bug.jpg)|Fix bug in deleting a concept relation by ID                                                     |

## Portal
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Bulk labelling can now be done from Explorer mode.|
|![](/images/improvement.jpg)|Show Check/X on custom detection model predictions in Portal                                     |
|![](/images/improvement.jpg)|Allow multi concepts per bbox
|![](/images/bug.jpg)|Negative tags not visible in Portal. Fixed

## Predict
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Remove extra round trip to storage in predict pathway                                            |
|![](/images/improvement.jpg)|Remove the image.crop argument during predict and POST /inputs calls to simplify the API         |
|![](/images/improvement.jpg)|Add region predictions from custom models to detections in videos

## Search
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg) |Implement search by annotation.status in backend                                                 |
|![](/images/improvement.jpg)|Connect saved searches and annotation status

## Workflow
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Implement thresholding workflow as pre-queue workflow


# Changelog 6.0

|New Feature|Improvement|Bug Fix|Enterprise Only
|:-:|:-:|:-:|:-:|
|![](/images/new_feature.jpg)|![](/images/improvement.jpg)|![](/images/bug.jpg)|![](/images/enterprise.jpg)

## Accounts
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Remove country field from signup form, simplifying new customer signups
|![](/images/bug.jpg)|Essential Plan User can't add collaborators. Fixed


## API
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg) |Introduce new [Python gRPC API client](https://docs.clarifai.com/api-guide/api-overview), enabling new features and performance enhancements across API
|![](/images/new_feature.jpg) |Introduce new [Java gRPC API client](https://docs.clarifai.com/api-guide/api-overview), enabling new features and performance enhancements across API
|![](/images/improvement.jpg)|Update API key type for "app_specific" for app-specific keys to be more clear to users


## Applications
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg) |Allow Personal Access Tokens when calling /users/me (GetUsers)
|![](/images/new_feature.jpg)|[Frontend] Enable "Copy Application" from collaborated apps, making it easy to duplicate and build upon existing applications
|![](/images/bug.jpg)|Program to clean internal apps crashing. Fixed


## Data Management
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Added the ability to accept b64 Gifs
|![](/images/bug.jpg)|Functionality to upload pre-tagged images missing. Fixed
|![](/images/bug.jpg)|Images pre-tagged with concepts do not successfully upload into Clarifai UI On doing bulk uploads (>20-30 urls). Fixed
|![](/images/bug.jpg)|Bulk image upload issue. Fixed
|![](/images/bug.jpg)|"Download Failed" error when uploading images. Fixed
|![](/images/bug.jpg)|Issue with post inputs key being a PAT in a collector. Fixed


## Annotate
|Status|Details|
|-|-------|
|![](/images/bug.jpg)|Skip aligning landmarks if landmark points are out of range to avoid errors and unexpected behavior
|![](/images/bug.jpg)|Bounding Boxes and Cropped Regions aren't displaying on Videos with default runtime config. Fixed
|![](/images/bug.jpg)|Insert annotations and related data in batch to improve performance


## Model
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Evaluate new face embedding model workflow end to end for optimal performance
|![](/images/improvement.jpg)|Validate that concept.app_id shouldn't be set when creating/patching models
|![](/images/improvement.jpg)|Add new predicate to knowledge graph for "relates_to" to represent synonyms
|![](/images/bug.jpg)|Model training lag. Fixed
|![](/images/bug.jpg)|Model has missing inputs. Fixed
|![](/images/bug.jpg)|Submitted models becoming stuck in queue. Fixed
|![](/images/bug.jpg)|Custom training models when uploaded images are not fully pre-processed. Fixed
|![](/images/bug.jpg)|Custom facial recognition bboxes do not correspond with detection boxes/ Custom facial recognition prediction interval for video is still 1000ms for apps supporting 100ms runtime config. Fixed
|![](/images/bug.jpg)|frame_info time off by a factor of 10 for general detection model. Fixed
|![](/images/bug.jpg)|Detection Models throw error at end of video due to invalid index lookup. Fixed


## Workflow
|Status|Details|
|-|-------|
|![](/images/bug.jpg)|Deleting a workflow should clear or update localStorage. Fixed

## Portal
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Clean up app overflow UI, improving user experience
|![](/images/improvement.jpg)|Improve Error boundary screen, improving user experience
|![](/images/improvement.jpg)|Add sentry error Id to Error Screen
|![](/images/bug.jpg)|Images not loading. Fixed
|![](/images/bug.jpg)|Label and prediction on the right side under Custom Model Predictions section no longer shows up automatically. Fixed
|![](/images/bug.jpg)|Provide a way for user.metadata to be updated from portal when there are failing apps stuck in there. Fixed
|![](/images/bug.jpg)|Predictions for a detection model don't show properly in portal. Fixed
|![](/images/bug.jpg)|Custom facial recognition Predict Boxes not displaying. Fixed
|![](/images/bug.jpg)|Adding inputs in explorer redirects to explorer view with flashing images. Fixed


## Predict
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Run prediction by ID in small batch, improving performance
|![](/images/bug.jpg)|Custom model predictions not displaying. Fixed
|![](/images/bug.jpg)|Custom model detections not displaying. Fixed


## Search
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg) |Add file upload input button to explorer search bar, simplifying the UX for file uploads
|![](/images/new_feature.jpg) |Filter custom facial recognition bboxes using a sliding bar, adding easy thresholding to custom facial recognition models
|![](/images/improvement.jpg)|Search Bar allows file upload
|![](/images/improvement.jpg)|Remove Explorer App Overflow Menu for improved UX



# Changelog 5.11

|New Feature|Improvement|Bug Fix|Enterprise Only
|:-:|:-:|:-:|:-:|
|![](/images/new_feature.jpg)|![](/images/improvement.jpg)|![](/images/bug.jpg)|![](/images/enterprise.jpg)

## Accounts
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg) |Create a UI for personal access tokens making it easier for users to access their own apps and any apps where they have been added as collaborators|
|![](/images/new_feature.jpg)| Updated /keys to work with PATs so that app-specific keys can be created programmatically. |
|![](/images/bug.jpg)|Login (user/PW) has no rate limit/max attempts. Fixed|
|![](/images/bug.jpg)|Remove all instances of worker_id from explorer
|![](/images/bug.jpg)|When email link to verify my email address clicked, still see "verify your email" banner. Fixed
|![](/images/bug.jpg) ![](/images/enterprise.jpg)|API services do not function once Queue goes down and comes back up. Fixed. This makes on premise deployments more resilient to power failures.

## Applications
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Add apps and keys scopes so they can be created with personal access tokens|
|![](/images/improvement.jpg) ![](/images/enterprise.jpg)|Copy app count and last_inputs added in app duplication
|![](/images/bug.jpg)|Fixed demo font syntax
|![](/images/bug.jpg)|Fixed details page header missing description
|![](/images/bug.jpg)|Added favicon for Portal
|![](/images/bug.jpg)|Unable to copy an app that has been shared via Collaborators. Fixed
|![](/images/bug.jpg)|Setting useCustomConfig isn't checked at login. Fixed
|![](/images/bug.jpg)|Collaboration apps have race condition where wrong user id is used
|![](/images/bug.jpg)|Stopped loading of collaborations for search demo/logged-out users
|![](/images/bug.jpg)|Return “All” scopes when listing available scopes so that you have that option when creating new keys.
|![](/images/bug.jpg)|Collaborators can not see workers. Fixed
|![](/images/bug.jpg)|Missing `Apps_Get` scope in session token auth caused creation of keys to fail temporarily. Fixed
|![](/images/bug.jpg)|List of missing scopes is not correct in error messages. Fixed

## Data Management
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Optimize video detection frame rate on Front end
|![](/images/improvement.jpg)|Improve JSON serialization performance in our servers by using an optimized third party library
|![](/images/improvement.jpg)|Able to overwrite default max conn for Citus
|![](/images/improvement.jpg)|Rewrite input counting in the API to be more scalable and robust
|![](/images/bug.jpg)|Allow RegionInfo from SpireDetectEmbedResponse to contain Point when saving to DB
|![](/images/bug.jpg)|Unable to upload same file(s) through browse files. Fixed
|![](/images/bug.jpg)|ffmpeg can produce no frames for very short videos
|![](/images/bug.jpg)|Add Inputs/View Explorer does not display in new app anymore. Fixed
|![](/images/bug.jpg)|Clicking video thumbs in detail view does not reload a video. Fixed
|![](/images/bug.jpg)|Keyboard navigation in image details view highlights incorrect thumb
|![](/images/bug.jpg)|No Prompt when uploading an image to Explorer through URL. Fixed
|![](/images/bug.jpg)|Properly return error if `AddAssets` failed to insert into database

## Annotate
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Remove classification/detection toggle in image details view
|![](/images/bug.jpg)|Improved adding negatives to regions
|![](/images/bug.jpg)|Create one annotation for each bbox
|![](/images/bug.jpg)|Log capability added for annotation/search request/response
|![](/images/bug.jpg)|Eliminated error if no annotation to be deleted
|![](/images/bug.jpg)|Last concept used for bounding boxes is retained between apps. Fixed
|![](/images/bug.jpg)|The Add Positives / Add Negatives buttons on a Concept details view breaks portal
|![](/images/bug.jpg)|Custom facial recognition bboxes on grid view do not correlate. Fixed

## Model
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Ability to keep concepts sorted by alpha in Portal
|![](/images/new_feature.jpg)|Implement image crop model to make it possible to work in subregions of an image
|![](/images/new_feature.jpg)|Implement random sample model type, adding to fixed function feature set
|![](/images/improvement.jpg)|Update training templates to have more straightforward names and more friendly defaults
|![](/images/improvement.jpg)|Fix the WorkflowInput field name in proto to workflow_input
|![](/images/improvement.jpg)|Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models
|![](/images/bug.jpg)|Confusion matrix predicted/true are swapped in evaluation results. Fixed
|![](/images/bug.jpg)|Fixed generalModel imports and optimize video click handlers with useCallback hooks
|![](/images/bug.jpg)|Fix for selectEmbedModelVersionId in detection apps
|![](/images/bug.jpg)|Drawing annotations: wrong embed model version id
|![](/images/bug.jpg)|Made custom training evaluations for large models stable.
|![](/images/bug.jpg)|Training progress is saved too frequently, causing very slow training
|![](/images/bug.jpg)|Return friendlier errors for incorrect parameters passed to templates
|![](/images/bug.jpg)|Fixed a bug in tracing setup for custom trainer and evaluator
|![](/images/bug.jpg)|Some models were operating slowly because of lack of resources. Fixed
|![](/images/bug.jpg)|Training System failed to train some layers. Fixed
|![](/images/bug.jpg)|Prevent users from evaluating models that are not trainable
|![](/images/bug.jpg)|Fixed node ID validation logic in Bug in workflows

## Predict
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Add colors to differentiate region results
|![](/images/bug.jpg)|Cannot view workflow results in a face app. Fixed
|![](/images/bug.jpg)|Video spire tests are not running correctly. Fixed
|![](/images/bug.jpg)|Video processing fails with 'caseids' error. fixed

## Search
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Add click to search metadata attributes in image details sidebar
|![](/images/new_feature.jpg)|Implement visual search in another app as a model type you can add to a workflow
|![](/images/bug.jpg)|Search bar missing in some cases. Fixed
|![](/images/bug.jpg)|Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed
|![](/images/bug.jpg)|Click Search button icons on Thumbs not working for localized search. Fixed
|![](/images/bug.jpg)|Disable all search by click handlers in Portal for Text Apps
|![](/images/bug.jpg)|Disable "hide all positively labeled" inputs button for NLP until search works
|![](/images/bug.jpg)|Scroll active thumb into view in image details carousel
|![](/images/bug.jpg)|Render Video Assets in Search Bar
|![](/images/bug.jpg)|Editing geo/json search items no longer work after adding the search bar tooltip. Fixed
|![](/images/bug.jpg)|TypeError: Cannot read 'get' of undefined when clicking image thumbnails in Explorer search bar. Fixed
|![](/images/bug.jpg)|Explorer Visibility in small resolution screen improved


# Changelog 5.10
|New Feature|Improvement|Bug Fix|Enterprise Only
|:-:|:-:|:-:|:-:|
|![](/images/new_feature.jpg)|![](/images/improvement.jpg)|![](/images/bug.jpg)|![](/images/enterprise.jpg)

## Accounts
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Create delete email endpoints in v2 to finally get off old internal endpoints to streamline operations
|![](/images/new_feature.jpg)|Create Patch, Delete, Get CreditCards endpoint in v2 APIs to finally get off old internal endpoints to streamline operations
|![](/images/improvement.jpg)|Improved billing for collaborators
|![](/images/bug.jpg)|PostVerifyEmail error causing some issues not being able to verify their email addresses upon sign-up. Fixed
|![](/images/bug.jpg)|Fixed flaky email verification integration test to provide more stability to sign-up process
|![](/images/bug.jpg)|Fixed a link to a non-public version of our API used for development purposes which led to a lot of login issues for users who landed there

## Applications
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Created display for scopes on collaborator invitations, allowing users to easily understand and control the scope of access allowed for app collaborators
|![](/images/new_feature.jpg)|Introduced Collaborators and Collaborations endpoints in API and UIs in Portal
|![](/images/new_feature.jpg)|Add ability to upload inputs from App Details screen in Portal
|![](/images/improvement.jpg)|Created collaboration tab in Portal, making it easy to add collaborators to apps
|![](/images/improvement.jpg)|Created display to show the user who invited you to collaborate on an app
|![](/images/improvement.jpg)|Update email phrases for collaborator invitations. After successful sign-up, the user is now redirected to the app's dashboard in Portal
|![](/images/bug.jpg)|Fixed issue with concept counts in some apps
|![](/images/bug.jpg)|Clicking pencil icon to edit an API Key in Portal crashed apps. Fixed

## Data Management
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|PATCH /inputs needs to check status of asset before patching
|![](/images/improvement.jpg)|Removed sync DELETE /inputs after runtime config tested
|![](/images/improvement.jpg)|Changed POST /inputs to be async always to simplify processing of workflows after API client tests updated
|![](/images/improvement.jpg)|Added pagination to clusters making for easier data management
|![](/images/bug.jpg)|Sporadic inability to delete any inputs via Portal or in bulk via the API
|![](/images/bug.jpg)|Numerous third party security fixes under the hood during ongoing upgrades
|![](/images/bug.jpg)|Fix 40012 status caused by parallel deletes and adds having a race condition
|![](/images/bug.jpg)|Update status\_changed\_at when deleting inputs so we can better track changes
|![](/images/bug.jpg)|Cache the input counts so that apps can display them in Portal efficiently
|![](/images/bug.jpg)|Handle killing URL downloading if it is processing for more than 60s. This will make URL processing much more reliable
|![](/images/bug.jpg)|Return an error if a user sends YouTube video URL as that is not a valid URL to a video we can download
|![](/images/bug.jpg)|Prevent PostInputs from creating inputs with a user-provided Input.ID that contains a colon
|![](/images/bug.jpg)|Video calls failed if URLs contain parameters after the file type. Fixed
|![](/images/bug.jpg)|Failed to resolve DNS MX record in URL down-loader which effected some downloads. Fixed
|![](/images/bug.jpg)|Investigate why some re-hosted s3 links are no longer working
|![](/images/bug.jpg)|Getting input counts was broken in some apps, reporting zero, which caused Portal to add an input view to display always
|![](/images/bug.jpg)|Debug UnicodeErrors in URL downloading to fix URLs with Unicode characters
|![](/images/bug.jpg)|Fix the poor handling of video too large error message
|![](/images/bug.jpg)|Unable to batch delete inputs from time to time has been fixed
|![](/images/bug.jpg)|Media processor video handling was having errors with decoding some videos
|![](/images/bug.jpg)|Delete Image Button doesn't work in some scenarios
|![](/images/bug.jpg)|Fixed support for webp image format so it is available again

## Annotate
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Deploy General Detection Beta Model to recognize multiple objects with bounding boxes.
|![](/images/new_feature.jpg)|Deployed new face detector for improved face detection performance over images and video
|![](/images/new_feature.jpg)|Created custom training enhancements that handle negatives better for improved model performance
|![](/images/new_feature.jpg)|Created evaluation metrics for custom facial recognition in backend for improved facial recognition performance
|![](/images/improvement.jpg)|Topological sort for workflows for scheduling a sequence based on dependencies
|![](/images/improvement.jpg)|Cleaned up duplicate models in workflow model list
|![](/images/improvement.jpg)|Deployed clarifai/main general v1.5 in concept model
|![](/images/improvement.jpg)|Create Pixel Training Hyperparameter Help Guide
|![](/images/improvement.jpg)|Improved accuracy of annotation counts, improving the user experience when annotating inputs
|![](/images/bug.jpg)|If an image is tagged with a concept that is not in the model, training fails due to KeyError, this is fixed
|![](/images/bug.jpg)|Fix detection labeling bug where previous images image ratio is used which would cause display issues
|![](/images/bug.jpg)|We have updated Portal to scale to a large number of concepts with much lower resource usage
|![](/images/bug.jpg)|Investigate face bounding box probabilities consistency to improve user experience
|![](/images/bug.jpg)|Bounding box creation canvas in Portal was breaking on resize of the window
|![](/images/bug.jpg)|Model
|![](/images/bug.jpg)|Cleaned up duplicate models in the workflow model list, so that you no longer see two General models
|![](/images/bug.jpg)|Unintended behavior for private model version IDs for certain customers has been fixed
|![](/images/bug.jpg)|Models referencing deleted backends should be marked as deleted
|![](/images/bug.jpg)|The latest version of our general model wasn't always default, now it is
|![](/images/bug.jpg)|Fixed a bug with face recognition evaluations.
|![](/images/bug.jpg)|Deleted Concepts Persisted in face recognition models. Not anymore!
|![](/images/bug.jpg)|Inability to see whether a large model is training and making progress, or hung has been addressed to better support our customers
|![](/images/bug.jpg)|Model won't train in some apps with no positive examples issue has been resolved
|![](/images/bug.jpg)|Fixed issues with color models failing for a short period of time
|![](/images/bug.jpg)|Fixed list of models available to workflows to only show a single General model

## Predict
|Status|Details|
|-|-------|
|![](/images/new_feature.jpg)|Return custom detection evaluations through the GO API
|![](/images/improvement.jpg)|Improved cluster page performance
|![](/images/bug.jpg)|Investigate health checks killing a prediction backend service, which could affect some predictions in the API
|![](/images/bug.jpg)|Workflow predict sometimes was failing with 98012 status code. Many fixes here should reduce that
|![](/images/bug.jpg)|Workflow Predict called the wrong model sometimes. Not any more!
|![](/images/bug.jpg)|Video playback out of sync with detections in our demos
|![](/images/bug.jpg)|Fixed issues with regions predicted on inputs would be carried over between inputs in Portal
|![](/images/bug.jpg)|Fixed the flaky face recognition tests to ensure stability of our face recognition product
|![](/images/bug.jpg)|Face Detection backends were running out of memory for some predictions, this has been resolved
|![](/images/bug.jpg)|Return more descriptive error msg for post metric endpoint

## Search
|Status|Details|
|-|-------|
|![](/images/improvement.jpg)|Added helper text/suggestions to improve Portal user experience
|![](/images/improvement.jpg)|Header Search return app_owner's user info in collaboration endpoints
|![](/images/bug.jpg)|Explorer Search Bar - Clicking the green/red circle icons didn't reliably detect click, now it does!
|![](/images/bug.jpg)|Portal not showing the correct number of results in concept search. Fixed.
|![](/images/bug.jpg)|Left/right arrows in single image view don't switch between images with regions. Fixed
|![](/images/bug.jpg)|Fixed carousel thumbnail clicks wiping query params / trigger new search
