# Secure Hosting

All hosted image URLs at Clarifai are authorized with a per-user token. The token is issued after a proper user authentication from the front-end in Portal.

## How Your Data is Stored

You begin by uploading an image from a local file (a jpeg for example).

The Clarifai platform hosts the image in an S3 bucket. The S3 URL of the file will not be presented to the world, so no one can access it.

Image hosting URLs are backed by an image hosting server with token-based authorization. Images can be only be fetched from the hosted URLs with an authorized token.

Once you logout, the image URLs will not be able to be fetched without a proper token, even with a valid image URL.


## How Your Image is Retrieved

The image serving service will read your image from S3, via the S3 API. S3 web URLs are not used.

You can only fetch images via the image serving service with a properly authorized token issued upon a successful login.
