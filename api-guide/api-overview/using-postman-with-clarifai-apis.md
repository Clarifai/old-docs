# Using Postman with Clarifai APIs

## **Overview**

This page explains how to use [Postman](https://www.postman.com/) to perform API calls to Clarifai by showing the actions available within the Clarifai API. You can use Postman to make a wide variety of `GET`, `POST`, `PATCH`, and `DELETE` calls.

## Prerequisites <a id="prerequisites"></a>

You have:

* An active Clarifai account.
* Access to your [Clarifai API key](https://docs.clarifai.com/getting-started/authentication/app-specific-api-keys) and user login credentials.
* Basic knowledge of API structure and JSON formatting.

## Setup <a id="setup"></a>

### Import the Clarifai collection into Postman <a id="import-the-datadog-collection-into-postman"></a>

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/8c7850b96f74d0fc03c0)

This collection works in Postman for Web or in your Postman application. It may take several seconds to load.

### Postman environment setup <a id="postman-environment-setup"></a>

After the Postman collection is imported, a full list of available Clarifai API calls is structured by folder in the left pane of Postman.

**AUTHENTICATION**

The collection includes a [Postman environment](https://learning.postman.com/docs/postman/variables-and-environments/variables/#environments-in-postman) called `Clarifai Authentication`, where you can add your username, password and [Clarifai API key](https://docs.clarifai.com/getting-started/authentication/app-specific-api-keys) or [Personal Access Token](https://docs.clarifai.com/getting-started/authentication/personal-access-tokens) for authentication.

Follow these steps to set up your environment:

1. Click the **Manage Environments** gear icon in the upper right corner of Postman.
2. Select **Clarifai Authentication**
3. Click **Edit**.
4. Add in your Clarifai API key as the initial value and current value for the `api_key` variable, and add your Clarifai Application key as the initial value and current value for the `application_key` variable.

## Working with the Collection <a id="working-with-the-collection"></a>

After setup is complete, you are ready to begin making API calls. In the Postman -&gt; Clarifai folder, there are subfolders for each type of API category listed in the Clarifai API Reference. Expand the subfolders to see the HTTP methods and API call names.

### Builder <a id="builder"></a>

When you click on an API call in the collection, it loads in the `Builder` pane on the right. On this pane you can send the API call and see the returned status, response time, and API response code.

### Description <a id="description"></a>

When you click on the Endpoint name a description of the endpoint and all required/optional parameters is displayed to help you build your requests:

### Params <a id="params"></a>

The **Params** tab shows all parameters and values that are currently on the API call. Here, you are able to add parameters and values. View the available arguments in the corresponding section of the [Clarifai API documentation](https://docs.clarifai.com/api-guide/api-overview).

This tab is an alternative to viewing the `param1:value1¶m2:value2` structure of the API call.

**Notes**:

* The ampersand \(&\) and colon \(:\) are not needed in the params table. Postman inserts these for you.
* All placeholders follow the format: `<PLACEHOLDER>` . They should be replaced before running a query.

