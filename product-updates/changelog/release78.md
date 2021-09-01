---
description: Changelog for Clarifai Release 7.8
---

# Release 7.8

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%2827%29.jpg) |


## Model

|Status     |Details                                                                       |
|-----------|------------------------------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Model: Published "person-detection-edge" Visual-Detector        |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Model: Published "person-vehicle-detection-edge" Visual Detector|

## Platform-Object

|Status     |Details                                                                         |
|-----------|--------------------------------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Annotation: Added support for Time-Segments                   |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Application: Reindexing with no inputs returns invalid request|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Model-Type: Added Track-Aggregator                            |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Model: Added Model.Notes field                                |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Task: Continuously check Consensus threshold logic            |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Task: Fix incorrect status mapping in Annotation stats        |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Task: Ignore Consensus logic on "Empty" annotations           |

## Portal

|Status     |Details                                                                                                   |
|-----------|----------------------------------------------------------------------------------------------------------|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Input-Details: Audio doesn't stop when exiting after playing video                        |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Task-Labeler: Added histogram showing count of objects throughout Video-Inputs            |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Task-Labeler: Added Time-Segment tool                                                     |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Task-Labeler: Added tracklet visualization for Object-Track labels                        |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Task-Labeler: AI-Assist suggestions not displaying for Public Visual-Classifiers          |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Task-Labeler: Fix carousel being pushed off-screen by timeline                            |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Task-Labeler: Loading animation continues indefinitely after GetTaskInputs returns no hits|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Task-Manager: Reduce minimum Consensus Threshold to 2                                     |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Task-Reviewer: Video-Input thumbnails fail to load                                        |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Workflow-Builder: Added new navigation options and tooltips                               |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Workflow-Builder: Fixed handling of non-create-able model-types                           |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Workflow-Builder: Fixed the logic for showing model/version selector in Node details      |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Improved handling of failed inputs that are not marked as failed                      |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28279%29.jpg) |Onboarding Dialog improvements                                                                            |
