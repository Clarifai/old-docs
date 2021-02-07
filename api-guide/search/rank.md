---
description: Search your data based on concepts or visual similarity
---

# Rank

Rank Order your search results with the intuitive insights of AI. Your model can identify concepts in your data and rank your search results by how confident it is that a given concept is present. You can even rank search results by how similar one input is to another input or region of the input model detected. The search results will return the input but also the annotation which includes the region.

## Search By Concepts

Once your images are indexed, you can search for them by concept.

### By clarifai/main App Concepts

When you add an input, it automatically gets predictions from the models in your base workflow which are typically models from the clarifai/main app such as the general model. You can search by those predictions.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder().addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                            Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                            Concept.newBuilder()
                                .setId("people")  // You could search by concept Name as well.
                                .setValue(1f)  // Value of 0 will search for images that don't have the concept.
                        )
                    )
                )
            )
        )    
    )
    .build()
);

if (postAnnotationsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post annotations searches failed, status: " + postAnnotationsSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postAnnotationsSearchesResponse.getHitsCount() + ":");
for (Hit hit : postAnnotationsSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for annotation % of input %s\n", hit.getScore(), hit.getAnnotation().getId(), hit.getInput().getId())
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    ranks: [
                        {
                            annotation: {
                                data: {
                                    concepts: [  // You can search by multiple concepts.
                                        {
                                            id: "people",  // You could search by concept Name as well.
                                            value: 1  // Value of 0 will search for images that don't have the concept
                                        }
                                    ]
                                }
                            }
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
            throw new Error("Post annotations searches failed, status: " + response.status.description);
        }

        console.log("Search result:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for annotation: " + hit.annotation.id + " of input: ", hit.input.id);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    ranks=[
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    concepts=[  # You can search by multiple concepts.
                                        resources_pb2.Concept(
                                            id="people",  # You could search by concept Name as well.
                                            value=1  # Value of 0 will search for images that don't have the concept.
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_annotations_searches_response.status.description)

print("Search result:")
for hit in post_annotations_searches_response.hits:
    print("\tScore %.2f for annotation: %s off input: %s" % (hit.score, hit.annotation.id, hit.input.id))
```
{% endtab %}

{% tab title="cURL" %}
```text
#
# Value of 0 will search for images that don't have the concept.
#
# Instead of "id" you can search by "name" as well.

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "searches": [
      {
        "query": {
        "ranks": [
            {
            "annotation": {
                "data": {
                "concepts": [
                    {
                    "id":"people",
                    "value": 1
                    }
                ]
                }
            }
            }
        ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}
{% endtabs %}

### By Custom Concepts

After you have [added inputs](https://github.com/Clarifai/docs/tree/1c1d25cdd43190c38a2edb313297c0d566b3a0e3/api-guide/search/data-management/inputs.md#add-inputs-with-concepts), [annotation the inputs](https://github.com/Clarifai/docs/tree/1c1d25cdd43190c38a2edb313297c0d566b3a0e3/api-guide/search/data-management/annotations.md#add-annotations), and try a custom model, you can search by those concepts.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder().addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                            Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                            Concept.newBuilder()
                                .setId("people")  // You could search by concept Name as well.
                                .setValue(1f)  // Value of 0 will search for images that don't have the concept.
                        )
                    )
                )
            )
        )    
    )
    .build()
);

if (postAnnotationsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post annotations searches failed, status: " + postAnnotationsSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postAnnotationsSearchesResponse.getHitsCount() + ":");
for (Hit hit : postAnnotationsSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for annotation % of input %s\n", hit.getScore(), hit.getAnnotation().getId(), hit.getInput().getId())
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    ranks: [
                        {
                            annotation: {
                                data: {
                                    concepts: [  // You can search by multiple concepts.
                                        {
                                            id: "people",  // You could search by concept Name as well.
                                            value: 1  // Value of 0 will search for images that don't have the concept
                                        }
                                    ]
                                }
                            }
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
            throw new Error("Post annotations searches failed, status: " + response.status.description);
        }

        console.log("Search result:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for annotation: " + hit.annotation.id + " of input: ", hit.input.id);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    ranks=[
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    concepts=[  # You can search by multiple concepts.
                                        resources_pb2.Concept(
                                            id="people",  # You could search by concept Name as well.
                                            value=1  # Value of 0 will search for images that don't have the concept.
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_annotations_searches_response.status.description)

print("Search result:")
for hit in post_annotations_searches_response.hits:
    print("\tScore %.2f for annotation: %s off input: %s" % (hit.score, hit.annotation.id, hit.input.id))
```
{% endtab %}

{% tab title="cURL" %}
```text
#
# Value of 0 will search for images that don't have the concept.
#
# Instead of "id" you can search by "name" as well.

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "searches": [
      {
        "query": {
        "ranks": [
            {
            "annotation": {
                "data": {
                "concepts": [
                    {
                    "id":"people",
                    "value": 1
                    }
                ]
                }
            }
            }
        ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}
{% endtabs %}

### By clarifai/main and custom concepts

You can combine a search to find inputs that have concepts you have supplied as well as predictions from your model.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

// Here we search for images which we labeled with "cat" and for which the General prediction model does not find
// a "dog" concept.
MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder().addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                            Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                            Concept.newBuilder()
                                .setId("cat")  // You could search by concept Name as well.
                                .setValue(1f)  // Value of 0 will search for images that don't have the concept.
                        )
                    )
                )
            )
            .addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                            Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                            Concept.newBuilder()
                                .setId("dog")  // You could search by concept Name as well.
                                .setValue(0f)  // Value of 0 will search for images that don't have the concept.
                        )
                    )
                )
            )
        )    
    )
    .build()
);

