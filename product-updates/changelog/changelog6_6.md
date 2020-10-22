# Changelog

## Changelog 6.6

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |


### API
|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Integrate Python functions service with API|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|List available model types through API     |

### Model
|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fix video error from new face cluster model in staging env|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|21312 Ground truth data caseids must be nonempty and unique. Fixed|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Update deep training to list the ModelTypes|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Move model_metadata to better place in protos. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Generalize the domex-visual-searcher model type|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|List available model types from backend services that provide models.

### Portal

|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fixed bug in submitting finished Labeler Task|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Select all concepts checkbox can be de-synced from actual concepts badges. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Disable Create Task button if not app owner|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Search by task_id returns incorrect data   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Removed model creation from concept creation action in portal|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Video scrubber cannot be moved. Fixed      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fixed ability to delete interpolation tracks (you can only delete frames at this time).|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Worker ids used instead of names in report overview in stats view. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Y-axis on labels created stats page is wrong. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|In task creation, adding concepts should be simple to click all the options right away. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Toggling concept visibility doesn't affect previously hidden child region. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Leftover                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|If reviewer is not a collaborator, UI sends empty reviewer id back instead of raising error. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Bounding box disappears on resizing. Fixed |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|While adjusting bounding box, it creates an additional bounding box over no object. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Using Play button brings up "Oops" page. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Error on opening Video Labeler. Fixed      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Labeler sidebar interaction bugs and unresponsiveness (due to lack of optimistic UI). Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Newly drawn object disappears from canvas after drawing, and reappears after API response. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Infinite loading in Labeler Mode for app without any inputs. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Use name field for tasks in Labeler admin. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Clicking labeler icon crashes. Fixed       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Moving bounding box around repeatedly creates a race condition, shows error notification and duplicate box. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Explorer inputs stale state. Fixed         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Diagnose issues affecting overall hanging/speed/performance of Labeler|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Carousel thumbnails not showing up in Labeler. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Not able to create overlapping bounding boxes. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|When user adds mass metadata in Explorer, the UI says success but metadata does not persist. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Create annotations while creating task. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Labeler board showing wrong task type. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Polygon annotations break Explorer. Fixed  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Concept autocomplete in Labeler task creation is showing clarifai/main concepts. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Should not be allowed to create a task with no concepts if my app has no concepts. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fixed image tools state                    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Restricted tasks to only the assigned users|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Add validation to TaskForm’s concept field |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Removed all instances of worker_id from Explorer|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Create one annotation for each bbox        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|98011 panic on ListTasks. Fixed            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|App names no longer display in Explorer. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Empty Annotations are not displaying after drawing a new bounding box until after refreshing the page. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Drawing a new bounding box in Explorer after previously labeling a region display an error. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Video search results do not play at the most relevant video time. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Change text upload UI to support moderation workflow|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Change object key lookup in boundingBoxContainer to use lodash/get|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Submitting Task for Review break Portal. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Labeling a region on an asset with multiple detected regions will put the child annotation in the wrong group in Explorer's sidebar. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|ConvertToBoundingBoxRegion function breaks Explorer when annotation information has not loaded at time of render. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Video Frame Annotating in Explorer throws errors. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|When drawing a new bounding box, Base64 string for video annotations shows the wrong regions. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fixe 10MB issue with video uploads         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Detection Regions and Indexes are thrown off on video assets. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Video Search Results still on showing Inputs. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|DetailsPageHeader adds 2.25rem margin to the DetailsPageBody. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Video Interpolation in Labeler breaks dev. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Redux is no longer calculating the sample_ms rate, preventing bounding boxes from rendering. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fixed video pause error when navigating between videos|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|ImagePile in Labeler Task View does not display image thumbs due to extraneous object nesting. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Remove warning error from console for immutable passed in props to SearchGrid.js|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Post annotation to detection region should use region id in portal. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Delete app button in app details takes you to blank page. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Incorrect bbox/label numbers displayed in image. Fixed|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Multiple video thumbs selected in search results when selecting one thumb. Fixed|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Improve Labeler mode window resizing.      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|W and E hotkeys for image labelling to go left/right. |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Polygon annotations break Explorer. Fixed. |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Polygons regions don’t appear when panning and zooming. Fixed. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Allow users to create concepts on task create view.|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fixed task list item count query.          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Utilising new task endpoints to Create tasks and integrate to show tasks in Portal.|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|LabelerPage refresh error. Fixed.          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Should not be allowed to create a task with no concepts if my app has no concepts. Fixed.|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Unknown page Error. Complete interpolation of an object doesn't show bbox. Complete tracking of a box will disappear from the video. Fixed.|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Fixed carousel padding.                    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Labeler board showing wrong task type. Fixed.|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Integrate worker/reviewer side of Labeler. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add 'name' field to new Tasks.             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Create annotations while creating task.    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Carousel thumbnails not showing up in Labeler. Fixed.|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|No image clearing/loading indicator in Labeler. Fixed.|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Use name field for tasks in Labeler administration.|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Bulk labeling value does not update in store upon labeling. Fixed.|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Record time per annotation and per input to /stats/values in Labeler mode of Portal. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Query and display stats across workers per task for time and count of annotations. |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Concept autocomplete in Labeler task creation is showing clarifai/main concepts. Fixed.|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Implement polygon task type in Labeler.    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Applying filters in Portal breaks bulk labeling / unlabeling. Fixed.|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|Unable to bulk-label annotations. Fixed.   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Change submit to "Complete Task" in Labeler page and add progress bar as it's working.|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Allow Patching region annotations in Labeler mode. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add AI assist thresholding.                |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add ability to set annotation_info in the annotation writer|
| ![](../.gitbook/assets/bug%20%28248%29.jpg)|`annotation_info` should be a valid JSON in Model Mode. Fixed.|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Upgrade gulp and node to latest version for testing-library support|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Write PropType declarations for componens/ConceptListTable|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Enable collapse behavior in sidebar concepts|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Create atomic reusable  sidebar components |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Integrate React Testing Library            |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Konva: Image centering, zooming, panning   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Move toolbar logic to react context        |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Refactor TaskForm related thunks to sagas  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|[Rearch]Scaffold Labeler Redux in a new nested state slice & Implement Sagas|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|[P2] Task id is used in dropdown of stats tasks rather than task.name|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|[P0]Show taskId at task list               |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Move region visibility state to its own React Context|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Get sidebar list data directly from redux  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|[P1] Don't hide task form if error occurs  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Remove delay of annotation request         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Remove animation for showing concepts on right side|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Perf: only fetch input predictions/annotations if user stays on image, not while navigating|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Get Labeler internal features ready for internal users|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Offload annotation creation to backend     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|allow reviewers update annotations         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|No image clearing/loading indicator in Labeler|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Controls for resizing bounding boxes need to be more visible|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Fabric rendering to be real-time; sync from API in background|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|make tasks endpoint public                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|list task by worker id/reviewer id         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add 'name' field to new Tasks              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Integrate worker/reviewer side of labeller |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Integrate and Implement task deletion using new endpoints|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Utilising new task endpoints to Create tasks and integrate to show tasks at portal|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Integrate and utilise new CRUD endpoints in portal|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Allow users to create concepts on task create view|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add empty CRUD endpoints for tasks         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Make polygons a separate task type         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add AI assist thresholding                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|W and E hotkeys for image labelling to go left/right. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Improve labeler mode window resizing.      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Allow Patching region annotations in labeler mode. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|crank up internal message size to handle larger videos with more outputs|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Introduce stats collection APIs for worker stats. |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Implement /tasks CRUD in API.              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add frame.id to API as well as track id.   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Remove ‘alt’ from hotkeys, just use letters and arrows straight up|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Update image tool icons                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Add support for fields under ENUM values during model creation|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Implement Dynamic model types              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Ungrouped Annotations/New Annotation Regions should display at the top of Explorer's Detections List|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Change explorer to use sample_ms instead from network response instead of deducing the value|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Hide Workflow List Elements if below Range Slider value|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Modify Annotating from Custom Model Predictions to post new annotations.|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Update model mode with new designs         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Refactor ImageUtils.js file to individual functions instead of one object|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Added threshold search result in Portal    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Update media player icons                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Display timestamp bar in Explorer grid view for video results|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg)|Concept relation should autocomplete concept name|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Send email to workers when they are added to task|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Assigning a worker or reviewer to a task sends an email|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Apps with empty workflow should allow all task types (concepts, bounding box, polygon) during task creation|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Edit Task feature                          |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Support consensus review settings          |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Support detection tasks                    |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Create new Single Image View and Image Tools|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Task view UI for workers                   |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Introduce AWAITING_REVIEW status for annotations|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Split tasks admin view into tabs           |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Test out idea behind tasks as saved searches and POST /annotations iterations|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Implement search by annotation.status in backend|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Search by images or video type in the right hand side bar of explorer's grid view|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Video Crop Region Search                   |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|video thumbs display relevant frame in search|


### Workflows

|Status     |Details                                    |
|-----------|-------------------------------------------|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg)|Display workflow detection predictions on the main/large image in Portal|
