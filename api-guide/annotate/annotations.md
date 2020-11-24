---
description: Label your data.
---

# Annotations

## Annotations

Annotations \(also known as labels\) describe your inputs. When you add inputs to your app, we will create an input level annotation for each input. This input level annotation contains any data you provided in `POST /inputs` call. Models in your default workflow can also write annotations.

Once your input is successfully indexed, you can add additional annotations such as concepts and bounding boxes.

### Add Annotations

You can label your inputs by calling the `POST /annotations` endpoint. For example, you can add concept\(s\) to an image, draw a bounding box, or label concept\(s\) in a video frame.

When you add an annotation, the app's default workflow will not run by default. This means that the annotation will not be immediately available for training of your custom model or for visual search. To make the annotation available for AI based search and training, you need to provide `embed_model_version_id` field. This field specifies how to associate the annotation for your input to one of the embedding models in your default workflow. When associated during patching then we know how to index it for training and visual search, therefore if your use case includes those features it is recommended to provide this field on each add annotation call.

You can add from 1 up to 128 annotations in a single API call.

Each annotation should contain at most one region. If it is a video, each annotation should contain 1 frame. If there are multiple regions in a frame you want to label, you can add multiple annotations for each regoin and each annotation will be contained within the same frame but a different region.

#### Annotate images with concepts

To annotate a concept present anywhere in an image:

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_annotations_response = stub.PostAnnotations(
    service_pb2.PostAnnotationsRequest(
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                        resources_pb2.Concept(id="water", value=0.)  # 0 means false, this concept is not present.
                    ]
                ),
                embed_model_version_id="{EMBED_MODEL_VERSION_ID}"
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post annotations failed, status: " + post_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse postAnnotationsResponse = stub.postAnnotations(
    PostAnnotationsRequest.newBuilder().addAnnotations(
        Annotation.newBuilder()
            .setInputId("{YOUR_INPUT_ID}")
            .setData(
                Data.newBuilder().addConcepts(
                    Concept.newBuilder()
                        .setId("tree")
                        .setValue(1f)  // 1 means true, this concept is present.
                        .build()
                    ).addConcepts(
                        Concept.newBuilder()
                            .setId("water")
                            .setValue(0f)  // 0 means false, this concept is not present.
                            .build()
                    )
            ).setEmbedModelVersionId("{EMBED_MODEL_VERSION_ID}") // so the concept can be used for custom model training
            .build()
    ).build()
);

if (postAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post annotations failed, status: " + postAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostAnnotations(
    {
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                // 1 means true, this concept is present.
                // 0 means false, this concept is not present.
                data: {
                    concepts: [
                        {id: "tree", value: 1},
                        {id: "water", value: 0}
                    ]
                },
                embed_model_version_id: "{EMBED_MODEL_VERSION_ID}"
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "data": {
          "concepts": [
            {
              "id": "tree",
              "value": 1
            },
            {
              "id": "water",
              "value": 0
            }
          ]
        },
        "embed_model_version_id": "{EMBED_MODEL_VERSION_ID}"
      }
    ]
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

#### Annotate New Bounding Boxes in an Image

