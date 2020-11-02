# Changelog

## Changelog 6.4

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Improved responsiveness of collaborations tab in /apps |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Enabled list collaborators to list deleted collaborators |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Login Form breaks app. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Deleting an app no longer redirects to /apps |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Can’t create models in new app. Fixed |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed .webp files not working when sent as base64 |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | MVP of labeler single image view functionality |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Support detection tasks |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Detection Labeler: Color Coded Concepts |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add workflow\_id to task creation and show AI predictions to verify in labeler mode |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Split tasks admin view into tabs |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add visual sections to task form |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add default queries for "all inputs" and "all unlabelled inputs" in task create view |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Autocomplete annotation user |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Implement Classification Task Review Logic |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Implement Review Process into tasks |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Introduce stats collection APIs for worker stats |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Implement APIs for polygon region support |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Incorporate image filters for labelling |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Update image tool icons |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Ability to zoom in on images |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove ‘alt’ from hotkeys, just use letters and arrows |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Label to draw box in video frame using frame bytes |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Display videos in labeler |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add video fps field for tasks |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Draw Bounding Boxes in Labeler Detection Videos |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add video controls for video in labeler |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix Classification Annotation |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Video annotation deletion. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | AI Assist Predictions did not show for General workflow classification task. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix Classification video annotation |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Display video in classification tasks |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix Labeler input urls |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix Annotation creation for video |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix Labeler post calls |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Detection Labeler: fix zoom |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed image cropper task description |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix concept threshold creation |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Set annotation status ‘success’ |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Restrict tasks to only the assigned users |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Add validation to TaskForm’s concept field |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Display human tags for human box as child |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Convert Deep Trained Model to Embedding Model for Use as "Base Workflow" |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Classification predictions for AI assistance |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Merge this detection and custom model prediction sections for detection models |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Video labelling UI for classification. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove the non-creatable types from model mode |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Improve the create classifier / detector view options in model mode |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add deep training options in model mode |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Update random sampling model to have a slider |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed public concept rank |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Support detection evaluations in PostAnnotationSearchMetrics |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Support nlp search \(only filtering\) |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Add evaluations between two saved search label sets |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Fix labeler search amount |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Error:  "Cannot search over `annotations`" when clicking a general app. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Model name and details is not populated upon model creation in model mode |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix annotation search when accessing the LabelerPage |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Search by annotation\_info should not return the embed annotation. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Search for metadata in detection apps doesn't work. Fixed |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Create Dual Range Slider |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Enable patching the default workflow from Portal and error if needs reindex |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Allow drawing bounding boxes on paused video frames |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add scopes for collaborators and metrics to Portal |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Allow up to 15-20x zoom level for really large images. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Allow selection the embed\_model\_version\_id from Portal when creating a model |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix inconsistent fps between uploading video and predicting video |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Missing frame time. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Model annotations not appearing in Explorer. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | When creating the auto annotation workflow editing the workflow crashes Portal |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix image tools state |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | CreateWorkflow model improvements |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Allow custom concept models in the default app workflows |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add a "Make a Copy" or "Copy to New Workflow" button for each workflow |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Allow patching the default workflow in Portal |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Show the default workflow in the list of workflows for the app |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Validate patching of default workflow is compatible in backend |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Large workflow name causes overlap in app details view. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Portal crashes if page reloads during workflow add/edit. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Detection workflow recompute also predict detect-concept |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Allow detect-concept models to be added to workflows |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Patch workflow create worker |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix validation of inputs in workflows |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix workflow embed\_join\_annotation\_id issue |

### Clients

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Clean up private API client repos |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Remove public workflows from Python client |
