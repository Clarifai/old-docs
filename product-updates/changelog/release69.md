---
description: Changelog for Clarifai Release 6.9
---

# Release 6.9

## Changelog 6.8

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![](../../.gitbook/assets/new_feature.jpg) | ![](../../.gitbook/assets/improvement.jpg) | ![](../../.gitbook/assets/bug.jpg) | ![](../../.gitbook/assets/enterprise.jpg) |

### Scribe

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement.jpg) | Improve email subject for canceled order |
| ![](../../.gitbook/assets/new_feature.jpg) | \[P0\]Cancel feature for Order owner |
| ![](../../.gitbook/assets/improvement.jpg) | Task form should select "All Inputs" by default |
| ![](../../.gitbook/assets/bug.jpg) | Create Task button is incorrectly locked due to missing inputs |
| ![](../../.gitbook/assets/bug.jpg) | Embed Model Version Id Missing in classification annotation requests |
| ![](../../.gitbook/assets/bug.jpg) | Detection Annotations with Predictions display out of order |
| ![](../../.gitbook/assets/bug.jpg) | Can only view app owner annotations when viewing an app as a collaborator |
| ![](../../.gitbook/assets/bug.jpg) | Fix Detection Annotations displayed as collaborator bug |

### Spacetime

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/bug.jpg) | Clicking the x on search item in explorer grid view for search across apps does not properly clear the url |
| ![](../../.gitbook/assets/new_feature.jpg) | Add Min Search Score Range Slider to Search Across Apps Tab |
| ![](../../.gitbook/assets/new_feature.jpg) | Clicking a video search result does not seek to the corresponding timestamp |
| ![](../../.gitbook/assets/new_feature.jpg) | Search By Region button on video thunbnails |
| ![](../../.gitbook/assets/new_feature.jpg) | Clicking see all within image details sidebar of the visual search across apps should render all of the search results in explorer's asset grid view |
| ![](../../.gitbook/assets/new_feature.jpg) | clicking see all from image details sidebar opens refine search search bar in explorer's asset grid view |
| ![](../../.gitbook/assets/new_feature.jpg) | Add getSeekedVideoFrame onMouseOver to visual search results of |
| ![](../../.gitbook/assets/new_feature.jpg) | Add video timestamps to video search results within the |
| ![](../../.gitbook/assets/new_feature.jpg) | Add search across apps to Image View righthand sidebar |
| ![](../../.gitbook/assets/new_feature.jpg) | Add select app in "Refine Search" righthand sidebar |
| ![](../../.gitbook/assets/new_feature.jpg) | Search for annotation.status in Explorer search bar. |
| ![](../../.gitbook/assets/new_feature.jpg) | Search for annotation.user\_id in Explorer search bar. |
| ![](../../.gitbook/assets/improvement.jpg) | Change Annotation Search To say "filter by" |
| ![](../../.gitbook/assets/bug.jpg) | Users having the same name as a collaborator causes annotation searching to break. |
| ![](../../.gitbook/assets/bug.jpg) | Manually typing annotation search crashes explorer |
| ![](../../.gitbook/assets/bug.jpg) | Endless error if a search fails in explorer |
| ![](../../.gitbook/assets/bug.jpg) | Search grid view in explorer gets stuck with old results |

### Enlight

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement.jpg) | Tracker evals: support for original coordinates |
| ![](../../.gitbook/assets/new_feature.jpg) | Integrate MORSE metrics and AP to tracker eval pipeline |
| ![](../../.gitbook/assets/improvement.jpg) | Cleanup trackers' interface |
| ![](../../.gitbook/assets/improvement.jpg) | Platform-aware triton orchestrator |
| ![](../../.gitbook/assets/improvement.jpg) | Connect tracker evaluations with the servicer |
| ![](../../.gitbook/assets/improvement.jpg) | Implement first version of tracking eval |
| ![](../../.gitbook/assets/improvement.jpg) | Add embed\_model\_version\_id to cluster and KNN model types |
| ![](../../.gitbook/assets/improvement.jpg) | Show ROC AUC even if 0.0 |
| ![](../../.gitbook/assets/bug.jpg) | crop model carriers forward concepts and other things but shouldn’t. |
| ![](../../.gitbook/assets/bug.jpg) | Edit model doesn't work in model details page and app details page |

