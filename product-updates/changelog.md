# Changelog

## Changelog 6.8

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |


### Labeler
|Status     |Details                                                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement.jpg)|Use single LabelerToolbar for all labelers, make shared using Context                                                                          |
| ![](../.gitbook/assets/improvement.jpg)|Remove all computation from components, move to selectors for perf                                                                             |
| ![](../.gitbook/assets/bug.jpg)       |Fixed carousel scroll behavior                                                                                                                 |
| ![](../.gitbook/assets/bug.jpg)       |Added button to add collaborator when adding reviewer                                                                                          |
| ![](../.gitbook/assets/bug.jpg)       |Post incorrect bounding box. Fixed                                                                                                             |
| ![](../.gitbook/assets/bug.jpg)       |Refreshing in Labeler Crashes Portal. Fixed                                                                                                    |
| ![](../.gitbook/assets/new_feature.jpg)|Add Grid Review UI to Review Page                                                                                                              |
| ![](../.gitbook/assets/bug.jpg)       |Panning while playing a video renders rects incorrectly. Fixed                                                                                 |
| ![](../.gitbook/assets/bug.jpg)       |Navigation from the task creation page if task creation fails. Fixed                                                                           |
| ![](../.gitbook/assets/improvement.jpg)|Konva: Image filters                                                                                                                           |
| ![](../.gitbook/assets/improvement.jpg)|Konva: Drawing rects                                                                                                                           |
| ![](../.gitbook/assets/improvement.jpg)|Konva: Drawing polygons                                                                                                                        |
| ![](../.gitbook/assets/improvement.jpg)|Smaller shapes should supersede zIndex values if they are engulfed by larger ones                                                              |
| ![](../.gitbook/assets/bug.jpg)       |Region selectors inefficient and running on each call, bypassing reselect memoization. Fixed                                                   |
| ![](../.gitbook/assets/bug.jpg)       |v2 interpolation: app crash on reload. Fixed                                                                                                   |
| ![](../.gitbook/assets/bug.jpg)       |CSS issue causing VideoControls to be inaccessible to mouse. Fixed                                                                             |
| ![](../.gitbook/assets/bug.jpg)       |v2 video: no thumbails in carousel. Fixed                                                                                                      |
| ![](../.gitbook/assets/bug.jpg)       |v2 keyboard hint showing weird characters. Fixed                                                                                               |
| ![](../.gitbook/assets/bug.jpg)       |Selected Shape becomes unselected on playing video (make selection persist across track). Fixed                                                |
| ![](../.gitbook/assets/bug.jpg)       |Ron is unable to create a task with AI assist in prod. Fixed                                                                                   |
| ![](../.gitbook/assets/bug.jpg)       |Write and Preview Tab style. Fixed                                                                                                             |
| ![](../.gitbook/assets/bug.jpg)       |Task create form shows name as "undefined undefined" when a user has not filled in profile details. Fixed                                      |
| ![](../.gitbook/assets/bug.jpg)       |Input source that was selected should be shown when task selected. Fixed                                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Create order fails if I'm a clarifai user. Fixed                                                                                               |
| ![](../.gitbook/assets/bug.jpg)       |Layout in order admin form has some issues. Fixed                                                                                              |
| ![](../.gitbook/assets/bug.jpg)       |Multiple errors when creating bounding boxes. Fixed                                                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Cannot see annotations from a collaborator in v2 linear review. Fixed                                                                          |
| ![](../.gitbook/assets/bug.jpg)       |Keyboard shortcuts dont work in labeler v2. Fixed                                                                                              |
| ![](../.gitbook/assets/bug.jpg)       |When a worker opens labeler, display the instructions by default. Fixed                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |Non-clarifai users should have v2 only, clarifai accounts should have v2 by default with option to switch to v1. Fixed                         |
| ![](../.gitbook/assets/bug.jpg)       |Cursor should change to a crosshair when drawing a bounding box. Fixed                                                                         |
| ![](../.gitbook/assets/bug.jpg)       |Cursor should change to an open hand when panning is selected and closed hand when grabbing/panning. Fixed                                     |
| ![](../.gitbook/assets/bug.jpg)       |Reviewer cannot see annotations by collaborators. Fixed                                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |If the reviewer is NOT the app owner, clicking review takes them to explorer. Fixed                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Tooltip for labeler nav icon should be uppercase. Fixed                                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |As a worker, if I return to Labeler, I should be able to continue from where I was previously. Fixed                                           |
| ![](../.gitbook/assets/bug.jpg)       |LaaS orders can't assign inputs which block the workers. Fixed                                                                                 |
| ![](../.gitbook/assets/bug.jpg)       |Community users should have LaaS option grayed out with an explanation. Fixed                                                                  |
| ![](../.gitbook/assets/bug.jpg)       |Make the "order admin view" text larger and prominent as a section header. Fixed                                                               |
| ![](../.gitbook/assets/bug.jpg)       |In labeler UI (worker), submit button should say "Submit Input for Review" to make it clear what the button does. Fixed                        |
| ![](../.gitbook/assets/bug.jpg)       |[P3] In all tasks view, only app owner should see edit/delete icons                                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Carousel blocks input visibility (not just video controls). Fixed                                                                              |
| ![](../.gitbook/assets/bug.jpg)       |In labeler UI carousel, show a check for any input that was submitted, and gray it out slightly. Fixed                                         |
| ![](../.gitbook/assets/improvement.jpg)|Separate annotation sagas + standardise request batching code (for v2 store)                                                                   |
| ![](../.gitbook/assets/bug.jpg)       |When creating a task in an app w/ no concepts, “Select all concepts” should not be checked by default. There are no concepts created yet. Fixed|
| ![](../.gitbook/assets/new_feature.jpg)|Update task status on task list                                                                                                                |
| ![](../.gitbook/assets/bug.jpg)       |Deleting an annotation in reviewer deletes all annotations. Fixed                                                                              |
| ![](../.gitbook/assets/bug.jpg)       |Too many scrollbars in sidebar. Fixed                                                                                                          |
| ![](../.gitbook/assets/bug.jpg)       |Partition worker strategy Error. Fixed                                                                                                         |
| ![](../.gitbook/assets/improvement.jpg)|Integrate feature gating with LaaS.                                                                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Panning state not in sync with drawing/moving. Fixed                                                                                           |
| ![](../.gitbook/assets/bug.jpg)       |Have to click the + button 2 times to make it work. Fixed                                                                                      |
| ![](../.gitbook/assets/bug.jpg)       |Dragging mouse outside of the canvas while drawing leaves the drawing in inconsistent state. Fixed                                             |
| ![](../.gitbook/assets/bug.jpg)       |Delete icon on v2 sidebar deletes all annotations on the input. Fixed                                                                          |
| ![](../.gitbook/assets/bug.jpg)       |Resizing shapes near the right edge of the frame causes weird resize behavior. Fixed                                                           |
| ![](../.gitbook/assets/bug.jpg)       |Entering date manually in Order control modal fixed                                                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Carousel Thumbnail animation not working; images looking weird in aspect-ratio due to incorrect CSS                                            |
| ![](../.gitbook/assets/bug.jpg)       |Task Form console errors. Fixed                                                                                                                |
| ![](../.gitbook/assets/bug.jpg)       |Add video icon to carousel for video inputs. Fixed                                                                                             |
| ![](../.gitbook/assets/bug.jpg)       |When we use keyboard shortcuts to activate a concept for bounding boxes, show visual feedback                                                  |
| ![](../.gitbook/assets/bug.jpg)       |Cannot read property '0' of undefined. Fixed                                                                                                   |
| ![](../.gitbook/assets/bug.jpg)       |Review tab shows new tasks that have no work ready to review. Fixed                                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Video Interpolation doesn't work. Fixed                                                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |Labeler UI sees last input even after submitting everything. Fixed                                                                             |
| ![](../.gitbook/assets/bug.jpg)       |Box disappears for a second while drawing on video. Fixed                                                                                      |
| ![](../.gitbook/assets/bug.jpg)       |Disable worker input when editing a task. Fixed                                                                                                |
| ![](../.gitbook/assets/bug.jpg)       |Input data stops being fetched if labeler is exited once and revisited. Fixed                                                                  |
| ![](../.gitbook/assets/bug.jpg)       |Make v2 annotations state flatter. Fixed                                                                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Darker colors poorly visible in sidebar region items. Fixed                                                                                    |
| ![](../.gitbook/assets/bug.jpg)       |Mysterious Phantom Boxes Appearing. Fixed                                                                                                      |
| ![](../.gitbook/assets/bug.jpg)       |Video not loading. Fixed                                                                                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Multiple boxes appearing. Fixed                                                                                                                |
| ![](../.gitbook/assets/bug.jpg)       |Misaligned Boxes. Fixed                                                                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |Bounding Boxes and Concepts inconsistent during video playback {Usability}. Fixed                                                              |
| ![](../.gitbook/assets/bug.jpg)       |Change Labeler to use getHostedAssetUrl. Fixed                                                                                                 |
| ![](../.gitbook/assets/bug.jpg)       |Enable drawing even if annotations haven't loaded. Fixed                                                                                       |
| ![](../.gitbook/assets/improvement.jpg)|Use new feature flags at frontend & Labeler for all                                                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Can't add Iris workers to LaaS order. Fixed                                                                                                    |
| ![](../.gitbook/assets/bug.jpg)       |Instructions shouldn't be false while editing. Fixed                                                                                           |
| ![](../.gitbook/assets/bug.jpg)       |Labelers/Reviewers should not see "--" when the task does not have AI Assist enabled. Fixed                                                    |
| ![](../.gitbook/assets/improvement.jpg)|Carousel should show some visual feedback when an input has been rejected                                                                      |
| ![](../.gitbook/assets/bug.jpg)       |Carousel flickers and re-renders images when submitting annotations. Fixed                                                                     |
| ![](../.gitbook/assets/improvement.jpg)|Add loading indicator to labeler view when fetching data                                                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Moving a polygon to the edge of the input causes it to patch outside the allowed range. Fixed                                                  |
| ![](../.gitbook/assets/bug.jpg)       |Wrong worker_per_input field. Fixed                                                                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Hide other regions during interpolation. Fixed                                                                                                 |
| ![](../.gitbook/assets/bug.jpg)       |Concepts Tasks: Cannot read property 'id' of undefined. Fixed                                                                                  |
| ![](../.gitbook/assets/improvement.jpg)|Carousel should show some visual feedback when an input has been skipped                                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Polygon points are sometimes too small to click. fixed                                                                                         |
| ![](../.gitbook/assets/bug.jpg)       |Send embed model id for image annotations. Fixed                                                                                               |
| ![](../.gitbook/assets/bug.jpg)       |Skipping/Submitting annotations causes unnecessary rerenders of the entire carousel (all thumbs). Fixed                                        |
| ![](../.gitbook/assets/bug.jpg)       |Get an error when submitting an input in a classification task. Fixed                                                                          |
| ![](../.gitbook/assets/improvement.jpg)|Improve concept creation process for new apps that you want to label                                                                           |
| ![](../.gitbook/assets/bug.jpg)       |Labeler Reviewer No longer renders assets. Fixed                                                                                               |
| ![](../.gitbook/assets/new_feature.jpg)|Add "Orders" section to task list admin view                                                                                                   |
| ![](../.gitbook/assets/new_feature.jpg)|Add checkbox to task creation for LaaS Orders                                                                                                  |
| ![](../.gitbook/assets/bug.jpg)       |List name field instead of id fields in task lists. Fixed                                                                                      |
| ![](../.gitbook/assets/improvement.jpg)|Set task error code and error description if task annotations pipeline fails                                                                   |
| ![](../.gitbook/assets/bug.jpg)       |Label task submit error: Malformed or invalid request. Fixed                                                                                   |
| ![](../.gitbook/assets/bug.jpg)       |Label video - playback control issue fixed                                                                                                     |
| ![](../.gitbook/assets/improvement.jpg)|Hovering annotations in sidebar of Labeler, should highlight the region in the image.                                                          |
| ![](../.gitbook/assets/bug.jpg)       |Jumping Boxes during video interpolation. Fixed                                                                                                |
| ![](../.gitbook/assets/improvement.jpg)|Polygon rendering in Labeler v2                                                                                                                |
| ![](../.gitbook/assets/improvement.jpg)|Virtual scrolling input carousel                                                                                                               |
| ![](../.gitbook/assets/bug.jpg)       |LabelOrders not fetched when refresh at /labeler page. Fixed                                                                                   |
| ![](../.gitbook/assets/improvement.jpg)|Lock Edit feature for LaasOrders other than pending orders                                                                                     |
| ![](../.gitbook/assets/improvement.jpg)|Account for system states (inputId, taskID) between heartbeats and account for them in canvas interaction manager                              |
| ![](../.gitbook/assets/improvement.jpg)|Cleanup labelerv2 state on unmount                                                                                                             |
| ![](../.gitbook/assets/improvement.jpg)|V2 Rendering Video Regions                                                                                                                     |
| ![](../.gitbook/assets/improvement.jpg)|V2 Video Interpolation                                                                                                                         |
| ![](../.gitbook/assets/improvement.jpg)|Labeler saga to process all remaining actions on input change & before user exits                                                              |
| ![](../.gitbook/assets/bug.jpg)       |Sometimes, bounding box values on Transformer go in the negative, Fixed                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |Task Form: Convert fps -> sample_ms                                                                                                            |
| ![](../.gitbook/assets/improvement.jpg)|Let Clarifai user permissions for status & ETA change                                                                                          |
| ![](../.gitbook/assets/improvement.jpg)|Implement clarifai user journey for LaaS                                                                                                       |
| ![](../.gitbook/assets/improvement.jpg)|Seperate LaaS order tasks from simple labeling tasks.                                                                                          |
| ![](../.gitbook/assets/improvement.jpg)|Edit task functionality for clarifai user                                                                                                      |
| ![](../.gitbook/assets/improvement.jpg)|Include Order Task in "assigned to me" and "for review"                                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |Regions disappeared in sidebar. Fixed                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg)|Implement a way for Clarifai users to review Order tasks                                                                                       |
| ![](../.gitbook/assets/improvement.jpg)|Video Rendering Sync with FPS                                                                                                                  |
| ![](../.gitbook/assets/improvement.jpg)|Reconcile V1 and V2 video frame index                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg)|Convert incorrectly created fps to sampleMs                                                                                                    |
| ![](../.gitbook/assets/improvement.jpg)|Better signposting of task instruction preview panel                                                                                           |
| ![](../.gitbook/assets/bug.jpg)       |Reset Button doesn't work. Fixed                                                                                                               |
| ![](../.gitbook/assets/bug.jpg)       |Can't go back from Labeler UI. Fixed                                                                                                           |
| ![](../.gitbook/assets/bug.jpg)       |Collaborators can not add collaborators. Fixed                                                                                                 |
| ![](../.gitbook/assets/improvement.jpg)|Labeler: Add both index and time to all video annotations                                                                                      |
| ![](../.gitbook/assets/new_feature.jpg)|Implement polygon drawing                                                                                                                      |
| ![](../.gitbook/assets/bug.jpg)       |Toolbar Next & Previous button issue fixed                                                                                                     |
| ![](../.gitbook/assets/bug.jpg)       |Worker filters don't work in review grid sidebar. Fixed                                                                                        |
| ![](../.gitbook/assets/bug.jpg)       |Fixed styling/layout of progress bar in the grid review page                                                                                   |
| ![](../.gitbook/assets/improvement.jpg)|Add "select all" link next to each concept heading in the grid                                                                                 |
| ![](../.gitbook/assets/new_feature.jpg)|Integrate order task with current implementation for reviewer and worker                                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Modify Labelerv2 sagas to be compatible with listening to polygon events                                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Instructions editor should not show toolbar toggle, when in preview mode. Fixed                                                                |
| ![](../.gitbook/assets/bug.jpg)       |Worker strategy should be included while adding workers. Fixed                                                                                 |
| ![](../.gitbook/assets/bug.jpg)       |Task creation form concept field should correctly handle paginated response. Fixed                                                             |
| ![](../.gitbook/assets/bug.jpg)       |Partition worker strategy should only be selectable if you have more than 1 worker. Fixed                                                      |
| ![](../.gitbook/assets/new_feature.jpg)|Labeler v2 submit functionality                                                                                                                |
| ![](../.gitbook/assets/bug.jpg)       |GridReview: app crash due to code for getting reviewer name. Fixed                                                                             |



