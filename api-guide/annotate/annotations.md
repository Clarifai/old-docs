# Annotations

## Annotations

When you add inputs to your app, we will create one input level annotations for each input. This annotation contains any data you provided in POST /inputs call. Meanwhile models in your default workflow could write annotations and can be used for search and train.

Once your input is successfully indexed, you can label the input by adding annotations, for example add cooncepts, draw bounding boxes and so on.


### Add Annotations

You can label your inputs by POST annotations. For example, add concept(s) to an image, draw a bounding box, label concept(s) to a video frame. Each annotation should contain at most 1 region. If it is a video, each annotation can have at most 1 frame. Later you coulld train your model using these data.

When you add an annotation, by default we will not run the workflow for this data. It means data will not be used to train your custom model or visual search. To make it available for training or searching, you need to provide `embed_model_version_id` field. This helps us to know how you want to apply the data and when to use this data. `embed_model_version_id` is the embed model version id in your app default workflow. It is recomended to provide this info.

You can add 1 or more annotations in a single API call but limited to sending 128 annotations at a time. 

#### Label an images with concepts

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
    ],
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}


#### Label model detected regions in an Image

When you index the input, our model will detect regions if your worfklow is detection workflow (for example `Face` or `General Detection`). You can check these detected regions by list model created annotations. Any data should be within `Region.Data`. Each annotation can have only 1 region. If you want to label multiple regions, you can post multiple annotations in a single API call.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiAnnotationResponse postAnnotationsResponse = stub.postAnnotations(
    PostAnnotationsRequest.newBuilder().addAnnotations(
        Annotation.newBuilder()
            .setInputId("{YOUR_INPUT_ID}")
            .setData(
                Data.newBuilder().addRegions(
                    Region.newBuilder()
                        .setId("{REGION_ID}") // this should be a region id  returned from list annotations call
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
    ).build()
);

if (postAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post annotations failed, status: " + postAnnotationsResponse.getStatus());
}

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotations(
    {
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                data: {
                    regions: [
                        {
                            id: "{REGION_ID}" // this should be a region id  returned from list annotations call
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_annotations_response = stub.PostAnnotations(
    service_pb2.PostAnnotationsRequest(
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            id="{REGION_ID}" ,  # this should be a region id returned from list annotations call
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
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post annotations failed, status: " + post_annotations_response.status.description)

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
              "id": "{REGION_ID}",
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
          ]
        },
        "embed_model_version_id": "{EMBED_MODEL_VERSION_ID}"
      }
    ],
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}


#### Label a new bounding box in an Image

You can label a new bounding box by providing bounding box coordinates.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiAnnotationResponse postAnnotationsResponse = stub.postAnnotations(
    PostAnnotationsRequest.newBuilder().addAnnotations(
        Annotation.newBuilder()
            .setInputId("{YOUR_INPUT_ID}")
            .setData(
                Data.newBuilder().addRegions(
                    Region.newBuilder()
                        .setRegionInfo(
                            RegionInfo.newBuilder()
                                .setBoundingBox(
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
    ).build()
);

if (postAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post annotations failed, status: " + postAnnotationsResponse.getStatus());
}

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotations(
    {
        annotations: [
            {
                input_id: "{YOUR_INPUT_ID}",
                data: {
                    regions: [
                        {
                            region_info: {
                                bounding_box: {
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_annotations_response = stub.PostAnnotations(
    service_pb2.PostAnnotationsRequest(
        annotations=[
            resources_pb2.Annotation(
                input_id="{YOUR_INPUT_ID}",
                data=resources_pb2.Data(
                    regions=[
                        resources_pb2.Region(
                            region_info=resources_pb2.RegionInfo(
                                bounding_box=resources_pb2.BoundingBox(
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
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post annotations failed, status: " + post_annotations_response.status.description)

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
          ]
        },
        "embed_model_version_id": "{EMBED_MODEL_VERSION_ID}"
      }
    ],
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}


### List annotations

You can get a list of annotations within your app with a GET call. Annotations will be returned from oldest to newest. 

These requests are paginated. By default each page will return 20 annotations.

#### List all labeled annotations in your app

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10
```
{% endtab %}
{% endtabs %}

#### List labeled annotations by Input IDs

To list all labeled annotations for specific input(s), you can supply a list of input Ids in request. 

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .addInputIds("{YOUR_INPUT_ID_1}")
        .addInputIds("{YOUR_INPUT_ID_2}")
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&input_ids=your_input_Id
```
{% endtab %}
{% endtabs %}

#### List labeled annotations by input Ids and annotation Ids

You can list annotations by both input Ids and annotation Ids. Number of input Ids and annotation Ids should be the same.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&input_ids=YOUR_INPUT_ID_1&input_ids=YOUR_INPUT_ID_2&ids=YOUR_ANNOTATION_ID_1&ids=YOUR_ANNOTATION_ID_2
```
{% endtab %}
{% endtabs %}


#### List annotations by user Ids

An annotation is created by either a user or a model. You can list annotations created by specific user(s).

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiAnnotationResponse listAnnotationsResponse = stub.listAnnotations(
    ListAnnotationsRequest.newBuilder()
        .addUserIDs("{USER_ID_1}")
        .addUserIDs("{USER_ID_2}")
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&user_ids=USER_ID_1&user_ids=USER_ID_2
```
{% endtab %}
{% endtabs %}


#### List annotations by model version Ids

An annotation is created by either a user or a model. For example if your workflow has detection model, when you add input, we will detect objects in your input. You can see these model detected objects by listing detection model created annotations.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="cURL" %}
```text
curl -X GET \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/annotations?page=1&per_page=10&model_version_ids=MODEL_VERSION_ID_1&model_version_ids=MODEL_VERSION_ID_2
```
{% endtab %}
{% endtabs %}


### Update annotations

You can change the data of annotation by making a PATCH call. Patch support `overwrite`, `merge`, `remove` actions. You can patch 1 or more annotations in a single API call but limited to sending 128 annotations at a time. 


#### Update annotation with concepts

To update an annotation of the entire image with a new concept, or to change a concept value from true/false, you can do that:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
    throw new RuntimeException("patch annotations failed, status: " + patchAnnotationsResponse.getStatus());
}

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
        "id": "{YOUR_ANNOTATION_ID}"
        "data": {
          "concepts": [
            {
              "id": "apple",
              "value": 1
            }
          ]
        },
      }
    ],
    "action":"merge"
}'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
{% endtabs %}

#### Update annotation with concepts in a region

When update annotation with region, you should provide region id if you are not intent to change the region. 

{% tabs %}
{% tab title="gRPC Java" %}
```java
import java.util.List;
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
                            .setId("{REGION_ID}") // this should be the region id of this annotation before patch
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
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
              "id": "{REGION_ID}",
              "data": {
                "concepts": [
                  {
                    "id": "apple",
                    "value": 1
                  }
                ]
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

### Delete annotations

#### Delete Annotation By Input Id and Annotation Id

You can delete a single annotation by input Id and annotation Id.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

BaseResponse deleteAnnotationResponse = stub.deleteAnnotation(
    DeleteAnnotationRequest.newBuilder()
        .setInputId("{YOUR_INPUT_ID_1}")
        .setAnnotationId("{YOUR_ANNOTATION_ID_2}")
        .build()
);

if (deleteAnnotationResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete annotation failed, status: " + deleteAnnotationResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  https://api.clarifai.com/v2/inputs/{YOUR_INPUT_ID}/annotations/{YOUR_ANNOTATION_ID}
```
{% endtab %}
{% endtabs %}

#### Bulk Delete Annotations By Input Ids and Annotation Ids

You can delete multiple annotations in one API call. You need to provide a list of input ids and a list of annotation Ids. Number of input Ids has to match number of annotation Ids.

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

BaseResponse deleteAnnotationsResponse = stub.deleteAnnotations(
    DeleteAnnotationsRequest.newBuilder()
        .addInputId("{YOUR_INPUT_ID_1}")
        .addInputId("{YOUR_INPUT_ID_2}")
        .setAnnotationId("{YOUR_ANNOTATION_ID_1}")
        .setAnnotationId("{YOUR_ANNOTATION_ID_2}")
        .build()
);

if (deleteAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete annotations failed, status: " + deleteAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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
{% endtab %}

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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
{% endtab %}

{% tab title="cURL" %}
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
{% endtab %}


#### Bulk Delete all annotations By Input Ids

If you want to delete all labels of a given input, you just need to set input Ids in request. This willl delete all annotations for these input(s) EXCEPT input level annotation. 

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

BaseResponse deleteAnnotationsResponse = stub.deleteAnnotations(
    DeleteAnnotationsRequest.newBuilder()
        .addInputId("{YOUR_INPUT_ID_1}")
        .addInputId("{YOUR_INPUT_ID_2}")
        .build()
);

if (deleteAnnotationsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Delete annotations failed, status: " + deleteAnnotationsResponse.getStatus());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

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

{% tab title="cURL" %}
```text
curl -X DELETE \
  -H "Authorization: Key YOUR_API_KEY" \
  -d '
  {
    "input_ids":["{YOUR_INPUT_ID_1}","{YOUR_INPUT_ID_2}"],
  }'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}
