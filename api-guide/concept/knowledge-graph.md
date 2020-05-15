# Knowledge Graph

# What is the Clarifai Knowledge Graph?

You will find that some of our endpoints have additional information returned from the clarifai/main app which contains our pre-trained models but also a large knowledge graph we've assembled over the years.

The nodes of the knowledge graph are concpets (aka unique things in the world). In the knowledge graph we have done significant AI research and human verification to split apart concepts that have different meanings into different concepts.

Once we had different and clear meanings for the concepts, we could introduce translations of the concept name into other languages and relationships between concepts such as "dog" is an "animal" or
  "pup" and "puppy" are synonyms.


When interacting with concepts in search queries, model predict requests, etc. we allow in many cases to perform operations with the names of concpets in the other languages.

Since names can appear in differnt languages and have different meanings, it is always important to remember to use concept IDs when interacting with our API and not concept names.

## Supported Languages

The currently supported languages are listed below.

| Language | Code |
| :--- | :--- |
| Arabic \(ar\) | ar |
| Bengali \(bn\) | bn |
| Danish \(da\) | da |
| German \(de\) | de |
| English \(en\) | en |
| Spanish \(es\) | es |
| Finnish \(fi\) | fi |
| French \(fr\) | fr |
| Hindi \(hi\) | hi |
| Hungarian \(hu\) | hu |
| Italian \(it\) | it |
| Japanese \(ja\) | ja |
| Korean \(ko\) | ko |
| Dutch \(nl\) | nl |
| Norwegian \(no\) | no |
| Punjabi \(pa\) | pa |
| Polish \(pl\) | pl |
| Portuguese \(pt\) | pt |
| Russian \(ru\) | ru |
| Swedish \(sv\) | sv |
| Turkish \(tr\) | tr |
| Chinese Simplified \(zh\) | zh |
| Chinese Traditional \(zh-TW\) | zh-TW |

## Default Language

When you create a new Application, you must specify a default language. This will be the default language concepts are returned in when you do not explicitly set a language in an API request. You cannot change the default language. You can however change languages per request.

![create new app](../../images/create-new-app-new.png)
