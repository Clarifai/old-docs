# Release 6.9

## Changelog 6.8

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%2852%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2883%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28248%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Scribe

|Status     |Details                                                                                    |
|-----------|-------------------------------------------------------------------------------------------|
|Bug        |When a reviewer opens the "For Review" tab, determine whether there is work to be reviewed |
|Improvement|Remove Labeler V1                                                                          |
|Bug        |Keybindings not working when buttons are clicked                                           |
|Bug        |Interpolation transforms not working                                                       |
|Bug        |Update Search API Endpoint                                                                 |
|Bug        |[P2] [Sales Ask] Prediction bounding box shows for concepts not included in task           |
|Bug        |[P0.5, Alfredo Ask] Image filters don’t work                                               |
|Bug        |AI Assist should not create predictions with 0% confidence                                 |
|Bug        |AI Assist is creating annotation but is not auto marking the green check box or the red "X"|
|Bug        |AI Assist sends incorrect app ID when fetching workflows                                   |
|Bug        |Full assignment strategy results in error during review                                    |
|Improvement|Tests: Labeler Interpolation Sagas                                                         |
|Improvement|Tests: Labeler Inputs Sagas                                                                |
|Improvement|Tests: Labeler Canvas Sagas                                                                |
|Improvement|Show Sentry Event Id for Saga Errors                                                       |
|Bug        |Labeler AI Assist Breaking for custom User ID                                              |
|Bug        |[P0] Unable to load/access "Assigned to me" labeler tasks                                  |
|Bug        |Only able to draw one bounding box while using interpolation                               |
|Bug        |Brightness, Saturation and Invert doesn't change                                           |
|Bug        |Task Edit form doesn't show the correct FPS value from the task object                     |
|Bug        |Task Form shows warning when creating a new task                                           |
|Bug        |Place Order button remains on page when switching back from LaaS option to self-labeling   |
|Improvement|Tests: Labeler UI Sagas                                                                    |
|Improvement|When "My own Labelers" is clicked. All fields are not shown back                           |
|Improvement|Testing LabelOrder reducer - user journey                                                  |
|Improvement|Change cancel order copy                                                                   |
|Improvement|Unit test LabelOrder reducer.                                                              |
|Improvement|Testing LabelOrder reducer                                                                 |
|Improvement|Feature gate Labelling suggestions                                                         |
|Bug        |Pinning apps breaking search app functionality                                             |
|Bug        |Unable to create a new Task in Labeler                                                     |
|New Feature|Better Video Features                                                                      |
|Improvement|Opening a task should ONLY fetch annotations for the task that was opened                  |
|Bug        |Task Edit form doesn't pre-populate worker strategy selection                              |
|Bug        |Submit for Review logic incorrectly assumes the last input is last                         |
|New Feature|On the Task creation form Add section to Review strategy block for Consensus type          |
|Bug        |Fix key issue in ExplorerAnnotationStatusList component in Explorer                        |
|New Feature|Handle Noisy Labels                                                                        |
|Bug        |Optimistically update "don't show again" in onboarding modal of Task Form                   |
|Bug        |Flipkart would like better formatting of markdown for instructions                         |
|Bug        |[P1] Show onboarding modals for each persona: Task creator, Reviewer, Worker               |
|Bug        |Onboarding tooltips for /apps doesn't go away when I click "awesome"                       |
|Bug        |Pressing ESC patches my metadata 4 times in a row                                          |
|Bug        |Move Hubspot chat icon into the navbar                                                     |
|Bug        |Task Form Inputs and Buttons are Misaligned                                                |
|Bug        |Task Creation submit not redirecting                                                       |
|Bug        |In Labeler, “Skip” and "Reject" buttons are hidden by the questions bot blob               |
|Bug        |[P2] [Matt Ask] Toggling panning makes the image blury                                     |
|Bug        |Clicking "Create Task" doesn't force you to exit the task creation screen.                 |
|New Feature|App Details - Tool Tip only shows 1/3 (there doesn't seem to be a 2/3 or 3/3)              |
|Improvement|Display onboarding modal for Reviewer                                                      |
|Improvement|Display onboarding modal for Task Creator                                                  |
|Improvement|Review Strategy for TaskForm                                                               |
|Improvement|AI Assist for TaskForm                                                                     |
|Improvement|Manual reviewers for TaskForm                                                              |
|Improvement|Worket strategy input for TaskForm                                                         |
|Improvement|Wroker input for TaskForm                                                                  |
|Improvement|Create ProposerWorkflow input for TaskForm                                                 |
|Improvement|Create VideoFps input for TaskForm                                                         |
|Improvement|Create Concepts input for TaskForm                                                         |
|Improvement|Create InputSource input for TaskForm                                                      |
|Improvement|Create TaskType input for TaskForm                                                         |
|Improvement|Create separate styled component file for FormTypeSection                                  |
|Bug        |Onboarding modal points to 2 videos and they link deeper into the same video.              |

### Enlight

|Status     |Details                                                                                    |
|-----------|-------------------------------------------------------------------------------------------|
|Improvement|Implement track association module                                                         |
|Improvement|implement log probability using kalman state as input                                      |
|Bug        |cannot save model details in portal with lrate < 0.001                                     |
|Improvement|[OCR] Scene Text Reco & Text Classify Integration [stretch]                                |
|New Feature|Splice Concepts Together                                                                   |
|New Feature|New Layers / Arch                                                                          |
|New Feature|Models on New Data Types                                                                   |
|New Feature|Neural Net Toolkit                                                                         |
|New Feature|Recurrent Nets Up and Running                                                              |
|Improvement|YOLO dataset script                                                                        |
|Improvement|deploy landmark model                                                                      |
|Improvement|Update roll up for task_input_counts table to have worker_id information                   |
|Improvement|[P 0.5] implement annotation count                                                         |
|Improvement|Integrate filter, status, association into a single tracker model                          |
|Improvement|implement aggregator                                                                       |
|Improvement|Design simulated data that mimic low confidence / high recall detections                   |
|Improvement|Design training losses                                                                     |
|Improvement|Try box in x y a r format (SORT format)                                                    |
|Improvement|Try box in x y w h format                                                                  |
|Bug        |checkpoint for test eval can be deleted before eval is started                             |
|Improvement|Improve face orientation bucketing of LandmarkAlignTransform in DataProvider               |
|Improvement|Use tracker state in TrackerPredict calls                                                  |
|Improvement|Make Text Aggregator Operator public                                                       |
|Improvement|Remove transformers dependency                                                             |
|Improvement|Simple visual tracker example                                                              |
|Improvement|ingest VGGFACE2                                                                            |
|Improvement|Explore multi-language support                                                             |
|Improvement|[Portal] Allow copying public workflows into existing workflows                            |
|Improvement|Rewrite Export Scripts                                                                     |
|New Feature|introduce region threshold model                                                           |
|Improvement|Add filter_other_concepts param to concept threshold model                                 |
|Improvement|Remove the unnecessary requires_sequential_frames field of ModelType                       |
|Improvement|Add support for image crop model to work on video                                          |
|Bug        |Fix duplicate_app.go restriction on number of annotations                                  |
|Improvement|Notebook to demo tracker evals                                                             |
|Improvement|RNN vs Model-based tracking: Real data                                                     |


### Armada

|Status     |Details                                                                                    |
|-----------|-------------------------------------------------------------------------------------------|
|Improvement|Triton GRPC Client Upgrade                                                                 |
|Improvement|Migrate Spire to use TextTokenizer Transform                                               |
|Improvement|Implement TextTokenizer Transform                                                          |
|Improvement|Export model to TorchScript                                                                |
|Improvement|HDFS for EID storage                                                                       |
|Improvement|Experiment tracking improvements                                                           |
|Improvement|Trace from EID                                                                             |
|Improvement|EID management                                                                             |
|Improvement|Ingest A Video dataset                                                                     |
|Improvement|Resolve TRT saved model Issues Across GPU compute Capabilities                              |
|Improvement|People/Vehicle Detector TRT conversion and inference benchmarking                          |



### Portal

|Status     |Details                                                                                    |
|-----------|-------------------------------------------------------------------------------------------|
|Bug        |CSS on toggles within model mode was cutting off the toggle                                |
|Bug        |Model creation broken                                                                      |
|New Feature|Create Hubspot dashboard with funnels and charts                                           |
|New Feature|Capture customer behavior analytics                                                        |
|Bug        |CORS error prevents uploaded images from rendering                                         |
|Bug        |Properly configure S3 bucket for inputs to allow portal (prod and dev)                     |
|Bug        |Investigate why the vendors bundle is 12MB                                                 |
|New Feature|Render relation-based parent-child relationship in Proposals                               |
|New Feature|Proposers UI with a new annotations reducer                                                |
|New Feature|Create annotations module in store/explorer for Proposers UI                               |
|Improvement|Move Proposers data transformation to a saga+web worker                                    |
|Improvement|Integrate Proposers with Classification apps                                               |
|Improvement|Show App Concepts alongside model concepts in Proposers UI                                 |
|Bug        |Explorer does exponentially increasing duplicate calls to GET inputs endpoint              |
|New Feature|Introduce knowledge graph link creation when check/X is clicked on clarifai/main models    |
|Improvement|update created-at timestamp format to: hours/minutes/seconds for model-input               |
|Bug        |data-mode - uploaded-images multiple elements get re-rendered                              |
|Improvement|zoom-in & zoom-out controls for explorer geo                                               |
|Improvement|Allow users to upload the same url twice from data mode                                    |
|Improvement|set app-id instead of the app-name on new app-creation for readable urls                   |
|Improvement|fully qualified url for app-listing                                                        |
|Bug        |NaN being displayed in model-versions                                                      |
|Bug        |Portal does not parse links properly                                                       |
|Bug        |Unable to view versions or eval metrics page as a collaborator                             |
|Improvement|Data Ingestions                                                                            |
|Improvement|Create initial eval script to test cascade approach                                        |
|Improvement|Work with BE to nurse input uploads                                                        |
|Improvement|Get Input Embeddings and Cluster over All                                                  |
|Improvement|Get Input Embeddings and Cluster over Concepts                                             |
|Bug        |Data Mode page performance issues when pasting 60 inputs in production                     |
|Bug        |Bulk unlabeling doesn't work                                                                |
|New Feature|Change model type to model type ID everywhere                                              |
|Improvement|slider for concept threshold should allow for full precision floats with box to set the value|
|Improvement|Upload third party models through Portal                                                   |
|Improvement|Develop the model predict view for portal for existing models.                             |
|New Feature|Add dropdown for model_type_id                                                             |
|New Feature|Allow users to upload pre-trained models                                                   |
|Improvement|Make versions tab as default in model details page                                         |
|Improvement|Update `ModelPredictions` component to make use of `reselect` & sagas                      |
|Bug        |Create collectors always selects user as clarifai                                          |
|Bug        |AnimatedList caches the children nodes causing improper renders                            |
|Bug        |Sending invalid fields during model creation                                               |
|Bug        |Workflow page crashes                                                                      |
|Bug        |Improve performance of explorer                                                            |
|Bug        |Remove console errors in various parts of portal                                           |
|Bug        |GetInputCount() is called on loop after exiting data mode                                  |
|Bug        |Create new Collector redirects to apps page                                                |
|Bug        |Collectors Adding app model bug                                                            |
|Bug        |copy public workflow do not populate workflow model                                        |
|Bug        |In eval metrics page, "Concept by Concept" section shows counts that are incorrect         |
|Bug        |In eval metrics page, "1 split" section is incorrect                                       |
|Bug        |Prevent patching model annotations                                                         |
|Bug        |Deprecate old search endpoint from FE                                                      |
|Bug        |Add Embed Model Version Id to Bulk Labeler Classification Annotations                      |
|Bug        |Range Slider on Eval Metrics Page causes app crash when moving                             |


### API

|Status     |Details                                                                                    |
|-----------|-------------------------------------------------------------------------------------------|
|Improvement|Overwrite user annotation info with annotation writer model info                           |
|Bug        |[P2] Unable to add polygon annotation with embed_model_version_id                          |
|Improvement|Experiment with docs.clarifai.com using API versions                                       |
|New Feature|Make gRPC Swift client                                                                     |
|Bug        |Can't assign a task to myself if I have a custom user_id                                   |
|Bug        |Annotation writer model & concept thresholder create incorrect additional annotations      |
|Bug        |app copy doesn't stop after timeout                                                        |
|New Feature|Asset search by status                                                                     |
|Improvement|monitor media processor predict err rate                                                   |
|Improvement|log spire name                                                                             |
|Bug        |clean idle/pending asset publish video asset to pipeline separately                        |
