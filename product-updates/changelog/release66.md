---
description: Changelog for Clarifai Release 6.6
---


# Release 6.6

## Changelog 6.6

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) |

### API

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Integrate Python functions service with API |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | List available model types through API |

### Model

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix video error from new face cluster model in staging env |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | 21312 Ground truth data caseids must be nonempty and unique. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update deep training to list the ModelTypes |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Move model\_metadata to better place in protos. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Generalize the domex-visual-searcher model type |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | List available model types from backend services that provide models. |

### Portal

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed bug in submitting finished Labeler Task |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Select all concepts checkbox can be de-synced from actual concepts badges. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Disable Create Task button if not app owner |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Search by task\_id returns incorrect data |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Removed model creation from concept creation action in portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video scrubber cannot be moved. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed ability to delete interpolation tracks \(you can only delete frames at this time\). |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Worker ids used instead of names in report overview in stats view. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Y-axis on labels created stats page is wrong. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | In task creation, adding concepts should be simple to click all the options right away. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Toggling concept visibility doesn't affect previously hidden child region. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Leftover |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | If reviewer is not a collaborator, UI sends empty reviewer id back instead of raising error. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Bounding box disappears on resizing. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | While adjusting bounding box, it creates an additional bounding box over no object. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Using Play button brings up "Oops" page. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Error on opening Video Labeler. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Labeler sidebar interaction bugs and unresponsiveness \(due to lack of optimistic UI\). Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Newly drawn object disappears from canvas after drawing, and reappears after API response. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Infinite loading in Labeler Mode for app without any inputs. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Use name field for tasks in Labeler admin. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Clicking labeler icon crashes. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Moving bounding box around repeatedly creates a race condition, shows error notification and duplicate box. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Explorer inputs stale state. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Diagnose issues affecting overall hanging/speed/performance of Labeler |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Carousel thumbnails not showing up in Labeler. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Not able to create overlapping bounding boxes. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | When user adds mass metadata in Explorer, the UI says success but metadata does not persist. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Create annotations while creating task. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Labeler board showing wrong task type. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Polygon annotations break Explorer. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Concept autocomplete in Labeler task creation is showing clarifai/main concepts. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Should not be allowed to create a task with no concepts if my app has no concepts. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed image tools state |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Restricted tasks to only the assigned users |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Add validation to TaskForm’s concept field |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Removed all instances of worker\_id from Explorer |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Create one annotation for each bbox |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | 98011 panic on ListTasks. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | App names no longer display in Explorer. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Empty Annotations are not displaying after drawing a new bounding box until after refreshing the page. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Drawing a new bounding box in Explorer after previously labeling a region display an error. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video search results do not play at the most relevant video time. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Change text upload UI to support moderation workflow |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Change object key lookup in boundingBoxContainer to use lodash/get |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Submitting Task for Review break Portal. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Labeling a region on an asset with multiple detected regions will put the child annotation in the wrong group in Explorer's sidebar. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ConvertToBoundingBoxRegion function breaks Explorer when annotation information has not loaded at time of render. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video Frame Annotating in Explorer throws errors. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | When drawing a new bounding box, Base64 string for video annotations shows the wrong regions. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixe 10MB issue with video uploads |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Detection Regions and Indexes are thrown off on video assets. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video Search Results still on showing Inputs. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | DetailsPageHeader adds 2.25rem margin to the DetailsPageBody. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video Interpolation in Labeler breaks dev. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Redux is no longer calculating the sample\_ms rate, preventing bounding boxes from rendering. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed video pause error when navigating between videos |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ImagePile in Labeler Task View does not display image thumbs due to extraneous object nesting. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Remove warning error from console for immutable passed in props to SearchGrid.js |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Post annotation to detection region should use region id in portal. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Delete app button in app details takes you to blank page. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Incorrect bbox/label numbers displayed in image. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Multiple video thumbs selected in search results when selecting one thumb. Fixed |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Improve Labeler mode window resizing. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | W and E hotkeys for image labelling to go left/right. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Polygon annotations break Explorer. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Polygons regions don’t appear when panning and zooming. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Allow users to create concepts on task create view. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed task list item count query. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Utilising new task endpoints to Create tasks and integrate to show tasks in Portal. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | LabelerPage refresh error. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Should not be allowed to create a task with no concepts if my app has no concepts. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Unknown page Error. Complete interpolation of an object doesn't show bbox. Complete tracking of a box will disappear from the video. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fixed carousel padding. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Labeler board showing wrong task type. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Integrate worker/reviewer side of Labeler. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add 'name' field to new Tasks. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Create annotations while creating task. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Carousel thumbnails not showing up in Labeler. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | No image clearing/loading indicator in Labeler. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Use name field for tasks in Labeler administration. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Bulk labeling value does not update in store upon labeling. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Record time per annotation and per input to /stats/values in Labeler mode of Portal. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Query and display stats across workers per task for time and count of annotations. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Concept autocomplete in Labeler task creation is showing clarifai/main concepts. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Implement polygon task type in Labeler. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Applying filters in Portal breaks bulk labeling / unlabeling. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Unable to bulk-label annotations. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Change submit to "Complete Task" in Labeler page and add progress bar as it's working. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Allow Patching region annotations in Labeler mode. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add AI assist thresholding. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add ability to set annotation\_info in the annotation writer |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | `annotation_info` should be a valid JSON in Model Mode. Fixed. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Upgrade gulp and node to latest version for testing-library support |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Write PropType declarations for componens/ConceptListTable |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Enable collapse behavior in sidebar concepts |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Create atomic reusable  sidebar components |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Integrate React Testing Library |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Konva: Image centering, zooming, panning |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Move toolbar logic to react context |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Refactor TaskForm related thunks to sagas |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | \[Rearch\]Scaffold Labeler Redux in a new nested state slice & Implement Sagas |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | \[P2\] Task id is used in dropdown of stats tasks rather than task.name |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | \[P0\]Show taskId at task list |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Move region visibility state to its own React Context |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Get sidebar list data directly from redux |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | \[P1\] Don't hide task form if error occurs |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove delay of annotation request |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove animation for showing concepts on right side |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Perf: only fetch input predictions/annotations if user stays on image, not while navigating |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Get Labeler internal features ready for internal users |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Offload annotation creation to backend |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | allow reviewers update annotations |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | No image clearing/loading indicator in Labeler |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Controls for resizing bounding boxes need to be more visible |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Fabric rendering to be real-time; sync from API in background |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | make tasks endpoint public |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | list task by worker id/reviewer id |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add 'name' field to new Tasks |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Integrate worker/reviewer side of labeller |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Integrate and Implement task deletion using new endpoints |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Utilising new task endpoints to Create tasks and integrate to show tasks at portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Integrate and utilise new CRUD endpoints in portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Allow users to create concepts on task create view |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add empty CRUD endpoints for tasks |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Make polygons a separate task type |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add AI assist thresholding |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | W and E hotkeys for image labelling to go left/right. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Improve labeler mode window resizing. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Allow Patching region annotations in labeler mode. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | crank up internal message size to handle larger videos with more outputs |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Introduce stats collection APIs for worker stats. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Implement /tasks CRUD in API. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add frame.id to API as well as track id. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove ‘alt’ from hotkeys, just use letters and arrows straight up |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update image tool icons |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add support for fields under ENUM values during model creation |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Implement Dynamic model types |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Ungrouped Annotations/New Annotation Regions should display at the top of Explorer's Detections List |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Change explorer to use sample\_ms instead from network response instead of deducing the value |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Hide Workflow List Elements if below Range Slider value |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Modify Annotating from Custom Model Predictions to post new annotations. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update model mode with new designs |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Refactor ImageUtils.js file to individual functions instead of one object |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Added threshold search result in Portal |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update media player icons |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Display timestamp bar in Explorer grid view for video results |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Concept relation should autocomplete concept name |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Send email to workers when they are added to task |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Assigning a worker or reviewer to a task sends an email |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Apps with empty workflow should allow all task types \(concepts, bounding box, polygon\) during task creation |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Edit Task feature |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Support consensus review settings |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Support detection tasks |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Create new Single Image View and Image Tools |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Task view UI for workers |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Introduce AWAITING\_REVIEW status for annotations |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Split tasks admin view into tabs |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Test out idea behind tasks as saved searches and POST /annotations iterations |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Implement search by annotation.status in backend |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Search by images or video type in the right hand side bar of explorer's grid view |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Video Crop Region Search |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | video thumbs display relevant frame in search |

### Workflows

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Display workflow detection predictions on the main/large image in Portal |
