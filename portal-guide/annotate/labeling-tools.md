---
description: Learn about the labeling tools that are available to you in Scribe.
---

# Labeling Tools

{% embed url="https://youtu.be/5bg51zyebC0" caption="Clarifai Scribe: Labeling for Bounding Box Detection" %}

Scribe provides special tools for working with images and video.

![label bounding box](../../.gitbook/assets/label_bounding_box%20%281%29%20%284%29%20%284%29%20%286%29.jpg)

## Images

### Brightness, saturation and color inversion

![invert colors](../../.gitbook/assets/brightness.jpg) ![](../../.gitbook/assets/saturation.jpg) ![](../../.gitbook/assets/invert%20%284%29%20%284%29%20%285%29.jpg)

You can enhance the visibility of your photos with image adjustments. Image adjustments can be combined. Just click reset to return to the original version of your input.

### Zoom and pan

![pan image](../../.gitbook/assets/zoom.jpg) ![](../../.gitbook/assets/pan.jpg)

Powerful zoom and panning features allow you to closely inspect specific regions of an image. Just click reset to return to 100% zoom.

## Shortcuts

![scribe shortcuts](../../.gitbook/assets/shortcuts.jpg)

### General Keyboard shortcuts

* Left arrow - Previous input
* Right arrow - Next input
* Enter - Submit label

### Image Keyboard shortcuts

* B - Brightness
* S - Saturation
* I - Inversion

## Video

Scribe provides powerful tools for labeling video. When working with video, you can leverage video interpolation tools to quickly label thousands of individual frames of video. This rapid labeling technique makes video an excellent source of training data, even if you want your model to primarily analyze still images. You can QuickTrain and DeepTrain models on video data that has been labeled in Scribe.

### Interpolation

Interpolation allows you to quickly label multiple frames of video with the same concept. Simply select the interpolation icon and draw a bounding box around the object that you would like to label. Then scrub the video player to a new point in the video and move and adjust the bounding box to the new location of the object. Interpolation will automatically draw a series of bounding boxes between them.

![video interpolation](../../.gitbook/assets/interpolation%20%281%29%20%281%29%20%281%29.jpg)

### Video Keyboard shortcuts

* Q - Start of video
* W - Scrub backward
* E - Scrub forward
* R - End of video

## Text

Scribe makes it easy to label your text data. You can review text inputs in the same view that you would reveiw images for classification tasks.

![label text](../../.gitbook/assets/label-text.jpg)

