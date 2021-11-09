---
description: Changelog for Clarifai Release 6.2
---

# Release 6.2

## Changelog 6.2

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Updated Privacy Policy URL |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed panic error in Signup |

### Applications

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Ensured collectors are deleted when apps are deleted |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | View In Explorer button missing in app details. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed failed to generate thumbnail |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed app duplication error when getting worker |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Deleted collaborator should also mark application\_worker to deleted. Fixed |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Inputs count stuck at &gt; 0 after delete all, with all inputs seemingly deleted |

### Label

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Task view UI for workers |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Create task manager page and task creation page |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | New Icon for Task Manager/Task Viewer |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed POST annotations call on frontend to use correct embed model |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Post annotations should include embed\_model\_version\_id. Fixed |

### Model

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Added Apparel Detection to Demo App |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Created UI for creating knowledge graph concept relations relations |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Create annotation writer model to write annotations to DB |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Pass and use test and train data queries to trainer |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Added migration to upgrade old model\_type in DB |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Depredated Face from Python client |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Unified the TypeExt and Type fields in model object. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Deprecated facedetect\* model types. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Unified FaceEmbedModel and DetectEmbedModel |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Converted face.Identity responses to concepts like other detection models to be consistent |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed demo font syntax |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video Timeline does not display on the demo app |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed Range Slider Value/Text in Apparel Detection Demo |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed demographics model to return embeddings and work with auto-annotate |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Adding collaborator model counter-intuitively requires ENTER in order to enable the submit button. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Validated that concept relation doesn't already exist on POST relations |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Prediction requests are being fired too frequently instead of using cache. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | postModelOutputs is not called for newly labeled assets without a manual refresh |

### Search

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Return annotations posted by user in search results |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Search by region not working for face detection. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Make “save” search button internal only |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Saved Searches in Portal use the incorrect user ID |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix crop search from single image view for faces/detections |

### Portal

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | UI for collector crud |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Deprecate Face from Portal |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Improve tabs UI |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video Predictions are failing in Portal |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed broken font syntax |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Video detection workflow prediction support |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Public general v1.5 workflow |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Allow Patching to existing public workflow |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Can not train LOPQ if app base workflow is face. Fixed |
