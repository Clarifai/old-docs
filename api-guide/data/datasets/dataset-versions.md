---
description: Manage dataset versions so you can track the performance of and iterate on your datasets
---


# Dataset Versions

## Add a dataset version
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request POST 'api.clarifai.com/v2/datasets/{{dataset_id}}/versions' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_versions": [
        {
            "id": "dataset-version-1633032673",
            "name": "foo",
            "dataset_filter": {
                "id": "{{dataset_filter_id}}"
            }
        }
    ]
}'
```
{% endtab %}
## List dataset versions
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request GET 'api.clarifai.com/v2/datasets/{{dataset_id}}/versions?page=1&per_page=100' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}
## Get a dataset versions
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request GET 'api.clarifai.com/v2/datasets/{{dataset_id}}/versions/{{dataset_version_id}}' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json'
```
{% endtab %}
## Change a dataset version
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request PATCH 'api.clarifai.com/v2/datasets/{{dataset_id}}/versions' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_versions": [
        {
            "id": "{{dataset_version_id}}",
            "name": "dataset version updated name"
        }
    ],
    "action": "overwrite"
}'
```
{% endtab %}
## Delete a dataset version
{% tabs %}
{% tab title="cURL" %}
```cURL
curl --location -g --request DELETE 'api.clarifai.com/v2/datasets/{{dataset_id}}/versions' \
--header 'Authorization: Key {{YOUR API KEY}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataset_version_ids": ["{{dataset_version_id}}"]
}'
```
{% endtab %}
{% endtabs %}
