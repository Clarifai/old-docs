---
description: This is a page about performing task annotations with the Clarifai API.
---

# Task Annotations

In order to keep track of each user's work assigned to a task, all the annotations of this user related to this task should be linked to the task id.

Therefore, when a user creates an annotation, the task id should be provided as below:

{% tabs %}
{% tab title="cURL" %}
```text
curl -X POST \
  -H "Authorization: Key YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '
    {
      "annotations": [
        {
          "input_id": "{{asset_id}}",
          "data": {
            "concepts": [
              {
                "id": "tree",
                "value": 1
              },
              {
                "id": "water",
                "value": 0
              }
            ]
          },
          "annotation_info": {
            "task_id": "{{task_id}}"
          }
        }
      ]
    }'\
  https://api.clarifai.com/v2/annotations
```
{% endtab %}

{% tab title="Javascript (REST)" %}
```javascript
const raw = JSON.stringify({
	"user_app_id": {
		"user_id": "{YOUR_USER_ID}",
		"app_id": "{YOUR_APP_ID}"
	},
	"annotations": [
    {
      "input_id": "{{asset_id}}",
      "data": {
        "concepts": [
          {
            "id": "tree",
            "value": 1
          },
          {
            "id": "water",
            "value": 0
          }
        ]
      },
      "annotation_info": {
        "task_id": "{{task_id}}"
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

fetch("https://api.clarifai.com/v2/annotations", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
{% endtab %}

{% endtabs %}

