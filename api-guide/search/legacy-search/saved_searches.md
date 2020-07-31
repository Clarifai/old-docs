# Saved Searches

With saved searches you can capture your search results at a given point in time, and record the inputs, annotations, search parameters and models that you are running through the platform. Saved searches help you to:

* Save a search so that you can return to those same results later
* Share a search with a collaborator in your app
* Carve out data that you want to evaluate your models on as a "golden set"
* Split your data into training sets and test tests

## Create a saved search

{% tabs %}
{% tab title="cURL" %}
```text
curl --location --request POST 'https://api.clarifai.com/v2/searches/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Key {{key}}' \
--data-raw '{
	"searches": [{
    	"query": {
    		"ands": [{
	        	"annotation":{
	            	"annotation_info": {
	                	"asset_set": ["set1", "set2"]
	            	}
	        	}
	        }]
		},
    	"save": true,
    	"id": "dataset-1589318146",
    	"name": "Dataset #1589318146"
	}]
}
'
```
{% endtab %}
{% endtabs %}

## List saved searches in an app

{% tabs %}
{% tab title="cURL" %}
```text
curl --location --request GET 'https://api.clarifai.com/v2/searches/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Key {{key}}'
```
{% endtab %}
{% endtabs %}

## Search by search ID

{% tabs %}
{% tab title="cURL" %}
```text
curl --location --request POST 'https://api.clarifai.com/v2/searches/{{search_id}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Key {{key}}' \
--data-raw '{
  "pagination": {
    "page": 1,
    "per_page": 5
  }
}'
```
{% endtab %}
{% endtabs %}

Saved searches are extremely helpful when testing out multiple versions of a model, or collaborating with a team. Just save your search, and refer back to it any time.
