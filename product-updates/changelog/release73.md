---
description: Changelog for Clarifai Release 7.3
---

# Release 7.3

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | ![improvement](../../.gitbook/assets/improvement.jpg) | ![bug](../../.gitbook/assets/bug.jpg) | ![enterprise](../../.gitbook/assets/enterprise.jpg) |

## Scribe

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | User-Login: New styling and authentication methods              |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Task-Reviewer: Added Grid display option                        |
| ![bug](../../.gitbook/assets/bug.jpg)  Task-Manager: Fixed non-responsive behavior of Workers column   |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Task-Manager: Added progress bars for Input-Assignment statuses |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Task-Manager: Added Input-Count column to table                 |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Task-List: Removed unnecessary "Mark Task as Done" button       |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Task-List: Redesigned "For-Review" tab                          |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Task-List: Redesigned "Assigned to Me" tab                      |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Task-Labeler: Added timeline panel for displaying video tracks  |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Task-Labeler: Added support for Polygon-Interpolation           |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Task-Labeler: Added count of pending Inputs                     |

## Portal

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![bug](../../.gitbook/assets/bug.jpg)  Model-Evaluation: Fixed incorrect Precision/Recall metrics for Visual-Detectors |
| ![bug](../../.gitbook/assets/bug.jpg)  Explorer: Fixed redundant scrolling issue with Saved-Searches                   |
| ![bug](../../.gitbook/assets/bug.jpg)  Explorer: Fixed issue preventing storage of filter values to Saved-Searches     |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Explorer: Added FPS Setting to "App Workflow Prediction" panel                  |
| ![bug](../../.gitbook/assets/bug.jpg)  Text Upload in Explorer Has Weird Styling                                       |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Remove `embed_model_version_id` from POST & PATCH annotations                   |
| ![bug](../../.gitbook/assets/bug.jpg)  Model predictions cors issue                                                    |
| ![improvement](../../.gitbook/assets/improvement.jpg) | create-workflow - sortable-tables - linear-view                                 |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Fix annotations approximate count query                                         |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Collectors Edit Function of Existing Task                                       |

## Enlight


|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![improvement](../../.gitbook/assets/improvement.jpg) | Task: Added "None" option for Input-Source                                                |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Model-Type: Initial release of Text-Token-Classifier                                      |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Model-Type: Added support for up to 18 languages for OCR-Scene                            |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Model-Type: Added support for up to 162 languages for OCR-Document                        |
| ![bug](../../.gitbook/assets/bug.jpg)  App slow due to loading 250+ requests in Model Versions selector on Create Workflows page |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Propagate error status code descriptions in deep training                                 |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Workflow-Card: Published new version of "face" with Landmark Detect + Align Transform     |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Model-Card: Published "general" Text-Token-Classifier                                     |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Weapon Model V1                                                                           |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Logo V2 POC                                                                               |

## API

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| Bug | Make a gRPC Python script new line replacement work in POSIX sed |
