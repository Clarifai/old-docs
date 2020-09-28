# CSV & TSV Uploads

You can upload your text directly from a `.csv` ([comma separated values](https://en.wikipedia.org/wiki/Comma-separated_values)) or `.tsv` ([tab separated values](https://en.wikipedia.org/wiki/Tab-separated_values)) file. This means you can work with your favorite spreadsheet software or text editor when preparing your data for upload. This can be especially useful when you want to upload inputs and concepts at the same time. Just use the provided "CSV template" to get started.

## CSV templates

To help you get started, you can download `.csv` templates for images and text uploads here:

[Image Upload Template](../../.gitbook/assets/ClarifaiImageUploadTemplate.csv)
[Text Upload Template](../../.gitbook/assets/ClarifaiTextUploadTemplate.csv)

### Working with your CSV file

At a minimum, you should add and image URL or text to the `input.data.image.url` or `input.data.text.raw` field respectively. You can add one concept per column to the `input.data.concepts[*].id` fields. For the `input.data.concepts[*].value` column, there are two options: enter the number `1` if the concept *is* present in the input, enter the value `0` if the concept is *not* present in the input (a negative example). If no value is entered, a default value of `1` will be assigned to your input.

You can add columns for as many concepts as you like, and you can add new columns to add values for any other values supported by the API:

| Field | Description |
| :--- | :--- |
| input.id | A unique identifier for your input |
| input.data.image.url | The URL (web address) for your input |
| input.data.text.raw | The "text" for your input |
| input.data.concepts\[i\].id | Your custom concept |
| input.data.concepts\[i\].value | The value for your custom concept \(`1` for true, `0` for false\) |
| input.metadata | Any additional metadata in valid [JSON](https://www.json.org/json-en.html) format |
| input.data.geo.geo\_point.latitude | Latitude for geodata |
| input.data.geo.geo\_point.longitude | Longitude for geodata |

Finally, you will need to save your work as a `.csv` file. If you are editing in Google Sheets, go to File &gt;&gt;&gt; Download &gt;&gt;&gt; Comma-separated values \(.csv, current sheet\). If you are using Excel, go to File &gt;&gt;&gt; Save As &gt;&gt;&gt; Browse &gt;&gt;&gt; Save as Type &gt;&gt;&gt; CSV.

Once you have downloaded the `.csv` file, you can then upload it by clicking on “Browse files”
