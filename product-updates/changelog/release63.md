# Changelog

## Changelog 6.3

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Send collaborator emails asynchronously |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | NLP bug fixes for non-text apps |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Consolidated input related status codes |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add frame.id to API as well as region.track\_id |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Granted select permission to clarifairead |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Added list annotations filter status |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Added concept selection for tasks |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Post/Patch annotations request now allow setting status |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Changed task form options |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Set annotation status to awaiting for review if the authorized user is not app owner |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Return only input\_level annotation in input.data |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Drawing annotations: wrong embed model version id. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Eliminated error if no annotation to be deleted |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Create one annotation for each bbox |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Added support for adding and training on text in the platform |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Created a NLP mock prediction endpoint |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Created test set to evaluate quick trained models or k-fold if no test search is specified |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Added vocab\_id for demographics model concepts |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Fixed sorting of A.G.E. concepts in golang for demographics model so we don't chop off sets of them |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Deprecated Face from javascript Client |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Deprecated Face from Java Client |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Confusion matrix predicted/true are swapped in evaluation results. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Explorer Image/Text Joint embedding |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed selectEmbedModelVersionId in detection apps |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed generalModel imports and optimized video click handlers with useCallback hooks |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Persisted the saved search used in train a model version |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Created log for annotation/search request/response |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Created new Single Image View and Image Tools |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Enabled Display Text Thumbnails in App Grid View and App Details View |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Text Thumbnails display in Portal/Search Bar disabled |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Enabled View Text Assets in Portal's Image View |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Added Text Inputs To Explorer Apps |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Imported new icons for Labeler Image Tools into the style guide |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Added login tracking to analytics package in Portal |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Allowed pasting into the add inputs text area and clear the text box after clicking submit |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Search bar not visible. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Removed all instances of worker\_id from Explorer |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed popover left/right overflow |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Disabled all search by click handlers in Portal for Text Apps |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Click Search button icons on Thumbs not working for localized search. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed details page header missing description |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fixed demo font syntax |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Added a Range Slider to filter Workflow Predictions by Value |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Updated Face workflow to include the detect faces as concepts for search |
