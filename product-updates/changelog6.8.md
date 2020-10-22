# Changelog

## Changelog 6.8

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |


### Labeler
|Status     |Details                                                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Use single LabelerToolbar for all labelers, make shared using Context                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Remove all computation from components, move to selectors for perf                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Fixed carousel scroll behavior                                                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Added button to add collaborator when adding reviewer                                                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Post incorrect bounding box. Fixed                                                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Refreshing in Labeler Crashes Portal. Fixed                                                                                                    |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Add Grid Review UI to Review Page                                                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Panning while playing a video renders rects incorrectly. Fixed                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Navigation from the task creation page if task creation fails. Fixed                                                                           |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Konva: Image filters                                                                                                                           |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Konva: Drawing rects                                                                                                                           |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Konva: Drawing polygons                                                                                                                        |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Smaller shapes should supersede zIndex values if they are engulfed by larger ones                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Region selectors inefficient and running on each call, bypassing reselect memoization. Fixed                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |v2 interpolation: app crash on reload. Fixed                                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |CSS issue causing VideoControls to be inaccessible to mouse. Fixed                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |v2 video: no thumbails in carousel. Fixed                                                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |v2 keyboard hint showing weird characters. Fixed                                                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Selected Shape becomes unselected on playing video (make selection persist across track). Fixed                                                |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Ron is unable to create a task with AI assist in prod. Fixed                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Write and Preview Tab style. Fixed                                                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Task create form shows name as "undefined undefined" when a user has not filled in profile details. Fixed                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Input source that was selected should be shown when task selected. Fixed                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Create order fails if I'm a clarifai user. Fixed                                                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Layout in order admin form has some issues. Fixed                                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Multiple errors when creating bounding boxes. Fixed                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Cannot see annotations from a collaborator in v2 linear review. Fixed                                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Keyboard shortcuts dont work in labeler v2. Fixed                                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |When a worker opens labeler, display the instructions by default. Fixed                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Non-clarifai users should have v2 only, clarifai accounts should have v2 by default with option to switch to v1. Fixed                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Cursor should change to a crosshair when drawing a bounding box. Fixed                                                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Cursor should change to an open hand when panning is selected and closed hand when grabbing/panning. Fixed                                     |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Reviewer cannot see annotations by collaborators. Fixed                                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |If the reviewer is NOT the app owner, clicking review takes them to explorer. Fixed                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Tooltip for labeler nav icon should be uppercase. Fixed                                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |As a worker, if I return to Labeler, I should be able to continue from where I was previously. Fixed                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |LaaS orders can't assign inputs which block the workers. Fixed                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Community users should have LaaS option grayed out with an explanation. Fixed                                                                  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Make the "order admin view" text larger and prominent as a section header. Fixed                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |In labeler UI (worker), submit button should say "Submit Input for Review" to make it clear what the button does. Fixed                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |[P3] In all tasks view, only app owner should see edit/delete icons                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Carousel blocks input visibility (not just video controls). Fixed                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |In labeler UI carousel, show a check for any input that was submitted, and gray it out slightly. Fixed                                         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Separate annotation sagas + standardise request batching code (for v2 store)                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |When creating a task in an app w/ no concepts, “Select all concepts” should not be checked by default. There are no concepts created yet. Fixed|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Update task status on task list                                                                                                                |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Deleting an annotation in reviewer deletes all annotations. Fixed                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Too many scrollbars in sidebar. Fixed                                                                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Partition worker strategy Error. Fixed                                                                                                         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Integrate feature gating with LaaS.                                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Panning state not in sync with drawing/moving. Fixed                                                                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Have to click the + button 2 times to make it work. Fixed                                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Dragging mouse outside of the canvas while drawing leaves the drawing in inconsistent state. Fixed                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Delete icon on v2 sidebar deletes all annotations on the input. Fixed                                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Resizing shapes near the right edge of the frame causes weird resize behavior. Fixed                                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Entering date manually in Order control modal fixed                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Carousel Thumbnail animation not working; images looking weird in aspect-ratio due to incorrect CSS                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Task Form console errors. Fixed                                                                                                                |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Add video icon to carousel for video inputs. Fixed                                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |When we use keyboard shortcuts to activate a concept for bounding boxes, show visual feedback                                                  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Cannot read property '0' of undefined. Fixed                                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Review tab shows new tasks that have no work ready to review. Fixed                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Video Interpolation doesn't work. Fixed                                                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Labeler UI sees last input even after submitting everything. Fixed                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Box disappears for a second while drawing on video. Fixed                                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Disable worker input when editing a task. Fixed                                                                                                |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Input data stops being fetched if labeler is exited once and revisited. Fixed                                                                  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Make v2 annotations state flatter. Fixed                                                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Darker colors poorly visible in sidebar region items. Fixed                                                                                    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Mysterious Phantom Boxes Appearing. Fixed                                                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Video not loading. Fixed                                                                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Multiple boxes appearing. Fixed                                                                                                                |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Misaligned Boxes. Fixed                                                                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Bounding Boxes and Concepts inconsistent during video playback {Usability}. Fixed                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Change Labeler to use getHostedAssetUrl. Fixed                                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Enable drawing even if annotations haven't loaded. Fixed                                                                                       |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Use new feature flags at frontend & Labeler for all                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Can't add Iris workers to LaaS order. Fixed                                                                                                    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Instructions shouldn't be false while editing. Fixed                                                                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Labelers/Reviewers should not see "--" when the task does not have AI Assist enabled. Fixed                                                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Carousel should show some visual feedback when an input has been rejected                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Carousel flickers and re-renders images when submitting annotations. Fixed                                                                     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add loading indicator to labeler view when fetching data                                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Moving a polygon to the edge of the input causes it to patch outside the allowed range. Fixed                                                  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Wrong worker_per_input field. Fixed                                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Hide other regions during interpolation. Fixed                                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Concepts Tasks: Cannot read property 'id' of undefined. Fixed                                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Carousel should show some visual feedback when an input has been skipped                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Polygon points are sometimes too small to click. fixed                                                                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Send embed model id for image annotations. Fixed                                                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Skipping/Submitting annotations causes unnecessary rerenders of the entire carousel (all thumbs). Fixed                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Get an error when submitting an input in a classification task. Fixed                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Improve concept creation process for new apps that you want to label                                                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Labeler Reviewer No longer renders assets. Fixed                                                                                               |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Add "Orders" section to task list admin view                                                                                                   |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Add checkbox to task creation for LaaS Orders                                                                                                  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |List name field instead of id fields in task lists. Fixed                                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Set task error code and error description if task annotations pipeline fails                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Label task submit error: Malformed or invalid request. Fixed                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Label video - playback control issue fixed                                                                                                     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Hovering annotations in sidebar of Labeler, should highlight the region in the image.                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Jumping Boxes during video interpolation. Fixed                                                                                                |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Polygon rendering in Labeler v2                                                                                                                |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Virtual scrolling input carousel                                                                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |LabelOrders not fetched when refresh at /labeler page. Fixed                                                                                   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Lock Edit feature for LaasOrders other than pending orders                                                                                     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Account for system states (inputId, taskID) between heartbeats and account for them in canvas interaction manager                              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Cleanup labelerv2 state on unmount                                                                                                             |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|V2 Rendering Video Regions                                                                                                                     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|V2 Video Interpolation                                                                                                                         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Labeler saga to process all remaining actions on input change & before user exits                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Sometimes, bounding box values on Transformer go in the negative, Fixed                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Task Form: Convert fps -> sample_ms                                                                                                            |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Let Clarifai user permissions for status & ETA change                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Implement clarifai user journey for LaaS                                                                                                       |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Seperate LaaS order tasks from simple labeling tasks.                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Edit task functionality for clarifai user                                                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Include Order Task in "assigned to me" and "for review"                                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Regions disappeared in sidebar. Fixed                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Implement a way for Clarifai users to review Order tasks                                                                                       |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Video Rendering Sync with FPS                                                                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Reconcile V1 and V2 video frame index                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Convert incorrectly created fps to sampleMs                                                                                                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Better signposting of task instruction preview panel                                                                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Reset Button doesn't work. Fixed                                                                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Can't go back from Labeler UI. Fixed                                                                                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Collaborators can not add collaborators. Fixed                                                                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Labeler: Add both index and time to all video annotations                                                                                      |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Implement polygon drawing                                                                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Toolbar Next & Previous button issue fixed                                                                                                     |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Worker filters don't work in review grid sidebar. Fixed                                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Fixed styling/layout of progress bar in the grid review page                                                                                   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add "select all" link next to each concept heading in the grid                                                                                 |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Integrate order task with current implementation for reviewer and worker                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Modify Labelerv2 sagas to be compatible with listening to polygon events                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Instructions editor should not show toolbar toggle, when in preview mode. Fixed                                                                |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Worker strategy should be included while adding workers. Fixed                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Task creation form concept field should correctly handle paginated response. Fixed                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Partition worker strategy should only be selectable if you have more than 1 worker. Fixed                                                      |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Labeler v2 submit functionality                                                                                                                |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |GridReview: app crash due to code for getting reviewer name. Fixed                                                                             |