### API
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/bug.jpg)       |Patch annotation req failed. Fixed                                                   |
| ![](../.gitbook/assets/new_feature.jpg)|Allow any type of task when the app default workflow is empty workflow               |
| ![](../.gitbook/assets/new_feature.jpg)|LaaS billing                                                                         |
| ![](../.gitbook/assets/bug.jpg)       |Undo the delete of cvat persistent volumes                                           |
| ![](../.gitbook/assets/bug.jpg)       |Copier failed in workflow prediction and causing 99009. Fixed                        |
| ![](../.gitbook/assets/new_feature.jpg)|Make gRPC C# client                                                                  |
| ![](../.gitbook/assets/new_feature.jpg)|Make gRPC PHP client                                                                 |
| ![](../.gitbook/assets/bug.jpg)       |Feedback for malinformend CSV formats                                                |
| ![](../.gitbook/assets/improvement.jpg)|Make PostKeys and PatchKeys support apps->user_id set to "me"                        |
| ![](../.gitbook/assets/new_feature.jpg)|Add automated testing of documentation code examples                                 |
| ![](../.gitbook/assets/improvement.jpg)|change to getHostedAssetUrl to support returning both video thumbnails and video urls|
| ![](../.gitbook/assets/improvement.jpg)|Prepare clients for the secure gRPC channel                                          |
| ![](../.gitbook/assets/improvement.jpg)|Update the gRPC copying code with C#, PHP                                            |
| ![](../.gitbook/assets/improvement.jpg)|Use sendgrid template for email                                                      |


### Model
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/new_feature.jpg)|Add AWS Lambda to model mode                                                         |
| ![](../.gitbook/assets/new_feature.jpg)|Add AWS Lambda model type to API                                                     |
| ![](../.gitbook/assets/new_feature.jpg)|Put Fairface model in production                                                     |
| ![](../.gitbook/assets/improvement.jpg)|Append landmark and pose annotations to Fairface dataset                             |
| ![](../.gitbook/assets/bug.jpg)       |Fix empty status response                                                            |
| ![](../.gitbook/assets/bug.jpg)       |Miscellaneous Fixes on Object Counter and KNN                                        |
| ![](../.gitbook/assets/improvement.jpg)|Allow empty statusCallbackURL and entityStatusCallbackURL                            |
| ![](../.gitbook/assets/new_feature.jpg)|Smart Reply                                                                          |
| ![](../.gitbook/assets/new_feature.jpg)|Remove isInternalUser Selector from Text Features                                    |


### Workflow
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/bug.jpg)       |Editing the Empty workflow throws an error in portal. Fixed                          |
| ![](../.gitbook/assets/improvement.jpg)|Add Filtering By Concepts for Text workflows                                         |
| ![](../.gitbook/assets/improvement.jpg)|Add supress_output field option to each workflow node in create workflow view        |
| ![](../.gitbook/assets/improvement.jpg)|Add workflows tab to model gallery                                                   |
| ![](../.gitbook/assets/bug.jpg)       |Allow reindexing to different workflow without having a shared workflow node (with the old one)|
| ![](../.gitbook/assets/bug.jpg)       |No response when "Update workflow" button is pressed. Fixed                          |


### Portal
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement.jpg)|Refactor Sidebar ✅/❌ functionality to sagas                                          |
| ![](../.gitbook/assets/improvement.jpg)|Combine Tool components                                                              |
| ![](../.gitbook/assets/bug.jpg)       |Cannot add card. Something went wrong. Fixed                                         |
| ![](../.gitbook/assets/bug.jpg)       |DOMEX face app using face detect. Clicking on any image causes portal to crash. Fixed|
| ![](../.gitbook/assets/bug.jpg)       |App in staging, crashing when using pause/play with video. Fixed                     |
| ![](../.gitbook/assets/improvement.jpg)|Improve algorithm for grouping annotations and predictions in explorer.              |
| ![](../.gitbook/assets/bug.jpg)       |N "Predicted Bounding Boxes" toggle button only works after clicking twice           |
| ![](../.gitbook/assets/improvement.jpg)|Show track ID for videos in explorer                                                 |
| ![](../.gitbook/assets/improvement.jpg)|Use ModelType to validate args and persist default values with model versions.       |
| ![](../.gitbook/assets/improvement.jpg)|Update create workflows page design                                                  |
| ![](../.gitbook/assets/improvement.jpg)|Add sortable columns when in list view of model mode. Fixed                          |
| ![](../.gitbook/assets/improvement.jpg)|Add pagination to the list of collaborations on app list page of Portal.             |
| ![](../.gitbook/assets/improvement.jpg)|Adopt same tabs everywhere in portal                                                 |
| ![](../.gitbook/assets/improvement.jpg)|Display user_id in user's profile page of portal.                                    |
| ![](../.gitbook/assets/improvement.jpg)|Use fully qualified urls throughout portal                                           |
| ![](../.gitbook/assets/improvement.jpg)|Expose the delete button in explorer single input view                               |
| ![](../.gitbook/assets/bug.jpg)       |Adding new concepts to classification apps disappear from Single Image View until refresh. Fixed|
| ![](../.gitbook/assets/improvement.jpg)|Fix CSS styling of Text Assets for Single Image View                                 |
| ![](../.gitbook/assets/improvement.jpg)|Image terminology in eval page                                                       |
| ![](../.gitbook/assets/bug.jpg)       |Empty workflow breaks explorer workflow dropdown. Fixed                              |
| ![](../.gitbook/assets/bug.jpg)       |Fix create model range selector min/max values                                       |
| ![](../.gitbook/assets/bug.jpg)       |Model gallery in model mode fails when you click on any concept model with a concept not found message. Fixed|
| ![](../.gitbook/assets/bug.jpg)       |Classification Prediction Scores still disappear for previously created apps. Fixed  |
| ![](../.gitbook/assets/bug.jpg)       |Disable "Train" button on pre-trained models                                         |
| ![](../.gitbook/assets/bug.jpg)       |Video times offset by 50ms                                                           |
| ![](../.gitbook/assets/bug.jpg)       |Detection Tab of Image Details Sidebar does not always display in Face apps.  Sometimes it shows classification equivalent. Fixed|
| ![](../.gitbook/assets/bug.jpg)       |Model details page crashes while displaying concepts. Fixed                          |
| ![](../.gitbook/assets/bug.jpg)       |Video thumbnails not displaying in search results. Fixed                             |
| ![](../.gitbook/assets/bug.jpg)       |Listing collaborators models in collector view doesn't work. Fixed                   |
| ![](../.gitbook/assets/bug.jpg)       |Fix API error while listing collaborators' models in collectors UI. Fixed            |
| ![](../.gitbook/assets/bug.jpg)       |Remove unnecessary field from model details page. Fixed                              |
| ![](../.gitbook/assets/bug.jpg)       |Slider for Explorer prediction confidence doesn't apply to all the workflow nodes. Fixed|
| ![](../.gitbook/assets/bug.jpg)       |Sending embed_model_version_id on all model types but that's not valid. Fixed        |
| ![](../.gitbook/assets/improvement.jpg)|Memoize sorted detection annotations and custom model predictions to prevent UI lag  |
| ![](../.gitbook/assets/improvement.jpg)|Modify the way users navigate to the model details page                              |
| ![](../.gitbook/assets/improvement.jpg)|Fix collector mode to filter by user, then app, then models, then model versions.    |
| ![](../.gitbook/assets/bug.jpg)       |Image carousel does not scroll to the currently selected text input being viewed     |




