The outputs from one workflow can be used as the inputs in another workflow. This allows you to link together the models in a graph. This ability to link together models is the key to building targeted AI solutions.

## Supported input and output types

Different models accept different types of inputs and produce different types of inputs and produce different outputs.

#### Inputs

* Concept
* Image
* Image and video
* Text

#### Outputs

* Cluster
* Color
* Concept
* Concepts
* Embed
* Region with concept
* Region with embed
* Region masks with concepts
* Region with text
* Region with image

## Clarifai models: The building blocks

You can create workflows out of any custom models that you have created for your app. The inputs and outputs supported by your custom models will depend on the inputs and outputs supported by the Clarifai models that you have used to build them. Clarifai models support different inputs and outputs depending on how they are designed and what they are used for.

#### Models types that accept images and video

* Visual Classifier (output concept)
* Clusterer (output cluster)
* Visual Detector + Classifier (output region with concept)

#### Models types that accept images only

* Image cropper (output image)

#### Models that accept concepts

* Concept Thresholder (output concepts)
* Concept Synonym Mapper (output concepts)

#### Models that accept text

* Text classifier (output concept)

#### Models that accept any input type

* Annotation writer (no outputs, writes annotation)
* Random sampler (any output type)
* Email alert (any output type)
* SMS Alert (any output type)
* Deep training (any output type)