### API
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Patch annotation req failed. Fixed                                                   |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Allow any type of task when the app default workflow is empty workflow               |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|LaaS billing                                                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Undo the delete of cvat persistent volumes                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Copier failed in workflow prediction and causing 99009. Fixed                        |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Make gRPC C# client                                                                  |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Make gRPC PHP client                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Feedback for malinformend CSV formats                                                |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Make PostKeys and PatchKeys support apps->user_id set to "me"                        |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Add automated testing of documentation code examples                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|change to getHostedAssetUrl to support returning both video thumbnails and video urls|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Prepare clients for the secure gRPC channel                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Update the gRPC copying code with C#, PHP                                            |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Use sendgrid template for email                                                      |


### Model
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Add AWS Lambda to model mode                                                         |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Add AWS Lambda model type to API                                                     |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Put Fairface model in production                                                     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Append landmark and pose annotations to Fairface dataset                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Fix empty status response                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Miscellaneous Fixes on Object Counter and KNN                                        |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Allow empty statusCallbackURL and entityStatusCallbackURL                            |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Smart Reply                                                                          |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Remove isInternalUser Selector from Text Features                                    |


### Workflow
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Editing the Empty workflow throws an error in portal. Fixed                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add Filtering By Concepts for Text workflows                                         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add supress_output field option to each workflow node in create workflow view        |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add workflows tab to model gallery                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Allow reindexing to different workflow without having a shared workflow node (with the old one)|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |No response when "Update workflow" button is pressed. Fixed                          |


