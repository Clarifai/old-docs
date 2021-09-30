---
description: Use filter and search functionality over your datasets
---


# Dataset Filters

## Add dataset filters
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request POST 'api.clarifai.com/v2/datasets/{{dataset_id}}/filters' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_filters": [
        {
            "id": "dataset-filter-1633032596",
            "name": "foo",
            "saved_search": {
                "id": "{{search_id}}"
            }
        }
    ]
}'
```
{% endtab %}
## List dataset Filters
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request GET 'api.clarifai.com/v2/datasets/{{dataset_id}}/filters?page=1&per_page=100' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}

## Get a dataset filter
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request GET 'api.clarifai.com/v2/datasets/{{dataset_id}}/filters/{{dataset_filter_id}}' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}

## Change a dataset filter

{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request PATCH 'api.clarifai.com/v2/datasets/{{dataset_id}}/filters' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_filters": [
        {
            "id": "{{dataset_filter_id}}",
            "name": "foo bar",
            "saved_search_id": "{{search_id}}"
        }
    ],
    "action": "overwrite"
}'
```
{% endtab %}
## Delete a dataset filter
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request DELETE 'api.clarifai.com/v2/datasets/{{dataset_id}}/filters' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_filter_ids": ["{{dataset_filter_id}}"]
}'
```
{% endtab %}
{% endtabs %}