## Changelog 6.7

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### API
|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement.jpg) |Don't allow updating task workers                                                                                                                             |
| ![](../.gitbook/assets/improvement.jpg) |Don't create duplicated task annotations                                                                                                                      |
| ![](../.gitbook/assets/improvement.jpg) |Fix detection evals showing and too many metrics calls                                                                                                        |
| ![](../.gitbook/assets/improvement.jpg) |Fix pillow installs for webp                                                                                                                                  |
| ![](../.gitbook/assets/improvement.jpg) |Add enum for embed model version id field type.                                                                                                               |
| ![](../.gitbook/assets/improvement.jpg) |Don't show model types for backends that aren't responding.                                                                                                   |
| ![](../.gitbook/assets/improvement.jpg) |Clean up output_info.data path                                                                                                                                |
| ![](../.gitbook/assets/improvement.jpg) |Add model_type_id to Model protos.                                                                                                                            |
| ![](../.gitbook/assets/improvement.jpg) |Add /models/types/{model_type_id} endpoint                                                                                                                    |
| ![](../.gitbook/assets/improvement.jpg) |Prevent models_versions.is_public from every being null.                                                                                                      |
| ![](../.gitbook/assets/bug.jpg) |model mode types that are internal only are being returned.                                                                                                   |
| ![](../.gitbook/assets/improvement.jpg) |Create Labeling Order Object and send email to datalabeling@clarifai.com each time backend receives an Labeling Order Object & makes datalabeling a super user|
| ![](../.gitbook/assets/improvement.jpg) |App reindex                                                                                                                                                   |
| ![](../.gitbook/assets/improvement.jpg) |Patchable multi-embed workflows with re-index                                                                                                                 |

### Model

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/bug.jpg) |Demographics model is now broken in model gallery.                                                                                                            |
| ![](../.gitbook/assets/improvement.jpg) |Deprecate model.type from model mode                                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg) |Update model gallery design                                                                                                                                   |
| ![](../.gitbook/assets/improvement.jpg) |embed_model_version_id should be a dropdown                                                                                                                   |


### Portal

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement.jpg) |Add versioning to repo, redux, on screen                                                                                                                      |
| ![](../.gitbook/assets/improvement.jpg) |Allow reviewer to modify annotations during review process.                                                                                                   |
| ![](../.gitbook/assets/new_feature.jpg) |Store entire canvas state in redux/context, and drive canvas updates by central store                                                                         |
| ![](../.gitbook/assets/improvement.jpg) |batch v2 shape events by only 1 PATCH/DELETE request                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg) |Delete functionality v2                                                                                                                                       |
| ![](../.gitbook/assets/improvement.jpg) |Completely detach labeler rendering from server syncing process to enable background syncing                                                                  |
| ![](../.gitbook/assets/improvement.jpg) |Input navigating functionality in v2                                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg) |Set new regionId as "selected" shape if user has selected a transient shape during async updates                                                              |
| ![](../.gitbook/assets/improvement.jpg) |Region edit + delete API sync                                                                                                                                 |
| ![](../.gitbook/assets/improvement.jpg) |Fix annotation denormalizer to rehydrate actual concept value                                                                                                 |
| ![](../.gitbook/assets/improvement.jpg) |Create new region in labeler v2                                                                                                                               |
| ![](../.gitbook/assets/improvement.jpg) |Logic to reduce batched drawing events to least number of API operations                                                                                      |
| ![](../.gitbook/assets/improvement.jpg) |Implement new selectors for regions in v2                                                                                                                     |
| ![](../.gitbook/assets/improvement.jpg) |Normalize Annotations & Regions data for redux storage                                                                                                        |
| ![](../.gitbook/assets/improvement.jpg) |Nest labelerTasks reducer inside labeler reducer                                                                                                              |
| ![](../.gitbook/assets/improvement.jpg) |Konva: Concept Region drawing implementation                                                                                                                  |
| ![](../.gitbook/assets/improvement.jpg) |Konva: Implement Rect Transformation                                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg) |Implement a futureproof schema for labeler interaction events                                                                                                 |
| ![](../.gitbook/assets/improvement.jpg) |Move to event-driven design & have the ability to batch updates using custom logic                                                                            |
| ![](../.gitbook/assets/improvement.jpg) |Create a single Sidebar component for all Labeling types, make children configurable                                                                          |
| ![](../.gitbook/assets/improvement.jpg) |Remove all props unnecessarily passed from LabelerPage to deep children and make components get props from Redux only                                         |
| ![](../.gitbook/assets/improvement.jpg) |Remove all logic from components to sagas for higher level orchestration of features                                                                          |
| ![](../.gitbook/assets/bug.jpg) |Video selector improvements & test updation                                                                                                                   |
| ![](../.gitbook/assets/bug.jpg) |Can only save 50 annotations on an image {Usability}                                                                                                          |
| ![](../.gitbook/assets/bug.jpg) |Konva: resizing BBox below minimum size and "crossing over" makes things awry                                                                                 |
| ![](../.gitbook/assets/bug.jpg) |LabelerPage complete re-render of all components on mouseHover, mousMove (img attached)                                                                       |
| ![](../.gitbook/assets/bug.jpg) |Cypress script doesn't terminate webpack-dev-server child process                                                                                             |
| ![](../.gitbook/assets/bug.jpg) |Cypress pre-run script doesn't check if dev server is already running                                                                                         |
| ![](../.gitbook/assets/bug.jpg) |Create Unit+Integration testing framework                                                                                                                     |
| ![](../.gitbook/assets/bug.jpg) |Integrate headless Cypress with build testing                                                                                                                 |
| ![](../.gitbook/assets/new_feature.jpg) |Switch to react-konva for performant canvas rendering                                                                                                         |
| ![](../.gitbook/assets/improvement.jpg) |Add task id to task list                                                                                                                                      |
| ![](../.gitbook/assets/improvement.jpg) |Panning functionality improvements                                                                                                                            |
| ![](../.gitbook/assets/bug.jpg) |Lock video playback and interpolation to fps                                                                                                                  |
| ![](../.gitbook/assets/bug.jpg) |Annotations created with interpolation seem to have incorrect frame indices                                                                                   |
| ![](../.gitbook/assets/bug.jpg) |Bounding Boxes and Concepts inconsistent during video playback {Usability}                                                                                    |
| ![](../.gitbook/assets/bug.jpg) |While annotating video, interpolation freezes and all annotations disappear                                                                                   |
| ![](../.gitbook/assets/bug.jpg) |Boxes/Interpolation objects are not saving after task submission                                                                                              |
| ![](../.gitbook/assets/improvement.jpg) |Display task instructions to workers in labeler mode                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg) |Add infinite scroll loading to labeler carousel                                                                                                               |
| ![](../.gitbook/assets/bug.jpg) |Not incrementing onNext and onPrev pages in Labeler Carousel                                                                                                  |
| ![](../.gitbook/assets/improvement.jpg) |Display only minimal log in Portal react app                                                                                                                  |
| ![](../.gitbook/assets/improvement.jpg) |Update Model mode to use the GET /models/types endpoint                                                                                                       |
| ![](../.gitbook/assets/improvement.jpg) |Add list/grid toggle in model mode on all view                                                                                                                |
| ![](../.gitbook/assets/improvement.jpg) |Collectors UI should use the layout similar to ModellingMode/LabellerMode                                                                                     |
| ![](../.gitbook/assets/bug.jpg) |Bulk add concepts to region annotations in app with multi-embed base workflow                                                                                 |
| ![](../.gitbook/assets/bug.jpg) |Profile page crashes on load                                                                                                                                  |
| ![](../.gitbook/assets/bug.jpg) |Model mode array of concepts should be unique                                                                                                                 |
| ![](../.gitbook/assets/bug.jpg) |Model creation/edit bugs                                                                                                                                      |
| ![](../.gitbook/assets/bug.jpg) |New Collector page not scrollable                                                                                                                             |
| ![](../.gitbook/assets/bug.jpg) |App Workflows - Unable to update model version for custom models                                                                                              |
| ![](../.gitbook/assets/new_feature.jpg) |Display Created At Date in App Grid View                                                                                                                      |
| ![](../.gitbook/assets/new_feature.jpg) |Support .txt files from local file browser                                                                                                                    |
| ![](../.gitbook/assets/new_feature.jpg) |Support uploading of multiple video assets as well as image and video assets within the same CSV file                                                         |
| ![](../.gitbook/assets/new_feature.jpg) |Add better user feedback for uploading text assets                                                                                                            |
| ![](../.gitbook/assets/new_feature.jpg) |Upload Text by CSV for NLP                                                                                                                                    |
| ![](../.gitbook/assets/improvement.jpg) |Final NLP MVP Feature Changes                                                                                                                                 |
| ![](../.gitbook/assets/improvement.jpg) |Remove 0 area detection filtering from frontend code                                                                                                          |
| ![](../.gitbook/assets/improvement.jpg) |Modify accepted CSV upload format so every column corresponds to a network request field                                                                      |
| ![](../.gitbook/assets/improvement.jpg) |Resolve final bugs with bounding box indexes                                                                                                                  |
| ![](../.gitbook/assets/improvement.jpg) |Prevent uploading image and video asset types to Text apps                                                                                                    |
| ![](../.gitbook/assets/improvement.jpg) |No Visual Feedback for Text input Upload                                                                                                                      |
| ![](../.gitbook/assets/improvement.jpg) |Support Uploading Files through the OS File Browser for NLP                                                                                                   |
| ![](../.gitbook/assets/bug.jpg) |Custom Model Prediction Bounding Boxes are misaligned from the Detections Bar                                                                                 |
| ![](../.gitbook/assets/bug.jpg) |Workflow Tab should display and load on initial view for text apps                                                                                            |
| ![](../.gitbook/assets/bug.jpg) |Unable to navigate between text assets within explorer's asset detail view                                                                                    |
| ![](../.gitbook/assets/bug.jpg) |CSV uploads not parsing metadata and concepts                                                                                                                 |
| ![](../.gitbook/assets/bug.jpg) |Explorer's Advanced Search does not support searching by concepts                                                                                             |
| ![](../.gitbook/assets/bug.jpg) |Training a classification model no longer display anything within the Custom Model Predictions tab                                                            |
| ![](../.gitbook/assets/improvement.jpg) |create annotation CUD sagas for labeler v2                                                                                                                    |
| ![](../.gitbook/assets/improvement.jpg) |Don't create task annotations in frontend                                                                                                                     |
| ![](../.gitbook/assets/bug.jpg) |Form: Input Source showing auto complete options from other apps                                                                                              |
| ![](../.gitbook/assets/bug.jpg) |Rich text instructions icon bugs                                                                                                                              |
| ![](../.gitbook/assets/bug.jpg) |Task create form doesnt force you to set a reviewer if you specify manual review                                                                              |
| ![](../.gitbook/assets/bug.jpg) |TypeError: val.add is not a function                                                                                                                          |
| ![](../.gitbook/assets/bug.jpg) |Fix autocomplete when user selects "All inputs" for selecting inputs in task creation                                                                         |
| ![](../.gitbook/assets/bug.jpg) |Error pops up when collaborator tries to edit task                                                                                                            |
| ![](../.gitbook/assets/bug.jpg) |When I attempt to edit an existing labeling task t...                                                                                                         |
| ![](../.gitbook/assets/bug.jpg) |Page not responding [Usability]                                                                                                                               |
| ![](../.gitbook/assets/bug.jpg) |[Explorer] concept thumbnails aren't displaying from model details view                                                                                       |
| ![](../.gitbook/assets/bug.jpg) |Concept Detail View displays incorrect assets                                                                                                                 |
| ![](../.gitbook/assets/improvement.jpg) |Add all concepts button to model mode forms                                                                                                                   |
| ![](../.gitbook/assets/bug.jpg) |Concept Autocomplete in Model Mode doesn't always display                                                                                                     |


