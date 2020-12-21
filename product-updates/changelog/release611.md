# Release 6.11

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%282%29.jpg) |

## Scribe

|Status     |Details                                                       |
|-----------|--------------------------------------------------------------|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Update annotations count for tasks with consensus review      |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |App Collaborators are unable to view model versions. Fixed    |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Refactor CustomEval worker                                    |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Trigger consensus review when non-anchor annotation is updated|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Collaborator annotation success by default                    |


## Account

|Status     |Details                                                       |
|-----------|--------------------------------------------------------------|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Signup form should show some visual feedback when submitting  |


## Spacetime Search

|Status     |Details                                                       |
|-----------|--------------------------------------------------------------|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |New Saved Searches not working. Fixed                         |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Unable to save search. Fixed                                  |

## Portal

|Status     |Details                                                       |
|-----------|--------------------------------------------------------------|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Frontend merge requests failing. Fixed                        |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Create a 'People Tracker' in Portal with specific parameters from centroid tracker|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Proposers - add filtering by status                           |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Proposers - switch workflows                                  |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Show concepts from workflows in proposals                     |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Natural language form for Proposals relation type chooser     |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Allow users to drag & reorder selected models during workflow creation|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Add filters to Proposers UI                                   |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Add rendering of Proposers UI bounding boxes                  |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Make predictions, versions and concept show for clarifai/main models|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|No loader in proposals causing user confusion                 |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Proposers - no name shown for collaborators. Fixed            |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Proposers - classification parent-child hit-or-miss if modelOutputs don't load. Fixed|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Button displays in Model Mode for text workflows are off. Fixed|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Allow users to bulk-unlabel previously labelled inputs        |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Adopt sortable table everywhere in portal                     |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Model Mode > OUTPUT_INFO.DATA.CONCEPTS > trashcan icon too far away from the concept name|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Display concepts in upload trained model page                 |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Omits being added as Rank instead of Filters. Fixed           |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |All model versions are not being displayed. Fixed             |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Support Secure Data Hosting for Text Assets                   |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Saved Searches not working in Explorer. Fixed                 |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Omit Negative/Positive and Filter Positive/Negative requests malformed. Fixed|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Workflow Range Slider not working for all workflows. Fixed    |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Bulk labeling should read labels from selected annotations/inputs. Fixed|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Disable fetching annotation in bulk-labeling                  |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Undefined is not an object (evaluating 'Ua[o].videos'). Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Failed prop type: Invalid prop `sm` supplied to `Col`. Fixed  |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Remove Create Workflow modal from Labeler                     |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |console.log data printed in Taskform. FIxed                   |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Uploading iPhone photos in Portal results in the inputs rotating incorrectly (inconsistent). Fixed|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Explorer console error in predictions reducer fixed           |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Broken thumbnail when uploading a video via data mode page. Fixed|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Switch collectors to use new labeler whitelist flag           |


## Armada

|Status     |Details                                                       |
|-----------|--------------------------------------------------------------|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Re-process assets faster                                      |


## API

|Status     |Details                                                       |
|-----------|--------------------------------------------------------------|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Update error status codes in daily_error_code_count           |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Add req_id to logged error                                    |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Finish gRPC Rust client                                       |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Move the python API client tests to gRPC Python client.       |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Update & release the clients with the secure gRPC channel     |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Improved workflow logging                                     |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Add PostModelOutputs retries to the gRPC Python test suite for dev & staging|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Validate new app id when duplicate app                        |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Workflow improvements                                         |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Fix undefined variable                                        |

## Enlight Train

|Staus      |Details                                                       |
|-----------|--------------------------------------------------------------|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Model training only uses available inputs, not waiting for all inputs to be processed. Fixed|
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29.jpg)|Add support for landmark extraction model type                |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Pre-trained model creation field improvements                 |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Fix new deep training: missing platform in benchmark config + torch import affecting TF benchmarking|
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%281%29.jpg)|Allow public model versions if they are used in public workflow|
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%284%29.jpg)        |Deep training Bug with small amount of inputs fixed           |
