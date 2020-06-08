API

## Create

### Create Deep Model (Classification)

{% tabs %}
{% tab title="gRPC Java" %}
```java
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js
// Insert here the initialization code as outlined on this page:
// https://docs.clarifai.com/api-guide/api-overview

{% endtab %}

{% tab title="gRPC Python" %}
```python

```
{% endtab %}


{% tab title="cURL" %}
```text

curl --location --request POST '{{base_url}}/v2/models' \
--header 'Authorization: Key {{key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": {
        "id": "lawrence-1591638385",
        "template_name": "small_image_classification",
        "output_info": {
            "data": {
                "concepts": [
                    {"id":"ferrari23"},
                    {"id":"outdoors23"}
                ]
            },
            "output_config": {
              "hyper_params": { "num_epochs": 2},
        	  "closed_environment" : true
            }
        }
    }
}'

{% endtab %}
{% endtabs %}


### Create Deep Model (Detection)

{% tabs %}
{% tab title="gRPC Java" %}
```java
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js


{% endtab %}

{% tab title="gRPC Python" %}
```python

```
{% endtab %}


{% tab title="cURL" %}
```text

curl --location --request POST '{{base_url}}/v2/models' \
--header 'Authorization: Key {{key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": {
        "id": "detection-test-1591638385",
        "template_name": "detection",
        "output_info": {
            "data": {
                "concepts": [
                    {"id":"ferrari23"},
                    {"id":"outdoors23"}
                ]
            },
            "output_config": {
              "hyper_params": { "num_epochs": 2},
        	  "closed_environment" : true
            }
        }
    }
}'

{% endtab %}
{% endtabs %}

## Get

### List training templates


{% tabs %}
{% tab title="gRPC Java" %}
```java
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js


{% endtab %}

{% tab title="gRPC Python" %}
```python

```
{% endtab %}


{% tab title="cURL" %}
```text

curl --location --request GET '{{base_url}}/v2/users/{{user_id}}/apps/{{app_id}}/templates' \
--header 'Content-Type: application/json' \
--header 'X-Clarifai-Session-Token: {{session_token}}'

{% endtab %}
{% endtabs %}


## Update

### Patch base workflow

curl --location --request PATCH '{{base_url}}/v2/users/84aesy5efwjl/apps/efe2d3cf79084c799cbde19a4e71527c/base-workflows' \
--header 'Content-Type: application/json' \
--header 'Authorization: Key 63bca3ac25124c2e852c8d81c5475356' \
--data-raw '{
    "workflows": [
        {
            "id": "General",
            "nodes": [
                {
                    "id": "embed",
                    "model": {
                        "id": "bbb5f41425b8468d9b7a554ff10f8581",
                        "model_version": {
                            "id": "bb7ac05c86be42d38b67bc473d33"
                        }
                    }
                },
                {
                    "id": "my-custom-model",
                    "model": {
                        "id": "f4e854e89c794d03b9ee31c201160d1a",
                        "model_version": {
                            "id": "d59832dc348c4cbf9146acec68c3366c"
                        }
                    },
                    "input": {
                        "node_id": "embed",
                        "output": "embed"
                    }
                }
            ]
        }
    ],
    "action": "merge",
    "reindex": true
}'



## Delete

### Delete deep model versions deployments


{% tabs %}
{% tab title="gRPC Java" %}
```java
{% endtab %}


{% tab title="gRPC NodeJS" %}
```js


{% endtab %}

{% tab title="gRPC Python" %}
```python

```
{% endtab %}


{% tab title="cURL" %}
```text

curl --location --request DELETE '{{base_url}}/v2/models/{{model_id}}/deployments' \
--header 'Authorization: Key {{key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
	"version_ids": [
    	"{{version_id}}"
	]
}'

{% endtab %}
{% endtabs %}
