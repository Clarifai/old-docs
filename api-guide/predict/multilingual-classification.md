---
description: Multilingual predictions.
---

# Multilingual Classification

The Clarifai API supports [many languages in addition to English](../concepts/languages.md). When making a [predict api request](./), you can pass in the language you would like the concepts returned in. When you create a new Application, you must specify a default language which will be the language of the returned concepts if not specified in the predict request.

## Example Predict API Request

You can predict concepts in a language other then the Application's default, by explicitly passing in the language. Here is how you predict concepts in Chinese:

{% tabs %}
{% tab title="gRPC Java" %}
```java
import com.clarifai.grpc.api.*;
import com.clarifai.grpc.api.status.*;

// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

MultiOutputResponse postModelOutputsResponse = stub.postModelOutputs(
    PostModelOutputsRequest.newBuilder()
        .setModelId("aaa03c23b3724a16a56b629203edc62c")  // This is model ID of the publicly available General model.
        .addInputs(
            Input.newBuilder().setData(
                Data.newBuilder().setImage(
                    Image.newBuilder().setUrl("https://samples.clarifai.com/metro-north.jpg")
                )
            )
        )
        .setModel(
            Model.newBuilder().setOutputInfo(
                OutputInfo.newBuilder().setOutputConfig(
                    OutputConfig.newBuilder().setLanguage("zh")  // Chinese
                )
            )
        )
        .build()
);

if (postModelOutputsResponse.getStatus().getCode() != StatusCode.SUCCESS) {
  throw new RuntimeException("Post model outputs failed, status: " + postModelOutputsResponse.getStatus());
}

// Since we have one input, one output will exist here.
Output output = postModelOutputsResponse.getOutputs(0);

System.out.println("Predicted concepts:");
for (Concept concept : output.getData().getConceptsList()) {
    System.out.printf("%s %.2f%n", concept.getName(), concept.getValue());
}
```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```javascript
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

stub.PostModelOutputs(
    {
        model_id: "aaa03c23b3724a16a56b629203edc62c",
        inputs: [
            {data: {image: {url: "https://samples.clarifai.com/metro-north.jpg"}}}
        ],
        model: {output_info: {output_config: {language: "zh"}}}
    },
    metadata,
    (err, response) => {
        if (err) {
            throw new Error(err);
        }

        if (response.status.code !== 10000) {
            throw new Error("Post model outputs failed, status: " + response.status.description);
        }

        // Since we have one input, one output will exist here.
        const output = response.outputs[0];

        console.log("Predicted concepts:");
        for (const concept of output.data.concepts) {
            console.log(concept.name + " " + concept.value);
        }
    }
);
```
{% endtab %}

{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="aaa03c23b3724a16a56b629203edc62c",  # This is model ID of the publicly available General model.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        ],
        model=resources_pb2.Model(
            output_info=resources_pb2.OutputInfo(
                output_config=resources_pb2.OutputConfig(
                    language="zh"  # Chinese
                )
            )
        )
    ),
    metadata=metadata
)

if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# Since we have one input, one output will exist here.
output = post_model_outputs_response.outputs[0]

print("Predicted concepts:")
for concept in output.data.concepts:
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
  "inputs": [
    {
      "data": {
        "image": {
          "url": "https://samples.clarifai.com/metro-north.jpg"
        }
      }
    }
  ],
  "model":{
    "output_info":{
      "output_config":{
        "language":"zh"
      }
    }
  }
}'\
  https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs

# Above is model ID of the publicly available General model.
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
  "outputs": [
    {
      "id": "b9f3c12f1534440fa984dc463e491780",
      "status": {
        "code": 10000,
        "description": "Ok"
      },
      "created_at": "2017-01-31T20:59:27Z",
      "model": {
        "name": "general-v1.3",
        "id": "aaa03c23b3724a16a56b629203edc62c",
        "created_at": "2016-03-09T17:11:39Z",
        "app_id": null,
        "output_info": {
          "message": "Show output_info with: GET /models/{model_id}/output_info",
          "type": "concept"
        },
        "model_version": {
          "id": "aa9ca48295b37401f8af92ad1af0d91d",
          "created_at": "2016-07-13T01:19:12Z",
          "status": {
            "code": 21100,
            "description": "Model trained successfully"
          }
        }
      },
      "input": {
        "id": "b9f3c12f1534440fa984dc463e491780",
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      },
      "data": {
        "concepts": [
          {
            "id": "ai_HLmqFqBf",
            "name": "铁路列车",
            "app_id": null,
            "value": 0.9989112
          },
          {
            "id": "ai_fvlBqXZR",
            "name": "铁路",
            "app_id": null,
            "value": 0.9975532
          },
          {
            "id": "ai_Xxjc3MhT",
            "name": "运输系统",
            "app_id": null,
            "value": 0.9959158
          },
          {
            "id": "ai_6kTjGfF6",
            "name": "站",
            "app_id": null,
            "value": 0.992573
          },
          {
            "id": "ai_RRXLczch",
            "name": "火车",
            "app_id": null,
            "value": 0.992556
          },
          {
            "id": "ai_VRmbGVWh",
            "name": "旅游",
            "app_id": null,
            "value": 0.98789215
          },
          {
            "id": "ai_SHNDcmJ3",
            "name": "地铁",
            "app_id": null,
            "value": 0.9816359
          },
          {
            "id": "ai_jlb9q33b",
            "name": "通勤",
            "app_id": null,
            "value": 0.9712483
          },
          {
            "id": "ai_46lGZ4Gm",
            "name": "铁路",
            "app_id": null,
            "value": 0.9690325
          },
          {
            "id": "ai_tr0MBp64",
            "name": "交通",
            "app_id": null,
            "value": 0.9687052
          },
          {
            "id": "ai_l4WckcJN",
            "name": "模煳",
            "app_id": null,
            "value": 0.9667078
          },
          {
            "id": "ai_2gkfMDsM",
            "name": "平台",
            "app_id": null,
            "value": 0.9624243
          },
          {
            "id": "ai_CpFBRWzD",
            "name": "城市的",
            "app_id": null,
            "value": 0.960752
          },
          {
            "id": "ai_786Zr311",
            "name": "沒有人",
            "app_id": null,
            "value": 0.95864904
          },
          {
            "id": "ai_6lhccv44",
            "name": "商业",
            "app_id": null,
            "value": 0.95720303
          },
          {
            "id": "ai_971KsJkn",
            "name": "跑道",
            "app_id": null,
            "value": 0.9494642
          },
          {
            "id": "ai_WBQfVV0p",
            "name": "城市",
            "app_id": null,
            "value": 0.94089437
          },
          {
            "id": "ai_dSCKh8xv",
            "name": "快速的",
            "app_id": null,
            "value": 0.9399334
          },
          {
            "id": "ai_TZ3C79C6",
            "name": "马路",
            "app_id": null,
            "value": 0.93121606
          },
          {
            "id": "ai_VSVscs9k",
            "name": "终点站",
            "app_id": null,
            "value": 0.9230834
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Example Search By Tag API Request

You can search for concepts in other languages even if the default language of your application is English. When you add inputs to your application, concepts are predicted for every language. Here is an example of searching for '人' which is simplified Chinese for 'people'.

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
                .setLanguage("zh")
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
        concept_query: {name: "人", language: "zh"}
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
            language="zh"
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
    "query": {
      "ands": [
        {
          "output": {
            "data": {
              "concepts": [
                {
                  "name": "人"
                }
              ]
            }
          }
        }
      ],
      "language": "zh"
    }
  }'\
  https://api.clarifai.com/v2/searches
```
{% endtab %}
{% endtabs %}

