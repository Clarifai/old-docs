# Combine or negate

You can also combine searches. Unlike our legacy search, in annotation search, `Filter` and `Rank` is a list of `Annotation` objects. Filtered annotations will be ANDed. When you combine both `Filter` and `Rank`, filter will be applied before ranking annotations. This is important because on large applications the filtering can speedup the 

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

// Here we search for images which we labeled with "cat" and for which the General prediction model does not find
// a "dog" concept.
MultiSearchResponse postAnnotationsSearchesResponse = stub.postAnnotationsSearches(
    PostAnnotationsSearchesRequest.newBuilder().addSearches(
        Search.newBuilder().setQuery(
            Query.newBuilder()
                .addFilters(
                    Filter.newBuilder().setAnnotation(
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

{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

// Here we search for images which we labeled with "cat" and for which the General prediction model does not find
// a "dog" concept.
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
                                            id: "cat",  // You could search by concept Name as well.
                                            value: 1  // Value of 0 will search for images that don't have the concept
                                        }
                                    ]
                                }
                            }
                        }
                    ],
                    ranks: [
                        {
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

{% tab title="gRPC Python" %}
```python
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

# Here we search for images which we labeled with "cat" and for which the General prediction model does not find
# a "dog" concept.
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
                                            id="cat",  # You could search by concept Name as well.
                                            value=1  # Value of 0 will search for images that don't have the concept.
                                        )
                                    ]
                                )
                            )
                        )
                    ],
                    ranks=[
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
# Here we search for images which we labeled with "cat" and for which the General prediction model does not find
# a "dog" concept.

curl -X POST \
  -H "Authorization: Key {api-key}" \
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
                  "concepts": [
                    {
                      "id":"people",
                      "value": 1
                    }
                  ]
                }
              }
            }
          ],
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
https://api.clarifai.com/v2/searches
```
{% endtab %}
{% endtabs %}