### Workflows

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/new_feature.jpg) |Allow run workflow and search embedding from embed model in workflow                                                                                          |

### Applications

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement.jpg) |Metadata Namespacing for Clarifai Apps                                                                                                                        |
| ![](../.gitbook/assets/bug.jpg) |App details page should send a user to models page to create models rather than using modal                                                                   |



# Changelog

## Changelog 6.6

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |


### API
|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/improvement.jpg)|Integrate Python functions service with API|
| ![](../.gitbook/assets/improvement.jpg)|List available model types through API     |

### Model
|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/bug.jpg)|Fix video error from new face cluster model in staging env|
| ![](../.gitbook/assets/bug.jpg)|21312 Ground truth data caseids must be nonempty and unique. Fixed|
| ![](../.gitbook/assets/improvement.jpg)|Update deep training to list the ModelTypes|
| ![](../.gitbook/assets/improvement.jpg)|Move model_metadata to better place in protos. |
| ![](../.gitbook/assets/improvement.jpg)|Generalize the domex-visual-searcher model type|
| ![](../.gitbook/assets/improvement.jpg)|List available model types from backend services that provide models.

### Portal

|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/bug.jpg)|Fixed bug in submitting finished Labeler Task|
| ![](../.gitbook/assets/bug.jpg)|Select all concepts checkbox can be de-synced from actual concepts badges. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Disable Create Task button if not app owner|
| ![](../.gitbook/assets/bug.jpg)|Search by task_id returns incorrect data   |
| ![](../.gitbook/assets/bug.jpg)|Removed model creation from concept creation action in portal|
| ![](../.gitbook/assets/bug.jpg)|Video scrubber cannot be moved. Fixed      |
| ![](../.gitbook/assets/bug.jpg)|Fixed ability to delete interpolation tracks (you can only delete frames at this time).|
| ![](../.gitbook/assets/bug.jpg)|Worker ids used instead of names in report overview in stats view. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Y-axis on labels created stats page is wrong. Fixed|
| ![](../.gitbook/assets/bug.jpg)|In task creation, adding concepts should be simple to click all the options right away. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Toggling concept visibility doesn't affect previously hidden child region. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Leftover                                   |
| ![](../.gitbook/assets/bug.jpg)|If reviewer is not a collaborator, UI sends empty reviewer id back instead of raising error. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Bounding box disappears on resizing. Fixed |
| ![](../.gitbook/assets/bug.jpg)|While adjusting bounding box, it creates an additional bounding box over no object. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Using Play button brings up "Oops" page. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Error on opening Video Labeler. Fixed      |
| ![](../.gitbook/assets/bug.jpg)|Labeler sidebar interaction bugs and unresponsiveness (due to lack of optimistic UI). Fixed|
| ![](../.gitbook/assets/bug.jpg)|Newly drawn object disappears from canvas after drawing, and reappears after API response. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Infinite loading in Labeler Mode for app without any inputs. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Use name field for tasks in Labeler admin. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Clicking labeler icon crashes. Fixed       |
| ![](../.gitbook/assets/bug.jpg)|Moving bounding box around repeatedly creates a race condition, shows error notification and duplicate box. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Explorer inputs stale state. Fixed         |
| ![](../.gitbook/assets/bug.jpg)|Diagnose issues affecting overall hanging/speed/performance of Labeler|
| ![](../.gitbook/assets/bug.jpg)|Carousel thumbnails not showing up in Labeler. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Not able to create overlapping bounding boxes. Fixed|
| ![](../.gitbook/assets/bug.jpg)|When user adds mass metadata in Explorer, the UI says success but metadata does not persist. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Create annotations while creating task. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Labeler board showing wrong task type. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Polygon annotations break Explorer. Fixed  |
| ![](../.gitbook/assets/bug.jpg)|Concept autocomplete in Labeler task creation is showing clarifai/main concepts. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Should not be allowed to create a task with no concepts if my app has no concepts. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Fixed image tools state                    |
| ![](../.gitbook/assets/bug.jpg)|Restricted tasks to only the assigned users|
| ![](../.gitbook/assets/bug.jpg)|Add validation to TaskForm’s concept field |
| ![](../.gitbook/assets/bug.jpg)|Removed all instances of worker_id from Explorer|
| ![](../.gitbook/assets/bug.jpg)|Create one annotation for each bbox        |
| ![](../.gitbook/assets/bug.jpg)|98011 panic on ListTasks. Fixed            |
| ![](../.gitbook/assets/bug.jpg)|App names no longer display in Explorer. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Empty Annotations are not displaying after drawing a new bounding box until after refreshing the page. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Drawing a new bounding box in Explorer after previously labeling a region display an error. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Video search results do not play at the most relevant video time. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Change text upload UI to support moderation workflow|
| ![](../.gitbook/assets/bug.jpg)|Change object key lookup in boundingBoxContainer to use lodash/get|
| ![](../.gitbook/assets/bug.jpg)|Submitting Task for Review break Portal. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Labeling a region on an asset with multiple detected regions will put the child annotation in the wrong group in Explorer's sidebar. Fixed|
| ![](../.gitbook/assets/bug.jpg)|ConvertToBoundingBoxRegion function breaks Explorer when annotation information has not loaded at time of render. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Video Frame Annotating in Explorer throws errors. Fixed|
| ![](../.gitbook/assets/bug.jpg)|When drawing a new bounding box, Base64 string for video annotations shows the wrong regions. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Fixe 10MB issue with video uploads         |
| ![](../.gitbook/assets/bug.jpg)|Detection Regions and Indexes are thrown off on video assets. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Video Search Results still on showing Inputs. Fixed|
| ![](../.gitbook/assets/bug.jpg)|DetailsPageHeader adds 2.25rem margin to the DetailsPageBody. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Video Interpolation in Labeler breaks dev. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Redux is no longer calculating the sample_ms rate, preventing bounding boxes from rendering. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Fixed video pause error when navigating between videos|
| ![](../.gitbook/assets/bug.jpg)|ImagePile in Labeler Task View does not display image thumbs due to extraneous object nesting. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Remove warning error from console for immutable passed in props to SearchGrid.js|
| ![](../.gitbook/assets/bug.jpg)|Post annotation to detection region should use region id in portal. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Delete app button in app details takes you to blank page. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Incorrect bbox/label numbers displayed in image. Fixed|
| ![](../.gitbook/assets/bug.jpg)|Multiple video thumbs selected in search results when selecting one thumb. Fixed|
| ![](../.gitbook/assets/improvement.jpg)|Improve Labeler mode window resizing.      |
| ![](../.gitbook/assets/improvement.jpg)|W and E hotkeys for image labelling to go left/right. |
| ![](../.gitbook/assets/bug.jpg)|Polygon annotations break Explorer. Fixed. |
| ![](../.gitbook/assets/bug.jpg)|Polygons regions don’t appear when panning and zooming. Fixed. |
| ![](../.gitbook/assets/improvement.jpg)|Allow users to create concepts on task create view.|
| ![](../.gitbook/assets/bug.jpg)|Fixed task list item count query.          |
| ![](../.gitbook/assets/improvement.jpg)|Utilising new task endpoints to Create tasks and integrate to show tasks in Portal.|
| ![](../.gitbook/assets/bug.jpg)|LabelerPage refresh error. Fixed.          |
| ![](../.gitbook/assets/bug.jpg)|Should not be allowed to create a task with no concepts if my app has no concepts. Fixed.|
| ![](../.gitbook/assets/bug.jpg)|Unknown page Error. Complete interpolation of an object doesn't show bbox. Complete tracking of a box will disappear from the video. Fixed.|
| ![](../.gitbook/assets/bug.jpg)|Fixed carousel padding.                    |
| ![](../.gitbook/assets/bug.jpg)|Labeler board showing wrong task type. Fixed.|
| ![](../.gitbook/assets/improvement.jpg)|Integrate worker/reviewer side of Labeler. |
| ![](../.gitbook/assets/improvement.jpg)|Add 'name' field to new Tasks.             |
| ![](../.gitbook/assets/bug.jpg)|Create annotations while creating task.    |
| ![](../.gitbook/assets/bug.jpg)|Carousel thumbnails not showing up in Labeler. Fixed.|
| ![](../.gitbook/assets/improvement.jpg)|No image clearing/loading indicator in Labeler. Fixed.|
| ![](../.gitbook/assets/bug.jpg)|Use name field for tasks in Labeler administration.|
| ![](../.gitbook/assets/bug.jpg)|Bulk labeling value does not update in store upon labeling. Fixed.|
| ![](../.gitbook/assets/improvement.jpg)|Record time per annotation and per input to /stats/values in Labeler mode of Portal. |
| ![](../.gitbook/assets/improvement.jpg)|Query and display stats across workers per task for time and count of annotations. |
| ![](../.gitbook/assets/bug.jpg)|Concept autocomplete in Labeler task creation is showing clarifai/main concepts. Fixed.|
| ![](../.gitbook/assets/new_feature.jpg)|Implement polygon task type in Labeler.    |
| ![](../.gitbook/assets/bug.jpg)|Applying filters in Portal breaks bulk labeling / unlabeling. Fixed.|
| ![](../.gitbook/assets/bug.jpg)|Unable to bulk-label annotations. Fixed.   |
| ![](../.gitbook/assets/improvement.jpg)|Change submit to "Complete Task" in Labeler page and add progress bar as it's working.|
| ![](../.gitbook/assets/improvement.jpg)|Allow Patching region annotations in Labeler mode. |
| ![](../.gitbook/assets/improvement.jpg)|Add AI assist thresholding.                |
| ![](../.gitbook/assets/improvement.jpg)|Add ability to set annotation_info in the annotation writer|
| ![](../.gitbook/assets/bug.jpg)|`annotation_info` should be a valid JSON in Model Mode. Fixed.|
| ![](../.gitbook/assets/improvement.jpg)|Upgrade gulp and node to latest version for testing-library support|
| ![](../.gitbook/assets/improvement.jpg)|Write PropType declarations for componens/ConceptListTable|
| ![](../.gitbook/assets/improvement.jpg)|Enable collapse behavior in sidebar concepts|
| ![](../.gitbook/assets/improvement.jpg)|Create atomic reusable  sidebar components |
| ![](../.gitbook/assets/improvement.jpg)|Integrate React Testing Library            |
| ![](../.gitbook/assets/improvement.jpg)|Konva: Image centering, zooming, panning   |
| ![](../.gitbook/assets/improvement.jpg)|Move toolbar logic to react context        |
| ![](../.gitbook/assets/improvement.jpg)|Refactor TaskForm related thunks to sagas  |
| ![](../.gitbook/assets/improvement.jpg)|[Rearch]Scaffold Labeler Redux in a new nested state slice & Implement Sagas|
| ![](../.gitbook/assets/improvement.jpg)|[P2] Task id is used in dropdown of stats tasks rather than task.name|
| ![](../.gitbook/assets/improvement.jpg)|[P0]Show taskId at task list               |
| ![](../.gitbook/assets/improvement.jpg)|Move region visibility state to its own React Context|
| ![](../.gitbook/assets/improvement.jpg)|Get sidebar list data directly from redux  |
| ![](../.gitbook/assets/improvement.jpg)|[P1] Don't hide task form if error occurs  |
| ![](../.gitbook/assets/improvement.jpg)|Remove delay of annotation request         |
| ![](../.gitbook/assets/improvement.jpg)|Remove animation for showing concepts on right side|
| ![](../.gitbook/assets/improvement.jpg)|Perf: only fetch input predictions/annotations if user stays on image, not while navigating|
| ![](../.gitbook/assets/improvement.jpg)|Get Labeler internal features ready for internal users|
| ![](../.gitbook/assets/improvement.jpg)|Offload annotation creation to backend     |
| ![](../.gitbook/assets/improvement.jpg)|allow reviewers update annotations         |
| ![](../.gitbook/assets/improvement.jpg)|No image clearing/loading indicator in Labeler|
| ![](../.gitbook/assets/improvement.jpg)|Controls for resizing bounding boxes need to be more visible|
| ![](../.gitbook/assets/improvement.jpg)|Fabric rendering to be real-time; sync from API in background|
| ![](../.gitbook/assets/improvement.jpg)|make tasks endpoint public                 |
| ![](../.gitbook/assets/improvement.jpg)|list task by worker id/reviewer id         |
| ![](../.gitbook/assets/improvement.jpg)|Add 'name' field to new Tasks              |
| ![](../.gitbook/assets/improvement.jpg)|Integrate worker/reviewer side of labeller |
| ![](../.gitbook/assets/improvement.jpg)|Integrate and Implement task deletion using new endpoints|
| ![](../.gitbook/assets/improvement.jpg)|Utilising new task endpoints to Create tasks and integrate to show tasks at portal|
| ![](../.gitbook/assets/improvement.jpg)|Integrate and utilise new CRUD endpoints in portal|
| ![](../.gitbook/assets/improvement.jpg)|Allow users to create concepts on task create view|
| ![](../.gitbook/assets/improvement.jpg)|Add empty CRUD endpoints for tasks         |
| ![](../.gitbook/assets/improvement.jpg)|Make polygons a separate task type         |
| ![](../.gitbook/assets/improvement.jpg)|Add AI assist thresholding                 |
| ![](../.gitbook/assets/improvement.jpg)|W and E hotkeys for image labelling to go left/right. |
| ![](../.gitbook/assets/improvement.jpg)|Improve labeler mode window resizing.      |
| ![](../.gitbook/assets/improvement.jpg)|Allow Patching region annotations in labeler mode. |
| ![](../.gitbook/assets/improvement.jpg)|crank up internal message size to handle larger videos with more outputs|
| ![](../.gitbook/assets/improvement.jpg)|Introduce stats collection APIs for worker stats. |
| ![](../.gitbook/assets/improvement.jpg)|Implement /tasks CRUD in API.              |
| ![](../.gitbook/assets/improvement.jpg)|Add frame.id to API as well as track id.   |
| ![](../.gitbook/assets/improvement.jpg)|Remove ‘alt’ from hotkeys, just use letters and arrows straight up|
| ![](../.gitbook/assets/improvement.jpg)|Update image tool icons                    |
| ![](../.gitbook/assets/improvement.jpg)|Add support for fields under ENUM values during model creation|
| ![](../.gitbook/assets/improvement.jpg)|Implement Dynamic model types              |
| ![](../.gitbook/assets/improvement.jpg)|Ungrouped Annotations/New Annotation Regions should display at the top of Explorer's Detections List|
| ![](../.gitbook/assets/improvement.jpg)|Change explorer to use sample_ms instead from network response instead of deducing the value|
| ![](../.gitbook/assets/improvement.jpg)|Hide Workflow List Elements if below Range Slider value|
| ![](../.gitbook/assets/improvement.jpg)|Modify Annotating from Custom Model Predictions to post new annotations.|
| ![](../.gitbook/assets/improvement.jpg)|Update model mode with new designs         |
| ![](../.gitbook/assets/improvement.jpg)|Refactor ImageUtils.js file to individual functions instead of one object|
| ![](../.gitbook/assets/improvement.jpg)|Added threshold search result in Portal    |
| ![](../.gitbook/assets/improvement.jpg)|Update media player icons                  |
| ![](../.gitbook/assets/improvement.jpg)|Display timestamp bar in Explorer grid view for video results|
| ![](../.gitbook/assets/improvement.jpg)|Concept relation should autocomplete concept name|
| ![](../.gitbook/assets/new_feature.jpg)|Send email to workers when they are added to task|
| ![](../.gitbook/assets/new_feature.jpg)|Assigning a worker or reviewer to a task sends an email|
| ![](../.gitbook/assets/new_feature.jpg)|Apps with empty workflow should allow all task types (concepts, bounding box, polygon) during task creation|
| ![](../.gitbook/assets/new_feature.jpg)|Edit Task feature                          |
| ![](../.gitbook/assets/new_feature.jpg)|Support consensus review settings          |
| ![](../.gitbook/assets/new_feature.jpg)|Support detection tasks                    |
| ![](../.gitbook/assets/new_feature.jpg)|Create new Single Image View and Image Tools|
| ![](../.gitbook/assets/new_feature.jpg)|Task view UI for workers                   |
| ![](../.gitbook/assets/new_feature.jpg)|Introduce AWAITING_REVIEW status for annotations|
| ![](../.gitbook/assets/new_feature.jpg)|Split tasks admin view into tabs           |
| ![](../.gitbook/assets/new_feature.jpg)|Test out idea behind tasks as saved searches and POST /annotations iterations|
| ![](../.gitbook/assets/new_feature.jpg)|Implement search by annotation.status in backend|
| ![](../.gitbook/assets/new_feature.jpg)|Search by images or video type in the right hand side bar of explorer's grid view|
| ![](../.gitbook/assets/new_feature.jpg)|Video Crop Region Search                   |
| ![](../.gitbook/assets/new_feature.jpg)|video thumbs display relevant frame in search|


