# Secure Hosting

All hosted image URLs at Clarifai are authorized with a per-user token. The token is issued after a proper user authentication from the front-end in Portal.

## How Your Data is Stored

You begin by uploading an image from a local file (a.jpeg).

The Clarifai platform hosts the image onto S3, onto a bucket. The S3 URL of the file will not be presented to the world, so no one can access it.

Image hosting URLs are backed by an image hosting server with token-based authorization. Only with an authorized token, the images could be fetched from the hosted URLs.

Once you logout, without the proper token, the image URLs will not be able to be fetched without a proper token, even with a valid image URL.


## How Your Image is Retrieved

The image serving service will read image from S3, via S3 API, other than S3 web URLs.

You can fetch images via the image serving service, only with a proper authorized token issued upon a successful login.
