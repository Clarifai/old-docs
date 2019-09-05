### Status Codes

All of our API endpoints return back a status code and description with details of the status. A full list of those status codes is shown below. If a status comes back that you do not see below, please reach out to support@clarifai.com

| CODE  | DESCRIPTION |
| ----- | ----------- |
| 10000 | Ok |
| 10010 | Mixed Success |
| 10020 | Failure |
| 11000 | Account or plan issue |
| 11001 | Invalid authentication token |
| 11002 | Invalid credentials |
| 11003 | Hourly request limit exceeded |
| 11004 | Monthly request limit exceeded |
| 11005 | Making too many requests |
| 11006 | Account limits exceeded |
| 11007 | API key has insufficient scopes |
| 11008 | Invalid API key or Invalid API key/application pair |
| 11009 | API key not found |
| 11100 | Bad request format |
| 11101 | Resource does not exist |
| 11102 | Invalid request |
| 11103 | Method not allowed |
| 11104 | No GDPR Consent |
| 21100 | Model trained successfully |
| 21101 | Model is training |
| 21102 | Model not yet trained |
| 21103 | Custom model is currently in queue for training, waiting on inputs to process. |
| 21110 | Model training had no data. |
| 21111 | Model training had no positive examples. |
| 21112 | Model training was with concepts_mutually_exclusive but with a single class. Try adding more concepts or setting concepts_mutually_exclusive = false. |
| 21113 | Training took longer than expected, contact support@clarifai.com if this continues to happen when creating new versions of your model. |
| 21114 | Training got error waiting on your inputs to process, please contact support@clarifai.com. |
| 21115 | Unknown error in training, please contact support@clarifai.com. |
| 21116 | Training request was unexpectedly redelivered, contact support@clarifai.com if this continues to happen. |
| 21150 | Model modification success |
| 21151 | Model modification pending |
| 21152 | Model modification failed |
| 21200 | Model does not exist |
| 21201 | Model permission denied |
| 21202 | Invalid model argument |
| 21203 | Invalid model request |
| 21300 | Model was successfully evaluated. |
| 21301 | Model is evaluating. |
| 21302 | Model is not yet evaluated. |
| 21303 | Model is queued for evaluation. |
| 21310 | Model evaluation timed out. |
| 21311 | Model evaluation timed out waiting on inputs to process. |
| 21312 | Model evaluation unknown internal error. |
| 21313 | Model prediction failed |
| 21315 | Model evaluation failed because there are not enough annotated inputs. Please ensure there are at least 2 concepts in your model before evaluating. |
| 21316 | Model evaluation failed because there are not enough labeled inputs. Please ensure there are at least 5 labeled inputs per concept before evaluating. |
| 22001 | Workflow does not have specified input model. |
| 22002 | New model in workflow needs to be trained. |
| 22100 | Duplicate URL in your application. Check the documentation to allow duplications. |
| 22101 | Workflow format unsupported |
| 22102 | Workflow does not exist |
| 22103 | Workflow permission denied |
| 22104 | Workflow invalid argument |
| 22106 | Template workflow is invalid |
| 22107 | Workflow graph is invalid |
| 22150 | Workflow modification success |
| 22151 | Workflow modification pending |
| 22152 | Workflow modification failed |
| 22999 | Invalid request |
| 24150 | Annotation success |
| 24151 | Annotation pending |
| 24152 | Annotation failed; check URL |
| 24153 | Annotation in progress |
| 24155 | Annotation invalid argument |
| 24156 | Permission to annotation denied |
| 24250 | Annotation modification success |
| 24251 | Annotation modification pending |
| 24252 | Annotation modification failed |
| 25000 | Custom Trainer unknown internal error |
| 25004 | Custom Trainer failed to retrieve data or train |
| 30000 | Download complete |
| 30001 | Download pending |
| 30002 | Download failed or we could not process it. Check URL or bytes you send in the request. |
| 30003 | Download in progress |
| 30100 | Duplicate URL in your application. Check the documentation to allow duplications. |
| 30101 | Input image format unsupported |
| 30102 | Input does not exist |
| 30103 | Input permission denied |
| 30104 | Input invalid argument |
| 30105 | Input image is larger than the allowed limit |
| 30106 | Input image URL invalid |
| 30200 | Input image modification success |
| 30201 | Input image modification pending |
| 30203 | Input image modification failed |
| 30300 | Input image decoding failed. Check URLs and bytes sent |
| 31000 | Download complete |
| 31001 | Download pending |
| 31002 | Download failed or we could not process it. Check URL or bytes you sent in the request. |
| 31100 | Duplicate URL in your application. Check the documentation to allow duplications. |
| 31101 | Input video format unsupported |
| 31102 | Input does not exist |
| 31103 | Input permission denied |
| 31104 | Input invalid argument |
| 31105 | Input video is larger the allowed limit |
| 31106 | Input video URL invalid |
| 31200 | Input video modification success |
| 31201 | Input video modification pending |
| 31203 | Input video modification failed |
| 31300 | Input video decoding failed. Check URLs and bytes sent |
| 39996 | Connection attempts to the input URL failed |
| 39997 | Sorry, this type of request has been disabled for maintenance. Please try again in a few hours. |
| 39998 | Input writes are disabled for maintenance. Please try again in a few hours. |
| 39999 | Invalid input request |
| 40001 | Invalid request |
| 40002 | Invalid search request |
| 40003 | Invalid request |
| 40010 | Object has a duplicate ID; another object with same ID already exist. |
| 40017 | Object violates a constraint. Try again with different values for the fields. |
| 40019 | The requested operation is currently processing for this app |
| 40030 | Sorry, the server is too busy at the moment. Please try again later. |
| 40031 | Sorry, the server is unavailable at the moment. Please try again later. |
| 40032 | Sorry, your request has timed out. Please try your request again. |
| 40033 | Sorry, the request sent is larger than the allowed limit. Please contact support@clarifai.com. |
| 41000 | Servers are busy. Please try again later. |
| 42000 | Visualization succeeded |
| 42001 | Visualization is pending |
| 42002 | Visualization failed |
| 42003 | Visualization invalid request |
| 42004 | Missing application visualization |
| 42005 | Too many URLs to visualize |
| 42006 | There is not inputs in app |
| 43001 | Search internal issue |
| 43002 | Search projection failure |
| 43003 | Search prediction failure |
| 43004 | Can only search by a fully indexed input |
| 46002 | Signup not permitted |
| 46003 | Filetype not supported |
| 60000 | License is active. |
| 60001 | License does not exist. |
| 60002 | License needs update. |
| 60003 | License has expired. |
| 60004 | License has been revoked. |
| 60006 | Exceeded volume limit on license |
| 99009 | Internal error |
