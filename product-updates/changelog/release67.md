---
description: Changelog for Clarifai Release 6.7
---


# Release 6.7

## Changelog 6.7

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/enterprise.jpg) |

### API

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Don't allow updating task workers |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Don't create duplicated task annotations |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Fix detection evals showing and too many metrics calls |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Fix pillow installs for webp |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add enum for embed model version id field type. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Don't show model types for backends that aren't responding. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Clean up output\_info.data path |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add model\_type\_id to Model protos. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add /models/types/{model\_type\_id} endpoint |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Prevent models\_versions.is\_public from every being null. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | model mode types that are internal only are being returned. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Create Labeling Order Object and send email to datalabeling@clarifai.com each time backend receives an Labeling Order Object & makes datalabeling a super user |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | App reindex |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Patchable multi-embed workflows with re-index |

### Model

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Demographics model is now broken in model gallery. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Deprecate model.type from model mode |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update model gallery design |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | embed\_model\_version\_id should be a dropdown |

### Portal

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add versioning to repo, redux, on screen |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Allow reviewer to modify annotations during review process. |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Store entire canvas state in redux/context, and drive canvas updates by central store |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | batch v2 shape events by only 1 PATCH/DELETE request |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Delete functionality v2 |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Completely detach labeler rendering from server syncing process to enable background syncing |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Input navigating functionality in v2 |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Set new regionId as "selected" shape if user has selected a transient shape during async updates |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Region edit + delete API sync |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Fix annotation denormalizer to rehydrate actual concept value |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Create new region in labeler v2 |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Logic to reduce batched drawing events to least number of API operations |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Implement new selectors for regions in v2 |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Normalize Annotations & Regions data for redux storage |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Nest labelerTasks reducer inside labeler reducer |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Konva: Concept Region drawing implementation |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Konva: Implement Rect Transformation |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Implement a futureproof schema for labeler interaction events |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Move to event-driven design & have the ability to batch updates using custom logic |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Create a single Sidebar component for all Labeling types, make children configurable |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove all props unnecessarily passed from LabelerPage to deep children and make components get props from Redux only |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove all logic from components to sagas for higher level orchestration of features |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Video selector improvements & test updation |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Can only save 50 annotations on an image {Usability} |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Konva: resizing BBox below minimum size and "crossing over" makes things awry |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | LabelerPage complete re-render of all components on mouseHover, mousMove \(img attached\) |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Cypress script doesn't terminate webpack-dev-server child process |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Cypress pre-run script doesn't check if dev server is already running |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Create Unit+Integration testing framework |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Integrate headless Cypress with build testing |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Switch to react-konva for performant canvas rendering |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add task id to task list |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Panning functionality improvements |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Lock video playback and interpolation to fps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Annotations created with interpolation seem to have incorrect frame indices |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Bounding Boxes and Concepts inconsistent during video playback {Usability} |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | While annotating video, interpolation freezes and all annotations disappear |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Boxes/Interpolation objects are not saving after task submission |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Display task instructions to workers in labeler mode |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add infinite scroll loading to labeler carousel |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Not incrementing onNext and onPrev pages in Labeler Carousel |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Display only minimal log in Portal react app |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Update Model mode to use the GET /models/types endpoint |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add list/grid toggle in model mode on all view |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Collectors UI should use the layout similar to ModellingMode/LabellerMode |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Bulk add concepts to region annotations in app with multi-embed base workflow |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Profile page crashes on load |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Model mode array of concepts should be unique |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Model creation/edit bugs |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | New Collector page not scrollable |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | App Workflows - Unable to update model version for custom models |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Display Created At Date in App Grid View |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Support .txt files from local file browser |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Support uploading of multiple video assets as well as image and video assets within the same CSV file |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Add better user feedback for uploading text assets |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Upload Text by CSV for NLP |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Final NLP MVP Feature Changes |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Remove 0 area detection filtering from frontend code |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Modify accepted CSV upload format so every column corresponds to a network request field |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Resolve final bugs with bounding box indexes |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Prevent uploading image and video asset types to Text apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | No Visual Feedback for Text input Upload |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Support Uploading Files through the OS File Browser for NLP |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Custom Model Prediction Bounding Boxes are misaligned from the Detections Bar |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Workflow Tab should display and load on initial view for text apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Unable to navigate between text assets within explorer's asset detail view |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | CSV uploads not parsing metadata and concepts |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Explorer's Advanced Search does not support searching by concepts |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Training a classification model no longer display anything within the Custom Model Predictions tab |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | create annotation CUD sagas for labeler v2 |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Don't create task annotations in frontend |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Form: Input Source showing auto complete options from other apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Rich text instructions icon bugs |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Task create form doesnt force you to set a reviewer if you specify manual review |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | TypeError: val.add is not a function |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Fix autocomplete when user selects "All inputs" for selecting inputs in task creation |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Error pops up when collaborator tries to edit task |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | When I attempt to edit an existing labeling task t... |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Page not responding \[Usability\] |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | \[Explorer\] concept thumbnails aren't displaying from model details view |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Concept Detail View displays incorrect assets |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Add all concepts button to model mode forms |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | Concept Autocomplete in Model Mode doesn't always display |

### Workflows

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/new_feature.jpg) | Allow run workflow and search embedding from embed model in workflow |

### Applications

| Status | Details |
| :--- | :--- |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/improvement.jpg) | Metadata Namespacing for Clarifai Apps |
| ![](https://github.com/Clarifai/old-docs/tree/1ece1cee27874f51aa11d50a825fff02b0b5243f/product-updates/.gitbook/assets/bug.jpg) | App details page should send a user to models page to create models rather than using modal |
