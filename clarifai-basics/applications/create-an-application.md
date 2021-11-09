# Create an Application

To create an application, head on over to the [applications page](https://portal.clarifai.com/apps) and press the 'Create a New Application' button. 

## Create an application in Portal

![Application creation window](../../.gitbook/assets/create-new-app-new.png)

### ID Validation

Application names and other names in Portal must follow a few rules. Names must be 1 to 32 letters or numbers in length, with hyphens or underscores as separators \(spaces, periods, etc are not allowed\).


You can also set the default language so that you can create, train and search on concepts in your own language. Please keep in mind that pre-trained model concepts currently only work in English.


## Create an application programmatically

For enterprise customers, it is also possible to generate applications and keys programmatically. If you are managing the work of multiple users who's data, models, and concepts need to be segregated, we recommend you create apps and a keys this way. This ensures that each individual user only has access to their own private resources.

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
{% endtabs %}

### Copy an application

You can also create an application by cloning an existing application. Cloning an existing application can be a great way to start a new project, or branch and existing one. We’ve made cloning easy with a simple interface in Portal. Just click “Create a copy” in the bottom-right corner of your app on the app management page.

![](../../.gitbook/assets/app_duplication.jpg)

