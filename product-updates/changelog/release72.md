---
description: Changelog for Clarifai Release 7.2
---

# Release 7.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | ![improvement](../../.gitbook/assets/improvement.jpg) | ![bug](../../.gitbook/assets/bug.jpg) | ![enterprise](../../.gitbook/assets/enterprise.jpg) |

## API

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature.jpg) |Add Rust/Go/Swift/C++ gRPC clients to be built + released|

## Portal

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature.jpg) |Set up NextJS for marketplace                            |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) |Delete and Deduplication UX for Explorer Sidebar         |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) |Grouping/Ranking/Prediction sliders in Explorer sidebar  |
| ![improvement](../../.gitbook/assets/improvement.jpg) |Hide predictions tab for models having unsupported output_type|
| ![improvement](../../.gitbook/assets/improvement.jpg) |Add tests for model predictions                          |
| ![improvement](../../.gitbook/assets/improvement.jpg) |Make error toast persistant (or at least stay longer)    |
| ![improvement](../../.gitbook/assets/improvement.jpg) |Add integration tests for model-gallery - sortable-tables|
| ![improvement](../../.gitbook/assets/improvement.jpg) |Design change for model-mode filters into dropdown-filter|
| ![improvement](../../.gitbook/assets/improvement.jpg) |Adopt auto-complete dropdown filters everywhere in Portal|
| ![bug](../../.gitbook/assets/bug.jpg) |Classification apps should always PATCH the input level annotation, not POST|
| ![bug](../../.gitbook/assets/bug.jpg) |Cannot read property 'filterNot' of undefined            |


## Scribe

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature.jpg) |[Portal-Screen] Labeler-Tasks-Overview: Removed Pending-Inputs count from Task-List|
| ![improvement](../../.gitbook/assets/improvement.jpg) |[Portal-Screen] Labeler-View: Added click-to-insert a new point on polygon edge|
| ![improvement](../../.gitbook/assets/improvement.jpg) |[Portal-Screen] Labeler-View: Added Un-submitted Labels Warning|
| ![bug](../../.gitbook/assets/bug.jpg) |AI Assist threshold panel is too large                   |
| ![bug](../../.gitbook/assets/bug.jpg) |Change Worker mode submit button text from "Submit input for review" to just "Submit input"|
| ![bug](../../.gitbook/assets/bug.jpg) |Keybindings don't work unless the sidebar is "focused"   |
| ![bug](../../.gitbook/assets/bug.jpg) |When submitting the last input in the carousel, I am taken back to admin view rather than fetching the next batch of inputs|
| ![bug](../../.gitbook/assets/bug.jpg) |Zoom goes to 510% then to NaN                            |

## Enlight

|Status     |Details                                                  |
|-----------|---------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature.jpg) |[Platform-Object] Training-Runner: Added Clarifai_EfficientDet template for Visual-Detector|
