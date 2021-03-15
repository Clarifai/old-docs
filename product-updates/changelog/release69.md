# Release 6.9

## Changelog 6.8

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28231%29%20%281%29.jpg) | ![](../../.gitbook/assets/improvement%20%2819%29%20%28533%29.jpg) | ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2818%29.jpg) | ![](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%2816%29.jpg) |

### Scribe

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28394%29.jpg) | Improve email subject for canceled order |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2821%29.jpg) | \[P0\]Cancel feature for Order owner |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28477%29.jpg) | Task form should select "All Inputs" by default |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28641%29.jpg) | Create Task button is incorrectly locked due to missing inputs |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2850%29.jpg) | Embed Model Version Id Missing in classification annotation requests |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28234%29.jpg) | Detection Annotations with Predictions display out of order |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281073%29.jpg) | Can only view app owner annotations when viewing an app as a collaborator |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281071%29.jpg) | Fix Detection Annotations displayed as collaborator bug |

### Spacetime

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28936%29.jpg) | Clicking the x on search item in explorer grid view for search across apps does not properly clear the url |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28365%29.jpg) | Add Min Search Score Range Slider to Search Across Apps Tab |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28245%29.jpg) | Clicking a video search result does not seek to the corresponding timestamp |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2864%29.jpg) | Search By Region button on video thunbnails |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28136%29.jpg) | Clicking see all within image details sidebar of the visual search across apps should render all of the search results in explorer's asset grid view |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28239%29.jpg) | clicking see all from image details sidebar opens refine search search bar in explorer's asset grid view |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28240%29.jpg) | Add getSeekedVideoFrame onMouseOver to visual search results of |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28106%29.jpg) | Add video timestamps to video search results within the |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28248%29.jpg) | Add search across apps to Image View righthand sidebar |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28131%29.jpg) | Add select app in "Refine Search" righthand sidebar |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28187%29.jpg) | Search for annotation.status in Explorer search bar. |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28178%29.jpg) | Search for annotation.user\_id in Explorer search bar. |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28721%29.jpg) | Change Annotation Search To say "filter by" |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28858%29.jpg) | Users having the same name as a collaborator causes annotation searching to break. |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2811%29.jpg) | Manually typing annotation search crashes explorer |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28698%29.jpg) | Endless error if a search fails in explorer |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28550%29.jpg) | Search grid view in explorer gets stuck with old results |

### Enlight

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28245%29.jpg) | Tracker evals: support for original coordinates |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2885%29.jpg) | Integrate MORSE metrics and AP to tracker eval pipeline |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28693%29.jpg) | Cleanup trackers' interface |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28316%29.jpg) | Platform-aware triton orchestrator |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28641%29.jpg) | Connect tracker evaluations with the servicer |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28506%29.jpg) | Implement first version of tracking eval |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28339%29.jpg) | Add embed\_model\_version\_id to cluster and KNN model types |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28359%29.jpg) | Show ROC AUC even if 0.0 |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28450%29.jpg) | crop model carriers forward concepts and other things but shouldn’t. |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2870%29.jpg) | Edit model doesn't work in model details page and app details page |

### Mesh

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28209%29.jpg) | Create pubic Visual Text Recognition workflow |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28156%29.jpg) | \[Portal\] Use only\_base parameter when choosing base workflow |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28355%29.jpg) | Display model name in Selected model row in workflows edit page |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28801%29.jpg) | Remove workflows creation discrepancy |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28265%29.jpg) | Workflows nodes being set as Loading |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28185%29.jpg) | Add Transform, Resize and Drag functionality to canvas rectangles |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28346%29.jpg) | Create CollabpsableBox block to provide app-wide reusable accordion boxes with menu items |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28347%29.jpg) | Create a central entities factory for app-wide entities like annotations to be shared across modules like Explorer and Labeler |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28255%29.jpg) | Mouse leave preserves the FE generated thumbnail of a video at a specific time. |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28228%29.jpg) | Set up end to end testing framework & write auth tests |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2846%29.jpg) | Create Data mode design |
| ![](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%2849%29.jpg) | Filter annotations by user id in explorer |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%2896%29.jpg) | re-position data-mode in sidebar |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28695%29.jpg) | Fix Development Environment Crashing on Portal |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28734%29.jpg) | Add responsiveness capability to Portal |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28396%29.jpg) | user can set a unique user\_id \( username \) in profile |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28524%29.jpg) | Enable HTML links for mode-switching icons |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28330%29.jpg) | Remove Upload from Explorer in favor of data mode |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28459%29.jpg) | Memoize video thumbnail urls |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%2868%29.jpg) | Fetch Tag icon data for Explorer inputs on hover |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28663%29.jpg) | Toast notifications should always be on top |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28226%29.jpg) | Refactor Data mode |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28837%29.jpg) | Refactor Data mode \(Upload component\) |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28740%29.jpg) | Remove Detection options dropdown menu |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28296%29%20%281%29.jpg) | Better Toast Notification System |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28258%29.jpg) | Update `ModelVersionSelector` component to make use of `reselect` |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28686%29.jpg) | Add create\_at date to explorer single input view. |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28407%29.jpg) | Expose geo coordinates just like metadata. |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28551%29.jpg) | Add input\_fields and output\_fields columns to model selection view \(from the ModelType\) |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28147%29.jpg) | Migrate model details page to model mode |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28691%29.jpg) | Copy button for personal access tokens doesn't work |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28119%29.jpg) | /models API request being made with appId as undefined |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2857%29.jpg) | hovering over inputs keeps fetching annotations even if fetched once |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28376%29.jpg) | Fix incorrect check for 'isDetectionModel' throughout Portal |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28947%29.jpg) | Broken TypeScript configuration for Cypress and Jest |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28980%29%20%281%29.jpg) | TypeScript type-checks not running on build/push |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2868%29.jpg) | Data Mode crashing due to legacy string refs |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28835%29.jpg) | Predictions don't show up if you reload on Explorer input |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28121%29.jpg) | Metrics view doesn't work anymore |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%2885%29.jpg) | Classification Annotations not loading |
| ![](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%28107%29.jpg) | Model filter app name resets when you click ctrl/alt key |

### API

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28493%29.jpg) | \[API Client Tests Javascript\] Fail fast when `stage` is invalid |
| ![](../../.gitbook/assets/improvement%20%2819%29%20%28405%29.jpg) | Don’t treat StatusCode\_FEATUREFLAG\_BLOCKED errors as server errors |

