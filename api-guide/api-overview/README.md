# API overview

The Clarifai API \(Application Programming Interface\) is the interface that allows clients and servers to “talk” to each other. This is for “software to software” communication, and it is useful for programmatically implementing Clarifai's AI technology within your own products and tools. The API acts as a sort of “gatekeeper” to our software that translates clients like Python, Node and Java. These clients are used to make requests, which the API translates to commands that the software can understand.

Clarifai’s API allows users to access the Clarifai platform through four request types:

* **POST** - Upload inputs and information
* **PATCH** - Update or modify existing information
* **GET** - Request information
* **DELETE** - Delete existing information

Access our API over HTTPS via `https://api.clarifai.com`.

In the examples throughout our documentation, we use single brackets `{variable}` to indicate variables that you should replace with a real value.

We recommend using a [client library](api-clients.md) to access the API. We offer official clients in a variety of languages. To access the Clarifai API in other languages, use the REST API directly. For REST documentation please see the cURL examples.