You can label a new bounding box by providing bounding box coordinates.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_annotations_response = stub.PostAnnotations(
    service_pb2.PostAnnotationsRequest(
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            region_info=resources_pb2.RegionInfo(
                                bounding_box=resources_pb2.BoundingBox(       # draw a bounding box
                                    top_row=0,
                                    left_col=0,
                                    bottom_row=0.5,
                                    right_col=0.5
                                )
                            ),
                            data=resources_pb2.Data(
                                concepts=[
                                    resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                                    resources_pb2.Concept(id="water", value=0.)  # 0 means false, this concept is not present.
                                ]
                            )
                        )
                    ]
                ),
                embed_model_version_id="{EMBED_MODEL_VERSION_ID}"
            ),
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            region_info=resources_pb2.RegionInfo(
                                bounding_box=resources_pb2.BoundingBox(        # draw another bounding box
                                    top_row=0.6,
                                    left_col=0.6,
                                    bottom_row=0.8,
                                    right_col=0.8
                                )
                            ),
                            data=resources_pb2.Data(
                                concepts=[
                                    resources_pb2.Concept(id="bike", value=1.),  # 1 means true, this concept is present.
                                ]
                            )
                        )
                    ]
                ),
                embed_model_version_id="{EMBED_MODEL_VERSION_ID}"
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post annotations failed, status: " + post_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse postAnnotationsResponse = stub.postAnnotations(
    PostAnnotationsRequest.newBuilder().addAnnotations(
        Annotation.newBuilder()                     // label a region in this image
            .setInputId("{YOUR_INPUT_ID}")
            .setData(
                Data.newBuilder().addRegions(
                    Region.newBuilder()
                        .setRegionInfo(
                            RegionInfo.newBuilder()
                                .setBoundingBox(        // draw a bounding box
                                    BoundingBox.newBuilder()
                                        .setTopRow(0f)
                                        .setLeftCol(0f)
                                        .setBottomRow(0.5f)
                                        .setRightCol(0.5f)
                                        .build()
                                )
                                .build()
                        )
                        .setData(
                            Data.newBuilder()
                                .addConcepts(
                                    Concept.newBuilder()
                                        .setId("tree")
                                        .setValue(1f)  // 1 means true, this concept is present.
                                        .build()
                                )
                                .addConcepts(
                                    Concept.newBuilder()
                                        .setId("water")
                                        .setValue(0f)  // 0 means false, this concept is not present.
                                        .build()
                                )
                        ).build()
                ).build()
            ).setEmbedModelVersionId("{EMBED_MODEL_VERSION_ID}") // so the concept can be used for custom model training
            .build()
    ).addAnnotations(                           // label another region in this image
            .setInputId("{YOUR_INPUT_ID}")
            .setData(
                Data.newBuilder().addRegions(
                    Region.newBuilder()
                        .setRegionInfo(
                            RegionInfo.newBuilder()
                                .setBoundingBox(        // draw another bounding box
                                    BoundingBox.newBuilder()
                                        .setTopRow(0.6f)
                                        .setLeftCol(0.6f)
                                        .setBottomRow(0.8f)
                                        .setRightCol(0.8f)
                                        .build()
                                )
                                .build()
                        )
                        .setData(
                            Data.newBuilder()
                                .addConcepts(
                                    Concept.newBuilder()
                                        .setId("bike")
                                        .setValue(1f)  // 1 means true, this concept is present.
                                        .build()
                                )
                        ).build()
                ).build()
            ).setEmbedModelVersionId("{EMBED_MODEL_VERSION_ID}") // so the concept can be used for custom model training
            .build()
    ).build()
);

if (postAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post annotations failed, status: " + postAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostAnnotations(
    {
        annotations: [
            {                     // label a region in this image
                input_id: "{YOUR_INPUT_ID}",
                data: {
                    regions: [
                        {
                            region_info: {
                                bounding_box: {        // draw a bounding box
                                    top_row: 0,
                                    left_col: 0,
                                    bottom_row: 0.5,
                                    right_col: 0.5
                                }
                            }
                            // 1 means true, this concept is present.
                            // 0 means false, this concept is not present.
                            data: {
                                concepts: [
                                    {id: "tree", value: 1},
                                    {id: "water", value: 0}
                                ]
                            },
                        }
                    ]
                }
                embed_model_version_id: "{EMBED_MODEL_VERSION_ID}"
            }, {                     // label another region in this image
                input_id: "{YOUR_INPUT_ID}",
                data: {
                    regions: [
                        {
                            region_info: {
                                bounding_box: {        // draw another bounding box
                                    top_row: 0.6,
                                    left_col: 0.6,
                                    bottom_row: 0.8,
                                    right_col: 0.8
                                }
                            }
                            // 1 means true, this concept is present.
                            // 0 means false, this concept is not present.
                            data: {
                                concepts: [
                                    {id: "bike", value: 1},
                                ]
                            },
                        }
                    ]
                }
                embed_model_version_id: "{EMBED_MODEL_VERSION_ID}"
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
# draw 2 bouding boxes in the same region
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "data": {
          "regions": [
            {
              "region_info": {
                  "bounding_box": {
                      "top_row": 0,
                      "left_col": 0,
                      "bottom_row": 0.5,
                      "right_col": 0.5
                  }
              },
              "data": {
                "concepts": [
                  {
                    "id": "tree",
                    "value": 1
                  },
                  {
                    "id": "water",
                    "value": 0
                  }
                ]
              }
            }
          ]
        },
        "embed_model_version_id": "{EMBED_MODEL_VERSION_ID}"
      }, {
        "input_id": "{YOUR_INPUT_ID}",
        "data": {
          "regions": [
            {
              "region_info": {
                  "bounding_box": {
                      "top_row": 0.6,
                      "left_col": 0.6,
                      "bottom_row": 0.8,
                      "right_col": 0.8
                  }
              },
              "data": {
                "concepts": [
                  {
                    "id": "bike",
                    "value": 1
                  }
                ]
              }
            }
          ]
        },
        "embed_model_version_id": "{EMBED_MODEL_VERSION_ID}"
      }
    ]
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

#### Annotate Existing Regions in an Image

When you add an input, detection models \(such as `Face Detection` or `General Detection`\) will detect regions in your image where there appear to be relevant objects. You can check these detected regions by listing model's annotations. Your labels should be contained within `Region.Data`. Each annotation can have only 1 region. If you want to label multiple regions, it is possible to label multiple annotations in a single API call.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_annotations_response = stub.PostAnnotations(
    service_pb2.PostAnnotationsRequest(
        annotations=[
            resources_pb2.Annotation(                # label a region in this image
                input_id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            id="{REGION_ID_1}" ,  # this should be a region id returned from list annotations call
                            data=resources_pb2.Data(
                                concepts=[
                                    resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                                    resources_pb2.Concept(id="water", value=0.)  # 0 means false, this concept is not present.
                                ]
                            )
                        )
                    ]
                ),
                embed_model_version_id="{EMBED_MODEL_VERSION_ID}"
            ),
            resources_pb2.Annotation(                # label another region in this image
                input_id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            id="{REGION_ID_2}" ,  # this should be a region id returned from list annotations call
                            data=resources_pb2.Data(
                                concepts=[
                                    resources_pb2.Concept(id="bike", value=1.),  # 1 means true, this concept is present.
                                ]
                            )
                        )
                    ]
                ),
                embed_model_version_id="{EMBED_MODEL_VERSION_ID}"
            ),
        ]
    ),
    metadata=metadata
)

