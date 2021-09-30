---
description: Create, explore and modify datasets
---


# Dataset Inputs


## Add inputs to a dataset
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request POST 'api.clarifai.com/v2/datasets/{{dataset_id}}/inputs' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_inputs": [
        {
            "input": {
                "id": "{{input_id}}"
            }
        }
    ]
}'
```
{% endtab %}
{% endtabs %}

## List inputs in a datasets
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request GET 'api.clarifai.com/v2/datasets/{{dataset_id}}/inputs?page=1&per_page=100' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}
{% endtabs %}

## Get a dataset inputs
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request GET 'api.clarifai.com/v2/datasets/{{dataset_id}}/inputs/{{input_id}}' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}
{% endtabs %}

## Delete Inputs
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request DELETE 'api.clarifai.com/v2/datasets/{{dataset_id}}/inputs' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input_ids": ["{{input_id}}"]
}'
```
{% endtab %}
{% endtabs %}
