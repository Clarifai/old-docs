---
description: Connect the knowledge of different models.
---

# Knowledge Graph

The Clarifai Knowledge Graph lets you map your custom concepts to a common set of concepts understood by all applications on the Clarifai platform. The knowledge graph makes it possible to link data across multiple custom and pre-built models in a meaningful way.

The Knowledge Graph uses Clarifai's concept mapping model to establish a hierarchical relationship between your concepts. Concept relationships are organized by three different _predicates_: hypernyms, hyponyms, and synonyms.

**Hyponym** represents an 'is a kind of' relation. The following relationship: 'honey' \(subject\), 'hyponym' \(predicate\), 'food' \(object\) is more easily be read as 'honey' 'is a kind of' 'food'.

**Hypernym** is the opposite of 'hyponym'. When you add one of the relationships the opposite will automatically appear for you in queries. The 'hypernym' can be read as 'is a parent of' so: 'food' \(subject\), 'hypernym' \(predicate\), 'honey' \(object\) can more easily be read as:'food' is a parent of 'honey'.

**Synonym** The 'synonym' relation defines two concepts that essential mean the same thing. This is more like a "is" relationship. So for example a 'synonym' relationship could be: "puppy" is "pup" The reverse is also true once the former is added so: "pup" is "puppy" will appear in queries as well.

You can create these mappings in your application with a few easy steps.

1. Consider the following application that has four concepts: beverages, smoothie, breakfast, and french\_toast. You can use the Knowledge Graph to create hierarchical relationships between the concepts.

![](../../.gitbook/assets/kg1%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%284%29.png)

1. You can link concepts as hierarchical by going to the details of either of the concepts. In the shown application, french\_toast falls under breakfast. You can link them by accessing the View Details section of either concept.

![](../../.gitbook/assets/kg2%20%282%29%20%282%29%20%283%29%20%283%29%20%282%29%20%2812%29%20%281%29.png)

1. Once, in the details dashboard, you can link breakfast as a hypernym to french\_toast under the Input Relations menu.

![](../../.gitbook/assets/kg3%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%283%29%20%281%29%20%281%29.png)

1. Once you list breakfast as a hypernym to french\_toast, it will set french\_toast as a hyponym to breakfast automatically.

![](../../.gitbook/assets/kg4%20%281%29%20%283%29%20%283%29%20%283%29%20%283%29%20%282%29%20%283%29.png)

1. This process can be used to create similar relationships between beverages and smoothie. Beverages will be listed as a hypernym to smoothie.

![](../../.gitbook/assets/kg5%20%282%29%20%282%29%20%283%29%20%283%29%20%283%29%20%283%29%20%281%29%20%287%29%20%281%29.png)

1. By doing this, smoothie will be listed as a hyponym to beverages automatically.

![](../../.gitbook/assets/kg6%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%286%29%20%284%29%20%281%29.png)