if post_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post annotations failed, status: " + post_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse postAnnotationsResponse = stub.postAnnotations(
    PostAnnotationsRequest.newBuilder().addAnnotations(
        Annotation.newBuilder()                // label a region in this image
            .setInputId("{YOUR_INPUT_ID}")
            .setData(
                Data.newBuilder().addRegions(
                    Region.newBuilder()
                        .setId("{REGION_ID_1}") // this should be a region id returned from list annotations call
                        .setData(
                            Data.newBuilder().addConcepts(
                                Concept.newBuilder()
                                    .setId("tree")
                                    .setValue(1f)  // 1 means true, this concept is present.
                                    .build()
                                ).addConcepts(
                                    Concept.newBuilder()
                                        .setId("water")
                                        .setValue(0f)  // 0 means false, this concept is not present.
                                        .build()
                                )
                        ).build()
                ).build()
            ).setEmbedModelVersionId("{EMBED_MODEL_VERSION_ID}") // so the concept can be used for custom model training
            .build()
    ).AddAnnotations(
        Annotation.newBuilder()                // label another region in the same image
            .setInputId("{YOUR_INPUT_ID}")
            .setData(
                Data.newBuilder().addRegions(
                    Region.newBuilder()
                        .setId("{REGION_ID_2}") // this should be a region id returned from list annotations call
                        .setData(
                            Data.newBuilder().addConcepts(
                                Concept.newBuilder()
                                    .setId("bike")
                                    .setValue(1f)  // 1 means true, this concept is present.
                                    .build()
                                )
                        ).build()
                ).build()
            ).setEmbedModelVersionId("{EMBED_MODEL_VERSION_ID}") // so the concept can be used for custom model training
            .build()
    ).build()
);