### Workflows

|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/new_feature.jpg)|Display workflow detection predictions on the main/large image in Portal|



# Changelog

## Changelog 6.5

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Can't Access Main Apps Page with invalid collaborators. Fixed. |
| ![](../.gitbook/assets/bug.jpg) | Unable to create new Application \(General Detection\). Fixed. |
| ![](../.gitbook/assets/bug.jpg) | `application_sharing` scopes field should be `json` instead of `jsonb`. Fixed. |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Pasting long text makes Uploader unusable due to lack of scrolling. Fixed. |
| ![](../.gitbook/assets/improvement.jpg) | Support uploading text containing emojis. |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Integrate and Implement task deletion using new endpoints. |
| ![](../.gitbook/assets/improvement.jpg) | Implement /tasks CRUD in API. |
| ![](../.gitbook/assets/improvement.jpg) | Allow annotation writer model to set the `task_id` in `annotation_info`. |
| ![](../.gitbook/assets/improvement.jpg) | Make polygons a separate task type. |
| ![](../.gitbook/assets/improvement.jpg) | Add empty CRUD endpoints for tasks. |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | `vocab_id` doesn't appear in the returned object for demographics model. Fixed. |
| ![](../.gitbook/assets/bug.jpg) | `segment-concept` model types are no longer returning the segmentation mask. Fixed. |
| ![](../.gitbook/assets/bug.jpg) | NLP text input does not scroll when longer than viewport height. Fixed. |
| ![](../.gitbook/assets/bug.jpg) | Clear text inputs after upload. |
| ![](../.gitbook/assets/improvement.jpg) | Improve the "TextFile" React Component for NLP. |
| ![](../.gitbook/assets/improvement.jpg) | Make existing model details view configurable by model type. |
| ![](../.gitbook/assets/bug.jpg) | Edit model should only contain the fields related to the selected model. Fixed |
| ![](../.gitbook/assets/bug.jpg) | NLP frontend text input is covered entirely blue when selected. Fixed. |
| ![](../.gitbook/assets/bug.jpg) | Enforce fields in post/patch models to adhere to model types. Fixed. |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Fixed fps issue for video predictions. |
| ![](../.gitbook/assets/bug.jpg) | Validate `stat_value_agg_type`. |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Dropdown Search Help Menu no longer displays in the search bar. Fixed. |
| ![](../.gitbook/assets/new_feature.jpg) | Video thumbs have relevant timestamp in search. |
| ![](../.gitbook/assets/improvement.jpg) | Added adjustable search results threshold. |
| ![](../.gitbook/assets/new_feature.jpg) | Search over multi-embed workflows. |
| ![](../.gitbook/assets/new_feature.jpg) | Added search on input level. |
| ![](../.gitbook/assets/improvement.jpg) | Improved search query by using multi join. |
| ![](../.gitbook/assets/bug.jpg) | Fixed panic in list saved searches endpoint. |
| ![](../.gitbook/assets/bug.jpg) | Input metadata search from table not working. Fixed. |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | "Return to Log in " doesn't redirect to login page. Fixed. |
| ![](../.gitbook/assets/bug.jpg) | Clicking on image, or Explorer Mode with images that contain geo coordinates crashed the app. |
| ![](../.gitbook/assets/improvement.jpg) | Portal model predicts use hosted URL when available instead of normal URL. |
| ![](../.gitbook/assets/bug.jpg) | When selecting a concept and going to the next image the concept checkbox won't stay selected. Fixed |
| ![](../.gitbook/assets/improvement.jpg) | Allow multi-select from explorer grid view and add metadata. |
| ![](../.gitbook/assets/improvement.jpg) | Integrate and utilize new CRUD endpoints in Portal. |
| ![](../.gitbook/assets/new_feature.jpg) | Allow for pasted text to keep formatting in the text box. |
| ![](../.gitbook/assets/bug.jpg) | Prediction threshold slider custom model predicts without base workflow annotations. Fixed |
| ![](../.gitbook/assets/improvement.jpg) | Strings without spacing format properly in Explorer's Asset Grid View |
| ![](../.gitbook/assets/bug.jpg) | `annotation_info` should be a valid JSON in Model Mode. Fixed. |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Hide the "add text" section of the add inputs modal for non text workflows. |
| ![](../.gitbook/assets/improvement.jpg) | Validate that all nodes in workflows list their inputs based on type. |
| ![](../.gitbook/assets/new_feature.jpg) | Add NLP to Workflows List |
| ![](../.gitbook/assets/improvement.jpg) | Generalize the iterations over regions/frames in workflow code. |
| ![](../.gitbook/assets/new_feature.jpg) | Add ability to "make a copy" of public\_workflows. |
| ![](../.gitbook/assets/improvement.jpg) | Allow indexing embedding from detect -&gt; crop -&gt; embed style workflows. |
| ![](../.gitbook/assets/improvement.jpg) | Allow setting input nodes for all users, not just @clarifai.com users. |
| ![](../.gitbook/assets/improvement.jpg) | Allow non-internal users setting input node when creating workflows. |
| ![](../.gitbook/assets/bug.jpg) | Create/Patch workflow uncaught exception. |

### Clients

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Update docs.clarifai.com to reflect our current API clients including grpc clients. |

