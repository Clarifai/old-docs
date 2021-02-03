# Legacy Search

You can send inputs \(as a url or bytes\) and once indexed, you can search for images by concept, image, or many advanced search parameters. When you `POST /inputs`, your base workflow is used to index your inputs, and this index enables search over the outputs of the models in your workflow.

## Rank

Your model can identify concepts in your data and rank your search results by how confident it is that a given concept is present. You can even rank search results by how similar one input is to another input.

## Filter

Trim down the amount of data returned in search. For example, you may only want to see inputs that one of your collaborators has labeled with the word “dog”. Or perhaps you want only those inputs that were captured in a certain geographical region.

## 'AND'

Combine multiple search parameters. For example, you can find all the inputs within a geographical region with a "weapon" in them, or all annotations assigned to user "Joe", or visually similar product images that are assigned the word "XL" in metadata.

{% hint style="info" %}
Search currently is only available for images.
{% endhint %}

![Image illustrating how to search by images using Clarifai&apos;s concepts](../../../.gitbook/assets/illustration-search%20%282%29%20%282%29%20%283%29%20%284%29%20%284%29%20%284%29%20%284%29%20%286%29%20%282%29%20%281%29.png)

