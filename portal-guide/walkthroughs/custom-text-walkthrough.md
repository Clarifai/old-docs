# Custom Text Models Walkthrough

Text models can be trained to understand the meaning of text passages. We offer a general text embedding model, as well as a specialized text moderation model. This walkthrough shows you how to create a custom text model from our text embedding model.

## Create an app

Create a new application and select “Text” as your default workflow.

![](../../images/create_text.jpg)

## Navigate to Explorer Mode

![](../../images/nav-to-explorer.jpg)

## Add your inputs

![](../../images/browse_add.jpg)

### Option 1: Browse your files

You can upload your text directly from a `.csv` file. This means you can work with your favorite spreadsheet software or text editor when preparing your data for upload. Just use the provided "CSV template" to get started.

Next, add your text data. At a minimum, you should add text to the `input.data.text.raw` field and the `input.data.concepts[i].id` field. Other fields are optional.

* **Input.data.text.raw** - This is where you will input the text that you want to analyze with the awesome power of AI
* **Input.data.concepts[i].id** - This is where you will list your custom concepts

Finally, you will need to save your work as a `.csv` file. If you are editing in Google Sheets, go to File >>> Download >>> Comma-separated values (.csv, current sheet). If you are using Excel, go to File >>> Save As >>> Browse >>> Save as Type >>> CSV.

Once you have downloaded the `.csv` file, you can then upload it by clicking on “Browse your files”


### Option 2: Add text
Just click “add text” and directly enter your text in the text field.

Label your inputs
If you “add text” you will need to then label your inputs in Portal.

![](../../images/browse_explorer.jpg)

#### Add custom concepts
Click on an input and add new concepts in the right hand sidebar. Just click in the empty form field under “Custom Model Predictions”, enter your concept, and hit “return”.

![](../../images/label_concept.jpg)

## Navigate to Model Mode

![](../../images/model_mode.jpg)

## Select Context-based Classifier

![](../../images/sci_phil_context.jpg)

* **MODEL ID (OPTIONAL)** - Optional custom model ID of your choosing.
* **DISPLAY NAME** - This is the name of your new custom model. Enter a descriptive name.
* **OUTPUT_INFO.DATA.CONCEPTS** - Click in the empty form field and select all of the custom concepts that you have added one-by-one.
* **OUTPUT_INFO.OUTPUT_CONFIG.CONCEPTS_MUTUALLY_EXCLUSIVE** - Use the default setting.
* **OUTPUT_INFO.OUTPUT_CONFIG.CLOSED_ENVIRONMENT** - Set CLOSED_ENVIRONMENT to “Yes”.
* **OUTPUT_INFO.OUTPUT_CONFIG.EMBED_MODEL_VERSION_ID** - Use the default setting.

Once you click “Create Model”, a new screen will appear.

Click “Train Model” in the upper right hand corner of the screen.

## Try out your new model
Navigate to “Explorer Mode” and “Add Inputs”. Add some new text inputs, and then navigate back to “Explorer Mode”

You will see custom concept predictions in the right hand sidebar when you click on an individual input.
