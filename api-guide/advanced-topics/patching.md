---
description: Patch data in your applications.
---

# Patching

We designed PATCH to work over multiple resources at the same time \(bulk\) and be flexible enough for all your needs to minimize round trips to the server. Therefore it might seem a little different to any PATCH you've seen before, but it's not complicated. All three actions that are supported do overwrite by default, but have special behaviour for lists of objects \(for example lists of concepts\).

## Merge

`merge` action will overwrite a key:value with key:new\_value or append to an existing list of values, merging dictionaries that match by a corresponding `id` field.

In the following examples A is being patched into B to create the Result:

```text
*Merges different key:values*
A = `{"a":[1,2,3]}`
B = `{"blah":true}`
Result = `{"blah":true, "a":[1,2,3]}`

*For id lists, merge will append*
A = `{"a":[{"id": 1}]}`
B = `{"a":[{"id": 2}]}`
Result = `{"a":[{"id": 2}, {"id":1}]}`

*Simple merge of key:values and within a list*
A = `{"a":[{"id": "1", "other":true}], "blah":1}`
B = `{"a":[{"id": "2"},{"id":"1", "other":false}]}`
Result = `{"a":[{"id": "2"},{"id": "1"}], "blah":1}`

*Different types should overwrite fine*
A = `{"a":[{"id": "1"}], "blah":1}`
B = `{"a":[{"id": "2"}], "blah":"string"}`
Result = `{"a":[{"id": "2"},{"id": "1"}], "blah":1}`

*Deep merge, notice the "id":"1" matches, so those dicts are merged in the list*
A = `{"a":[{"id": "1","hey":true}], "blah":1}`
B = `{"a":[{"id": "1","foo":"bar","hey":false},{"id":"2"}], "blah":"string"}`
Result = `{"a":[{"hey":true,"id": "1","foo":"bar"},{"id":"2"}], "blah":1}`

*For non-id lists, merge will append*
A = `{"a":[{"blah": "1"}], "blah":1}`
B = `{"a":[{"blah": "2"}], "blah":"string"}`
Result = `{"a":[{"blah": "2"}, {"blah":"1"}], "blah":1}`

*For non-id lists, merge will append*
A = `{"a":[{"blah": "1"}], "blah":1, "dict":{"a":1,"b":2}}`
B = `{"a":[{"blah": "2"}], "blah":"string"}`
Result = `{"a":[{"blah": "2"}, {"blah":"1"}], "blah":1, "dict":{"a":1,"b":2}}`

*Simple overwrite root element*
A = `{"key1":true}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":true}`

*Overwrite a sub element*
A = `{"key1":{"key2":true}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key2":true, "key3":"value3"}}`

*Merge a sub element*
A = `{"key1":{"key2":{"key4":"value4"}}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key2":{"key4":"value4"}, "key3":"value3"}}`

*Merge multiple trees*
A = `{"key1":{"key2":{"key9":"value9"}, "key3":{"key4":"value4", "key10":[1,2,3]}}, "key6":{"key11":"value11"}}`
B = `{"key1":{"key2":"value2", "key3":{"key4":{"key5":"value5"}}}, "key6":{"key7":{"key8":"value8"}}}`
Result = `{"key1":{"key2":{"key9":"value9"}, "key3":{"key4":"value4", "key10":[1,2,3]}}, "key6":{"key7":{"key8":"value8"}, "key11":"value11"}}`

*Merge {} element will replace*
A = `{"key1":{"key2":{}}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key2":{}, "key3":"value3"}}`

*Merge a null element does nothing*
A = `{"key1":{"key2":null}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key2":"value2", "key3":"value3"}}`

*Merge a blank list [] will replace root element*
A = `{"key1":[]}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":[]}`

*Merge a blank list [] will replace single element*
A = `{"key1":{"key2":[]}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key2":[], "key3":"value3"}}`

*Merge a blank list [] will remove nested objects*
A = `{"key1":{"key2":[{"key3":"value3"}]}}`
B = `{"key1":{"key2":{"key3":"value3"}}}`
Result = `{"key1":{"key2":[{"key3":"value3"}]}}`

*Merge an existing list with some other struct*
A = `{"key1":{"key2":{"key3":[{"key4":"value4"}]}}}`
B = `{"key1":{"key2":[]}}`
Result = `{"key1":{"key2":{"key3":[{"key4":"value4"}]}}}`
```

## Remove

`remove` action will overwrite a key:value with key:new\_value or delete anything in a list that matches the provided values' ids.

In the following examples A is being patched into B to create the Result:

```text
*Remove from list*
A = `{"a":[{"id": "1"}], "blah":1}`
B = `{"a":[{"id": "2"},{"id": "3"}, {"id":"1"}], "blah":"string"}`
Result = `{"a":[{"id": "2"},{"id":"3"}], "blah":1}`

*For non-id lists, remove will append*
A = `{"a":[{"blah": "1"}], "blah":1}`
B = `{"a":[{"blah": "2"}], "blah":"string"}`
Result = `{"a":[{"blah": "2"}, {"blah":"1"}], "blah":1}`

*Empty out a nested dictionary*
A = `{"key1":{"key2":true}}`
B = `{"key1":{"key2":"value2"}}`
Result = `{"key1":{}}`

*Remove the root element, should be empty*
A = `{"key1":true}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{}`

*Remove a sub element*
A = `{"key1":{"key2":true}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key3":"value3"}}`

*Remove a multiple sub elements*
A = `{"key1":{"key2":{"key3":true}, "key4":true}}`
B = `{"key1":{"key2":{"key3":{"key5":"value5"}}, "key4":{"key6":{"key7":"value7"}}}}`
Result = `{"key1":{"key2":{}}}`

