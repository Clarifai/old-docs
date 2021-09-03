---
description: Changelog for Clarifai Release 7.3
---

# Release 7.3

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%2827%29.jpg) |

## Scribe

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | User-Login: New styling and authentication methods              |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Task-Reviewer: Added Grid display option                        |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg)  Task-Manager: Fixed non-responsive behavior of Workers column   |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Task-Manager: Added progress bars for Input-Assignment statuses |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Task-Manager: Added Input-Count column to table                 |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Task-List: Removed unnecessary "Mark Task as Done" button       |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Task-List: Redesigned "For-Review" tab                          |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Task-List: Redesigned "Assigned to Me" tab                      |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Task-Labeler: Added timeline panel for displaying video tracks  |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Task-Labeler: Added support for Polygon-Interpolation           |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Task-Labeler: Added count of pending Inputs                     |

## Portal

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg)  Model-Evaluation: Fixed incorrect Precision/Recall metrics for Visual-Detectors |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg)  Explorer: Fixed redundant scrolling issue with Saved-Searches                   |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg)  Explorer: Fixed issue preventing storage of filter values to Saved-Searches     |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Explorer: Added FPS Setting to "App Workflow Prediction" panel                  |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg)  Text Upload in Explorer Has Weird Styling                                       |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Remove `embed_model_version_id` from POST & PATCH annotations                   |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg)  Model predictions cors issue                                                    |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | create-workflow - sortable-tables - linear-view                                 |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Fix annotations approximate count query                                         |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Collectors Edit Function of Existing Task                                       |

## Enlight


|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Task: Added "None" option for Input-Source                                                |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Model-Type: Initial release of Text-Token-Classifier                                      |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Model-Type: Added support for up to 18 languages for OCR-Scene                            |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Model-Type: Added support for up to 162 languages for OCR-Document                        |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg)  App slow due to loading 250+ requests in Model Versions selector on Create Workflows page |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | Propagate error status code descriptions in deep training                                 |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Workflow-Card: Published new version of "face" with Landmark Detect + Align Transform     |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Model-Card: Published "general" Text-Token-Classifier                                     |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Weapon Model V1                                                                           |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | Logo V2 POC                                                                               |

## API

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| Bug | Make a gRPC Python script new line replacement work in POSIX sed |
