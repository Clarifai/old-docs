---
description: Changelog for Clarifai Release 6.5
---

# Release 6.5

## Changelog 6.5

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise%20%2810%29.jpg) |

### Applications

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Can't Access Main Apps Page with invalid collaborators. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Unable to create new Application \(General Detection\). Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | `application_sharing` scopes field should be `json` instead of `jsonb`. Fixed. |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Pasting long text makes Uploader unusable due to lack of scrolling. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Support uploading text containing emojis. |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Integrate and Implement task deletion using new endpoints. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Implement /tasks CRUD in API. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Allow annotation writer model to set the `task_id` in `annotation_info`. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Make polygons a separate task type. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Add empty CRUD endpoints for tasks. |

### Model

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | `vocab_id` doesn't appear in the returned object for demographics model. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | `segment-concept` model types are no longer returning the segmentation mask. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | NLP text input does not scroll when longer than viewport height. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Clear text inputs after upload. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Improve the "TextFile" React Component for NLP. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Make existing model details view configurable by model type. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Edit model should only contain the fields related to the selected model. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | NLP frontend text input is covered entirely blue when selected. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Enforce fields in post/patch models to adhere to model types. Fixed. |

### Predict

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Fixed fps issue for video predictions. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Validate `stat_value_agg_type`. |

### Search

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Dropdown Search Help Menu no longer displays in the search bar. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Video thumbs have relevant timestamp in search. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Added adjustable search results threshold. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Search over multi-embed workflows. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Added search on input level. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Improved search query by using multi join. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Fixed panic in list saved searches endpoint. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Input metadata search from table not working. Fixed. |

### Portal

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | "Return to Log in " doesn't redirect to login page. Fixed. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Clicking on image, or Explorer Mode with images that contain geo coordinates crashed the app. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Portal model predicts use hosted URL when available instead of normal URL. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | When selecting a concept and going to the next image the concept checkbox won't stay selected. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Allow multi-select from explorer grid view and add metadata. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Integrate and utilize new CRUD endpoints in Portal. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Allow for pasted text to keep formatting in the text box. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Prediction threshold slider custom model predicts without base workflow annotations. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Strings without spacing format properly in Explorer's Asset Grid View |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | `annotation_info` should be a valid JSON in Model Mode. Fixed. |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Hide the "add text" section of the add inputs modal for non text workflows. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Validate that all nodes in workflows list their inputs based on type. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Add NLP to Workflows List |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Generalize the iterations over regions/frames in workflow code. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Add ability to "make a copy" of public\_workflows. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Allow indexing embedding from detect -&gt; crop -&gt; embed style workflows. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Allow setting input nodes for all users, not just @clarifai.com users. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Allow non-internal users setting input node when creating workflows. |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Create/Patch workflow uncaught exception. |

### Clients

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Update docs.clarifai.com to reflect our current API clients including grpc clients. |
