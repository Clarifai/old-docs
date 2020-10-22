# Changelog

## Changelog 6.2

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Updated Privacy Policy URL |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed panic error in Signup |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Ensured collectors are deleted when apps are deleted |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | View In Explorer button missing in app details. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed failed to generate thumbnail |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed app duplication error when getting worker |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Deleted collaborator should also mark application\_worker to deleted. Fixed |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Inputs count stuck at &gt; 0 after delete all, with all inputs seemingly deleted |

### Label

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Task view UI for workers |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Create task manager page and task creation page |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | New Icon for Task Manager/Task Viewer |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed POST annotations call on frontend to use correct embed model |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Post annotations should include embed\_model\_version\_id. Fixed |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Added Apparel Detection to Demo App |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Created UI for creating knowledge graph concept relations relations |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Create annotation writer model to write annotations to DB |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Pass and use test and train data queries to trainer |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Added migration to upgrade old model\_type in DB |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Depredated Face from Python client |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Unified the TypeExt and Type fields in model object. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Deprecated facedetect\* model types. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Unified FaceEmbedModel and DetectEmbedModel |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Converted face.Identity responses to concepts like other detection models to be consistent |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed demo font syntax |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Video Timeline does not display on the demo app |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed Range Slider Value/Text in Apparel Detection Demo |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed demographics model to return embeddings and work with auto-annotate |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Adding collaborator model counter-intuitively requires ENTER in order to enable the submit button. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Validated that concept relation doesn't already exist on POST relations |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Prediction requests are being fired too frequently instead of using cache. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | postModelOutputs is not called for newly labeled assets without a manual refresh |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Return annotations posted by user in search results |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Search by region not working for face detection. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Make “save” search button internal only |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Saved Searches in Portal use the incorrect user ID |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix crop search from single image view for faces/detections |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | UI for collector crud |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Deprecate Face from Portal |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Improve tabs UI |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Video Predictions are failing in Portal |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed broken font syntax |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Video detection workflow prediction support |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Public general v1.5 workflow |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Allow Patching to existing public workflow |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Can not train LOPQ if app base workflow is face. Fixed |
