# Changelog

## Changelog 6.7

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../.gitbook/assets/bug%20%28248%29.jpg) | ![](../.gitbook/assets/enterprise%20%2810%29.jpg) |

### API
|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Don't allow updating task workers                                                                                                                             |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Don't create duplicated task annotations                                                                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Fix detection evals showing and too many metrics calls                                                                                                        |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Fix pillow installs for webp                                                                                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add enum for embed model version id field type.                                                                                                               |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Don't show model types for backends that aren't responding.                                                                                                   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Clean up output_info.data path                                                                                                                                |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add model_type_id to Model protos.                                                                                                                            |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add /models/types/{model_type_id} endpoint                                                                                                                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Prevent models_versions.is_public from every being null.                                                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |model mode types that are internal only are being returned.                                                                                                   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Create Labeling Order Object and send email to datalabeling@clarifai.com each time backend receives an Labeling Order Object & makes datalabeling a super user|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |App reindex                                                                                                                                                   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Patchable multi-embed workflows with re-index                                                                                                                 |

### Model

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Demographics model is now broken in model gallery.                                                                                                            |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Deprecate model.type from model mode                                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Update model gallery design                                                                                                                                   |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |embed_model_version_id should be a dropdown                                                                                                                   |


### Portal

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add versioning to repo, redux, on screen                                                                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Allow reviewer to modify annotations during review process.                                                                                                   |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Store entire canvas state in redux/context, and drive canvas updates by central store                                                                         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |batch v2 shape events by only 1 PATCH/DELETE request                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Delete functionality v2                                                                                                                                       |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Completely detach labeler rendering from server syncing process to enable background syncing                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Input navigating functionality in v2                                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Set new regionId as "selected" shape if user has selected a transient shape during async updates                                                              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Region edit + delete API sync                                                                                                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Fix annotation denormalizer to rehydrate actual concept value                                                                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Create new region in labeler v2                                                                                                                               |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Logic to reduce batched drawing events to least number of API operations                                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Implement new selectors for regions in v2                                                                                                                     |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Normalize Annotations & Regions data for redux storage                                                                                                        |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Nest labelerTasks reducer inside labeler reducer                                                                                                              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Konva: Concept Region drawing implementation                                                                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Konva: Implement Rect Transformation                                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Implement a futureproof schema for labeler interaction events                                                                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Move to event-driven design & have the ability to batch updates using custom logic                                                                            |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Create a single Sidebar component for all Labeling types, make children configurable                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Remove all props unnecessarily passed from LabelerPage to deep children and make components get props from Redux only                                         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Remove all logic from components to sagas for higher level orchestration of features                                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Video selector improvements & test updation                                                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Can only save 50 annotations on an image {Usability}                                                                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Konva: resizing BBox below minimum size and "crossing over" makes things awry                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |LabelerPage complete re-render of all components on mouseHover, mousMove (img attached)                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Cypress script doesn't terminate webpack-dev-server child process                                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Cypress pre-run script doesn't check if dev server is already running                                                                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Create Unit+Integration testing framework                                                                                                                     |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Integrate headless Cypress with build testing                                                                                                                 |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Switch to react-konva for performant canvas rendering                                                                                                         |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add task id to task list                                                                                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Panning functionality improvements                                                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Lock video playback and interpolation to fps                                                                                                                  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Annotations created with interpolation seem to have incorrect frame indices                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Bounding Boxes and Concepts inconsistent during video playback {Usability}                                                                                    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |While annotating video, interpolation freezes and all annotations disappear                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Boxes/Interpolation objects are not saving after task submission                                                                                              |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Display task instructions to workers in labeler mode                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add infinite scroll loading to labeler carousel                                                                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Not incrementing onNext and onPrev pages in Labeler Carousel                                                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Display only minimal log in Portal react app                                                                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Update Model mode to use the GET /models/types endpoint                                                                                                       |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add list/grid toggle in model mode on all view                                                                                                                |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Collectors UI should use the layout similar to ModellingMode/LabellerMode                                                                                     |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Bulk add concepts to region annotations in app with multi-embed base workflow                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Profile page crashes on load                                                                                                                                  |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Model mode array of concepts should be unique                                                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Model creation/edit bugs                                                                                                                                      |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |New Collector page not scrollable                                                                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |App Workflows - Unable to update model version for custom models                                                                                              |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Display Created At Date in App Grid View                                                                                                                      |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Support .txt files from local file browser                                                                                                                    |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Support uploading of multiple video assets as well as image and video assets within the same CSV file                                                         |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Add better user feedback for uploading text assets                                                                                                            |
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Upload Text by CSV for NLP                                                                                                                                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Final NLP MVP Feature Changes                                                                                                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Remove 0 area detection filtering from frontend code                                                                                                          |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Modify accepted CSV upload format so every column corresponds to a network request field                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Resolve final bugs with bounding box indexes                                                                                                                  |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Prevent uploading image and video asset types to Text apps                                                                                                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |No Visual Feedback for Text input Upload                                                                                                                      |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Support Uploading Files through the OS File Browser for NLP                                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Custom Model Prediction Bounding Boxes are misaligned from the Detections Bar                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Workflow Tab should display and load on initial view for text apps                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Unable to navigate between text assets within explorer's asset detail view                                                                                    |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |CSV uploads not parsing metadata and concepts                                                                                                                 |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Explorer's Advanced Search does not support searching by concepts                                                                                             |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Training a classification model no longer display anything within the Custom Model Predictions tab                                                            |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |create annotation CUD sagas for labeler v2                                                                                                                    |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Don't create task annotations in frontend                                                                                                                     |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Form: Input Source showing auto complete options from other apps                                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Rich text instructions icon bugs                                                                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Task create form doesnt force you to set a reviewer if you specify manual review                                                                              |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |TypeError: val.add is not a function                                                                                                                          |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Fix autocomplete when user selects "All inputs" for selecting inputs in task creation                                                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Error pops up when collaborator tries to edit task                                                                                                            |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |When I attempt to edit an existing labeling task t...                                                                                                         |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Page not responding [Usability]                                                                                                                               |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |[Explorer] concept thumbnails aren't displaying from model details view                                                                                       |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Concept Detail View displays incorrect assets                                                                                                                 |
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Add all concepts button to model mode forms                                                                                                                   |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |Concept Autocomplete in Model Mode doesn't always display                                                                                                     |


### Workflows

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/new_feature%20%2852%29.jpg) |Allow run workflow and search embedding from embed model in workflow                                                                                          |

### Applications

|Status     |Details                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../.gitbook/assets/improvement%20%2883%29.jpg) |Metadata Namespacing for Clarifai Apps                                                                                                                        |
| ![](../.gitbook/assets/bug%20%28248%29.jpg) |App details page should send a user to models page to create models rather than using modal                                                                   |