*Remove one of the root elements if there are more than one*
A = `{"key1":true}`
B = `{"key1":{"key2":"value2", "key3":"value3"}, "key4":["a", "b", "c"]}`
Result = `{"key4":["a", "b", "c"]}`

*Remove with false should over write*
A = `{"key1":{"key2":false, "key3":true}, "key4":false}`
B = `{"key1":{"key2":"value2", "key3":"value3"}, "key4":[{"key5":"value5", "key6":"value6"}, {"key7": "value7"}]}`
Result = `{"key1":{"key2":false}, "key4":false}`

*Only objects with id's can be put into lists*
A = `{"key1":[{"key2":true}]}`
B = `{"key1":[{"key2":"value2"}, {"key3":"value3"}]}`
Result = `{}`

*Elements with {} should do nothing*
A = `{"key1":{}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key2":"value2", "key3":"value3"}}`

*Elements with nil should do nothing*
A = `{"key1":{"key2":null}}`
B = `{"key1":{"key2":"value2", "key3":"value3"}}`
Result = `{"key1":{"key2":"value2", "key3":"value3"}}`
```

## Overwrite

The `overwrite` action will overwrite the old object with the new object. If you want to change a field or sub-object with the `overwrite` action, it is suggested to first call `Get` to obtain the original object. Then you can change the field or sub-object you would like to overwrite, followed by assembling the `overwrite` request with the entire object.

In the following examples A is being patched into B to create the Result:

```text
A = `{"a":[{"id": "1"}], "blah":1}`
B = `{"a":[{"id": "2"}], "blah":"string", "foo": "bar}`
Result = `{"a":[{"id": "1"}], "blah":1}`

A = `{}`
B = `{"a":[{"blah": "2"}], "blah":"string"}`
Result = `{}`
```

_Patch inputs with overwrite action will overwrite data object_

```text
*Before Patch*
"input": {
    "id": "68be8de5a7de42c4873bf63fb6b8683d",
    "data": {
        "image": {
            "url": "https://samples.clarifai.com/your-image.jpg",
        },
        "concepts": [
            {
                "id": "car",
                "name": "car",
                "value": 1,
                "app_id": "your-application-id"
            }
        ],
        "geo": {
            "geo_point": {
                "longitude": 40.7129,
                "latitude": 74.0058
            }
        }
    },
}

*Patch Request*
{
    "inputs": [
        {
            "id": "68be8de5a7de42c4873bf63fb6b8683d",
            "data": {
                "concepts": [
                    {
                        "id": "ferrari",
                        "value": 1.0
                    }
                ],
                "metadata": {
                    "foo": "bar"
                }
            }
        }
    ],
    "action": "overwrite"
}

*Result*
"input": {
    "id": "68be8de5a7de42c4873bf63fb6b8683d",
    "data": {
        "image": {
            "url": "https://samples.clarifai.com/your-image.jpg",
        },
        "concepts": [
            {
                "id": "ferrari",
                "name": "ferrari",
                "value": ,
                "app_id": "your-application-id"
            }
        ],
        "metadata": {
            "foo": "bar"
        }
    },
}
```

_Patch models with overwrite action will overwrite output\_info and name_

```text
*Before Patch*
"model": {
    "id": "test-model-1580486147",
    "name": "test-model-1580486147",
    "app_id": "test-app-1580486122",
    "output_info": {
        "data": {
            "concepts": [
                {
                    "id": "car",
                    "name": "car",
                    "value": 1,
                    "language": "en",
                    "app_id": "test-app-1580486122"
                },
                {
                    "id": "ferrari",
                    "name": "ferrari",
                    "value": 1,
                    "language": "en",
                    "app_id": "test-app-1580486122"
                }
            ]
        },
        "output_config": {
            "concepts_mutually_exclusive": false,
            "closed_environment": false,
            "max_concepts": 0,
            "min_value": 0,
            "test_split_percent": 10,
            "embed_model_version_id": "bb186755eda04f9cbb6fe32e816be104",
            "invalid_data_tolerance_percent": 5
        },
        "type": "concept",
        "type_ext": "concept"
    }
}

*Patch Request*
{
    "models": [
        {
            "id": "test-model-1580486147",
            "name": "my-new-model",
            "output_info": {
                "data": {
                    "concepts": [
                        {
                            "id": "animal"
                        },
                        {
                            "id": "dog"
                        },
                        {
                            "id": "cat"
                        }
                    ]
                },
                "output_config": {
                    "concepts_mutually_exclusive": true
                }
            }
        }
    ],
    "action": "overwrite"
}

*Result*
"model": {
    "id": "test-model-1580486147",
    "name": "my-new-model",
    "app_id": "test-app-1580486122",
    "output_info": {
        "data": {
            "concepts": [
                {
                    "id": "animal",
                    "name": "animal",
                    "value": 1,
                    "language": "en",
                    "app_id": "test-app-1580486122"
                },
                {
                    "id": "cat",
                    "name": "cat",
                    "value": 1,
                    "language": "en",
                    "app_id": "test-app-1580486122"
                },
                {
                    "id": "dog",
                    "name": "dog",
                    "value": 1,
                    "language": "en",
                    "app_id": "test-app-1580486122"
                }
            ]
        },
        "output_config": {
            "concepts_mutually_exclusive": true,
            "closed_environment": false,
            "max_concepts": 0,
            "min_value": 0,
            "test_split_percent": 10,
            "embed_model_version_id": "bb186755eda04f9cbb6fe32e816be104",
            "invalid_data_tolerance_percent": 5
        },
        "type": "concept",
        "type_ext": "concept"
    }
}
```

