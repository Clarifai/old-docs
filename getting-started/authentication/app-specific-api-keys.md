# App-Specific API Keys

App-specific API Keys are used to authorize your Clarifai applications. A key is automatically generated when you create a new application. You can also go to the [Application's List](https://portal.clarifai.com/apps), select an app of your choice and create a new key in the app details page. _Each API key is tied to a specific user and a specific app._

You have fine-grained control over the data exposed through your app. You can control the scope of an API Key through a simple checkbox interface when you first set up your app.

## Create an API Key in Portal

Just navigate to the app management page and click "Create an API Key"

![](../../.gitbook/assets/apikey-screen%20%282%29%20%282%29.png)

## Create an API Key programmatically

For enterprise customers, it is also possible to generate applications and keys programmatically. If you are managing the work of multiple users who's data, models, and concepts need to be segregated, we recommend you create apps and a keys this way. This ensures that each individual user only has access to their own private resources.

{% tabs %}
{% tab title="cURL" %}
```text
curl --location --request POST 'https://api.clarifai.com/v2/users/{{user_id}}/keys' \
--header 'Content-Type: application/json' \
--header 'X-Clarifai-Session-Token: {{session_token}}' \
--data-raw '{
    "keys": [
        {
            "description": "All permissions",
            "scopes": [
                "All"
            ],
            "apps": [
                {
                    "id": "{{app_id}}",
                    "user_id": "{{user_id}}"
                }
            ]
        }
    ]
}'
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
API Keys do not expire. In case your API Key gets compromised, you should delete that key, and create a new one with the same scopes. We recommend that you do **not** share your API Key with other users.
{% endhint %}

