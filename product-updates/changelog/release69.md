# Changelog

## Changelog 6.8

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../../.gitbook/assets/new_feature%20%2852%29.jpg) | ![](../../.gitbook/assets/improvement%20%2883%29.jpg) | ![](../../.gitbook/assets/bug%20%28248%29.jpg) | ![](../../.gitbook/assets/enterprise%20%2810%29.jpg) |

### Scribe

|Status     |Details                                                                  |
|-----------|-------------------------------------------------------------------------|
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Improve email subject for canceled order                                 |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|[P0]Cancel feature for Order owner                                       |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Task form should select "All Inputs" by default                          |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Create Task button is incorrectly locked due to missing inputs           |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Embed Model Version Id Missing in classification annotation requests     |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Detection Annotations with Predictions display out of order              |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Can only view app owner annotations when viewing an app as a collaborator|
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Fix Detection Annotations displayed as collaborator bug                  |

### Spacetime

|Status     |Details                                                                  |
|-----------|-------------------------------------------------------------------------|
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Clicking the x on search item in explorer grid view for search across apps does not properly clear the url|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Add Min Search Score Range Slider to Search Across Apps Tab              |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Clicking a video search result does not seek to the corresponding timestamp|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Search By Region button on video thunbnails                              |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Clicking see all within image details sidebar of the visual search across apps should render all of the search results in explorer's asset grid view|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|clicking see all from image details sidebar opens refine search search bar in explorer's asset grid view|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Add getSeekedVideoFrame onMouseOver to visual search results of <ImageDetailsSidebar />|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Add video timestamps to video search results within the <ImageDetailsSidebar />|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Add search across apps to Image View righthand sidebar                   |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Add select app in "Refine Search" righthand sidebar                      |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Search for annotation.status in Explorer search bar.                     |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Search for annotation.user_id in Explorer search bar.                    |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Change Annotation Search To say "filter by"                              |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Users having the same name as a collaborator causes annotation searching to break.|
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Manually typing annotation search crashes explorer                       |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Endless error if a search fails in explorer                              |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Search grid view in explorer gets stuck with old results                 |

### Enlight

|Status     |Details                                                                  |
|-----------|-------------------------------------------------------------------------|
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Tracker evals: support for original coordinates                          |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Integrate MORSE metrics and AP to tracker eval pipeline                  |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Cleanup trackers' interface                                              |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Platform-aware triton orchestrator                                       |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Connect tracker evaluations with the servicer                            |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Implement first version of tracking eval                                 |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Add embed_model_version_id to cluster and KNN model types                |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Show ROC AUC even if 0.0                                                 |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |crop model carriers forward concepts and other things but shouldn’t.     |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Edit model doesn't work in model details page and app details page       |

### Mesh

|Status     |Details                                                                  |
|-----------|-------------------------------------------------------------------------|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Create pubic Visual Text Recognition workflow                            |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|[Portal] Use only_base parameter when choosing base workflow             |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Display model name in Selected model row in workflows edit page          |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Remove workflows creation discrepancy                                    |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Workflows nodes being set as Loading                                     |

### Portal

|Status     |Details                                                                  |
|-----------|-------------------------------------------------------------------------|
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Add Transform, Resize and Drag functionality to canvas rectangles        |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Create CollabpsableBox block to provide app-wide reusable accordion boxes with menu items|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Create a central entities factory for app-wide entities like annotations to be shared across modules like Explorer and Labeler|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Mouse leave preserves the FE generated thumbnail of a video at a specific time.|
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Set up end to end testing framework & write auth tests                   |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Create Data mode design                                                  |
|![](../../.gitbook/assets/new_feature%20%2852%29.jpg)|Filter annotations by user id in explorer                                |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|re-position data-mode in sidebar                                         |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Fix Development Environment Crashing on Portal                           |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Add responsiveness capability to Portal                                  |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|user can set a unique user_id ( username ) in profile                    |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Enable HTML links for mode-switching icons                               |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Remove Upload from Explorer in favor of data mode                        |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Memoize video thumbnail urls                                             |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Fetch Tag icon data for Explorer inputs on hover                         |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Toast notifications should always be on top                              |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Refactor Data mode                                                       |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Refactor Data mode (Upload component)                                    |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Remove Detection options dropdown menu                                   |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Better Toast Notification System                                         |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Update `ModelVersionSelector` component to make use of `reselect`        |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Add create_at date to explorer single input view.                        |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Expose geo coordinates just like metadata.                               |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Add input_fields and output_fields columns to model selection view (from the ModelType)|
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Migrate model details page to model mode                                 |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Copy button for personal access tokens doesn't work                      |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |/models API request being made with appId as undefined                   |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |hovering over inputs keeps fetching annotations even if fetched once     |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Fix incorrect check for 'isDetectionModel' throughout Portal             |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Broken TypeScript configuration for Cypress and Jest                     |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |TypeScript type-checks not running on build/push                         |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Data Mode crashing due to legacy string refs                             |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Predictions don't show up if you reload on Explorer input                |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Metrics view doesn't work anymore                                        |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Classification Annotations not loading                                   |
|![](../../.gitbook/assets/bug%20%28248%29.jpg)        |Model filter app name resets when you click ctrl/alt key                 |

### API

|Status     |Details                                                                  |
|-----------|-------------------------------------------------------------------------|
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|[API Client Tests Javascript] Fail fast when `stage` is invalid          |
|![](../../.gitbook/assets/improvement%20%2883%29.jpg)|Don’t treat StatusCode_FEATUREFLAG_BLOCKED errors as server errors       |
