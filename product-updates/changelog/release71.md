---
description: Changelog for Clarifai Release 7.1
---

# Release 7.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | ![improvement](../../.gitbook/assets/improvement.jpg) | ![bug](../../.gitbook/assets/bug.jpg) | ![enterprise](../../.gitbook/assets/enterprise.jpg) |

## API

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Add apps and keys scopes so they can be created with personal access tokens. |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Change /keys to work with PATs |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Change /apps to work with personal access tokens |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Split java proto files into multiple and add package name. |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Write script to prune the proto files into public only rpcs and messages |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Mark the appropriate fields in protos as cl\_private\_rpc to release grpc clients. |
| ![improvement](../../.gitbook/assets/improvement.jpg) | copy app count and last\_inputs added in app duplication |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Rewrite input counting in the API to be more scalable and robust. |
| ![bug](../../.gitbook/assets/bug.jpg) | Fix collector scopes so that predict keys don't need Collectors:Get |
| ![bug](../../.gitbook/assets/bug.jpg) | Check the GetInputsKey of collectors has access to userA's information. |
| ![bug](../../.gitbook/assets/bug.jpg) | Return “All” scopes when listing available scopes so that you have that option when creating new keys. |
| ![bug](../../.gitbook/assets/bug.jpg) | properly return err if `AddAssets` failed to insert into DB |
| ![bug](../../.gitbook/assets/bug.jpg) | POST inputs wasn’t using batch model optimizations correctly. |
| ![bug](../../.gitbook/assets/bug.jpg) | created\_at field in sharing table is incorrect |
| ![bug](../../.gitbook/assets/bug.jpg) | Missing Apps\_Get scope in session token auth caused creation of keys to fail temporarily. |
| ![bug](../../.gitbook/assets/bug.jpg) | API services do not function once Queue goes down and comes back up has been fixed. This makes on premise deployments more resilient to power failures. |
| ![bug](../../.gitbook/assets/bug.jpg) | List of missing scopes is not correct in error messages |
| ![bug](../../.gitbook/assets/bug.jpg) | Fix node ID validation logic in Bug in workflows |

## Armada

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Create endpoint for taking down a spire |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Create endpoint to deploy deep training models |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Calculate detection pr and roc curves using score buckets |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Support for pytorch inference in spire |
| ![improvement](../../.gitbook/assets/improvement.jpg) | able to overwrite default max conn for Citus |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Upgrade to go version for performance boost. |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Make runtime config to remote the extra round trip to storage in predict pathway. |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Improve JSON serialization performance in our servers by using an optimized third party library. |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Fix the WorkflowInput field name in proto to workflow\_input |
| ![bug](../../.gitbook/assets/bug.jpg) | When reaching the final page, network request responds with 500 internal service error. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Spire fails to launch in local-k8s-USER with error "persistentvolumeclaim not found". Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Video processing fails with 'caseids' error. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Fix a connection issue from Golang backend service to media processing service |
| ![bug](../../.gitbook/assets/bug.jpg) | Allocated resources for faster model performance |

## Enlight

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Return deep training evals through the API |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | OCR Model |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Update templates to have more straightforward names and more friendly defaults |
| ![bug](../../.gitbook/assets/bug.jpg) | Add 'Face' Default workflow to \`[https://api-dev.clarifai.com](https://api-dev.clarifai.com)' |
| ![bug](../../.gitbook/assets/bug.jpg) | Make custom/transfer training evaluations for large models stable. |
| ![bug](../../.gitbook/assets/bug.jpg) | training progress is saved too frequently, causing very slow training |
| ![bug](../../.gitbook/assets/bug.jpg) | Return friendlier errors for incorrect parameters passed to templates |
| ![bug](../../.gitbook/assets/bug.jpg) | Fix a bug in tracing setup for custom trainer and evaluator |
| ![bug](../../.gitbook/assets/bug.jpg) | Accellerated training for specific cases |
| ![bug](../../.gitbook/assets/bug.jpg) | Training System failed to train some layers |

## Mesh

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Implement image crop model |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Implement RandomSample model type |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models. |

## Portal

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | make UI for personal access token |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Send event to Hubspot when a user signs up on portal |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Change HTML tag of ImagePile component from '' to '' |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Optimize Video Detection Frame Rate on Front end |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Remove classification/detection toggle in image details view |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Add colors to differentiate region results |
| ![bug](../../.gitbook/assets/bug.jpg) | Scroll active thumb into view in image details carousel |
| ![bug](../../.gitbook/assets/bug.jpg) | Unable to upload same file\(s\) through browse files. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Added a favicon for Portal |
| ![bug](../../.gitbook/assets/bug.jpg) | Can’t create a new API key or edit the information of API key. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Delete input while having other inputs selected deselects everything. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Cannot view workflow results in a face app. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Setting useCustomConfig isn't checked at login. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | ffmpeg can produce no frames for very short videos. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Video spire tests are not running correctly. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Verify your email |
| ![bug](../../.gitbook/assets/bug.jpg) | Last concept used for bounding boxes is retained between apps. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Intercom links to old community site \(and maybe old FAQ page\). Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Add Inputs/View Explorer does not display in new app anymore |
| ![bug](../../.gitbook/assets/bug.jpg) | Clicking video thumbs in detail view does not reload a video |
| ![bug](../../.gitbook/assets/bug.jpg) | The Add Positives / Add Negatives buttons on a Concept details view breaks portal |
| ![bug](../../.gitbook/assets/bug.jpg) | Collaboration apps have race condition where wrong user id is used |
| ![bug](../../.gitbook/assets/bug.jpg) | Don't load collaborations for search demo/logged-out users |
| ![bug](../../.gitbook/assets/bug.jpg) | Keyboard navigation in image details view highlights incorrect thumb |
| ![bug](../../.gitbook/assets/bug.jpg) | Render Video Assets in Search Bar |
| ![bug](../../.gitbook/assets/bug.jpg) | AppDetailsPanel add inputs/view in explorer no longer displays in devel |
| ![bug](../../.gitbook/assets/bug.jpg) | Editing geo/json search items no longer work after adding the search bar tooltip |
| ![bug](../../.gitbook/assets/bug.jpg) | TypeError: Cannot read 'get' of undefined when clicking image thumbnails in explorer search bar |
| ![bug](../../.gitbook/assets/bug.jpg) | Explorer Visibility in small resolution screen |
| ![bug](../../.gitbook/assets/bug.jpg) | No Prompt when uploading an image to explorer through url |
| ![bug](../../.gitbook/assets/bug.jpg) | CFR rectangles on grid view do not correlate |
| ![bug](../../.gitbook/assets/bug.jpg) | Prevent users from evaluating models that are not trainable. |

## Scribe

| Status | Details |
| :--- | :--- |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Mark the /annotation endpoints with cl\_private\_rpc |
| ![bug](../../.gitbook/assets/bug.jpg) | No longer able to copy an app that has been shared with you via Collaborators. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Collaborators can not see workers |

## Spacetime

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Implement visual search in another app as a model type you can add to a workflow. |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Add click to search metadata attributes in image details sidebar |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Ability to keep concepts sorted by alpha. |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Refactor search |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Add metadata to collector added inputs so that you can filter by collector ID |