## Changelog 6.4

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Improved responsiveness of collaborations tab in /apps |
| ![](../.gitbook/assets/improvement.jpg) | Enabled list collaborators to list deleted collaborators |
| ![](../.gitbook/assets/bug.jpg) | Login Form breaks app. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Deleting an app no longer redirects to /apps |
| ![](../.gitbook/assets/bug.jpg) | Can’t create models in new app. Fixed |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Fixed .webp files not working when sent as base64 |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | MVP of labeler single image view functionality |
| ![](../.gitbook/assets/new_feature.jpg) | Support detection tasks |
| ![](../.gitbook/assets/improvement.jpg) | Detection Labeler: Color Coded Concepts |
| ![](../.gitbook/assets/improvement.jpg) | Add workflow\_id to task creation and show AI predictions to verify in labeler mode |
| ![](../.gitbook/assets/new_feature.jpg) | Split tasks admin view into tabs |
| ![](../.gitbook/assets/improvement.jpg) | Add visual sections to task form |
| ![](../.gitbook/assets/improvement.jpg) | Add default queries for "all inputs" and "all unlabelled inputs" in task create view |
| ![](../.gitbook/assets/improvement.jpg) | Autocomplete annotation user |
| ![](../.gitbook/assets/new_feature.jpg) | Implement Classification Task Review Logic |
| ![](../.gitbook/assets/new_feature.jpg) | Implement Review Process into tasks |
| ![](../.gitbook/assets/improvement.jpg) | Introduce stats collection APIs for worker stats |
| ![](../.gitbook/assets/new_feature.jpg) | Implement APIs for polygon region support |
| ![](../.gitbook/assets/new_feature.jpg) | Incorporate image filters for labelling |
| ![](../.gitbook/assets/improvement.jpg) | Update image tool icons |
| ![](../.gitbook/assets/new_feature.jpg) | Ability to zoom in on images |
| ![](../.gitbook/assets/improvement.jpg) | Remove ‘alt’ from hotkeys, just use letters and arrows |
| ![](../.gitbook/assets/new_feature.jpg) | Label to draw box in video frame using frame bytes |
| ![](../.gitbook/assets/improvement.jpg) | Display videos in labeler |
| ![](../.gitbook/assets/improvement.jpg) | Add video fps field for tasks |
| ![](../.gitbook/assets/improvement.jpg) | Draw Bounding Boxes in Labeler Detection Videos |
| ![](../.gitbook/assets/improvement.jpg) | Add video controls for video in labeler |
| ![](../.gitbook/assets/bug.jpg) | Fix Classification Annotation |
| ![](../.gitbook/assets/bug.jpg) | Video annotation deletion. Fixed |
| ![](../.gitbook/assets/bug.jpg) | AI Assist Predictions did not show for General workflow classification task. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Fix Classification video annotation |
| ![](../.gitbook/assets/bug.jpg) | Display video in classification tasks |
| ![](../.gitbook/assets/bug.jpg) | Fix Labeler input urls |
| ![](../.gitbook/assets/bug.jpg) | Fix Annotation creation for video |
| ![](../.gitbook/assets/bug.jpg) | Fix Labeler post calls |
| ![](../.gitbook/assets/bug.jpg) | Detection Labeler: fix zoom |
| ![](../.gitbook/assets/bug.jpg) | Fixed image cropper task description |
| ![](../.gitbook/assets/bug.jpg) | Fix concept threshold creation |
| ![](../.gitbook/assets/bug.jpg) | Set annotation status ‘success’ |
| ![](../.gitbook/assets/bug.jpg) | Restrict tasks to only the assigned users |
| ![](../.gitbook/assets/bug.jpg) | Add validation to TaskForm’s concept field |
| ![](../.gitbook/assets/bug.jpg) | Display human tags for human box as child |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Convert Deep Trained Model to Embedding Model for Use as "Base Workflow" |
| ![](../.gitbook/assets/new_feature.jpg) | Classification predictions for AI assistance |
| ![](../.gitbook/assets/new_feature.jpg) | Merge this detection and custom model prediction sections for detection models |
| ![](../.gitbook/assets/improvement.jpg) | Video labelling UI for classification. |
| ![](../.gitbook/assets/improvement.jpg) | Remove the non-creatable types from model mode |
| ![](../.gitbook/assets/improvement.jpg) | Improve the create classifier / detector view options in model mode |
| ![](../.gitbook/assets/improvement.jpg) | Add deep training options in model mode |
| ![](../.gitbook/assets/improvement.jpg) | Update random sampling model to have a slider |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Fixed public concept rank |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Support detection evaluations in PostAnnotationSearchMetrics |
| ![](../.gitbook/assets/new_feature.jpg) | Support nlp search \(only filtering\) |
| ![](../.gitbook/assets/new_feature.jpg) | Add evaluations between two saved search label sets |
| ![](../.gitbook/assets/improvement.jpg) | Fix labeler search amount |
| ![](../.gitbook/assets/bug.jpg) | Error:  "Cannot search over `annotations`" when clicking a general app. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Model name and details is not populated upon model creation in model mode |
| ![](../.gitbook/assets/bug.jpg) | Fix annotation search when accessing the LabelerPage |
| ![](../.gitbook/assets/bug.jpg) | Search by annotation\_info should not return the embed annotation. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Search for metadata in detection apps doesn't work. Fixed |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Create Dual Range Slider |
| ![](../.gitbook/assets/new_feature.jpg) | Enable patching the default workflow from Portal and error if needs reindex |
| ![](../.gitbook/assets/new_feature.jpg) | Allow drawing bounding boxes on paused video frames |
| ![](../.gitbook/assets/improvement.jpg) | Add scopes for collaborators and metrics to Portal |
| ![](../.gitbook/assets/improvement.jpg) | Allow up to 15-20x zoom level for really large images. |
| ![](../.gitbook/assets/improvement.jpg) | Allow selection the embed\_model\_version\_id from Portal when creating a model |
| ![](../.gitbook/assets/bug.jpg) | Fix inconsistent fps between uploading video and predicting video |
| ![](../.gitbook/assets/bug.jpg) | Missing frame time. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Model annotations not appearing in Explorer. Fixed |
| ![](../.gitbook/assets/bug.jpg) | When creating the auto annotation workflow editing the workflow crashes Portal |
| ![](../.gitbook/assets/bug.jpg) | Fix image tools state |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | CreateWorkflow model improvements |
| ![](../.gitbook/assets/improvement.jpg) | Allow custom concept models in the default app workflows |
| ![](../.gitbook/assets/improvement.jpg) | Add a "Make a Copy" or "Copy to New Workflow" button for each workflow |
| ![](../.gitbook/assets/improvement.jpg) | Allow patching the default workflow in Portal |
| ![](../.gitbook/assets/improvement.jpg) | Show the default workflow in the list of workflows for the app |
| ![](../.gitbook/assets/improvement.jpg) | Validate patching of default workflow is compatible in backend |
| ![](../.gitbook/assets/bug.jpg) | Large workflow name causes overlap in app details view. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Portal crashes if page reloads during workflow add/edit. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Detection workflow recompute also predict detect-concept |
| ![](../.gitbook/assets/bug.jpg) | Allow detect-concept models to be added to workflows |
| ![](../.gitbook/assets/bug.jpg) | Patch workflow create worker |
| ![](../.gitbook/assets/bug.jpg) | Fix validation of inputs in workflows |
| ![](../.gitbook/assets/bug.jpg) | Fix workflow embed\_join\_annotation\_id issue |

### Clients

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Clean up private API client repos |
| ![](../.gitbook/assets/bug.jpg) | Remove public workflows from Python client |

## Changelog 6.3

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Send collaborator emails asynchronously |
| ![](../.gitbook/assets/bug.jpg) | NLP bug fixes for non-text apps |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Consolidated input related status codes |
| ![](../.gitbook/assets/improvement.jpg) | Add frame.id to API as well as region.track\_id |
| ![](../.gitbook/assets/bug.jpg) | Granted select permission to clarifairead |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Added list annotations filter status |
| ![](../.gitbook/assets/improvement.jpg) | Added concept selection for tasks |
| ![](../.gitbook/assets/improvement.jpg) | Post/Patch annotations request now allow setting status |
| ![](../.gitbook/assets/improvement.jpg) | Changed task form options |
| ![](../.gitbook/assets/improvement.jpg) | Set annotation status to awaiting for review if the authorized user is not app owner |
| ![](../.gitbook/assets/improvement.jpg) | Return only input\_level annotation in input.data |
| ![](../.gitbook/assets/bug.jpg) | Drawing annotations: wrong embed model version id. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Eliminated error if no annotation to be deleted |
| ![](../.gitbook/assets/bug.jpg) | Create one annotation for each bbox |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Added support for adding and training on text in the platform |
| ![](../.gitbook/assets/new_feature.jpg) | Created a NLP mock prediction endpoint |
| ![](../.gitbook/assets/improvement.jpg) | Created test set to evaluate quick trained models or k-fold if no test search is specified |
| ![](../.gitbook/assets/improvement.jpg) | Added vocab\_id for demographics model concepts |
| ![](../.gitbook/assets/improvement.jpg) | Fixed sorting of A.G.E. concepts in golang for demographics model so we don't chop off sets of them |
| ![](../.gitbook/assets/improvement.jpg) | Deprecated Face from javascript Client |
| ![](../.gitbook/assets/improvement.jpg) | Deprecated Face from Java Client |
| ![](../.gitbook/assets/bug.jpg) | Confusion matrix predicted/true are swapped in evaluation results. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Explorer Image/Text Joint embedding |
| ![](../.gitbook/assets/bug.jpg) | Fixed selectEmbedModelVersionId in detection apps |
| ![](../.gitbook/assets/bug.jpg) | Fixed generalModel imports and optimized video click handlers with useCallback hooks |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Persisted the saved search used in train a model version |
| ![](../.gitbook/assets/bug.jpg) | Created log for annotation/search request/response |
| ![](../.gitbook/assets/bug.jpg) | Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Created new Single Image View and Image Tools |
| ![](../.gitbook/assets/new_feature.jpg) | Enabled Display Text Thumbnails in App Grid View and App Details View |
| ![](../.gitbook/assets/new_feature.jpg) | Text Thumbnails display in Portal/Search Bar disabled |
| ![](../.gitbook/assets/new_feature.jpg) | Enabled View Text Assets in Portal's Image View |
| ![](../.gitbook/assets/new_feature.jpg) | Added Text Inputs To Explorer Apps |
| ![](../.gitbook/assets/new_feature.jpg) | Imported new icons for Labeler Image Tools into the style guide |
| ![](../.gitbook/assets/improvement.jpg) | Added login tracking to analytics package in Portal |
| ![](../.gitbook/assets/improvement.jpg) | Allowed pasting into the add inputs text area and clear the text box after clicking submit |
| ![](../.gitbook/assets/bug.jpg) | Search bar not visible. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Removed all instances of worker\_id from Explorer |
| ![](../.gitbook/assets/bug.jpg) | Fixed popover left/right overflow |
| ![](../.gitbook/assets/bug.jpg) | Disabled all search by click handlers in Portal for Text Apps |
| ![](../.gitbook/assets/bug.jpg) | Click Search button icons on Thumbs not working for localized search. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Fixed details page header missing description |
| ![](../.gitbook/assets/bug.jpg) | Fixed demo font syntax |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Added a Range Slider to filter Workflow Predictions by Value |
| ![](../.gitbook/assets/improvement.jpg) | Updated Face workflow to include the detect faces as concepts for search |

## Changelog 6.2

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Updated Privacy Policy URL |
| ![](../.gitbook/assets/bug.jpg) | Fixed panic error in Signup |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Ensured collectors are deleted when apps are deleted |
| ![](../.gitbook/assets/bug.jpg) | View In Explorer button missing in app details. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Fixed failed to generate thumbnail |
| ![](../.gitbook/assets/bug.jpg) | Fixed app duplication error when getting worker |
| ![](../.gitbook/assets/bug.jpg) | Deleted collaborator should also mark application\_worker to deleted. Fixed |

### Inputs

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Inputs count stuck at &gt; 0 after delete all, with all inputs seemingly deleted |

