---
description: >-
  Clarifai supports the most popular image, video and text formats for your
  input data.
---

# Your Data

Upload your inputs into the Clarifai platform for data labeling, training new models, search, or predictions. The platform can upload images, video and text from URLs or from a local directory.

## Inputs and outputs guide

### Example:

When choosing one of Clarifai's pre-built models, you might see something like this from our `person-vehicle` model:


Input Type    | Output Type
------------- | -------------
image        | regions[...].data.concepts, regions[...].region\_info.bounding\_box

These inputs and outputs can be clarified with the following table explaining these data types:

### Table of uploadable data types:

Data Type  | Meaning
---------- | -------------
text  | This is freeform plain text which can be uploaded via raw text or specified with a URI.
image | This is an image in an accepted format, which currently includes JPG, PNG, TIFF, BMP, WEBP, CSV, and TSV. It can be uploaded via base64 bytes or specified with a URI.
video | This is video in an accepted format, which currently includes AVI, MP4, WMV, MOV, GIF, and 3GPP. It can be uploaded via base64 bytes or specified with a URI.


All these data formats are read in as raw bytes in base64 format.

### Table of single data types passed between models:

Data Type  | Meaning
---------- | -------------
embeddings | Vector representions of data passed from model to model. These are not uploadable by users.
clusters | These are IDs that identify clusters. These are primarily used for image search.
concepts | The list of concepts used in a model. For the general model, these would be the top 20 concepts with classified with the highest confidence.

### Table of `regions[...]` data types:

The notation of `[...]` means that the variable is a list of things, so `regions[...]` represents a list of regions of data. This could be parts of an image, text, video, or audio:

Data Type     | Meaning
------------- | -------------
regions[...].region_info.point  | This is a list of points which specify regions of an image.
regions[...].region_info.bounding\_box  | This is a list of regions each containing the four corners of a bounding box in a specific region of an image.
regions[...].region_info.mask |  The mask is an overlay of the entire image, with the specific concepts pixels set to a certain color.
regions[...].data.text | This is a list of regions and their associated text. This could be OCR data for an image, or subtext within a larger text for NLP.
regions[...].data.embeddings |  This is a list of regions and their associated vector representions.
regions[...].data.concepts | This is a list of regions and their associated or high confidence concepts.

### Table of `frames[...]` data types:

The notation of `[...]` means that the variable is a list of things, so `frames[...]` represents a list of frames of video or audio, and therefore `frames[...].data.regions[...]` represents a 2D matrix of the number of frames by the number of regions in each frame.

Data Type     | Meaning
------------- | -------------
frames[...].data.regions[...].region\_info.bounding\_box | These are the four corners of a bounding box in a specific region of a specific frame of video.
frames[...].data.regions[...].data.concepts | This is the matrix of frames and regions containing the  concepts used in a model. For the general model, these would be the top 20 concepts with classified with the highest confidence in a specific region of a specific frame of video.
frames[...].data.regions[...].track_id |  This is the matrix of frames and regions containing a tracking ids used to track objects across frames of a video.
