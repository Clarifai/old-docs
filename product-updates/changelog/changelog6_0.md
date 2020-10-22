# Changelog

## Changelog 6.0

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove country field from signup form, simplifying new customer signups |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Essential Plan User can't add collaborators. Fixed |

### API

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Introduce new [Python gRPC API client](https://docs.clarifai.com/api-guide/api-overview), enabling new features and performance enhancements across API |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Introduce new [Java gRPC API client](https://docs.clarifai.com/api-guide/api-overview), enabling new features and performance enhancements across API |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Update API key type for "app\_specific" for app-specific keys to be more clear to users |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Allow Personal Access Tokens when calling /users/me \(GetUsers\) |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | \[Frontend\] Enable "Copy Application" from collaborated apps, making it easy to duplicate and build upon existing applications |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Program to clean internal apps crashing. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Added the ability to accept b64 Gifs |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Functionality to upload pre-tagged images missing. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Images pre-tagged with concepts do not successfully upload into Clarifai UI On doing bulk uploads \(&gt;20-30 urls\). Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Bulk image upload issue. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | "Download Failed" error when uploading images. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Issue with post inputs key being a PAT in a collector. Fixed |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Skip aligning landmarks if landmark points are out of range to avoid errors and unexpected behavior |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Bounding Boxes and Cropped Regions aren't displaying on Videos with default runtime config. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Insert annotations and related data in batch to improve performance |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Evaluate new face embedding model workflow end to end for optimal performance |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Validate that concept.app\_id shouldn't be set when creating/patching models |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add new predicate to knowledge graph for "relates\_to" to represent synonyms |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Model training lag. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Model has missing inputs. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Submitted models becoming stuck in queue. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Custom training models when uploaded images are not fully pre-processed. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Custom facial recognition bboxes do not correspond with detection boxes/ Custom facial recognition prediction interval for video is still 1000ms for apps supporting 100ms runtime config. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | frame\_info time off by a factor of 10 for general detection model. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Detection Models throw error at end of video due to invalid index lookup. Fixed |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Deleting a workflow should clear or update localStorage. Fixed |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Clean up app overflow UI, improving user experience |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Improve Error boundary screen, improving user experience |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add sentry error Id to Error Screen |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Images not loading. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Label and prediction on the right side under Custom Model Predictions section no longer shows up automatically. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Provide a way for user.metadata to be updated from portal when there are failing apps stuck in there. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Predictions for a detection model don't show properly in portal. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Custom facial recognition Predict Boxes not displaying. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Adding inputs in explorer redirects to explorer view with flashing images. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Run prediction by ID in small batch, improving performance |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Custom model predictions not displaying. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Custom model detections not displaying. Fixed |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Add file upload input button to explorer search bar, simplifying the UX for file uploads |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Filter custom facial recognition bboxes using a sliding bar, adding easy thresholding to custom facial recognition models |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Search Bar allows file upload |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove Explorer App Overflow Menu for improved UX |