### Label

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Task view UI for workers |
| ![](../.gitbook/assets/new_feature.jpg) | Create task manager page and task creation page |
| ![](../.gitbook/assets/new_feature.jpg) | New Icon for Task Manager/Task Viewer |
| ![](../.gitbook/assets/bug.jpg) | Fixed POST annotations call on frontend to use correct embed model |
| ![](../.gitbook/assets/bug.jpg) | Post annotations should include embed\_model\_version\_id. Fixed |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Added Apparel Detection to Demo App |
| ![](../.gitbook/assets/new_feature.jpg) | Created UI for creating knowledge graph concept relations relations |
| ![](../.gitbook/assets/new_feature.jpg) | Create annotation writer model to write annotations to DB |
| ![](../.gitbook/assets/improvement.jpg) | Pass and use test and train data queries to trainer |
| ![](../.gitbook/assets/improvement.jpg) | Added migration to upgrade old model\_type in DB |
| ![](../.gitbook/assets/improvement.jpg) | Depredated Face from Python client |
| ![](../.gitbook/assets/improvement.jpg) | Unified the TypeExt and Type fields in model object. |
| ![](../.gitbook/assets/improvement.jpg) | Deprecated facedetect\* model types. |
| ![](../.gitbook/assets/improvement.jpg) | Unified FaceEmbedModel and DetectEmbedModel |
| ![](../.gitbook/assets/improvement.jpg) | Converted face.Identity responses to concepts like other detection models to be consistent |
| ![](../.gitbook/assets/bug.jpg) | Fixed demo font syntax |
| ![](../.gitbook/assets/bug.jpg) | Video Timeline does not display on the demo app |
| ![](../.gitbook/assets/bug.jpg) | Fixed Range Slider Value/Text in Apparel Detection Demo |
| ![](../.gitbook/assets/bug.jpg) | Fixed demographics model to return embeddings and work with auto-annotate |
| ![](../.gitbook/assets/bug.jpg) | Adding collaborator model counter-intuitively requires ENTER in order to enable the submit button. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Validated that concept relation doesn't already exist on POST relations |
| ![](../.gitbook/assets/bug.jpg) | Prediction requests are being fired too frequently instead of using cache. Fixed |
| ![](../.gitbook/assets/bug.jpg) | postModelOutputs is not called for newly labeled assets without a manual refresh |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Return annotations posted by user in search results |
| ![](../.gitbook/assets/bug.jpg) | Search by region not working for face detection. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Make “save” search button internal only |
| ![](../.gitbook/assets/bug.jpg) | Saved Searches in Portal use the incorrect user ID |
| ![](../.gitbook/assets/bug.jpg) | Fix crop search from single image view for faces/detections |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | UI for collector crud |
| ![](../.gitbook/assets/improvement.jpg) | Deprecate Face from Portal |
| ![](../.gitbook/assets/improvement.jpg) | Improve tabs UI |
| ![](../.gitbook/assets/bug.jpg) | Video Predictions are failing in Portal |
| ![](../.gitbook/assets/bug.jpg) | Fixed broken font syntax |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Video detection workflow prediction support |
| ![](../.gitbook/assets/new_feature.jpg) | Public general v1.5 workflow |
| ![](../.gitbook/assets/bug.jpg) | Allow Patching to existing public workflow |
| ![](../.gitbook/assets/bug.jpg) | Can not train LOPQ if app base workflow is face. Fixed |

