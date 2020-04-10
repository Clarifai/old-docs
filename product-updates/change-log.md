# Change log

## Accounts
* Create a UI for personal access tokens making it easier for users to access their own apps and any apps where they have been added as collaborators
* Updated /keys to work with PATs
* Login (user/PW) has no rate limit/max attempts. Fixed
* Remove all instances of worker_id from explorer

## Applications
* Add apps and keys scopes so they can be created with personal access tokens
* copy app count and last_inputs added in app duplication
* Fix demo font syntax, part 2
* Fixed details page header missing description

## Data Management
* Optimize Video Detection Frame Rate on Front end
* Improve JSON serialization performance in our servers by using an optimized third party library
* able to overwrite default max conn for Citus
* Rewrite input counting in the API to be more scalable and robust
* Allow RegionInfo from SpireDetectEmbedResponse to contain Point when saving to DB
* grant select permission to clarifairead


## Annotate
* Remove classification/detection toggle in image details view
* Mark /annotation endpoints with cl_private_rpc
* Improved adding negatives to regions
* Create one annotation for each bbox
* Log capability added for annotation/search request/response
* Eliminated error if no annotation to be deleted


## Model
* Return deep training evals through the API to automate evaluation process
* Update templates to have more straightforward names and more friendly defaults
* Ability to keep concepts sorted by alpha
* Implement image crop model to make it possible to work in subregions of an image
* Implement RandomSample model type, adding to fixed function feature set
* Fix the WorkflowInput field name in proto to workflow_input
* Allow models that need outputs from previous nodes in a workflow to have access to those outputs to support chaining complex graphs of models
* Confusion matrix predicted/true are swapped in evaluation results. Fixed
* Explore Image/Text Joint embedding
* Fixed generalModel imports and optimize video click handlers with useCallback hooks
* Fix for selectEmbedModelVersionId in detection apps
* NLP bug fixes for non text apps
* Drawing annotations: wrong embed model version id

## Predict
* Add colors to differentiate region results


## Search
* Add click to search metadata attributes in image details sidebar
* Implement visual search in another app as a model type you can add to a workflow
* Add metadata to collector added inputs so that you can filter by collector ID
* Search bar missing. Fixed   
* Region Searches within Search Bar still use crop coordinates instead of base64 bytes. Fixed
* Click Search button icons on Thumbs not working for localized search. Fixed
* Disable all search by click handlers in Portal for Text Apps
* Disable "hide all positively labeled" inputs button for NLP until search works
