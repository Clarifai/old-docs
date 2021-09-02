---
description: Develop your own custom text classifier.
---

# Custom Text Model

The Clarifai API has the ability not only to learn concepts from images and videos, but from text as well.

In this walkthrough, you'll learn how to create and use a custom text model, learn from your own text data using the power of the Clarifai's base Text model, and predict on new text examples.

The steps below can all be done via [the Clarifai's portal](https://portal.clarifai.com). But here you'll learn how to do them programmatically via API, using our [gRPC Python client](https://github.com/Clarifai/clarifai-python-grpc).

The examples below map directly to any of our other gRPC clients.

The walkthrough assumes you have already created your Clarifai's user account and the [Personal Access Token](https://portal.clarifai.com/settings/authentication). Also, first set up the gRPC Python client together with the initial code, see [Client Installation Instructions](https://github.com/Clarifai/docs/tree/1c1d25cdd43190c38a2edb313297c0d566b3a0e3/api-guide/api-overview/api-clients/README.md#client-installation-instructions).

For debugging purposes, each response returned by a method call can be printed to the console, and its entire data and structure will be shown verbosely.

## Create a new application

The first step is manual: in the Clarifai Portal, [create an new application](https://docs.clarifai.com/getting-started/applications/create-an-application) with **Text** selected as the Base Workflow.

Afterward, copy the newly-created application's _API key_ and set it in the variable below. This variable is going to be used, for authorization purposes, by all Clarifai API calls that follow.

{% tabs %}
{% tab title="gRPC Python" %}
```python
# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

api_key_metadata = (('authorization', 'Key ' + post_keys_response.keys[0].id),)
```
{% endtab %}
{% endtabs %}

## Add a batch of texts

We'll now add several text inputs that we will later use as a training data in our custom model. The idea is that we'll create a model which can differentiate between positive and negative sentences \(in a grammatical sense\). We'll mark each input with one of the two concepts: `positive` or `negative`.

The text can be added either directly \(it's called raw\), or from a URL.

{% tabs %}
{% tab title="gRPC Python" %}
```python
positive_raw_texts = [
    "Marie is a published author.",
    "In three years, everyone will be happy.",
    "Nora Roberts is the most prolific romance writer the world has ever known.",
    "She has written more than 225 books.",
    "If you walk into Knoxville, you'll find a shop named Rala.",
    "There are more than 850 miles of hiking trails in the Great Smoky Mountains.",
    "Harrison Ford is 6'1\".",
    "According to Reader's Digest, in the original script of Return of The Jedi, Han Solo died.",
    "Kate travels to Doolin, Ireland every year for a writers' conference.",
    "Fort Stevens was decommissioned by the United States military in 1947.",
]
negative_text_urls = [
    "https://samples.clarifai.com/negative_sentence_1.txt",
    "https://samples.clarifai.com/negative_sentence_2.txt",
    "https://samples.clarifai.com/negative_sentence_3.txt",
    "https://samples.clarifai.com/negative_sentence_4.txt",
    "https://samples.clarifai.com/negative_sentence_5.txt",
    "https://samples.clarifai.com/negative_sentence_6.txt",
    "https://samples.clarifai.com/negative_sentence_7.txt",
    "https://samples.clarifai.com/negative_sentence_8.txt",
    "https://samples.clarifai.com/negative_sentence_9.txt",
    "https://samples.clarifai.com/negative_sentence_10.txt",
]

post_inputs_response = stub.PostInputs(
    service_pb2.PostInputsRequest(
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    text=resources_pb2.Text(raw=raw_text),
                    concepts=[resources_pb2.Concept(id="positive", value=1)]
                )
            )
            for raw_text in positive_raw_texts
        ] + [
            resources_pb2.Input(
                data=resources_pb2.Data(
                    text=resources_pb2.Text(
                        url=text_url,
                        allow_duplicate_url=True
                    ),
                    concepts=[resources_pb2.Concept(id="negative", value=1)]
                )
            )
            for text_url in negative_text_urls
        ]
    ),
    metadata=api_key_metadata
)

# You may print the response to see what the structure and the data of the response is.
# print(post_inputs_response)

if post_inputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_inputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_inputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_inputs_response.outputs[0].status.details))
    raise Exception("Failed response, status: " + str(post_inputs_response.status))
```
{% endtab %}
{% endtabs %}

## Wait for inputs to download

Let's now wait for all the inputs to download.

{% tabs %}
{% tab title="gRPC Python" %}
```python
import time

while True:
    list_inputs_response = stub.ListInputs(
        service_pb2.ListInputsRequest(page=1, per_page=100),
        metadata=api_key_metadata
    )

    if list_inputs_response.status.code != status_code_pb2.SUCCESS:
        print("There was an error with your request!")
        print("\tCode: {}".format(list_inputs_response.outputs[0].status.code))
        print("\tDescription: {}".format(list_inputs_response.outputs[0].status.description))
        print("\tDetails: {}".format(list_inputs_response.outputs[0].status.details))
        raise Exception("Failed response, status: " + str(list_inputs_response.status))

    for the_input in list_inputs_response.inputs:
        input_status_code = the_input.status.code
        if input_status_code == status_code_pb2.INPUT_DOWNLOAD_SUCCESS:
            continue
        elif input_status_code in (status_code_pb2.INPUT_DOWNLOAD_PENDING, status_code_pb2.INPUT_DOWNLOAD_IN_PROGRESS):
            print("Not all inputs have been downloaded yet. Checking again shortly.")
            break
        else:
            error_message = (
                    str(input_status_code) + " " +
                    the_input.status.description + " " +
                    the_input.status.details
            )
            raise Exception(
                f"Expected inputs to download, but got {error_message}. Full response: {list_inputs_response}"
            )
    else:
        # Once all inputs have been successfully downloaded, break the while True loop.
        print("All inputs have been successfully downloaded.")
        break
    time.sleep(2)
```
{% endtab %}
{% endtabs %}

## Create a custom model

Now we can create a custom model that's going to be using the concepts `positive` and `negative`. All inputs \(in our application\) associated with these two concepts will be used as a training data, once we actually train the model.

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_models_response = stub.PostModels(
    service_pb2.PostModelsRequest(
        models=[
            resources_pb2.Model(
                id="my-text-model",
                output_info=resources_pb2.OutputInfo(
                    data=resources_pb2.Data(
                        concepts=[
                            resources_pb2.Concept(id="positive"),
                            resources_pb2.Concept(id="negative"),
                        ]
                    ),
                    output_config=resources_pb2.OutputConfig(closed_environment=True)
                )
            )
        ]
    ),
    metadata=api_key_metadata
)

if post_models_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_models_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_models_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_models_response.outputs[0].status.details))
    raise Exception("Failed response, status: " + str(post_models_response.status))
```
{% endtab %}
{% endtabs %}

## Train the model

Let's train the model, making it learn from the inputs, so we can later use it to predict new text examples!

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_model_versions_response = stub.PostModelVersions(
    service_pb2.PostModelVersionsRequest(model_id="my-text-model"),
    metadata=api_key_metadata
)

if post_model_versions_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_model_versions_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_model_versions_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_model_versions_response.outputs[0].status.details))
    raise Exception("Failed response, status: " + str(post_model_versions_response.status))
```
{% endtab %}
{% endtabs %}

## Wait for model training to complete

Let's wait for the model training to complete.

Each model training produces a new model version. See on the bottom of the code example, that we put the model version ID into its own variable. We'll be using it below to specify which specific model version we want to use \(since a model can have multiple versions\).

{% tabs %}
{% tab title="gRPC Python" %}
```python
import time

while True:
    get_model_response = stub.GetModel(
        service_pb2.GetModelRequest(model_id="my-text-model"),
        metadata=api_key_metadata
    )

    if get_model_response.status.code != status_code_pb2.SUCCESS:
        print("There was an error with your request!")
        print("\tCode: {}".format(get_model_response.outputs[0].status.code))
        print("\tDescription: {}".format(get_model_response.outputs[0].status.description))
        print("\tDetails: {}".format(get_model_response.outputs[0].status.details))
        raise Exception("Failed response, status: " + str(get_model_response.status))

    version_status_code = get_model_response.model.model_version.status.code
    if version_status_code == status_code_pb2.MODEL_TRAINED:
        print("The model has been successfully trained.")
        break
    elif version_status_code in (status_code_pb2.MODEL_QUEUED_FOR_TRAINING, status_code_pb2.MODEL_TRAINING):
        print("The model hasn't been trained yet. Trying again shortly.")
        time.sleep(2)
    else:
        error_message = (
                str(get_model_response.status.code) + " " +
                get_model_response.status.description + " " +
                get_model_response.status.details
        )
        raise Exception(
            f"Expected model to train, but got {error_message}. Full response: {get_model_response}"
        )

model_version_id = get_model_response.model.model_version.id
```
{% endtab %}
{% endtabs %}

## Predict on new inputs

Now we can use the new custom model to predict new text examples.

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id="my-text-model",
        # By default, the latest model version will be used, but it doesn't hurt to set it explicitly.
        version_id=model_version_id,
        inputs=[
            resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(raw="Butchart Gardens contains over 900 varieties of plants."))),
            resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(url="https://samples.clarifai.com/negative_sentence_12.txt"))),
        ]
    ),
    metadata=api_key_metadata
)

