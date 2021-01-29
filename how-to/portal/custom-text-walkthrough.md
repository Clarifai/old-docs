---
description: Build a powerful and flexible application for classifying text passages.
---

# Text Classification

{% embed url="https://youtu.be/-blQVbccAF0" caption="Natural Language Processing with Clarifai" %}

Text models can be trained to understand the meaning of text passages. We offer a general text embedding model, as well as a specialized text moderation model. This walkthrough shows you how to create a custom text model from our text embedding model.

## Create an app

Create a new application and select “Text” as your default workflow.

![](../../.gitbook/assets/create_text.jpg)

## Navigate to Explorer Mode

![](../../.gitbook/assets/nav-to-explorer.jpg)

## Add your inputs

### Option 1: Browse your files

You can upload your text directly from a `.csv` file. This means you can work with your favorite spreadsheet software or text editor when preparing your data for upload. Just use the provided "CSV template" to get started.

![](../../.gitbook/assets/csv_template.jpg)

Next, add your text data. At a minimum, you should add text to the `input.data.text.raw` field. You can add one concept per column to the `input.data.concepts[*].id` fields. For the `input.data.concepts[*].value` column, there are two options: enter the number `1` if the concept _is_ present in the input, enter the value `0` if the concept is _not_ present in the input \(a negative example\). If no value is entered, a default value of `1` will be assigned to your input.

You can add columns for as many concepts as you like, and you can add new columns to add values for any other values supported by the API:

| Field | Description |
| :--- | :--- |
| input.id | A unique identifier for your input |
| input.data.text.raw | The "text" for your input |
| input.data.concepts\[i\].id | Your custom concept |
| input.data.concepts\[i\].value | The value for your custom concept \(`1` for true, `0` for false\) |
| input.metadata | Any additional metadata in valid [JSON](https://www.json.org/json-en.html) format |
| input.data.geo.geo\_point.latitude | Latitude for geodata |
| input.data.geo.geo\_point.longitude | Longitude for geodata |

Finally, you will need to save your work as a `.csv` file. If you are editing in Google Sheets, go to File &gt;&gt;&gt; Download &gt;&gt;&gt; Comma-separated values \(.csv, current sheet\). If you are using Excel, go to File &gt;&gt;&gt; Save As &gt;&gt;&gt; Browse &gt;&gt;&gt; Save as Type &gt;&gt;&gt; CSV.

Once you have downloaded the `.csv` file, you can then upload it by clicking on “Browse your files”

### Option 2: Add text

Just click “add text” and directly enter your text in the text field.

Label your inputs If you “add text” you will need to then label your inputs in Portal.

![](../../.gitbook/assets/browse_explorer.jpg)

#### Add custom concepts

Click on an input and add new concepts in the right hand sidebar. Just click in the empty form field under “Custom Model Predictions”, enter your concept, and hit “return”.

![](../../.gitbook/assets/label_concept.jpg)

## Navigate to Model Mode

![](../../.gitbook/assets/model_mode%20%285%29%20%285%29%20%287%29%20%287%29%20%283%29%20%285%29.jpg)

## Select Context-based Classifier

![](../../.gitbook/assets/sci_phil_context.jpg)

* **MODEL ID \(OPTIONAL\)** - Optional custom model ID of your choosing.
* **DISPLAY NAME** - This is the name of your new custom model. Enter a descriptive name.
* **OUTPUT\_INFO.DATA.CONCEPTS** - Click in the empty form field and select all of the custom concepts that you have added one-by-one.
* **OUTPUT\_INFO.OUTPUT\_CONFIG.CONCEPTS\_MUTUALLY\_EXCLUSIVE** - Use the default setting.
* **OUTPUT\_INFO.OUTPUT\_CONFIG.CLOSED\_ENVIRONMENT** - Set CLOSED\_ENVIRONMENT to “Yes”.
* **OUTPUT\_INFO.OUTPUT\_CONFIG.EMBED\_MODEL\_VERSION\_ID** - Use the default setting.

Once you click “Create Model”, a new screen will appear.

Click “Train Model” in the upper right hand corner of the screen.

## Try out your new model

Navigate to “Explorer Mode” and “Add Inputs”. Add some new text inputs, and then navigate back to “Explorer Mode”

You will see custom concept predictions in the right hand sidebar when you click on an individual input.

