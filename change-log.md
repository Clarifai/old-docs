## 5.10

### New Feature

* Created display for scopes on collaborator invitations, allowing users to easily understand and control the scope of access allowed for app collaborators
* Deployed new face detector for improved face detection performance over images and video
* Created negative embeddings enhancements for improved model performance
* Completed annotation counts, improving the user experience when annotating inputs
* Created evaluation metrics for custom facial recognition in backend for improved facial recognition performance
* Created delete email endpoint
* Created GetSharedApps endpoint
* Implement ApplicationSharing endpoints
* Deployed General Detection Model
* Return custom detection evaluations through the GO API
* Custom detection training with new datadump
* Created Cluster loading UX

### Improvement

* Topological sort for workflows
* Added helper text/suggestions to improve Portal user experience  
* Header Search return app_owner's user info in collaboration endpoints
* Improved billing for app sharing
* Created collaboration tab in Portal, making it easy to add collaborators to apps
* Created display to show the user who invited you to collaborate on an app
* Update email phrases for collaborator invitations
* Cleaned up duplicate models in workflow model list
* PATCH /inputs needs to check status of asset before patching
* Removed sync DELETE /inputs after runtime config tested
* Changed POST /inputs to be async always to simplify processing of workflows after API client tests updated
* Deployed public general v1.5 in concept model
* Improved app sharing package to support HumanLabeler
* Create Pixel Training Hyperparameter Help Guide
* Improved cluster page performance
* Added pagination to clusters making for easier data management