if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_model_outputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_model_outputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_model_outputs_response.outputs[0].status.details))
    raise Exception("Failed response, status: " + str(post_model_outputs_response.status))

for output in post_model_outputs_response.outputs:
    text_object = output.input.data.text
    val = text_object.raw if text_object.raw else text_object.url

    print(f"The following concepts were predicted for the input `{val}`:")
    for concept in output.data.concepts:
        print(f"\t{concept.name}: {concept.value:.2f}")
```
{% endtab %}
{% endtabs %}

## Start model evaluation

Let's now test the performance of the model by using model evaluation. See the [the Model Evaluation page](https://docs.clarifai.com/portal-guide/model/evaluate) to learn more.

{% tabs %}
{% tab title="gRPC Python" %}
```python
post_model_version_metrics = stub.PostModelVersionMetrics(
    service_pb2.PostModelVersionMetricsRequest(
        model_id="my-text-model",
        version_id=model_version_id
    ),
    metadata=api_key_metadata
)

if post_model_version_metrics.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_model_version_metrics.outputs[0].status.code))
    print("\tDescription: {}".format(post_model_version_metrics.outputs[0].status.description))
    print("\tDetails: {}".format(post_model_version_metrics.outputs[0].status.details))
    raise Exception("Failed response, status: " + str(post_model_version_metrics.status))
