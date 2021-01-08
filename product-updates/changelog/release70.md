# Release 7.0

| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature%20%281%29%20%281%29%20%28181%29.jpg) | ![improvement](../../.gitbook/assets/improvement%20%2819%29%20%2838%29.jpg) | ![bug](../../.gitbook/assets/bug%20%28196%29%20%28452%29%20%281%29.jpg) | ![enterprise](../../.gitbook/assets/enterprise%20%2818%29%20%2816%29%20%281%29%20%2819%29.jpg) |

## Scribe

| Status | Details |
| :--- | :--- |
| New Feature | Return UserIDs for Reject/Approve annotation endpoint and fix bug |
| Bug | Integration test timeout when waiting for post input |
| Improvement | Sortable-tables for labeler tasks-list |

## Portal

| Status | Details |
| :--- | :--- |
| Bug | Fixed inconsistency in interpolation & drawing state |
| Bug | Fixed ghost transformer |
| Improvement | Migrate Front-End Deployment Jobs |
| Improvement | Enable all features for default user on local env |
| Improvement | Allow adding collaborator by non-primary email address |
| Bug | Fixed nil pointer dereference in model validation |
| Bug | Fixed nil pointer dereference in workflow validation |
| New Feature | Multi search item search support in Portal |
| New Feature | Support positive and negative metadata searches |
| New Feature | Add geo coordinates in bulk edit in explorer grid view |
| Improvement | display app-id in app-listing card |
| Improvement | Make the Portal header short |
| Improvement | display app re-indexing stats in data-mode \( internal-users \) |
| Improvement | Add Search By Region and Hiding region capabilities to Annotations & Proposals |
| Improvement | better CSV upload error messages |
| Improvement | Clean up Bulk labeling code |
| Bug | Fixed modelId is null in Model details page |
| Bug | Fixed model-versions not loading |
| Bug | Fixed collectors user-selection API-calls fail with invalid-token |
| Bug | Collectors pre & post-queue have incorrect labels. Fixed |
| Bug | Fixed copy user-id to clipboard in profile |
| Bug | Workflow Selection causes app crashes when using an empty workflow |
| Bug | Portal sub-pages doesn't load on refresh |
| Bug | Endless Concept Relation Calls |
| Bug | Annotations Panel shows no annotations in classification app. Fixed |
| Bug | User is able to create workflow without nodes \(click grey button\). Fixed |
| Bug | Fixed 404 notifs when fetching concept relations in proposals |
| Bug | Proposers - no relation type rendered if just model output |
| Bug | New workflow model id is incorrectly populated |
| Bug | Input Details page isn't confirming/showing the labelled concept |
| Bug | Fixed 1 Model version is being displayed in modelversionselector |
| Bug | Fixed copying apps |
| Bug | Fixed demo app to correctly load fonts |

## Armada

| Status | Details |
| :--- | :--- |
| Bug | When predicting by input ID, fall back to using the model if we fail to retrieve outputs from the DB |
| Bug | Publish videos separately when reindexing |
| Improvement | Prefer clarifai rehosted URLs over original urls when predicting |
| Bug | Fixed failure of cluster inferencing when no embeddings were received |
| Bug | Fix workflow failures in tracker workflows when there is no detection in the first frame |
| Bug | Validated training examples have bounding boxes in them during deep training. |

## Enlight

| Status | Details |
| :--- | :--- |
| Improvement | Revise template parameters |
| Bug | Fixed BERT EIDs |
| Bug | Fixed centroid tracker bug |
| New Feature | Centroid tracker Platform Integration |
| Sub-task | Landmark post processing in Python Media Processor |
| New Feature | Add `Track` export method to neural lite tracker handler |
| Bug | Fixed DST directory\_upload script |
| New Feature | Add model version descriptions |
| New Feature | Add new multilingual text similarity embed model version and update the Text workflow to use it. |
| New Feature | Add support for audio indexing and transfer learning |
| New Feature | Thread through audio support in the platform |

## API

| Status | Details |
| :--- | :--- |
| New Feature | Make gRPC Go client |
| Improvement | Add reading URL from CLARIFAI\_GRPC\_BASE to all clients |
| Improvement | Create endpoint for fetching relations of multiple concepts in one API call |
| Bug | Fixed app-description duplication on app-copy |
| Bug | Fixed tracker model prediction panic |
| Bug | Reclaimed infinite loop |
| Bug | Fixed incorrect asset count in pipeline |
| Bug | Fixed redis stream msg id to timestamp err |
| Bug | Fixed video ingestion using empty workflow |
| Bug | Fixed app description during app creation is not being saved. |

