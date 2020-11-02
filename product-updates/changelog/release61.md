# Changelog

## Changelog 6.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Clients

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove Feedback endpoints from Python client |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove Feedback endpoints from Java client |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove Feedback endpoints from Javascript client |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove Feedback endpoints from Portal/demo |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove image.crop field from Python API client |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove image.crop field from Java API client |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove image.crop field from Javascript API client |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Added detection evaluation in platform |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Introduce concept mapping model that uses the knowledge graph relations, creating a path for users to eventually benefit from pool of networked data |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix a bug that caused the new face predictions to have a huge performance drop |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Train and eval worker didn't invalidate model related cache. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Fix bug in deleting a concept relation by ID |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Bulk labelling can now be done from Explorer mode grid view. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Show Check/X on custom detection model predictions in Portal |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Allow multi concepts per bbox |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) | Negative tags not visible in Portal. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove extra round trip to storage in predict pathway |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Remove the image.crop argument during predict and POST /inputs calls to simplify the API |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Add region predictions from custom models to detections in videos |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | Implement search by annotation.status in backend |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) | Connect saved searches and annotation status |