```
{% endtab %}
{% endtabs %}

## Wait for model evaluation results

Model evaluation takes some time, depending on the amount of data in our model. Let's wait for it to complete, and print all the results that it gives us.

{% tabs %}
{% tab title="gRPC Python" %}
```python
import time

while True:
    get_model_version_metrics_response = stub.GetModelVersionMetrics(
        service_pb2.GetModelVersionMetricsRequest(
            model_id="my-text-model",
            version_id=model_version_id,
            fields=resources_pb2.FieldsValue(
                confusion_matrix=True,
                cooccurrence_matrix=True,
                label_counts=True,
                binary_metrics=True,
                test_set=True,
                metrics_by_area=True,
                metrics_by_class=True,
            )
        ),
        metadata=api_key_metadata
    )

    if get_model_version_metrics_response.status.code != status_code_pb2.SUCCESS:
        print("There was an error with your request!")
        print("\tCode: {}".format(get_model_version_metrics_response.outputs[0].status.code))
        print("\tDescription: {}".format(get_model_version_metrics_response.outputs[0].status.description))
        print("\tDetails: {}".format(get_model_version_metrics_response.outputs[0].status.details))
        raise Exception("Get model version metrics failed: " + str(get_model_version_metrics_response.status))

    metrics_status_code = get_model_version_metrics_response.model_version.metrics.status.code
    if metrics_status_code == status_code_pb2.MODEL_EVALUATED:
        print("The model has been successfully evaluated.")
        break
    elif metrics_status_code in (status_code_pb2.MODEL_NOT_EVALUATED, status_code_pb2.MODEL_QUEUED_FOR_EVALUATION, status_code_pb2.MODEL_EVALUATING):
        print("The model hasn't been evaluated yet. Trying again shortly.")
        time.sleep(2)
    else:
        error_message = (
                str(get_model_version_metrics_response.status.code) + " " +
                get_model_version_metrics_response.status.description + " " +
                get_model_version_metrics_response.status.details
        )
        raise Exception(
            f"Expected model to evaluate, but got {error_message}. Full response: {get_model_version_metrics_response}"
        )

print("The model metrics response object:")
print(get_model_version_metrics_response)
```
{% endtab %}
{% endtabs %}