### Mesh

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/new_feature.jpg) | Create pubic Visual Text Recognition workflow |
| ![](../../.gitbook/assets/improvement.jpg) | \[Portal\] Use only\_base parameter when choosing base workflow |
| ![](../../.gitbook/assets/improvement.jpg) | Display model name in Selected model row in workflows edit page |
| ![](../../.gitbook/assets/bug.jpg) | Remove workflows creation discrepancy |
| ![](../../.gitbook/assets/bug.jpg) | Workflows nodes being set as Loading |

### Portal

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement.jpg) | Add Transform, Resize and Drag functionality to canvas rectangles |
| ![](../../.gitbook/assets/improvement.jpg) | Create CollabpsableBox block to provide app-wide reusable accordion boxes with menu items |
| ![](../../.gitbook/assets/new_feature.jpg) | Create a central entities factory for app-wide entities like annotations to be shared across modules like Explorer and Labeler |
| ![](../../.gitbook/assets/new_feature.jpg) | Mouse leave preserves the FE generated thumbnail of a video at a specific time. |
| ![](../../.gitbook/assets/new_feature.jpg) | Set up end to end testing framework & write auth tests |
| ![](../../.gitbook/assets/new_feature.jpg) | Create Data mode design |
| ![](../../.gitbook/assets/new_feature.jpg) | Filter annotations by user id in explorer |
| ![](../../.gitbook/assets/improvement.jpg) | re-position data-mode in sidebar |
| ![](../../.gitbook/assets/improvement.jpg) | Fix Development Environment Crashing on Portal |
| ![](../../.gitbook/assets/improvement.jpg) | Add responsiveness capability to Portal |
| ![](../../.gitbook/assets/improvement.jpg) | user can set a unique user\_id \( username \) in profile |
| ![](../../.gitbook/assets/improvement.jpg) | Enable HTML links for mode-switching icons |
| ![](../../.gitbook/assets/improvement.jpg) | Remove Upload from Explorer in favor of data mode |
| ![](../../.gitbook/assets/improvement.jpg) | Memoize video thumbnail urls |
| ![](../../.gitbook/assets/improvement.jpg) | Fetch Tag icon data for Explorer inputs on hover |
| ![](../../.gitbook/assets/improvement.jpg) | Toast notifications should always be on top |
| ![](../../.gitbook/assets/improvement.jpg) | Refactor Data mode |
| ![](../../.gitbook/assets/improvement.jpg) | Refactor Data mode \(Upload component\) |
| ![](../../.gitbook/assets/improvement.jpg) | Remove Detection options dropdown menu |
| ![](../../.gitbook/assets/improvement.jpg) | Better Toast Notification System |
| ![](../../.gitbook/assets/improvement.jpg) | Update `ModelVersionSelector` component to make use of `reselect` |
| ![](../../.gitbook/assets/improvement.jpg) | Add create\_at date to explorer single input view. |
| ![](../../.gitbook/assets/improvement.jpg) | Expose geo coordinates just like metadata. |
| ![](../../.gitbook/assets/improvement.jpg) | Add input\_fields and output\_fields columns to model selection view \(from the ModelType\) |
| ![](../../.gitbook/assets/improvement.jpg) | Migrate model details page to model mode |
| ![](../../.gitbook/assets/bug.jpg) | Copy button for personal access tokens doesn't work |
| ![](../../.gitbook/assets/bug.jpg) | /models API request being made with appId as undefined |
| ![](../../.gitbook/assets/bug.jpg) | hovering over inputs keeps fetching annotations even if fetched once |
| ![](../../.gitbook/assets/bug.jpg) | Fix incorrect check for 'isDetectionModel' throughout Portal |
| ![](../../.gitbook/assets/bug.jpg) | Broken TypeScript configuration for Cypress and Jest |
| ![](../../.gitbook/assets/bug.jpg) | TypeScript type-checks not running on build/push |
| ![](../../.gitbook/assets/bug.jpg) | Data Mode crashing due to legacy string refs |
| ![](../../.gitbook/assets/bug.jpg) | Predictions don't show up if you reload on Explorer input |
| ![](../../.gitbook/assets/bug.jpg) | Metrics view doesn't work anymore |
| ![](../../.gitbook/assets/bug.jpg) | Classification Annotations not loading |
| ![](../../.gitbook/assets/bug.jpg) | Model filter app name resets when you click ctrl/alt key |

### API

| Status | Details |
| :--- | :--- |
| ![](../../.gitbook/assets/improvement.jpg) | \[API Client Tests Javascript\] Fail fast when `stage` is invalid |
| ![](../../.gitbook/assets/improvement.jpg) | Don’t treat StatusCode\_FEATUREFLAG\_BLOCKED errors as server errors |