if (postAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post annotations failed, status: " + postAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostAnnotations(
    {
        annotations: [
            {                // label a region in this image
                input_id: "{YOUR_INPUT_ID}",
                data: {
                    regions: [
                        {
                            id: "{REGION_ID_1}" // this should be a region id  returned from list annotations call
                            // 1 means true, this concept is present.
                            // 0 means false, this concept is not present.
                            data: {
                                concepts: [
                                    {id: "tree", value: 1},
                                    {id: "water", value: 0}
                                ]
                            },
                        }
                    ]
                }
                embed_model_version_id: "{EMBED_MODEL_VERSION_ID}"
            }, {                // label another region in this image
                input_id: "{YOUR_INPUT_ID}",
                data: {
                    regions: [
                        {
                            id: "{REGION_ID_2}" // this should be a region id  returned from list annotations call
                            // 1 means true, this concept is present.
                            // 0 means false, this concept is not present.
                            data: {
                                concepts: [
                                    {id: "bike", value: 1},
                                ]
                            },
                        }
                    ]
                }
                embed_model_version_id: "{EMBED_MODEL_VERSION_ID}"
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
# region id should be a region id returned from list annotations call
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "data": {
          "regions": [
            {
              "id": "{REGION_ID_1}",
              "data": {
                "concepts": [
                  {
                    "id": "tree",
                    "value": 1
                  },
                  {
                    "id": "water",
                    "value": 0
                  }
                ]
              }
            }
          ]
        },
        "embed_model_version_id": "{EMBED_MODEL_VERSION_ID}"
      }, {
        "input_id": "{YOUR_INPUT_ID}",
        "data": {
          "regions": [
            {
              "id": "{REGION_ID_2}",
              "data": {
                "concepts": [
                  {
                    "id": "bike",
                    "value": 1
                  }
                ]
              }
            }
          ]
        },
        "embed_model_version_id": "{EMBED_MODEL_VERSION_ID}"
      }
    ]
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

#### Annotate Images with Different `user_id` and `status`.

Each annotation is tied to a user or a model in your workflow. By default, when a user posts an annotation, this user is the owner of the annotation. Sometimes however, you might want to post an annotation as other user, for example, when assigning an image to another user, an annotation can be created with another user\_id \(and status `PENDING`\).

Note: only the app owner can post an annotation with other user's `user_id`, collaborators cannot.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_annotations_response = stub.PostAnnotations(
    service_pb2.PostAnnotationsRequest(
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                user_id="{USER_ID}",    # If empty, it is the user who posts this annotation
                data=status_pb2.Status(
                    code=status_code_pb2.ANNOTATION_PENDING  # annotation pending status. By default success.
                ),
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post annotations failed, status: " + post_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse postAnnotationsResponse = stub.postAnnotations(
    PostAnnotationsRequest.newBuilder().addAnnotations(
        Annotation.newBuilder()
            .setInputId("{YOUR_INPUT_ID}")
            .setUserId("{USER_ID}")  // If empty, it is the user who posts this annotation
            .setStatus(
                Status.newBuilder()
                    .setCodeValue(StatusCode.ANNOTATION_PENDING_VALUE) // annotation pending status. By default, it's ANNOTATION_SUCCESS_VALUE.
                    .build()
            )
            .build()
    ).build()
);

if (postAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post annotations failed, status: " + postAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostAnnotations(
    {
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                user_id: "{USER_ID}",  // If empty, it is the user who posts this annotation
                status: {
                    code: 24151    // annotation pending status. By default success.
                }
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "user_id": "{USER_ID}",
        "status": {
            "code": "ANNOTATION_PENDING"
        }
      }
    ]
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

### List Annotations

You can get a list of annotations within your app with a GET call. Annotations will be returned from oldest to newest.

These requests are paginated. By default each page will return 20 annotations.

#### List All User Created Annotations in Your App

To list all your user labelled annotations.

Note this will not show annotations by models in your worfklow. To include model created annotations, you need to set `list_all_annotations` to `true`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(per_page=10),
    metadata=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List annotations failed, status: " + list_annotations_response.status.description)

for annotation_object in list_annotations_response.annotations:
    print(annotation_object)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .setPerPage(10)
        .setPage(1)  // Pages start at 1.
        .build()
);

if (listAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List annotations failed, status: " + listAnnotationsResponse.getStatus());
}

for (Annotation annotation : listAnnotationsResponse.getAnnotationsList()) {
    System.out.println(annotation);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListAnnotations(
    {page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List annotations failed, status: " + response.status.description);
        }

        for (const annotation of response.annotations) {
            console.log(JSON.stringify(annotation, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10
```
{% endtab %}
{% endtabs %}

#### List All Annotations in Your App

List all annotations, including models created.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(per_page=10, list_all_annotations=True),
    metadata=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List annotations failed, status: " + list_annotations_response.status.description)

for annotation_object in list_annotations_response.annotations:
    print(annotation_object)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .setPerPage(10)
        .setListAllAnnotations(true)
        .setPage(1)  // Pages start at 1.
        .build()
);

if (listAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List annotations failed, status: " + listAnnotationsResponse.getStatus());
}

for (Annotation annotation : listAnnotationsResponse.getAnnotationsList()) {
    System.out.println(annotation);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListAnnotations(
    {list_all_annotations: true, page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List annotations failed, status: " + response.status.description);
        }

        for (const annotation of response.annotations) {
            console.log(JSON.stringify(annotation, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&list_all_annotations=true
```
{% endtab %}
{% endtabs %}

#### List User Created Annotations by Input IDs

To list all user created annotations for certain input \(one or several\), provide a list of input IDs.

Note: this will not show annotations by models in your worfklow. To include model created annotations, you need to set `list_all_annotations` to `true`.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(input_ids=["{YOUR_INPUT_ID_1}". "{YOUR_INPUT_ID_2}"], per_page=10),
    metadta=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List annotations failed, status: " + list_annotations_response.status.description)

for annotation_object in list_annotations_response.annotations:
    print(annotation_object)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .addInputIds("{YOUR_INPUT_ID_1}")
        .addInputIds("{YOUR_INPUT_ID_2}")
        .setPerPage(10)
        .setPage(1)  // Pages start at 1.
        .build()
);

if (listAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List annotations failed, status: " + listAnnotationsResponse.getStatus());
}

for (Annotation annotation : listAnnotationsResponse.getAnnotationsList()) {
    System.out.println(annotation);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListAnnotations(
    {input_ids: ["{YOUR_INPUT_ID_2}", "{YOUR_INPUT_ID_2}"], page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List annotations failed, status: " + response.status.description);
        }

        for (const annotation of response.annotations) {
            console.log(JSON.stringify(annotation, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&input_ids=your_input_Id
```
{% endtab %}
{% endtabs %}

#### List Annotations by Input IDs and Annotation IDs

You can list annotations by both input IDs and annotation IDs. Number of input IDs and annotation IDs should be the same. Since we are finding annotatieon by IDs this will match any user or model created annotations.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(
       input_ids=["{YOUR_INPUT_ID_1}". "{YOUR_INPUT_ID_2}"]
        ids=["{YOUR_ANNOTATION_ID_1}", "{YOUR_ANNOTATION_ID_2}"],
        per_page=10
    ),
    metadata=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List annotations failed, status: " + list_annotations_response.status.description)

for annotation_object in list_annotations_response.annotations:
    print(annotation_object)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .setPerPage(10)
        .addInputIds("{YOUR_INPUT_ID_1}").
        .addInputIds("{YOUR_INPUT_ID_2}").
        .addIds("{YOUR_ANNOTATION_ID_1}")
        .addIds("{YOUR_ANNOTATION_ID_2}")
        .build()
);

if (listAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List annotations failed, status: " + listAnnotationsResponse.getStatus());
}

for (Annotation annotation : listAnnotationsResponse.getAnnotationsList()) {
    System.out.println(annotation);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListAnnotations(
    {
        input_ids: ["{YOUR_INPUT_ID_2}", "{YOUR_INPUT_ID_2}"],
        ids: ["{YOUR_ANNOTATION_ID_1}", "{YOUR_ANNOTATION_ID_2}"],
        page: 1, per_page: 10
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List annotations failed, status: " + response.status.description);
        }

        for (const annotation of response.annotations) {
            console.log(JSON.stringify(annotation, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&input_ids=YOUR_INPUT_ID_1&input_ids=YOUR_INPUT_ID_2&ids=YOUR_ANNOTATION_ID_1&ids=YOUR_ANNOTATION_ID_2
```
{% endtab %}
{% endtabs %}

#### List Annotations by User IDs

An annotation is created by either a user or a model. You can list annotations created by specific user\(s\) by provider their user IDs.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(user_ids=["{USER_ID_1}", "{USER_ID_2}"], per_page=10),
    metadata=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List annotations failed, status: " + list_annotations_response.status.description)

for annotation_object in list_annotations_response.annotations:
    print(annotation_object)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .addUserIds("{USER_ID_1}")
        .addUserIds("{USER_ID_2}")
        .setPerPage(10)
        .build()
);

if (listAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List annotations failed, status: " + listAnnotationsResponse.getStatus());
}

for (Annotation annotation : listAnnotationsResponse.getAnnotationsList()) {
    System.out.println(annotation);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListAnnotations(
    {user_ids: ["{USER_ID_1}", "{USER_ID_2}"], page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List annotations failed, status: " + response.status.description);
        }

        for (const annotation of response.annotations) {
            console.log(JSON.stringify(annotation, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&user_ids=USER_ID_1&user_ids=USER_ID_2
```
{% endtab %}
{% endtabs %}

#### List Annotations by Model Version IDs

An annotation is created by either a user or a model. For example if your workflow has a detection model, when you add input, the model will detect objects in your input. You can see these detected objects by listing the annotations created detection model. You can also label these regions by using `Post annotation` with the region id returned from this call.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

list_annotations_response = stub.ListAnnotations(
    service_pb2.ListAnnotationsRequest(
        model_version_ids=["{MODEL_VERSION_ID_1}", "{MODEL_VERSION_ID_2}"],
        per_page=10
    ),
    metadata=metadata
)

if list_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("List annotations failed, status: " + list_annotations_response.status.description)

for annotation_object in list_annotations_response.annotations:
    print(annotation_object)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .addModelVersionIds("{MODEL_VERSION_ID_1}")
        .addModelVersionIds("{MODEL_VERSION_ID_2}")
        .setPerPage(10)
        .build()
);

if (listAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("List annotations failed, status: " + listAnnotationsResponse.getStatus());
}

for (Annotation annotation : listAnnotationsResponse.getAnnotationsList()) {
    System.out.println(annotation);
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.ListAnnotations(
    {model_version_ids: ["{MODEL_VERSION_ID_1}", "{MODEL_VERSION_ID_2}"], page: 1, per_page: 10},
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("List annotations failed, status: " + response.status.description);
        }

        for (const annotation of response.annotations) {
            console.log(JSON.stringify(annotation, null, 2));
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&model_version_ids=MODEL_VERSION_ID_1&model_version_ids=MODEL_VERSION_ID_2
```
{% endtab %}
{% endtabs %}

### Update Annotations

Changing annotation data is possible by PATCHing exisitng annotations. The application owner can change any user-created annotations. Collaborators are not allowed to change annotations made by other collaborators.

Generally speaking, you should send PATCH when you want to change the data you have posted, for example, changing the concept from positive to negative or adjusting the bbounding box cooridnates. If you want to adding more tags, you can always POST new annotations. There is no limit on how many annotations an input can have.

Update supports overwrite, merge, remove actions. You can update from 1 up to 128 annotations in a single API call.

#### Update Annotation with Concepts

Update an annotation of a image with a new concept, or to change a concept value from true to false \(or vice versa\).

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_annotations_response = stub.PatchAnnotations(
    service_pb2.PatchAnnotationsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove.
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                id="{YOUR_ANNOTATION_ID}",
                data=resources_pb2.Data(
                    concepts=[
                        resources_pb2.Concept(id="apple", value=1.)  # 1 means true, this concept is present.
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch annotations failed, status: " + patch_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse patchAnnotationsResponse = stub.patchAnnotations(
    PatchAnnotationsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove.
        .addAnnotations(
        Annotation.newBuilder()
            .setInputId("{YOUR_INPUT_ID}")
            .setId("{YOUR_ANNOTATION_ID}")
            .setData(
                Data.newBuilder().addConcepts(
                    Concept.newBuilder()
                        .setId("apple")
                        .setValue(1f)  // 1 means true, this concept is present.
                        .build()
                    )
            )
            .build()
    ).build()
);

if (patchAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch annotations failed, status: " + patchAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchAnnotations(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove.
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                id: "{YOUR_ANNOTATION_ID}",
                // 1 means true, this concept is present.
                // 0 means false, this concept is not present.
                data: {
                    concepts: [
                        {id: "apple", value: 1}
                    ]
                }
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
# Value of 1 means true, this concept is present.
# Value of 0 means false, this concept is not present.
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "id": "{YOUR_ANNOTATION_ID}",
        "data": {
          "concepts": [
            {
              "id": "apple",
              "value": 1
            }
          ]
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

#### Update Annotation with Concepts in a Region

When you update region data, you must nest this new data within region.data. Set the region\_id to the current region\_id if you do not want to change or remove this region.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_annotations_response = stub.PatcchAnnotations(
    service_pb2.PatchAnnotationsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove.
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                id="{YOUR_ANNOTATION_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            id="{REGION_ID}" ,  # this should be the region id of this annotation before patch
                            data=resources_pb2.Data(
                                concepts=[
                                    resources_pb2.Concept(id="tree", value=1.),  # 1 means true, this concept is present.
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch annotations failed, status: " + patch_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse patchAnnotationsResponse = stub.patchAnnotations(
    PatchAnnotationsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove.
        .addAnnotations(
            Annotation.newBuilder()
                .setInputId("{YOUR_INPUT_ID}")
                .setId("{YOUR_ANNOTATION_ID}")
                .setData(
                    Data.newBuilder().addRegions(
                        Region.newBuilder()
                            .setId("{REGION_ID}") // this should be the region id of this annotation
                            .setData(
                                Data.newBuilder().addConcepts(
                                    Concept.newBuilder()
                                        .setId("apple")
                                        .setValue(1f)  // 1 means true, this concept is present.
                                        .build()
                                    )
                            ).build()
                    ).build()
                )
                .build()
    ).build()
);

if (patchAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch annotations failed, status: " + patchAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchAnnotations(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove.
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                id: "{YOUR_ANNOTATION_ID}",
                data: {
                    regions: [
                        {
                            id: "{REGION_ID}" // this should be the region id of this annotation before patch
                            // 1 means true, this concept is present.
                            data: {
                                concepts: [
                                    {id: "apple", value: 1},
                                ]
                            },
                        }
                    ]
                }
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
# Value of 1 means true, this concept is present.
# region id should be the region id of this annotation before patch
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "id": "{YOUR_ANNOTATION_ID}",
        "data": {
          "regions": [
            {
              "id": "{REGION_ID}",
              "data": {
                "concepts": [
                  {
                    "id": "apple",
                    "value": 1
                  }
                ]
              }
            }
          ]
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

#### Update Annotation Region Coordinates

You can update region bounding boxes coordinates. When changing the region, you should use `overwrite` action. With `overwrite` action, you need to provide any data you want to keep in this annotation.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_annotations_response = stub.PatcchAnnotations(
    service_pb2.PatchAnnotationsRequest(
        action="overwrite",
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                id="{YOUR_ANNOTATION_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            region_info=resources_pb2.RegionInfo(
                                bounding_box=resources_pb2.BoundingBox(        # move bounding bbox to a new cooridnates
                                    top_row=0.5,
                                    left_col=0.5,
                                    bottom_row=0.8,
                                    right_col=0.8
                                )
                            ),
                            data=resources_pb2.Data(    # need to provde tags you previously labeled since this is overwrite action
                                concepts=[
                                    resources_pb2.Concept(id="bike", value=1.),  # 1 means true, this concept is present.
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch annotations failed, status: " + patch_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse patchAnnotationsResponse = stub.patchAnnotations(
    PatchAnnotationsRequest.newBuilder()
        .setAction("overwrite")
        .addAnnotations(
            Annotation.newBuilder()
                .setInputId("{YOUR_INPUT_ID}")
                .setId("{YOUR_ANNOTATION_ID}")
                .setData(
                    Data.newBuilder().addRegions(
                        Region.newBuilder()
                            .setRegionInfo(
                                RegionInfo.newBuilder()
                                    .setBoundingBox(        // move bounding box to a new cooridnates
                                        BoundingBox.newBuilder()
                                            .setTopRow(0.5f)
                                            .setLeftCol(0.5f)
                                            .setBottomRow(0.8f)
                                            .setRightCol(0.8f)
                                            .build()
                                    )
                                    .build()
                            )
                            .setData(
                                Data.newBuilder()
                                    .addConcepts(
                                        Concept.newBuilder()
                                            .setId("bike")
                                            .setValue(1f)  // 1 means true, this concept is present.
                                            .build()
                                    )
                            ).build()
                    ).build()
                )
                .build()
    ).build()
);

if (patchAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Patch annotations failed, status: " + patchAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchAnnotations(
    {
        action: "overwrite",
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                id: "{YOUR_ANNOTATION_ID}",
                data: {
                    regions: [
                        {
                            region_info: {
                                bounding_box: {        // move bounding box to a new coordiates
                                    top_row: 0.5,
                                    left_col: 0.5,
                                    bottom_row: 0.8
                                    right_col: 0.8
                                }
                            }
                            // 1 means true, this concept is present.
                            // 0 means false, this concept is not present.
                            data: {
                                concepts: [
                                    {id: "bike", value: 1},
                                ]
                            },
                        }
                    ]
                }
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
# Value of 1 means true, this concept is present.
# region id should be the region id of this annotation before patch
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "id": "{YOUR_ANNOTATION_ID}",
        "data": {
          "regions": [
            {
              "id": "{REGION_ID}",
              "data": {
                "concepts": [
                  {
                    "id": "apple",
                    "value": 1
                  }
                ]
              }
            }
          ]
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

#### Update Annotation Status

You can update an annotation status.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

patch_annotations_response = stub.PatchAnnotations(
    service_pb2.PatchAnnotationsRequest(
        action="merge",  # Supported actions: overwrite, merge, remove.
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                id="{YOUR_ANNOTATION_ID}",
                status=status_pb2.Status(
                    code=status_code_pb2.ANNOTATION_SUCCESS
                )
            )
        ]
    ),
    metadata=metadata
)

if patch_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Patch annotations failed, status: " + patch_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiAnnotationResponse patchAnnotationsResponse = stub.patchAnnotations(
    PatchAnnotationsRequest.newBuilder()
        .setAction("merge")  // Supported actions: overwrite, merge, remove.
        .addAnnotations(
        Annotation.newBuilder()
            .setInputId("{YOUR_INPUT_ID}")
            .setId("{YOUR_ANNOTATION_ID}")
            .setStatus(
                Status.newBuilder()
                    .setCodeValue(StatusCode.ANNOTATION_SUCCESS_VALUE)
                    .build()
            )
            .build()
    ).build()
);

if (patchAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("patch annotations failed, status: " + patchAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PatchAnnotations(
    {
        action: "merge",  // Supported actions: overwrite, merge, remove.
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                id: "{YOUR_ANNOTATION_ID}",
                status: {
                    code: 24150
                }
            }
        ]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Patch annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X PATCH \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "annotations": [
      {
        "input_id": "{YOUR_INPUT_ID}",
        "id": "{YOUR_ANNOTATION_ID}",
        "status": {
          "code": "ANNOTATION_SUCCESS"
        }
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

### Delete Annotations

#### Delete Annotation by Input ID and Annotation ID

You can delete a single annotation by input ID and annotation ID.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_annotation_response = stub.DeleteAnnotation(
    service_pb2.DeleteAnnotationRequest(
        input_id="{YOUR_INPUT_ID}",
        annotation_id="{YOUR_ANNOTATION_ID}"
    ),
    metadata=metadata
)

if delete_annotation_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete annotation failed, status: " + delete_annotation_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteAnnotationResponse = stub.deleteAnnotation(
    DeleteAnnotationRequest.newBuilder()
        .setInputId("{YOUR_INPUT_ID}")
        .setAnnotationId("{YOUR_ANNOTATION_ID}")
        .build()
);

if (deleteAnnotationResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete annotation failed, status: " + deleteAnnotationResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteAnnotation(
    {
        input_id: "{YOUR_INPUT_ID}",
        annotation_id: "{YOUR_ANNOTATION_ID}"
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete annotation failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs/{YOUR_INPUT_ID}/annotations/{YOUR_ANNOTATION_ID}
```
{% endtab %}
{% endtabs %}

#### Bulk Delete Annotations by Input Ids and Annotation IDs

You can delete multiple annotations in one API call. You need to provide a list of input IDs and a list of annotation IDs. The number of input IDs has to match number of annotation IDs.

{% tabs %}

```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_annotations_response = stub.DeleteAnnotations(
    service_pb2.DeleteAnnotationsRequest(
        input_ids=["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"],
        annotation_id=["{YOUR_ANNOTATION_ID_1}", "{YOUR_ANNOTATION_ID_2}"]
    ),
    metadata=metadata
)

if delete_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete annotations failed, status: " + delete_annotations_response.status.description)
```

```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteAnnotationsResponse = stub.deleteAnnotations(
    DeleteAnnotationsRequest.newBuilder()
        .addInputIds("{YOUR_INPUT_ID_1}")
        .addInputIds("{YOUR_INPUT_ID_2}")
        .addIds("{YOUR_ANNOTATION_ID_1}")
        .addIds("{YOUR_ANNOTATION_ID_2}")
        .build()
);

if (deleteAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete annotations failed, status: " + deleteAnnotationsResponse.getStatus());
}
```

```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteAnnotations(
    {
        input_ids: ["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"],
        annotation_ids: ["{YOUR_ANNOTATION_ID_1}", "{YOUR_ANNOTATION_ID_2}"]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete annotations failed, status: " + response.status.description);
        }
    }
);
```

```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  -d '
  {
    "input_ids":["{YOUR_INPUT_ID_1}","{YOUR_INPUT_ID_2}"],
    "ids":["{YOUR_ANNOTATION_ID_1}", "{YOUR_ANNOTATION_ID_2}"]
  }'\
  https://api.clarifai.com/v2/annotations
```

#### Bulk Delete All Annotations by Input IDs

To delete all annotations of a given input, you just need to set input ID\(s\). This will delete all annotations for these input\(s\) EXCEPT input level annotations which only get deleted if you delete the inputs themselves.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

delete_annotations_response = stub.DeleteAnnotations(
    service_pb2.DeleteAnnotationsRequest(
        input_ids=["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"]
    ),
    metadata=metadata
)

if delete_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Delete annotations failed, status: " + delete_annotations_response.status.description)
```
{% endtab %}

{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

BaseResponse deleteAnnotationsResponse = stub.deleteAnnotations(
    DeleteAnnotationsRequest.newBuilder()
        .addInputIds("{YOUR_INPUT_ID_1}")
        .addInputIds("{YOUR_INPUT_ID_2}")
        .build()
);

if (deleteAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete annotations failed, status: " + deleteAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.DeleteAnnotations(
    {
        input_ids: ["{YOUR_INPUT_ID_1}", "{YOUR_INPUT_ID_2}"]
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Delete annotations failed, status: " + response.status.description);
        }
    }
);
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  -d '
  {
    "input_ids":["{YOUR_INPUT_ID_1}","{YOUR_INPUT_ID_2}"]
  }'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

