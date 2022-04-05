---
description: Changelog for Clarifai Release 5.10
---

# Release 5.10

## Changelog 5.10

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Create delete email endpoints in v2 to finally get off old internal endpoints to streamline operations |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Create Patch, Delete, Get CreditCards endpoint in v2 APIs to finally get off old internal endpoints to streamline operations |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Improved billing for collaborators |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | PostVerifyEmail error causing some issues not being able to verify their email addresses upon sign-up. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed flaky email verification integration test to provide more stability to sign-up process |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed a link to a non-public version of our API used for development purposes which led to a lot of login issues for users who landed there |

### Applications

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Created display for scopes on collaborator invitations, allowing users to easily understand and control the scope of access allowed for app collaborators |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Introduced Collaborators and Collaborations endpoints in API and UIs in Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Add ability to upload inputs from App Details screen in Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Created collaboration tab in Portal, making it easy to add collaborators to apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Created display to show the user who invited you to collaborate on an app |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update email phrases for collaborator invitations. After successful sign-up, the user is now redirected to the app's dashboard in Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed issue with concept counts in some apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Clicking pencil icon to edit an API Key in Portal crashed apps. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | PATCH /inputs needs to check status of asset before patching |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Removed sync DELETE /inputs after runtime config tested |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Changed POST /inputs to be async always to simplify processing of workflows after API client tests updated |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Added pagination to clusters making for easier data management |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Sporadic inability to delete any inputs via Portal or in bulk via the API |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Numerous third party security fixes under the hood during ongoing upgrades |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix 40012 status caused by parallel deletes and adds having a race condition |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Update status\_changed\_at when deleting inputs so we can better track changes |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Cache the input counts so that apps can display them in Portal efficiently |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Handle killing URL downloading if it is processing for more than 60s. This will make URL processing much more reliable |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Return an error if a user sends YouTube video URL as that is not a valid URL to a video we can download |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Prevent PostInputs from creating inputs with a user-provided Input.ID that contains a colon |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video calls failed if URLs contain parameters after the file type. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Failed to resolve DNS MX record in URL down-loader which effected some downloads. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Investigate why some re-hosted s3 links are no longer working |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Getting input counts was broken in some apps, reporting zero, which caused Portal to add an input view to display always |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Debug UnicodeErrors in URL downloading to fix URLs with Unicode characters |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix the poor handling of video too large error message |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Unable to batch delete inputs from time to time has been fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Media processor video handling was having errors with decoding some videos |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Delete Image Button doesn't work in some scenarios |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed support for webp image format so it is available again |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Deploy General Detection Beta Model to recognize multiple objects with bounding boxes. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Deployed new face detector for improved face detection performance over images and video |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Created custom training enhancements that handle negatives better for improved model performance |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Created evaluation metrics for custom facial recognition in backend for improved facial recognition performance |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Topological sort for workflows for scheduling a sequence based on dependencies |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Cleaned up duplicate models in workflow model list |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Deployed clarifai/main general v1.5 in concept model |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Create Pixel Training Hyperparameter Help Guide |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Improved accuracy of annotation counts, improving the user experience when annotating inputs |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | If an image is tagged with a concept that is not in the model, training fails due to KeyError, this is fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix detection labeling bug where previous images image ratio is used which would cause display issues |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | We have updated Portal to scale to a large number of concepts with much lower resource usage |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Investigate face bounding box probabilities consistency to improve user experience |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Bounding box creation canvas in Portal was breaking on resize of the window |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Model |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Cleaned up duplicate models in the workflow model list, so that you no longer see two General models |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Unintended behavior for private model version IDs for certain customers has been fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Models referencing deleted backends should be marked as deleted |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | The latest version of our general model wasn't always default, now it is |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed a bug with face recognition evaluations. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Deleted Concepts Persisted in face recognition models. Not anymore! |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Inability to see whether a large model is training and making progress, or hung has been addressed to better support our customers |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Model won't train in some apps with no positive examples issue has been resolved |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed issues with color models failing for a short period of time |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed list of models available to workflows to only show a single General model |

### Predict

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Return custom detection evaluations through the GO API |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Improved cluster page performance |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Investigate health checks killing a prediction backend service, which could affect some predictions in the API |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Workflow predict sometimes was failing with 98012 status code. Many fixes here should reduce that |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Workflow Predict called the wrong model sometimes. Not any more! |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video playback out of sync with detections in our demos |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed issues with regions predicted on inputs would be carried over between inputs in Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed the flaky face recognition tests to ensure stability of our face recognition product |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Face Detection backends were running out of memory for some predictions, this has been resolved |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Return more descriptive error msg for post metric endpoint |

### Search

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Added helper text/suggestions to improve Portal user experience |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Header Search return app\_owner's user info in collaboration endpoints |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Explorer Search Bar - Clicking the green/red circle icons didn't reliably detect click, now it does! |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Portal not showing the correct number of results in concept search. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Left/right arrows in single image view don't switch between images with regions. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed carousel thumbnail clicks wiping query params / trigger new search |
