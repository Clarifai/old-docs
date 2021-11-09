---
description: Changelog for Clarifai Release 7.0
---

# Release 7.0


| New Feature | Improvement | Bug Fix | Enterprise Only |
| :---: | :---: | :---: | :---: |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | ![improvement](../../.gitbook/assets/improvement.jpg) | ![bug](../../.gitbook/assets/bug.jpg) | ![enterprise](../../.gitbook/assets/enterprise.jpg) |

## Scribe

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Return UserIDs for Reject/Approve annotation endpoint and fix bug |
| ![bug](../../.gitbook/assets/bug.jpg) | Integration test timeout when waiting for post input |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Sortable-tables for labeler tasks-list |

## Portal

| Status | Details |
| :--- | :--- |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed inconsistency in interpolation & drawing state |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed ghost transformer |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Migrate Front-End Deployment Jobs |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Enable all features for default user on local env |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Allow adding collaborator by non-primary email address |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed nil pointer dereference in model validation |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed nil pointer dereference in workflow validation |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Multi search item search support in Portal |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Support positive and negative metadata searches |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Add geo coordinates in bulk edit in explorer grid view |
| ![improvement](../../.gitbook/assets/improvement.jpg) | display app-id in app-listing card |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Make the Portal header short |
| ![improvement](../../.gitbook/assets/improvement.jpg) | display app re-indexing stats in data-mode \( internal-users \) |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Add Search By Region and Hiding region capabilities to Annotations & Proposals |
| ![improvement](../../.gitbook/assets/improvement.jpg) | better CSV upload error messages |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Clean up Bulk labeling code |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed modelId is null in Model details page |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed model-versions not loading |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed collectors user-selection API-calls fail with invalid-token |
| ![bug](../../.gitbook/assets/bug.jpg) | Collectors pre & post-queue have incorrect labels. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed copy user-id to clipboard in profile |
| ![bug](../../.gitbook/assets/bug.jpg) | Workflow Selection causes app crashes when using an empty workflow |
| ![bug](../../.gitbook/assets/bug.jpg) | Portal sub-pages doesn't load on refresh |
| ![bug](../../.gitbook/assets/bug.jpg) | Endless Concept Relation Calls |
| ![bug](../../.gitbook/assets/bug.jpg) | Annotations Panel shows no annotations in classification app. Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | User is able to create workflow without nodes \(click grey button\). Fixed |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed 404 notifs when fetching concept relations in proposals |
| ![bug](../../.gitbook/assets/bug.jpg) | Proposers - no relation type rendered if just model output |
| ![bug](../../.gitbook/assets/bug.jpg) | New workflow model id is incorrectly populated |
| ![bug](../../.gitbook/assets/bug.jpg) | Input Details page isn't confirming/showing the labelled concept |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed 1 Model version is being displayed in modelversionselector |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed copying apps |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed demo app to correctly load fonts |

## Armada

| Status | Details |
| :--- | :--- |
| ![bug](../../.gitbook/assets/bug.jpg) | When predicting by input ID, fall back to using the model if we fail to retrieve outputs from the DB |
| ![bug](../../.gitbook/assets/bug.jpg) | Publish videos separately when reindexing |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Prefer clarifai rehosted URLs over original urls when predicting |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed failure of cluster inferencing when no embeddings were received |
| ![bug](../../.gitbook/assets/bug.jpg) | Fix workflow failures in tracker workflows when there is no detection in the first frame |
| ![bug](../../.gitbook/assets/bug.jpg) | Validated training examples have bounding boxes in them during deep training. |

## Enlight

| Status | Details |
| :--- | :--- |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Revise template parameters |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed BERT EIDs |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed centroid tracker bug |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Centroid tracker Platform Integration |
| Sub-task | Landmark post processing in Python Media Processor |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Add `Track` export method to neural lite tracker handler |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed DST directory\_upload script |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Add model version descriptions |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Add new multilingual text similarity embed model version and update the Text workflow to use it. |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Add support for audio indexing and transfer learning |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Thread through audio support in the platform |

## API

| Status | Details |
| :--- | :--- |
| ![new-feature](../../.gitbook/assets/new_feature.jpg) | Make gRPC Go client |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Add reading URL from CLARIFAI\_GRPC\_BASE to all clients |
| ![improvement](../../.gitbook/assets/improvement.jpg) | Create endpoint for fetching relations of multiple concepts in one API call |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed app-description duplication on app-copy |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed tracker model prediction panic |
| ![bug](../../.gitbook/assets/bug.jpg) | Reclaimed infinite loop |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed incorrect asset count in pipeline |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed redis stream msg id to timestamp err |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed video ingestion using empty workflow |
| ![bug](../../.gitbook/assets/bug.jpg) | Fixed app description during app creation is not being saved. |
