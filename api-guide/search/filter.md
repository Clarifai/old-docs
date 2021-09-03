---
description: Select a subset of your data based on useful filters.
---

# Filter

You can filter and customize your search results to find exactly what you want. Filtering helps you reduce the amount of data returned in search results by removing irrelevant content, or by allowing you to select a specific subset of your data.

## By Custom Concepts

After you [annotate inputs with custom concepts](https://github.com/Clarifai/docs/tree/1c1d25cdd43190c38a2edb313297c0d566b3a0e3/api-guide/search/data-management/annotations.md#annotate-images-with-concepts), you can filter by concepts.

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
            Query.newBuilder().addFilters(
                Filter.newBuilder().setAnnotation(
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
                    filters: [
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
                    filters=[
                        resources_pb2.Filter(
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
    "searches": [{
      "query": {
        "filters": [
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
    }]

  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "searches": [{
    "query": {
      "filters": [
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
  }]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/annotations/searches`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## By User ID

If you have collaborators in your app and they helped you annotate your inputs, you can also filter annotations by user id.

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
            Query.newBuilder().addFilters(
                Filter.newBuilder().setAnnotation(
                    Annotation.newBuilder().setUserId("{user_id}")
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
                    filters: [
                        {
                            annotation: {
                                user_id: "{user_id}"
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
                    filters=[
                        resources_pb2.Filter(
                            annotation=resources_pb2.Annotation(
                                user_id="{user_id}"
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
    print("There was an error with your request!")
    print("\tCode: {}".format(post_annotations_searches_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_annotations_searches_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_annotations_searches_response.outputs[0].status.details))
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
    "searches": [{
      "query": {
        "filters": [
          {
            "annotation": {
              "user_id": "{user_id}"
            }
          }
        ]
      }
    }]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "searches": [{
    "query": {
      "filters": [
        {
          "annotation": {
            "user_id": "{user_id}"
          }
        }
      ]
    }
  }]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/annotations/searches`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## By Annotation Status

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
            Query.newBuilder().addFilters(
                Filter.newBuilder().setAnnotation(
                    Annotation.newBuilder()
                    .setStatus(
                        Status.newBuilder()
                            .setCodeValue(StatusCode.ANNOTATION_SUCCESS_VALUE)
                            .build()
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
                    filters: [
                        {
                            annotation: {
                                status: {
                                    code: 24150
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
                    filters=[
                        resources_pb2.Filter(
                            annotation=resources_pb2.Annotation(
                                status=status_pb2.Status(
                                    code=status_code_pb2.ANNOTATION_SUCCESS
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
    print("There was an error with your request!")
    print("\tCode: {}".format(post_annotations_searches_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_annotations_searches_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_annotations_searches_response.outputs[0].status.details))
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
    "searches": [{
      "query": {
        "filters": [
          {
            "annotation": {
              "status": {
                "code": "ANNOTATION_SUCCESS"
              }          
            }
          }
        ]
      }
    }]
  }'\
  https://api.clarifai.com/v2/annnotations/searches
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "searches": [{
    "query": {
      "filters": [
        {
          "annotation": {
            "status": {
              "code": "ANNOTATION_SUCCESS"
            }          
          }
        }
      ]
    }
  }]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/annotations/searches`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## By Geo Location

Search by geo location allows you to restrict your search results to a bounding box based on longitude and latitude points. There are two ways you can provide longitude/latitude points. You can provide one point and a radius or you can provide two points.

It is important to note that a search by geo location acts as a filter and returns results ranked by any other provided search criteria, whether that is a visual search, concept search or something else. If no other criteria is provided, results will return in the order the inputs were created, NOT by their distance to center of the search area.

If you are providing one point and a radius, the radius can be in "mile", "kilometer", "degree", or "radian", marked by keywords `withinMiles`, `withinKilometers`, `withinDegrees`, `withinRadians`.

If you are providing two points, a box will be drawn from the uppermost point to the lowermost point and the leftmost point to the rightmost point.

Before you perform a search by geo location, make sure you have added inputs with longitude and latitude points.

### Add inputs with longitude and latitude points

Provide a geo point to an input. The geo point is a JSON object consisting of a longitude and a latitude in GPS coordinate system \(SRID 4326\). There can be at most one single geo point associated with each input.

{% tabs %}
{% tab title="Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

MultiInputResponse postInputsResponse = stub.postInputs(
    PostInputsRequest.newBuilder().addInputs(
        Input.newBuilder().setData(
            Data.newBuilder()
                .setImage(
                    Image.newBuilder()
                        .setUrl("https://samples.clarifai.com/dog.tiff")
                        .setAllowDuplicateUrl(true)
                )
                .setGeo(
                    Geo.newBuilder().setGeoPoint(
                        GeoPoint.newBuilder()
                            .setLongitude(-30)
                            .setLatitude(40)
                    )
                )
        )
    ).build()
);

if (postInputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
    throw new RuntimeException("Post inputs failed, status: " + postInputsResponse.getStatus());
}
```
{% endtab %}

{% tab title="NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostInputs(
    {
        inputs: [
            {
                data: {
                    image: {url: "https://samples.clarifai.com/dog.tiff", allow_duplicate_url: true},
                    geo: {
                        geo_point: {
                            longitude: -30,
                            latitude: 40
                        }
                    }
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
            throw new Error("Post inputs failed, status: " + response.status.description);
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

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/dog.tiff",
                        allow_duplicate_url=True
                    ),
                    geo=resources_pb2.Geo(
                        geo_point=resources_pb2.GeoPoint(
                            longitude=-30.0,
                            latitude=40.0,
                        )
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_inputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_inputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_inputs_response.outputs[0].status.details))
    raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/dog.tiff",
            "allow_duplicate_url": true
          },
          "geo": {
            "geo_point": {
              "longitude": -30,
              "latitude": 40
            }
          }
        }
      }
    ]
  }'\
  https://api.clarifai.com/v2/inputs
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "inputs": [
    {
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/dog.tiff",
          "allow_duplicate_url": true
        },
        "geo": {
          "geo_point": {
            "longitude": -30,
            "latitude": 40
          }
        }
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/inputs`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Perform a search with one geo point and radius in kilometers

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
            Query.newBuilder().addFilters(
                Filter.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                            Data.newBuilder().setGeo(
                                Geo.newBuilder()
                                    .setGeoPoint(
                                        GeoPoint.newBuilder()
                                            .setLongitude(-29)
                                            .setLatitude(40)
                                    )
                                    .setGeoLimit(
                                        GeoLimit.newBuilder()
                                            .setType("withinKilometers")
                                            .setValue(150.0f)
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

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    filters: [
                        {
                            annotation: {
                                data: {
                                    geo: {
                                        geo_point: {
                                            longitude: -29,
                                            latitude: 40
                                        },
                                        geo_limit: {
                                            type: "withinKilometers",
                                            value: 150.0
                                        }
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
                    filters=[
                        resources_pb2.Filter(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    geo=resources_pb2.Geo(
                                        geo_point=resources_pb2.GeoPoint(
                                            longitude=-29.0,
                                            latitude=40.0,
                                        ),
                                        geo_limit=resources_pb2.GeoLimit(
                                            type="withinKilometers",
                                            value=150.0
                                        )
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
    print("There was an error with your request!")
    print("\tCode: {}".format(post_annotations_searches_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_annotations_searches_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_annotations_searches_response.outputs[0].status.details))
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
          "filters": [
            {
            "annotation": {
                "data": {
                "geo": {
                    "geo_point": {
                    "longitude": -29.0,
                    "latitude": 40.0
                    },
                    "geo_limit": {
                    "type": "withinKilometers",
                    "value": 150
                    }
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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "searches": [
    {
      "query": {
        "filters": [
          {
          "annotation": {
              "data": {
              "geo": {
                  "geo_point": {
                  "longitude": -29.0,
                  "latitude": 40.0
                  },
                  "geo_limit": {
                  "type": "withinKilometers",
                  "value": 150
	              }
              }
            }
          }
        }
      ]
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/annnotations/searches`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

### Perform a search with two geo points

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
            Query.newBuilder().addFilters(
                Filter.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                            Data.newBuilder().setGeo(
                                Geo.newBuilder()
                                    .addGeoBox(
                                        GeoBoxedPoint.newBuilder().setGeoPoint(
                                            GeoPoint.newBuilder()
                                                .setLongitude(-31)
                                                .setLatitude(42)
                                        )
                                    )
                                    .addGeoBox(
                                        GeoBoxedPoint.newBuilder().setGeoPoint(
                                            GeoPoint.newBuilder()
                                                .setLongitude(-29)
                                                .setLatitude(39)
                                        ).build()
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

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    filters: [
                        {
                            annotation: {
                                data: {
                                    geo: {
                                        geo_box: [
                                            {
                                                geo_point: {
                                                    longitude: -31,
                                                    latitude: 42
                                                }
                                            },
                                            {
                                                geo_point: {
                                                    longitude: -29,
                                                    latitude: 39
                                                }
                                            }
                                        ]
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
                    filters=[
                        resources_pb2.Filter(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    geo=resources_pb2.Geo(
                                        geo_box=[
                                            resources_pb2.GeoBoxedPoint(
                                                geo_point=resources_pb2.GeoPoint(
                                                    longitude=-31.0,
                                                    latitude=42.0,
                                                ),
                                            ),
                                            resources_pb2.GeoBoxedPoint(
                                                geo_point=resources_pb2.GeoPoint(
                                                    longitude=-29.0,
                                                    latitude=39.0,
                                                ),
                                            ),
                                        ]
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
    print("There was an error with your request!")
    print("\tCode: {}".format(post_annotations_searches_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_annotations_searches_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_annotations_searches_response.outputs[0].status.details))
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
        "filters": [
            {
            "annotation": {
                "data": {
                "geo": {
                    "geo_box": [
                    {
                        "geo_point": {
                        "latitude": 42,
                        "longitude": -31
                        }
                    },
                    {
                        "geo_point": {
                        "latitude": 39,
                        "longitude": -29
                        }
                    }
                    ]
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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "searches": [
    {
      "query": {
      "filters": [
          {
          "annotation": {
              "data": {
              "geo": {
                  "geo_box": [
                  {
                      "geo_point": {
                      "latitude": 42,
                      "longitude": -31
                      }
                  },
                  {
                      "geo_point": {
                      "latitude": 39,
                      "longitude": -29
                      }
                  }
                  ]
              }
              }
          }
          }
      ]
      }       
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/annnotations/searches`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## By Custom Annotation Info

After you have [added inputs with custom metadata](https://github.com/Clarifai/docs/tree/1c1d25cdd43190c38a2edb313297c0d566b3a0e3/api-guide/search/data-management/inputs.md#add-inputs-with-custom-metadata), you can search by that metadata.

Below is an example of searching over custom metadata. You can exact match any `key`: `value` pair no matter how nested it is. For example, if the metadata on an input is:

```javascript
{
  "keyname": "value1",
  "somelist": [1,2,3],
  "somenesting": {
     "keyname2":"value2",
     "list2":[4,5]
   }
}
```

Then the following searches will find this:

```javascript
{
  "keyname": "value1"
}
```

```javascript
{
  "somelist": [1,2,3]
}
```

```javascript
{
  "somelist": [1,2]
}
```

```javascript
{
  "somenesting": {"keyname2":"value2"}
}
```

```javascript
{
  "somenesting": {"list2":[5]}
}
```

How to perform searches:

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
            Query.newBuilder().addFilters(
                Filter.newBuilder().setAnnotation(
                    Annotation.newBuilder().setData(
                        Data.newBuilder().setMetadata(
                            Struct.newBuilder()
                                .putFields("type", Value.newBuilder().setStringValue("animal").build())
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
                    filters: [
                        {
                            annotation: {
                                data: {
                                    metadata: {
                                        "type": "animal"
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
from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

search_metadata = Struct()
search_metadata.update({"type": "animal"})

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    filters=[
                        resources_pb2.Filter(
                            annotation=resources_pb2.Annotation(
                                data=resources_pb2.Data(
                                    metadata=search_metadata
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
    print("There was an error with your request!")
    print("\tCode: {}".format(post_annotations_searches_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_annotations_searches_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_annotations_searches_response.outputs[0].status.details))
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
        "filters": [
            {
            "annotation": {
                "data": {
                "metadata": {
                    "type": "animal"
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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "searches": [
    {
      "query": {
      "filters": [
          {
          "annotation": {
              "data": {
              "metadata": {
                  "type": "animal"
              }
              }
          }
          }
      ]
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/annnotations/searches`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

## By Annotation Info

Each annotation has annotation info. Similar to metadata, you have full control of this field and can be any arbitrary JSON.

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
            Query.newBuilder().addFilters(
                Filter.newBuilder().setAnnotation(
                    Annotation.newBuilder().setAnnotationInfo(
                        Struct.newBuilder()
                            .putFields("type", Value.newBuilder().setStringValue("animal").build())
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

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

stub.PostAnnotationsSearches(
    {
        searches: [
            {
                query: {
                    filters: [
                        {
                            annotation: {
                                annotation_info: {
                                    "type": "animal"
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
from google.protobuf.struct_pb2 import Struct

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview

search_annotation_info = Struct()
search_annotation_info.update({"type": "animal"})

post_annotations_searches_response = stub.PostAnnotationsSearches(
    service_pb2.PostAnnotationsSearchesRequest(
        searches = [
            resources_pb2.Search(
                query=resources_pb2.Query(
                    filters=[
                        resources_pb2.Filter(
                            annotation=resources_pb2.Annotation(
                                annotation_info=search_annotation_info
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
    print("There was an error with your request!")
    print("\tCode: {}".format(post_annotations_searches_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_annotations_searches_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_annotations_searches_response.outputs[0].status.details))
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
        "filters": [
            {
            "annotation": {
                "annotation_info": {
                "type": "animal"
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

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
  "user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
  "searches": [
    {
      "query": {
      "filters": [
          {
          "annotation": {
              "annotation_info": {
              "type": "animal"
              }
          }
          }
      ]
      }
    }
  ]
});

const requestOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Key {YOUR_PERSONAL_TOKEN}'
  },
	body: raw
};

fetch(`https://api.clarifai.com/v2/annnotations/searches`, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

