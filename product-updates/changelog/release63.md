---
description: Changelog for Clarifai Release 6.3
---

# Release 6.3

## Changelog 6.3

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise%20%2810%29.jpg) |

### Applications

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Send collaborator emails asynchronously |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | NLP bug fixes for non-text apps |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Consolidated input related status codes |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Add frame.id to API as well as region.track\_id |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Granted select permission to clarifairead |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Added list annotations filter status |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Added concept selection for tasks |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Post/Patch annotations request now allow setting status |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Changed task form options |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Set annotation status to awaiting for review if the authorized user is not app owner |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Return only input\_level annotation in input.data |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Drawing annotations: wrong embed model version id. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Eliminated error if no annotation to be deleted |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Create one annotation for each bbox |

### Model

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Added support for adding and training on text in the platform |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Created a NLP mock prediction endpoint |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Created test set to evaluate quick trained models or k-fold if no test search is specified |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Added vocab\_id for demographics model concepts |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Fixed sorting of A.G.E. concepts in golang for demographics model so we don't chop off sets of them |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Deprecated Face from javascript Client |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Deprecated Face from Java Client |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Confusion matrix predicted/true are swapped in evaluation results. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Explorer Image/Text Joint embedding |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Fixed selectEmbedModelVersionId in detection apps |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Fixed generalModel imports and optimized video click handlers with useCallback hooks |

### Search

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Persisted the saved search used in train a model version |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Created log for annotation/search request/response |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed |

### Portal

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Created new Single Image View and Image Tools |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Enabled Display Text Thumbnails in App Grid View and App Details View |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Text Thumbnails display in Portal/Search Bar disabled |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Enabled View Text Assets in Portal's Image View |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Added Text Inputs To Explorer Apps |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Imported new icons for Labeler Image Tools into the style guide |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Added login tracking to analytics package in Portal |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Allowed pasting into the add inputs text area and clear the text box after clicking submit |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Search bar not visible. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Removed all instances of worker\_id from Explorer |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Fixed popover left/right overflow |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Disabled all search by click handlers in Portal for Text Apps |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Click Search button icons on Thumbs not working for localized search. Fixed |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Fixed details page header missing description |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug%20%28248%29.jpg) | Fixed demo font syntax |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature%20%2852%29.jpg) | Added a Range Slider to filter Workflow Predictions by Value |
| ![](https://github.com/Clarifai/docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement%20%2883%29.jpg) | Updated Face workflow to include the detect faces as concepts for search |
