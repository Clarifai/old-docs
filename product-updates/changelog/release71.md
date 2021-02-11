---
description: Changelog for Clarifai Release 7.1
---

# Release 7.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28254%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28820%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28577%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%2825%29.jpg) |

## API

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28315%29.jpg) | Add apps and keys scopes so they can be created with personal access tokens. |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%287%29.jpg) | Change /keys to work with PATs |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2843%29.jpg) | Change /apps to work with personal access tokens |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2876%29.jpg) | Split java proto files into multiple and add package name. |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28467%29.jpg) | Write script to prune the proto files into public only rpcs and messages |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28383%29.jpg) | Mark the appropriate fields in protos as cl\_private\_rpc to release grpc clients. |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28468%29.jpg) | copy app count and last\_inputs added in app duplication |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28296%29.jpg) | Rewrite input counting in the API to be more scalable and robust. |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28389%29.jpg) | Fix collector scopes so that predict keys don't need Collectors:Get |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28557%29.jpg) | Check the GetInputsKey of collectors has access to userA's information. |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28609%29.jpg) | Return “All” scopes when listing available scopes so that you have that option when creating new keys. |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28686%29.jpg) | properly return err if `AddAssets` failed to insert into DB |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28224%29.jpg) | POST inputs wasn’t using batch model optimizations correctly. |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28667%29.jpg) | created\_at field in sharing table is incorrect |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281140%29.jpg) | Missing Apps\_Get scope in session token auth caused creation of keys to fail temporarily. |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28555%29.jpg) | API services do not function once Queue goes down and comes back up has been fixed. This makes on premise deployments more resilient to power failures. |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28403%29.jpg) | List of missing scopes is not correct in error messages |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28679%29.jpg) | Fix node ID validation logic in Bug in workflows |

## Armada

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28341%29.jpg) | Create endpoint for taking down a spire |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28283%29.jpg) | Create endpoint to deploy deep training models |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28124%29.jpg) | Calculate detection pr and roc curves using score buckets |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28222%29.jpg) | Support for pytorch inference in spire |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28766%29.jpg) | able to overwrite default max conn for Citus |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28395%29.jpg) | Upgrade to go version for performance boost. |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28232%29.jpg) | Make runtime config to remote the extra round trip to storage in predict pathway. |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2881%29.jpg) | Improve JSON serialization performance in our servers by using an optimized third party library. |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2810%29.jpg) | Fix the WorkflowInput field name in proto to workflow\_input |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28994%29.jpg) | When reaching the final page, network request responds with 500 internal service error. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28112%29.jpg) | Spire fails to launch in local-k8s-USER with error "persistentvolumeclaim not found". Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281180%29.jpg) | Video processing fails with 'caseids' error. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28436%29.jpg) | Fix a connection issue from Golang backend service to media processing service |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28881%29.jpg) | Allocated resources for faster model performance |

## Enlight

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28311%29.jpg) | Return deep training evals through the API |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28144%29.jpg) | OCR Model |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28606%29.jpg) | Update templates to have more straightforward names and more friendly defaults |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28650%29.jpg) | Add 'Face' Default workflow to \`[https://api-dev.clarifai.com](https://api-dev.clarifai.com)' |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28945%29.jpg) | Make custom/transfer training evaluations for large models stable. |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28104%29.jpg) | training progress is saved too frequently, causing very slow training |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281007%29.jpg) | Return friendlier errors for incorrect parameters passed to templates |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281125%29.jpg) | Fix a bug in tracing setup for custom trainer and evaluator |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28978%29.jpg) | Accellerated training for specific cases |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28892%29.jpg) | Training System failed to train some layers |

## Mesh

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28286%29.jpg) | Implement image crop model |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%285%29.jpg) | Implement RandomSample model type |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28475%29.jpg) | Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models. |

## Portal

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28269%29.jpg) | make UI for personal access token |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28776%29.jpg) | Send event to Hubspot when a user signs up on portal |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28579%29.jpg) | Change HTML tag of ImagePile component from '' to '' |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28815%29.jpg) | Optimize Video Detection Frame Rate on Front end |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28553%29.jpg) | Remove classification/detection toggle in image details view |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28630%29.jpg) | Add colors to differentiate region results |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28890%29.jpg) | Scroll active thumb into view in image details carousel |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28427%29.jpg) | Unable to upload same file\(s\) through browse files. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281074%29.jpg) | Added a favicon for Portal |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281205%29.jpg) | Can’t create a new API key or edit the information of API key. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28596%29.jpg) | Delete input while having other inputs selected deselects everything. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28746%29.jpg) | Cannot view workflow results in a face app. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2880%29.jpg) | Setting useCustomConfig isn't checked at login. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28442%29.jpg) | ffmpeg can produce no frames for very short videos. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28330%29.jpg) | Video spire tests are not running correctly. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28513%29.jpg) | Verify your email |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28451%29.jpg) | Last concept used for bounding boxes is retained between apps. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281189%29.jpg) | Intercom links to old community site \(and maybe old FAQ page\). Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28220%29.jpg) | Add Inputs/View Explorer does not display in new app anymore |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28390%29.jpg) | Clicking video thumbs in detail view does not reload a video |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28675%29.jpg) | The Add Positives / Add Negatives buttons on a Concept details view breaks portal |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28497%29.jpg) | Collaboration apps have race condition where wrong user id is used |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28138%29.jpg) | Don't load collaborations for search demo/logged-out users |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281058%29.jpg) | Keyboard navigation in image details view highlights incorrect thumb |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28631%29.jpg) | Render Video Assets in Search Bar |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28130%29.jpg) | AppDetailsPanel add inputs/view in explorer no longer displays in devel |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28897%29.jpg) | Editing geo/json search items no longer work after adding the search bar tooltip |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28480%29.jpg) | TypeError: Cannot read 'get' of undefined when clicking image thumbnails in explorer search bar |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281128%29.jpg) | Explorer Visibility in small resolution screen |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28273%29.jpg) | No Prompt when uploading an image to explorer through url |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28930%29.jpg) | CFR rectangles on grid view do not correlate |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28581%29.jpg) | Prevent users from evaluating models that are not trainable. |

## Scribe

| Status | Details |
| :--- | :--- |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28586%29.jpg) | Mark the /annotation endpoints with cl\_private\_rpc |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281123%29.jpg) | No longer able to copy an app that has been shared with you via Collaborators. Fixed |
| ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281065%29.jpg) | Collaborators can not see workers |

## Spacetime

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2855%29.jpg) | Implement visual search in another app as a model type you can add to a workflow. |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2866%29.jpg) | Add click to search metadata attributes in image details sidebar |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2827%29.jpg) | Ability to keep concepts sorted by alpha. |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28281%29.jpg) | Refactor search |
| ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%28198%29.jpg) | Add metadata to collector added inputs so that you can filter by collector ID |