if (postAnnotationsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post annotations searches failed, status: " + postAnnotationsSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postAnnotationsSearchesResponse.getHitsCount() + ":");
for (Hit hit : postAnnotationsSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for annotation % of input %s\n", hit.getScore(), hit.getAnnotation().getId(), hit.getInput().getId())
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

// Here we search for images which we labeled with "cat" and for which the General prediction model does not find
// a "dog" concept.

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    ranks: [
                        {
                            annotation: {
                                data: {
                                    concepts: [  // You can search by multiple concepts.
                                        {
                                            id: "cat",  // You could search by concept Name as well.
                                            value: 1  // Value of 0 will search for images that don't have the concept
                                        }
                                    ]
                                }
                            }
                        }, {
                            annotation: {
                                data: {
                                    concepts: [  // You can search by multiple concepts.
                                        {
                                            id: "dog",  // You could search by concept Name as well.
                                            value: 0  // Value of 0 will search for images that don't have the concept
                                        }
                                    ]
                                }
                            }
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
            throw new Error("Post annotations searches failed, status: " + response.status.description);
        }

        console.log("Search result:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for annotation: " + hit.annotation.id + " of input: ", hit.input.id);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

# Here we search for images which we labeled with "cat" and for which the General prediction model does not find
# a "dog" concept.

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    ranks=[
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    concepts=[  # You can search by multiple concepts.
                                        resources_pb2.Concept(
                                            id="cat",  # You could search by concept Name as well.
                                            value=1  # Value of 0 will search for images that don't have the concept.
                                        )
                                    ]
                                )
                            )
                        ),
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    concepts=[  # You can search by multiple concepts.
                                        resources_pb2.Concept(
                                            id="dog",  # You could search by concept Name as well.
                                            value=0  # Value of 0 will search for images that don't have the concept.
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_annotations_searches_response.status.description)

print("Search result:")
for hit in post_annotations_searches_response.hits:
    print("\tScore %.2f for annotation: %s off input: %s" % (hit.score, hit.annotation.id, hit.input.id))
```
{% endtab %}

{% tab title="cURL" %}
```text
#
# Value of 0 will search for images that don't have the concept.
#
# Instead of "id" you can search by "name" as well.

# Here we search for images which we labeled with "cat" and for which the General prediction model does not find
# a "dog" concept.

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "searches": [
      {
        "query": {
        "ranks": [
            {
            "annotation": {
                "data": {
                "concepts": [
                    {
                    "id":"cat",
                    "value": 1
                    }
                ]
                }
            }
            }, {   
            "annotation": {
                "data": {
                "concepts": [
                    {
                    "id":"dog",
                    "value": 0
                    }
                ]
                }
            }
            }
        ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}
{% endtabs %}

### By concept in another language

Concepts that have a translation into another language can be searched for in that language, even without having the default language for your app being in that language. This uses Clarifai's knowledge graph to lookup the translation and then perform the search. For example, if you app is in english and you want to search for "dog" in Japanese, then you could search with `language="ja"` and `name="犬"`.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder().addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                            Data.newBuilder().addConcepts(  // You can search by multiple concepts.
                            Concept.newBuilder()
                                .setName("犬")  // You could search by concept ID as well.
                                .setLanguage("ja") // japanese
                                .setValue(1f)  // Value of 0 will search for images that don't have the concept.
                        )
                    )
                )
            )
        )    
    )
    .build()
);

