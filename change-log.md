## 5.10

### New Feature


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


### Improvement

* Improved accuracy of annotation counts, improving the user experience when annotating inputs
* Topological sort for workflows
* Added helper text/suggestions to improve Portal user experience
* Header Search return app_owner's user info in collaboration endpoints
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

### Bug Fixes
* Cleaned up duplicate models in the workflow model list, so that you no longer see two General models
* Unintended behavior for private model version IDs for certain customers has been fixed
* Sporadic inability to delete any inputs via Portal or in bulk via the API
* Numerous third party security fixes under the hood during ongoing upgrades
* Fix 40012 status caused by parallel deletes and adds having a race condition
* Investigate health checks killing a prediction backend service, which could affect some predictions in the API
* Update status_changed_at when deleting inputs so we can better track changes
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
