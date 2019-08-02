# Getting Started

### Getting Started

The Clarifai API offers image and video recognition as a service. Whether you have one image or billions, you are only steps away from using artificial intelligence to recognize your visual content.

The API is built around a simple idea. You send inputs \(an image or video\) to the service and it returns predictions.

The type of prediction is based on what model you run the input through. For example, if you run your input through the 'food' model, the predictions it returns will contain concepts that the 'food' model knows about. If you run your input through the 'color' model, it will return predictions about the dominant colors in your image.

![inputs outputs](/images/inputs-outputs.png)

Before you get started, if you haven't created an account and received your free API key, [please do so](/signup) before proceeding with this guide. You can begin making API calls for free, a credit card is not required.

Please note that your account will be limited to 100 API calls until you verify your email address. After verification, you will receive the full amount of API calls under your plan.

All API access is over HTTPS, and accessed via the `https://api.clarifai.com` domain. The relative path prefix `/v2/` indicates that we are currently using version 2 of the API.

In the below examples, we use single brackets `{variable}` to indicate that this is a variable you should replace with a real value.

