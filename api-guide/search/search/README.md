# Search

You can send inputs \(as a url or bytes\) and once indexed, you can search for images by concept, image, or many advanced search parameters. When you `POST /inputs`, your base workflow is used to index your inputs, and this index enables search over the outputs of the models in your workflow.

## Rank

Your model can identify concepts in your data and rank your search results by how confident it is that a given concept is present. You can even rank search results by how similar one input is to another input.

## Filter

Trim down the amount of data returned in search. For example, you may only want to see inputs that one of your collaborators has labeled with the word “dog”. Or perhaps you want only those inputs that were captured in a certain geographical region.