### Portal
|Status     |Details                                                                              |
|-----------|-------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Refactor Sidebar ✅/❌ functionality to sagas                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Combine Tool components                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Cannot add card. Something went wrong. Fixed                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |DOMEX face app using face detect. Clicking on any image causes portal to crash. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |App in staging, crashing when using pause/play with video. Fixed                     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Improve algorithm for grouping annotations and predictions in explorer.              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |N "Predicted Bounding Boxes" toggle button only works after clicking twice           |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Show track ID for videos in explorer                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Use ModelType to validate args and persist default values with model versions.       |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Update create workflows page design                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add sortable columns when in list view of model mode. Fixed                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add pagination to the list of collaborations on app list page of Portal.             |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Adopt same tabs everywhere in portal                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Display user_id in user's profile page of portal.                                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Use fully qualified urls throughout portal                                           |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Expose the delete button in explorer single input view                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Adding new concepts to classification apps disappear from Single Image View until refresh. Fixed|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Fix CSS styling of Text Assets for Single Image View                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Image terminology in eval page                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Empty workflow breaks explorer workflow dropdown. Fixed                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Fix create model range selector min/max values                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Model gallery in model mode fails when you click on any concept model with a concept not found message. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Classification Prediction Scores still disappear for previously created apps. Fixed  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Disable "Train" button on pre-trained models                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Video times offset by 50ms                                                           |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Detection Tab of Image Details Sidebar does not always display in Face apps.  Sometimes it shows classification equivalent. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Model details page crashes while displaying concepts. Fixed                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Video thumbnails not displaying in search results. Fixed                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Listing collaborators models in collector view doesn't work. Fixed                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Fix API error while listing collaborators' models in collectors UI. Fixed            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Remove unnecessary field from model details page. Fixed                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Slider for Explorer prediction confidence doesn't apply to all the workflow nodes. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Sending embed_model_version_id on all model types but that's not valid. Fixed        |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Memoize sorted detection annotations and custom model predictions to prevent UI lag  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Modify the way users navigate to the model details page                              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Fix collector mode to filter by user, then app, then models, then model versions.    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)       |Image carousel does not scroll to the currently selected text input being viewed     |
