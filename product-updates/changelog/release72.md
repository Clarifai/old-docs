---
description: Changelog for Clarifai Release 7.2
---

# Release 7.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%2827%29.jpg) |

## API

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Add Rust/Go/Swift/C++ gRPC clients to be built + released|

## Portal

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Set up NextJS for marketplace                            |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Delete and Deduplication UX for Explorer Sidebar         |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |Grouping/Ranking/Prediction sliders in Explorer sidebar  |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |Hide predictions tab for models having unsupported output_type|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |Add tests for model predictions                          |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |Make error toast persistant (or at least stay longer)    |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |Add integration tests for model-gallery - sortable-tables|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |Design change for model-mode filters into dropdown-filter|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |Adopt auto-complete dropdown filters everywhere in Portal|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Classification apps should always PATCH the input level annotation, not POST|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Cannot read property 'filterNot' of undefined            |


## Scribe

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |[Portal-Screen] Labeler-Tasks-Overview: Removed Pending-Inputs count from Task-List|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |[Portal-Screen] Labeler-View: Added click-to-insert a new point on polygon edge|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28881%29.jpg) |[Portal-Screen] Labeler-View: Added Un-submitted Labels Warning|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |AI Assist threshold panel is too large                   |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Change Worker mode submit button text from "Submit input for review" to just "Submit input"|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Keybindings don't work unless the sidebar is "focused"   |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |When submitting the last input in the carousel, I am taken back to admin view rather than fetching the next batch of inputs|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28606%29.jpg) |Zoom goes to 510% then to NaN                            |

## Enlight

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28282%29.jpg) |[Platform-Object] Training-Runner: Added Clarifai_EfficientDet template for Visual-Detector|
