---
description: Create, explore and modify datasets
---


# Basic dataset functions

## Create a dataset

{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location --request POST 'api.clarifai.com/v2/datasets' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasets": [
        {
            "id": "dataset-1633032323",
            "name": "foo",
            "description": "This is the foo dataset",
            "metadata": {
                "lol": "hey"
            }
        }
    ]
}'
```

{% endtab %}

## List datasets
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location --request GET 'api.clarifai.com/v2/datasets?page=1&per_page=100' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}


## Get datasets
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request GET 'api.clarifai.com/v2/datasets/{{dataset_id}}' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}


## Update datasets
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location --request PATCH 'api.clarifai.com/v2/datasets' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasets": [
        {
            "id": "{{dataset_id}}",
            "name": "foo",
            "description": "This is the new foo dataset",
            "metadata": {
                "foo": "bar"
            }
        }
    ],
    "action": "overwrite"
}'
```
{% endtab %}

## Update datasets with default filter
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location --request PATCH 'api.clarifai.com/v2/datasets' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasets": [
        {
            "id": "{{dataset_id}}",
            "name": "foo",
            "description": "This is the new foo dataset",
            "metadata": {
                "foo": "bar"
            },
            "default_filter_id": "{{dataset_filter_id}}"
        }
    ],
    "action": "overwrite"
}'
```
{% endtab %}

## Delete datasets
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location --request DELETE 'api.clarifai.com/v2/datasets' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_ids": ["{{dataset_id}}"]
}'
```
{% endtab %}
{% endtabs %}