## Changelog 6.1

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Clients

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Python client |
| ![](../.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Java client |
| ![](../.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Javascript client |
| ![](../.gitbook/assets/improvement.jpg) | Remove Feedback endpoints from Portal/demo |
| ![](../.gitbook/assets/improvement.jpg) | Remove image.crop field from Python API client |
| ![](../.gitbook/assets/improvement.jpg) | Remove image.crop field from Java API client |
| ![](../.gitbook/assets/improvement.jpg) | Remove image.crop field from Javascript API client |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Added detection evaluation in platform |
| ![](../.gitbook/assets/new_feature.jpg) | Introduce concept mapping model that uses the knowledge graph relations, creating a path for users to eventually benefit from pool of networked data |
| ![](../.gitbook/assets/bug.jpg) | Fix a bug that caused the new face predictions to have a huge performance drop |
| ![](../.gitbook/assets/bug.jpg) | Train and eval worker didn't invalidate model related cache. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Fix bug in deleting a concept relation by ID |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Bulk labelling can now be done from Explorer mode grid view. |
| ![](../.gitbook/assets/improvement.jpg) | Show Check/X on custom detection model predictions in Portal |
| ![](../.gitbook/assets/improvement.jpg) | Allow multi concepts per bbox |
| ![](../.gitbook/assets/bug.jpg) | Negative tags not visible in Portal. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Remove extra round trip to storage in predict pathway |
| ![](../.gitbook/assets/improvement.jpg) | Remove the image.crop argument during predict and POST /inputs calls to simplify the API |
| ![](../.gitbook/assets/improvement.jpg) | Add region predictions from custom models to detections in videos |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Implement search by annotation.status in backend |
| ![](../.gitbook/assets/improvement.jpg) | Connect saved searches and annotation status |

## Changelog 6.0

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Remove country field from signup form, simplifying new customer signups |
| ![](../.gitbook/assets/bug.jpg) | Essential Plan User can't add collaborators. Fixed |

### API

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Introduce new [Python gRPC API client](https://docs.clarifai.com/api-guide/api-overview), enabling new features and performance enhancements across API |
| ![](../.gitbook/assets/new_feature.jpg) | Introduce new [Java gRPC API client](https://docs.clarifai.com/api-guide/api-overview), enabling new features and performance enhancements across API |
| ![](../.gitbook/assets/improvement.jpg) | Update API key type for "app\_specific" for app-specific keys to be more clear to users |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Allow Personal Access Tokens when calling /users/me \(GetUsers\) |
| ![](../.gitbook/assets/new_feature.jpg) | \[Frontend\] Enable "Copy Application" from collaborated apps, making it easy to duplicate and build upon existing applications |
| ![](../.gitbook/assets/bug.jpg) | Program to clean internal apps crashing. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Added the ability to accept b64 Gifs |
| ![](../.gitbook/assets/bug.jpg) | Functionality to upload pre-tagged images missing. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Images pre-tagged with concepts do not successfully upload into Clarifai UI On doing bulk uploads \(&gt;20-30 urls\). Fixed |
| ![](../.gitbook/assets/bug.jpg) | Bulk image upload issue. Fixed |
| ![](../.gitbook/assets/bug.jpg) | "Download Failed" error when uploading images. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Issue with post inputs key being a PAT in a collector. Fixed |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Skip aligning landmarks if landmark points are out of range to avoid errors and unexpected behavior |
| ![](../.gitbook/assets/bug.jpg) | Bounding Boxes and Cropped Regions aren't displaying on Videos with default runtime config. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Insert annotations and related data in batch to improve performance |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Evaluate new face embedding model workflow end to end for optimal performance |
| ![](../.gitbook/assets/improvement.jpg) | Validate that concept.app\_id shouldn't be set when creating/patching models |
| ![](../.gitbook/assets/improvement.jpg) | Add new predicate to knowledge graph for "relates\_to" to represent synonyms |
| ![](../.gitbook/assets/bug.jpg) | Model training lag. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Model has missing inputs. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Submitted models becoming stuck in queue. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Custom training models when uploaded images are not fully pre-processed. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Custom facial recognition bboxes do not correspond with detection boxes/ Custom facial recognition prediction interval for video is still 1000ms for apps supporting 100ms runtime config. Fixed |
| ![](../.gitbook/assets/bug.jpg) | frame\_info time off by a factor of 10 for general detection model. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Detection Models throw error at end of video due to invalid index lookup. Fixed |

### Workflow

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/bug.jpg) | Deleting a workflow should clear or update localStorage. Fixed |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Clean up app overflow UI, improving user experience |
| ![](../.gitbook/assets/improvement.jpg) | Improve Error boundary screen, improving user experience |
| ![](../.gitbook/assets/improvement.jpg) | Add sentry error Id to Error Screen |
| ![](../.gitbook/assets/bug.jpg) | Images not loading. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Label and prediction on the right side under Custom Model Predictions section no longer shows up automatically. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Provide a way for user.metadata to be updated from portal when there are failing apps stuck in there. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Predictions for a detection model don't show properly in portal. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Custom facial recognition Predict Boxes not displaying. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Adding inputs in explorer redirects to explorer view with flashing images. Fixed |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Run prediction by ID in small batch, improving performance |
| ![](../.gitbook/assets/bug.jpg) | Custom model predictions not displaying. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Custom model detections not displaying. Fixed |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Add file upload input button to explorer search bar, simplifying the UX for file uploads |
| ![](../.gitbook/assets/new_feature.jpg) | Filter custom facial recognition bboxes using a sliding bar, adding easy thresholding to custom facial recognition models |
| ![](../.gitbook/assets/improvement.jpg) | Search Bar allows file upload |
| ![](../.gitbook/assets/improvement.jpg) | Remove Explorer App Overflow Menu for improved UX |

## Changelog 5.11

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Create a UI for personal access tokens making it easier for users to access their own apps and any apps where they have been added as collaborators |
| ![](../.gitbook/assets/new_feature.jpg) | Updated /keys to work with PATs so that app-specific keys can be created programmatically. |
| ![](../.gitbook/assets/bug.jpg) | Login \(user/PW\) has no rate limit/max attempts. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Remove all instances of worker\_id from explorer |
| ![](../.gitbook/assets/bug.jpg) | When email link to verify my email address clicked, still see "verify your email" banner. Fixed |
| ![](../.gitbook/assets/bug.jpg) ![](../.gitbook/assets/enterprise.jpg) | API services do not function once Queue goes down and comes back up. Fixed. This makes on premise deployments more resilient to power failures. |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Add apps and keys scopes so they can be created with personal access tokens |
| ![](../.gitbook/assets/improvement.jpg) ![](../.gitbook/assets/enterprise.jpg) | Copy app count and last\_inputs added in app duplication |
| ![](../.gitbook/assets/bug.jpg) | Fixed demo font syntax |
| ![](../.gitbook/assets/bug.jpg) | Fixed details page header missing description |
| ![](../.gitbook/assets/bug.jpg) | Added favicon for Portal |
| ![](../.gitbook/assets/bug.jpg) | Unable to copy an app that has been shared via Collaborators. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Setting useCustomConfig isn't checked at login. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Collaboration apps have race condition where wrong user id is used |
| ![](../.gitbook/assets/bug.jpg) | Stopped loading of collaborations for search demo/logged-out users |
| ![](../.gitbook/assets/bug.jpg) | Return “All” scopes when listing available scopes so that you have that option when creating new keys. |
| ![](../.gitbook/assets/bug.jpg) | Collaborators can not see workers. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Missing `Apps_Get` scope in session token auth caused creation of keys to fail temporarily. Fixed |
| ![](../.gitbook/assets/bug.jpg) | List of missing scopes is not correct in error messages. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Optimize video detection frame rate on Front end |
| ![](../.gitbook/assets/improvement.jpg) | Improve JSON serialization performance in our servers by using an optimized third party library |
| ![](../.gitbook/assets/improvement.jpg) | Able to overwrite default max conn for Citus |
| ![](../.gitbook/assets/improvement.jpg) | Rewrite input counting in the API to be more scalable and robust |
| ![](../.gitbook/assets/bug.jpg) | Allow RegionInfo from SpireDetectEmbedResponse to contain Point when saving to DB |
| ![](../.gitbook/assets/bug.jpg) | Unable to upload same file\(s\) through browse files. Fixed |
| ![](../.gitbook/assets/bug.jpg) | ffmpeg can produce no frames for very short videos |
| ![](../.gitbook/assets/bug.jpg) | Add Inputs/View Explorer does not display in new app anymore. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Clicking video thumbs in detail view does not reload a video. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Keyboard navigation in image details view highlights incorrect thumb |
| ![](../.gitbook/assets/bug.jpg) | No Prompt when uploading an image to Explorer through URL. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Properly return error if `AddAssets` failed to insert into database |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Remove classification/detection toggle in image details view |
| ![](../.gitbook/assets/bug.jpg) | Improved adding negatives to regions |
| ![](../.gitbook/assets/bug.jpg) | Create one annotation for each bbox |
| ![](../.gitbook/assets/bug.jpg) | Log capability added for annotation/search request/response |
| ![](../.gitbook/assets/bug.jpg) | Eliminated error if no annotation to be deleted |
| ![](../.gitbook/assets/bug.jpg) | Last concept used for bounding boxes is retained between apps. Fixed |
| ![](../.gitbook/assets/bug.jpg) | The Add Positives / Add Negatives buttons on a Concept details view breaks portal |
| ![](../.gitbook/assets/bug.jpg) | Custom facial recognition bboxes on grid view do not correlate. Fixed |

### Model

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Ability to keep concepts sorted by alpha in Portal |
| ![](../.gitbook/assets/new_feature.jpg) | Implement image crop model to make it possible to work in subregions of an image |
| ![](../.gitbook/assets/new_feature.jpg) | Implement random sample model type, adding to fixed function feature set |
| ![](../.gitbook/assets/improvement.jpg) | Update training templates to have more straightforward names and more friendly defaults |
| ![](../.gitbook/assets/improvement.jpg) | Fix the WorkflowInput field name in proto to workflow\_input |
| ![](../.gitbook/assets/improvement.jpg) | Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models |
| ![](../.gitbook/assets/bug.jpg) | Confusion matrix predicted/true are swapped in evaluation results. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Fixed generalModel imports and optimize video click handlers with useCallback hooks |
| ![](../.gitbook/assets/bug.jpg) | Fix for selectEmbedModelVersionId in detection apps |
| ![](../.gitbook/assets/bug.jpg) | Drawing annotations: wrong embed model version id |
| ![](../.gitbook/assets/bug.jpg) | Made custom training evaluations for large models stable. |
| ![](../.gitbook/assets/bug.jpg) | Training progress is saved too frequently, causing very slow training |
| ![](../.gitbook/assets/bug.jpg) | Return friendlier errors for incorrect parameters passed to templates |
| ![](../.gitbook/assets/bug.jpg) | Fixed a bug in tracing setup for custom trainer and evaluator |
| ![](../.gitbook/assets/bug.jpg) | Some models were operating slowly because of lack of resources. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Training System failed to train some layers. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Prevent users from evaluating models that are not trainable |
| ![](../.gitbook/assets/bug.jpg) | Fixed node ID validation logic in Bug in workflows |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Add colors to differentiate region results |
| ![](../.gitbook/assets/bug.jpg) | Cannot view workflow results in a face app. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Video spire tests are not running correctly. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Video processing fails with 'caseids' error. fixed |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Add click to search metadata attributes in image details sidebar |
| ![](../.gitbook/assets/new_feature.jpg) | Implement visual search in another app as a model type you can add to a workflow |
| ![](../.gitbook/assets/bug.jpg) | Search bar missing in some cases. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Click Search button icons on Thumbs not working for localized search. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Disable all search by click handlers in Portal for Text Apps |
| ![](../.gitbook/assets/bug.jpg) | Disable "hide all positively labeled" inputs button for NLP until search works |
| ![](../.gitbook/assets/bug.jpg) | Scroll active thumb into view in image details carousel |
| ![](../.gitbook/assets/bug.jpg) | Render Video Assets in Search Bar |
| ![](../.gitbook/assets/bug.jpg) | Editing geo/json search items no longer work after adding the search bar tooltip. Fixed |
| ![](../.gitbook/assets/bug.jpg) | TypeError: Cannot read 'get' of undefined when clicking image thumbnails in Explorer search bar. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Explorer Visibility in small resolution screen improved |

## Changelog 5.10

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature.jpg) | ![](../.gitbook/assets/improvement.jpg) | ![](../.gitbook/assets/bug.jpg) | ![](../.gitbook/assets/enterprise.jpg) |

### Accounts

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Create delete email endpoints in v2 to finally get off old internal endpoints to streamline operations |
| ![](../.gitbook/assets/new_feature.jpg) | Create Patch, Delete, Get CreditCards endpoint in v2 APIs to finally get off old internal endpoints to streamline operations |
| ![](../.gitbook/assets/improvement.jpg) | Improved billing for collaborators |
| ![](../.gitbook/assets/bug.jpg) | PostVerifyEmail error causing some issues not being able to verify their email addresses upon sign-up. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Fixed flaky email verification integration test to provide more stability to sign-up process |
| ![](../.gitbook/assets/bug.jpg) | Fixed a link to a non-public version of our API used for development purposes which led to a lot of login issues for users who landed there |

### Applications

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Created display for scopes on collaborator invitations, allowing users to easily understand and control the scope of access allowed for app collaborators |
| ![](../.gitbook/assets/new_feature.jpg) | Introduced Collaborators and Collaborations endpoints in API and UIs in Portal |
| ![](../.gitbook/assets/new_feature.jpg) | Add ability to upload inputs from App Details screen in Portal |
| ![](../.gitbook/assets/improvement.jpg) | Created collaboration tab in Portal, making it easy to add collaborators to apps |
| ![](../.gitbook/assets/improvement.jpg) | Created display to show the user who invited you to collaborate on an app |
| ![](../.gitbook/assets/improvement.jpg) | Update email phrases for collaborator invitations. After successful sign-up, the user is now redirected to the app's dashboard in Portal |
| ![](../.gitbook/assets/bug.jpg) | Fixed issue with concept counts in some apps |
| ![](../.gitbook/assets/bug.jpg) | Clicking pencil icon to edit an API Key in Portal crashed apps. Fixed |

### Data Management

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | PATCH /inputs needs to check status of asset before patching |
| ![](../.gitbook/assets/improvement.jpg) | Removed sync DELETE /inputs after runtime config tested |
| ![](../.gitbook/assets/improvement.jpg) | Changed POST /inputs to be async always to simplify processing of workflows after API client tests updated |
| ![](../.gitbook/assets/improvement.jpg) | Added pagination to clusters making for easier data management |
| ![](../.gitbook/assets/bug.jpg) | Sporadic inability to delete any inputs via Portal or in bulk via the API |
| ![](../.gitbook/assets/bug.jpg) | Numerous third party security fixes under the hood during ongoing upgrades |
| ![](../.gitbook/assets/bug.jpg) | Fix 40012 status caused by parallel deletes and adds having a race condition |
| ![](../.gitbook/assets/bug.jpg) | Update status\_changed\_at when deleting inputs so we can better track changes |
| ![](../.gitbook/assets/bug.jpg) | Cache the input counts so that apps can display them in Portal efficiently |
| ![](../.gitbook/assets/bug.jpg) | Handle killing URL downloading if it is processing for more than 60s. This will make URL processing much more reliable |
| ![](../.gitbook/assets/bug.jpg) | Return an error if a user sends YouTube video URL as that is not a valid URL to a video we can download |
| ![](../.gitbook/assets/bug.jpg) | Prevent PostInputs from creating inputs with a user-provided Input.ID that contains a colon |
| ![](../.gitbook/assets/bug.jpg) | Video calls failed if URLs contain parameters after the file type. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Failed to resolve DNS MX record in URL down-loader which effected some downloads. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Investigate why some re-hosted s3 links are no longer working |
| ![](../.gitbook/assets/bug.jpg) | Getting input counts was broken in some apps, reporting zero, which caused Portal to add an input view to display always |
| ![](../.gitbook/assets/bug.jpg) | Debug UnicodeErrors in URL downloading to fix URLs with Unicode characters |
| ![](../.gitbook/assets/bug.jpg) | Fix the poor handling of video too large error message |
| ![](../.gitbook/assets/bug.jpg) | Unable to batch delete inputs from time to time has been fixed |
| ![](../.gitbook/assets/bug.jpg) | Media processor video handling was having errors with decoding some videos |
| ![](../.gitbook/assets/bug.jpg) | Delete Image Button doesn't work in some scenarios |
| ![](../.gitbook/assets/bug.jpg) | Fixed support for webp image format so it is available again |

### Annotate

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Deploy General Detection Beta Model to recognize multiple objects with bounding boxes. |
| ![](../.gitbook/assets/new_feature.jpg) | Deployed new face detector for improved face detection performance over images and video |
| ![](../.gitbook/assets/new_feature.jpg) | Created custom training enhancements that handle negatives better for improved model performance |
| ![](../.gitbook/assets/new_feature.jpg) | Created evaluation metrics for custom facial recognition in backend for improved facial recognition performance |
| ![](../.gitbook/assets/improvement.jpg) | Topological sort for workflows for scheduling a sequence based on dependencies |
| ![](../.gitbook/assets/improvement.jpg) | Cleaned up duplicate models in workflow model list |
| ![](../.gitbook/assets/improvement.jpg) | Deployed clarifai/main general v1.5 in concept model |
| ![](../.gitbook/assets/improvement.jpg) | Create Pixel Training Hyperparameter Help Guide |
| ![](../.gitbook/assets/improvement.jpg) | Improved accuracy of annotation counts, improving the user experience when annotating inputs |
| ![](../.gitbook/assets/bug.jpg) | If an image is tagged with a concept that is not in the model, training fails due to KeyError, this is fixed |
| ![](../.gitbook/assets/bug.jpg) | Fix detection labeling bug where previous images image ratio is used which would cause display issues |
| ![](../.gitbook/assets/bug.jpg) | We have updated Portal to scale to a large number of concepts with much lower resource usage |
| ![](../.gitbook/assets/bug.jpg) | Investigate face bounding box probabilities consistency to improve user experience |
| ![](../.gitbook/assets/bug.jpg) | Bounding box creation canvas in Portal was breaking on resize of the window |
| ![](../.gitbook/assets/bug.jpg) | Model |
| ![](../.gitbook/assets/bug.jpg) | Cleaned up duplicate models in the workflow model list, so that you no longer see two General models |
| ![](../.gitbook/assets/bug.jpg) | Unintended behavior for private model version IDs for certain customers has been fixed |
| ![](../.gitbook/assets/bug.jpg) | Models referencing deleted backends should be marked as deleted |
| ![](../.gitbook/assets/bug.jpg) | The latest version of our general model wasn't always default, now it is |
| ![](../.gitbook/assets/bug.jpg) | Fixed a bug with face recognition evaluations. |
| ![](../.gitbook/assets/bug.jpg) | Deleted Concepts Persisted in face recognition models. Not anymore! |
| ![](../.gitbook/assets/bug.jpg) | Inability to see whether a large model is training and making progress, or hung has been addressed to better support our customers |
| ![](../.gitbook/assets/bug.jpg) | Model won't train in some apps with no positive examples issue has been resolved |
| ![](../.gitbook/assets/bug.jpg) | Fixed issues with color models failing for a short period of time |
| ![](../.gitbook/assets/bug.jpg) | Fixed list of models available to workflows to only show a single General model |

### Predict

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/new_feature.jpg) | Return custom detection evaluations through the GO API |
| ![](../.gitbook/assets/improvement.jpg) | Improved cluster page performance |
| ![](../.gitbook/assets/bug.jpg) | Investigate health checks killing a prediction backend service, which could affect some predictions in the API |
| ![](../.gitbook/assets/bug.jpg) | Workflow predict sometimes was failing with 98012 status code. Many fixes here should reduce that |
| ![](../.gitbook/assets/bug.jpg) | Workflow Predict called the wrong model sometimes. Not any more! |
| ![](../.gitbook/assets/bug.jpg) | Video playback out of sync with detections in our demos |
| ![](../.gitbook/assets/bug.jpg) | Fixed issues with regions predicted on inputs would be carried over between inputs in Portal |
| ![](../.gitbook/assets/bug.jpg) | Fixed the flaky face recognition tests to ensure stability of our face recognition product |
| ![](../.gitbook/assets/bug.jpg) | Face Detection backends were running out of memory for some predictions, this has been resolved |
| ![](../.gitbook/assets/bug.jpg) | Return more descriptive error msg for post metric endpoint |

### Search

| Status | Details |
| :--- | :--- |
| ![](../.gitbook/assets/improvement.jpg) | Added helper text/suggestions to improve Portal user experience |
| ![](../.gitbook/assets/improvement.jpg) | Header Search return app\_owner's user info in collaboration endpoints |
| ![](../.gitbook/assets/bug.jpg) | Explorer Search Bar - Clicking the green/red circle icons didn't reliably detect click, now it does! |
| ![](../.gitbook/assets/bug.jpg) | Portal not showing the correct number of results in concept search. Fixed. |
| ![](../.gitbook/assets/bug.jpg) | Left/right arrows in single image view don't switch between images with regions. Fixed |
| ![](../.gitbook/assets/bug.jpg) | Fixed carousel thumbnail clicks wiping query params / trigger new search |
