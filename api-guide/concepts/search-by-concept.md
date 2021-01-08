---
description: Search based on specific words.
---

# Search by Concept

You can search for concepts by `name`, even in a different `language` using the concept searches endpoint:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiConceptResponse postConceptsSearchesResponse = stub.postConceptsSearches(
    PostConceptsSearchesRequest.newBuilder()
        .setConceptQuery(
            ConceptQuery.newBuilder()
                .setName("人")
                .setLanguage("ja")
        )
        .build()
);

if (postConceptsSearchesResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post concepts searches failed, status: " + postConceptsSearchesResponse.getStatus());
}

System.out.println("Found concepts:");
for (Concept concept : postConceptsSearchesResponse.getConceptsList()) {
    System.out.printf("\t%s %.2f%n", concept.getName(), concept.getValue());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostConceptsSearches(
    {
        concept_query: {name: "人", language: "ja"}
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post concepts searches failed, status: " + response.status.description);
        }

        console.log("Found concepts:");
        for (const concept of response.concepts) {
            console.log("\t" + concept.name + " " + concept.value);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_concepts_searches_response = stub.PostConceptsSearches(
    service_pb2.PostConceptsSearchesRequest(
        concept_query=resources_pb2.ConceptQuery(
            name="人",
            language="ja"
        )
    ),
    metadata=metadata
)

if post_concepts_searches_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post concepts searches failed, status: " + post_concepts_searches_response.status.description)

print("Found concepts:")
for concept in post_concepts_searches_response.concepts:
    print("\t%s %.2f" % (concept.name, concept.value))
```
{% endtab %}

{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "concept_query": {
      "name":"人",
      "language": "ja"
    }
  }'\
  https://api.clarifai.com/v2/concepts/searches
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Response JSON" %}
```javascript
{
  "status": {
    "code": 10000,
    "description": "Ok"
  },
  "concepts": [
    {
      "id": "ai_l8TKp2h5",
      "name": "人",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_ZKJ48TFz",
      "name": "人",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_GlPlRlTZ",
      "name": "人为破坏",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_8ZsdCrVZ",
      "name": "人体模型",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_K1KL0zgk",
      "name": "人力的",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_Tm9d2BZ2",
      "name": "人口",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_NLF8h1fJ",
      "name": "人口",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_8bHdFtsg",
      "name": "人口",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_vLnr3Mcj",
      "name": "人孔",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_HRt4nfvL",
      "name": "人工智能",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_Qc3mqxTJ",
      "name": "人才",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_VFKQ0qD6",
      "name": "人物",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_Wz8JXXMB",
      "name": "人类免疫缺陷病毒",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_bzp3Lg81",
      "name": "人类的",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_dJ15S9s6",
      "name": "人群",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_MNCVrmml",
      "name": "人行天桥",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_CChWH41S",
      "name": "人行横道",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_4lbXrFgT",
      "name": "人造",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_277LRf4d",
      "name": "人造卫星",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    },
    {
      "id": "ai_H3RDmvSn",
      "name": "人造奶油",
      "created_at": "2016-03-17T11:43:01Z",
      "updated_at": "2016-03-17T11:43:01Z",
      "app_id": null,
      "language": "zh"
    }
  ]
}
```
{% endtab %}
{% endtabs %}

