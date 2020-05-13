# Create an Application

To create an application, head on over to the [applications page](https://portal.clarifai.com/apps) and press the 'Create a New Application' button. You have the option of using our General, Travel, Food, Face, Moderation, and Wedding models in your base workflow. More information on these, and other Clarifai Models can be found in our [model gallery](https://www.clarifai.com/models).

## Create an application in Portal

![](../../images/create-new-app-new.png)

{% hint style="info" %}
You can also set the default language so that you can create, train and search on concepts in your own language. Please keep in mind that pre-trained model concepts currently only work in English.
{% endhint %}

## Create an application programmatically

{% tabs %}
{% tab title="cURL" %}
```text
curl --location --request POST 'https://api.clarifai.com/v2/users/{{user_id}}/apps/' \
--header 'Content-Type: application/json' \
--header 'X-Clarifai-Session-Token: {{session_token}}' \
--data-raw '{
    "apps": [
        {
            "id": "test-application-1589318146"
        }
    ]
}'
```
{% endtab %}


## Copy an application

You can also create an application by cloning an existing application. Cloning an existing application can be a great way to start a new project, or branch and existing one. We’ve made cloning easy with a simple interface in Portal. Just click “Create a copy” in the bottom-right corner of your app on the app management page.

![](../../images/app_duplication.jpg)
