# Custom Text Models Walkthrough


## Create an app

Create a new application and select “Text” as your default workflow



## Navigate to Explorer Mode



## Add your inputs
### Option 1: Browse your files

You can upload your text directly from a spreadsheet. If you like to use Google Sheets, you can start by making a copy of this template: https://docs.google.com/spreadsheets/d/1cnsLQAxIVlW7jUNEf8VWbUE1CDBxzrxEV3wPxJ1KJn4/edit?usp=sharing

Next, add your text data. At a minimum, you should add text to the `input.data.text.raw` field and the `input.data.concepts[i].id` field. Other fields are optional.

Input.data.text.raw - This is where you will input the text that you want to analyze with the awesome power of AI
Input.data.concepts[i].id - This is where you will list your custom concepts

Finally, you will need to Download this file as a .CSV file. In Google Sheets, go to File >>> Download >>> Comma-separated values (.csv, current sheet)

Once you have downloaded the .csv file, you can then upload it by clicking on “Browse your files”


### Option 2: Add text
Just click “add text” and directly enter your text in the text field.

Label your inputs
If you “add text” you will need to then label your inputs in Portal.

Navigate to Explorer Mode


## Add custom concepts
Click on an input and add new concepts in the right hand sidebar. Just click in the empty form field under “Custom Model Predictions”, enter your concept, and hit “return”.



## Navigate to Model Mode

Click Create Custom Model

Select Context-based Classifier
MODEL ID (OPTIONAL) - You do not need to create a custom model ID
DISPLAY NAME - This is the name of your new custom model. Enter a descriptive name.
OUTPUT_INFO.DATA.CONCEPTS - Click in the empty form field and select all of the custom concepts that you have added one-by-one
OUTPUT_INFO.OUTPUT_CONFIG.CONCEPTS_MUTUALLY_EXCLUSIVE - Use the default setting
OUTPUT_INFO.OUTPUT_CONFIG.CLOSED_ENVIRONMENT - Set CLOSED_ENVIRONMENT to “Yes”
OUTPUT_INFO.OUTPUT_CONFIG.EMBED_MODEL_VERSION_ID - Use the default setting


Click Create Model
Click Train Model
Once you click “Create Model”, a new screen will appear. Click “Train Model” in the upper right hand corner of the screen.

## Try out your new model
Navigate to “Explorer Mode” and “Add Inputs”. Add some new text inputs, and then navigate back to “Explorer Mode”

You will see custom concept predictions in the right hand sidebar when you click on an individual input.