if (postAnnotationsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post annotations searches failed, status: " + postAnnotationsSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postAnnotationsSearchesResponse.getHitsCount() + ":");
for (Hit hit : postAnnotationsSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for annotation % of input %s\n", hit.getScore(), hit.getAnnotation().getId(), hit.getInput().getId())
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    ranks: [
                        {
                            annotation: {
                                data: {
                                    concepts: [  // You can search by multiple concepts.
                                        {
                                            name: "犬",  // You could search by concept Id as well.
                                            language: "ja", // japanese
                                            value: 1  // Value of 0 will search for images that don't have the concept
                                        }
                                    ]
                                }
                            }
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
            throw new Error("Post annotations searches failed, status: " + response.status.description);
        }

        console.log("Search result:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for annotation: " + hit.annotation.id + " of input: ", hit.input.id);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    ranks=[
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    concepts=[  # You can search by multiple concepts.
                                        resources_pb2.Concept(
                                            name="犬",  # You could search by concept ID as well.
                                            language="ja", # japanese
                                            value=1  # Value of 0 will search for images that don't have the concept.
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_annotations_searches_response.status.description)

print("Search result:")
for hit in post_annotations_searches_response.hits:
    print("\tScore %.2f for annotation: %s off input: %s" % (hit.score, hit.annotation.id, hit.input.id))
```
{% endtab %}

{% tab title="cURL" %}
```text
#
# Value of 0 will search for images that don't have the concept.
#
# Instead of "name" you can search by "id" as well.

curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "searches": [
      {
        "query": {
        "ranks": [
            {
            "annotation": {
                "data": {
                "concepts": [
                    {
                    "name":"犬",
                    "language": "ja",
                    "value": 1
                    }
                ]
                }
            }
            }
        ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}
{% endtabs %}

## Search by visual similarity

You can use images to search through your collection. The API will return ranked results based on how similar the results are to the image you provided in your query.

### Search by image URL

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder().addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                        Data.newBuilder().setImage(
                            Image.newBuilder()
                                .setUrl("{YOUR_IMAGE_URL}")
                        )
                    )
                )
            )
        )    
    )
    .build()
);

if (postAnnotationsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post annotations searches failed, status: " + postAnnotationsSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postAnnotationsSearchesResponse.getHitsCount() + ":");
for (Hit hit : postAnnotationsSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for annotation % of input %s\n", hit.getScore(), hit.getAnnotation().getId(), hit.getInput().getId())
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotationsSearches(
    {
        searches: [
            {
            query: {
                ranks: [
                    {
                        annotation: {
                            data: {
                                image: {
                                    url: "{YOUR_IMAGE_URL}"
                                }
                            }
                        }
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
            throw new Error("Post annotations searches failed, status: " + response.status.description);
        }

        console.log("Search result:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for annotation: " + hit.annotation.id + " of input: ", hit.input.id);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    ranks=[
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    image=resources_pb2.Image(
                                        url="{YOUR_IMAGE_URL}"
                                    )
                                )
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_annotations_searches_response.status.description)

print("Search result:")
for hit in post_annotations_searches_response.hits:
    print("\tScore %.2f for annotation: %s off input: %s" % (hit.score, hit.annotation.id, hit.input.id))
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "searches": [
      {
        "query": {
        "ranks": [
            {
            "annotation": {
                "data": {
                "image": {
                    "url": "{YOUR_IMAGE_URL}"
                }
                }
            }
            }
        ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}
{% endtabs %}

### Search by image Bytes

You can also search for an input by URL.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;
import com.google.protobuf.ByteString;
import java.io.File;
import java.nio.file.Files;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder().addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                        Data.newBuilder().setImage(
                            Image.newBuilder()
                                .setBase64(ByteString.copyFrom(Files.readAllBytes(
                                    new File("{YOUR_IMAGE_LOCATION}").toPath()
                                ))
                            )
                        )
                    )
                )
            )
        )    
    )
    .build()
);

if (postAnnotationsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post annotations searches failed, status: " + postAnnotationsSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postAnnotationsSearchesResponse.getHitsCount() + ":");
for (Hit hit : postAnnotationsSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for annotation % of input %s\n", hit.getScore(), hit.getAnnotation().getId(), hit.getInput().getId())
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

const fs = require("fs");
const imageBytes = fs.readFileSync("{YOUR_IMAGE_LOCATION}");

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    ranks: [
                        {
                            annotation: {
                                data: {
                                    image: {
                                        base64: imageBytess
                                    }
                                }
                            }
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
            throw new Error("Post annotations searches failed, status: " + response.status.description);
        }

        console.log("Search result:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for annotation: " + hit.annotation.id + " of input: ", hit.input.id);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

with open("{YOUR_IMAGE_LOCATION}", "rb") as f:
    file_bytes = f.read()

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    ranks=[
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    image=resources_pb2.Image(
                                        base64=file_bytes
                                    )
                                )
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_annotations_searches_response.status.description)

print("Search result:")
for hit in post_annotations_searches_response.hits:
    print("\tScore %.2f for annotation: %s off input: %s" % (hit.score, hit.annotation.id, hit.input.id))
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "searches": [
      {
        "query": {
        "ranks": [
            {
            "annotation": {
                "data": {
                "image": {
                    "base64": '"`base64 /home/user/image.jpeg`"'"
                }
                }
            }
            }
        ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}
{% endtabs %}

### By Input ID

If the input has been indexed, we can use the input ID. If there are multiple embeddings \(for example multiple regions\), we will average the embeddings.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder().addRanks(
                Rank.newBuilder().setAnnotation(
                    Annotation.newBuilder().setInputId("{input_id}")    
                )
            )
        )    
    )
    .build()
);

if (postAnnotationsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post annotations searches failed, status: " + postAnnotationsSearchesResponse.getStatus());
}

System.out.println("Found inputs " + postAnnotationsSearchesResponse.getHitsCount() + ":");
for (Hit hit : postAnnotationsSearchesResponse.getHitsList()) {
    System.out.printf("\tScore %.2f for annotation % of input %s\n", hit.getScore(), hit.getAnnotation().getId(), hit.getInput().getId())
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    ranks: [
                        {
                            annotation: {
                                input_id: "{input_ids}"
                            }
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
            throw new Error("Post annotations searches failed, status: " + response.status.description);
        }

        console.log("Search result:");
        for (const hit of response.hits) {
            console.log("\tScore " + hit.score + " for annotation: " + hit.annotation.id + " of input: ", hit.input.id);
        }
    }
);
```
{% endtab %}

{% tab title="Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    ranks=[
                        resources_pb2.Rank(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    image=resources_pb2.Image(
                                        input_id="{input_ids}"
                                    )
                                )
                            )
                        )
                    ]
                )
            )
        ]
    ),
    metadata=metadata
)

if post_annotations_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post searches failed, status: " + post_annotations_searches_response.status.description)

print("Search result:")
for hit in post_annotations_searches_response.hits:
    print("\tScore %.2f for annotation: %s off input: %s" % (hit.score, hit.annotation.id, hit.input.id))
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "searches": [
      {
        "query": {
          "ranks": [
            {
              "annotation": {
                "data": {
                  "image": {
                    "url": "{YOUR_IMAGE_URL}"
                  }
                }
              }
            }
          ]
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}
{% endtabs %}

