---
description: Changelog for Clarifai Release 6.1
---

# Release 6.1

## Changelog 6.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) |

### Clients

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Python client |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Java client |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Javascript client |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Portal/demo |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove image.crop field from Python API client |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove image.crop field from Java API client |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove image.crop field from Javascript API client |

### Model

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Added detection evaluation in platform |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Introduce concept mapping model that uses the knowledge graph relations, creating a path for users to eventually benefit from pool of networked data |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix a bug that caused the new face predictions to have a huge performance drop |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Train and eval worker didn't invalidate model related cache. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix bug in deleting a concept relation by ID |

### Portal

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Bulk labelling can now be done from Explorer mode grid view. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Show Check/X on custom detection model predictions in Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Allow multi concepts per bbox |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Negative tags not visible in Portal. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove extra round trip to storage in predict pathway |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove the image.crop argument during predict and POST /inputs calls to simplify the API |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add region predictions from custom models to detections in videos |

### Search

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Implement search by annotation.status in backend |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Connect saved searches and annotation status |
