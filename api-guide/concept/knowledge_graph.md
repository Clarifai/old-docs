The Clarifai Knowledge Graph enables you to build a (hierarchy) and to map your custom concepts to a common set of concepts understood by all Clarifai Models. The knowledge graph makes it possible to link data across multiple custom and pre-built models in a meaningful way.

The knowledge graph uses three different *predicates* to organize your concepts: hypernyms, hyponyms, and synonyms.

**Hyponym** represents an 'is a kind of' relation. The following relationship: 'honey' (subject), 'hyponym' (predicate), 'food' (object) is more easily be read as 'honey' 'is a kind of' 'food'.

**Hypernym** is the opposite of 'hyponym'. When you add one of the relationships the opposite will automatically appear for you in queries. The 'hypernym' can be read as 'is a parent of' so: 'food' (subject), 'hypernym' (predicate), 'honey' (object)can more easily be read as:'food' is a parent of 'honey'.

**Synonym** The 'synonym' relation defines two concepts that essential mean the same thing. This is more like a "is" relationship. So for example a 'synonym' relationship could be: "puppy" is "pup" The reverse is also true once the former is added so: "pup" is "puppy" will appear in queries as well.



What you need to make these calls

PAT
need docs to explain the best way to get user id
need to explain pat
need to explain APP ID
concepts


(returned in login request)

## Create

Point out that will need to have concept as part of model

{% tabs %}
{% tab title="gRPC Python" %}
```python

```
{% endtab %}

{% tab title="gRPC Java" %}
```java

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js

```
{% endtab %}

{% tab title="cURL" %}
```text
curl --location --request POST 'https://api.clarifai.com/v2/users/{{user_id}}/apps/{{app_id}}/concepts/walker/relations' \
--header 'Authorization: Key {{personal_access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "concept_relations": [
        {
            "object_concept": {
                "id": "person"
            },
            "predicate": "hyponym"
        }
    ]
}'
```
{% endtab %}
{% endtabs %}




## Get

### Get existing relations

{% tabs %}
{% tab title="gRPC Python" %}
```python

```
{% endtab %}

{% tab title="gRPC Java" %}
```java

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js

```
{% endtab %}

{% tab title="cURL" %}
```text
curl --location --request GET 'https://api.clarifai.com/v2/users/{{user_id}}/apps/{{app_id}}/concepts/lamborghini23/relations' \
--header 'Authorization: Key {{key}}'
```
{% endtab %}
{% endtabs %}


### Get existing hypernym

{% tabs %}
{% tab title="gRPC Python" %}
```python

```
{% endtab %}

{% tab title="gRPC Java" %}
```java

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js

```
{% endtab %}

{% tab title="cURL" %}
```text
curl --location --request GET 'https://api.clarifai.com/v2/users/{{user_id}}/apps/{{app_id}}/concepts/{{concept_id}}/relations?predicate=hypernym' \
--header 'Authorization: Key {{key}}'
```
{% endtab %}
{% endtabs %}



### Get existing hyponym

{% tabs %}
{% tab title="gRPC Python" %}
```python

```
{% endtab %}

{% tab title="gRPC Java" %}
```java

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js

```
{% endtab %}

{% tab title="cURL" %}
```text
curl --location --request GET '{{base_url}}/v2/users/{{user_id}}/apps/{{app_id}}/concepts/{{concept_id}}/relations?predicate=hyponym' \
--header 'Authorization: Key {{key}}'
```
{% endtab %}
{% endtabs %}




## Delete

{% tabs %}
{% tab title="gRPC Python" %}
```python

```
{% endtab %}

{% tab title="gRPC Java" %}
```java

```
{% endtab %}

{% tab title="gRPC NodeJS" %}
```js

```
{% endtab %}

{% tab title="cURL" %}
```text

curl --location --request DELETE '{{base_url}}/v2/users/{{user_id}}/apps/{{app_id}}/concepts/{{your_concept}}/relations' \
--header 'Authorization: Key {{key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ids": [
    	"{{your_related_concept}}"
    ]
}'

```
{% endtab %}
{% endtabs %}







You can create these mappings in your application with a few easy steps.  

1. Consider the following application that has four concepts: beverages, smoothie, breakfast, and french_toast. You can use the Knowledge Graph to create hierarchical relationships between the concepts.

![](../../images/kg1.png)

2. You can link concepts as hierarchical by going to the details of either of the concepts. In the shown application, french_toast falls under breakfast. You can link them by accessing the View Details section of either concept.

![](../../images/kg2.png)

3. Once, in the details dashboard, you can link breakfast as a hypernym to french_toast under the Input Relations menu.

![](../../images/kg3.png)

4. Once you list breakfast as a hypernym to french_toast, it will set french_toast as a hyponym to breakfast automatically.

![](../../images/kg4.png)

5. This process can be used to create similar relationships between beverages and smoothie. Beverages will be listed as a hypernym to smoothie.

![](../../images/kg5.png)

6. By doing this, smoothie will be listed as a hyponym to beverages automatically.

![](../../images/kg6.png)
