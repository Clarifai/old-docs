## Upcoming API Changes for Clarifai

Here is a list of upcoming changes to the API that we want you to be aware of well in advance. Some
of the changes may be scheduled downtime, others may require you to update your client side code
in order to operate properly with changes to the API specifications. We created this page with the
mindset of being as transparent as possible about upcoming changes so you as a Clarifai user can
plan corresponding changes to your codebase.

The dates listed in the following table are the date we plan to make the change. We may actually
make the change in the days following the specified date. However, to be safe, your client side code
needs updating before that date to minimize any downtime to your applications.

We will continue to update this page regularly, so a good way to always stay up to date is to
watch our [documentation repo on GitHub](https://github.com/Clarifai/docs).

### Completed Changes

Coming soon...

### Upcoming Changes

| Change | Date |
| ------ | ---- |
| **Scheduled Database Downtime**<br>We plan to upgrade our database to make it faster and provide more space for your applications. We expect a few minutes of downtime during this upgrade.  | September 10, 2019. 8:00pm |
| **`POST /inputs` will only be async**<br>We are cleaning up some inconsistent behaviour in the API where a single image added with `POST /inputs` was a synchronouse operation, but a batch of images as asynchronous. We are making both asynchronous. This allows us to provide more advanced functionality with workflows that index your inputs as you add them.<br>What this means for your code is if you application relies on the input having been indexed after the `POST /inputs` call returns, you now need to add a second call to `GET /inputs/{input_id}` in order to check the status of the input you just added to look for SUCCESS status code.  | September 10, 2019 |
| **`DELETE /inputs` will only be async**<br>Along the same lines as the `POST /inputs` change to being completely asynchronous, we are cleaning up some inconsistent behaviour in the API for deletion. Previously, when a single image is deleted with `DELETE /inputs` or `DELETE /inputs/{input_id}` it was a synchronouse operation, but when a batch of images were delete it was asynchronous. We are making both asynchronous. This allows us to provide more advanced functionality with workflows that index your inputs as you add them.<br>What this means for your code is if you application relies on the input having been deleted after the `DELETE /inputs` or `DELETE /inputs/{input_id}` calls return, you now need to add a second call to `GET /inputs/{input_id}` in order to check that it fails with a not found error.  | September 10, 2019 |
| **`PATCH /inputs`** overwrite action change<br>The overwrite action when patching currently does some inconsistent behaviour. If you patch `data.metadata` or `data.geo` fields on an input that has concepts already added to it, the concepts will remain after the patch even though the patch action was `overwrite`.<br>Going forward, the overwrite behaviour will overwrite the entire `data` object with what is included in the `PATCH /inputs` API call. Therefore if concepts are not provided in the patch call, but were originally on that input, they will be erased (overwritten with an empty list of concepts). This is unlikely to change much in your application and you can keep existing behvaiour by always sending back the `data` object from `GET /input/{input_id}` along with any modification to it if you are using the overwrite action. | September 10, 2019 |
