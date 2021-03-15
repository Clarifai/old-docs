---
description: Choose the best channel for accessing Clarifai API endpoints
---

# gRPC vs HTTP Channels

The Clarifai API offers you an encrypted gRPC channel, as well as an HTTPS+JSON channel for making requests. Why the different options? Learn about the many convenient benefits of using the Clarifai API built on gRPC. 

## Why did we build our API on gRPC in the first place?

![grpc vs http clarifai](https://www.clarifai.com/hs-fs/hubfs/Screen%20Shot%202021-02-09%20at%2011.04.10%20AM.png?width=1252&name=Screen%20Shot%202021-02-09%20at%2011.04.10%20AM.png)

### Cutting edge performance

Clarifai gRPC is built to deliver lightweight microservices. This is one of the keys to Clarifai Amada’s ability to load and balance thousands of different instances of machine learning models, and deliver MLOps at scale. With low latency and high throughput communication, we can deliver high performance machine learning services anywhere you are.  
  
Clarifai also uses gRPC to reduce network constraints. Our API messages are serialized using Protobuf, a compact, binary \(though non human-readable\) message format that is always smaller than the equivalent JSON. gRPC Protobuf serializes very quickly on the server and client. 

gRPC is specifically designed for HTTP/2, a major revision of HTTP that provides significant performance benefits over HTTP. The HTTP/2 protocol is efficient both when sending and receiving messages. HTTP/2 also eliminates head-of-line blocking by allowing multiplexing of multiple HTTP/2 calls over a single TCP connection. 

### Clean code and resource management

There simply is no formal definition of how to build an HTTP API with JSON, and there is ongoing debate about the best format for URLs, HTTP verbs, and response codes. The gRPC specification is prescriptive about the format a gRPC service must follow, which means that behavior is consistent across platforms and implementations.

Resource management is also made easier by virtue of the fact that gRPC also allows clients to specify how long they are willing to wait for an RPC to complete. The deadline is sent to the server, and the server has the ability to “timeout” in-progress gRPC/HTTP/database requests.

### A gift for languages

 Clarifai is a global, multi-lingual organization. We offer multi-lingual support for our models, and our API is a “polyglot” as well. Clarifai takes advantage of the fact that gRPC tooling supports all popular development languages, and we offer clients in many of the most popular programming languages.

Code generation of the client creates a strongly-typed client, and eliminates duplication of messages on the client and server. Clarifai automatically creates RESTful JSON Web APIs from gRPC services. This allows us to support both gRPC and JSON web APIs, without duplicating effort of building separate services for both.

### Streaming capabilities

Two-way real-time communication is needed for many promising ML use cases. gRPC offers support for bi-directional streaming, allowing gRPC services to push messages in real-time without polling. All streaming combinations are natively supported when using our gRPC clients: unary \(no streaming\), server to client streaming, client to server streaming and bi-directional streaming. 

## When to use the HTTP Channel

We recommend using the encrypted gRPC channel for most of our customers in most use cases, but the HTTP+JSON channel does have its advantages:

### Familiarity

Working with a RESTful JSON Web API will be familiar to many developers. In these cases, you may want to evaluate the tradeoff between development time and the additional performance offered by the gRPC channel.

### Browser support

It's impossible to directly call a gRPC service from a browser today. gRPC uses HTTP/2 features which major browsers currently do not support.

### Human readability

HTTP API requests are sent as text and can be read and created by humans. gRPC messages are encoded with Protobuf by default. While serializing Protobuf is more efficient and the payloads are smaller, its binary format isn't human readable. Additional tooling is required to analyze Protobuf payloads and to compose requests by hand.[  
](https://www.clarifai.com/cs/c/?cta_guid=d83de292-8100-4201-a297-439e9e7d8ce1&signature=AAH58kF3hgr_iPeCmLO-RAMhmALPTHzu-w&pageId=41346788799&placement_guid=555ef883-4a3e-4f83-a2d1-7deb924c8cbc&click=077a7099-8a84-4ad0-b75c-c00dfdb8e3d3&hsutk=b22d359e95a9f4a0d8b3edf2b4d25675&canon=https%3A%2F%2Fwww.clarifai.com%2Fblog%2Fhttp-vs-grpc-choose-your-favorite-interface&utm_referrer=https%3A%2F%2Fwww.clarifai.com%2Fblog&portal_id=4505120&redirect_url=APefjpEd5m2LKG3nqH2n0l-ZHpB0knyCNkx1463lPfb7D75sLZCE2ett0yPW7NybdmY758IiAqHqMfKE29sdu-1xrizWpo954sadX6m-uqqRn114AMxYNj0fznCcuYaph2k5WcnSVzHkFsjSxeRG-Tmpk03GD93vNC-njgs7g6wRDc3tSt0k4i2mnpZRq00YUwtSUBKjeFg5elosnz_83LRlA_WgUyU6_j3QFnqp2SNmz8jqrNi3TX05wynvK7hxd6mkD-0eJhJh5gmu6gZJv2wJk90cot5cO_V6L9z4I8TZZNlxhK3sckQ&__hstc=65403889.b22d359e95a9f4a0d8b3edf2b4d25675.1611605883164.1614285157634.1614312302697.99&__hssc=65403889.3.1614312302697&__hsfp=3570637114&contentType=blog-post)

