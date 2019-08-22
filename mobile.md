## Apple SDK

Clarifai’s Apple SDK enables machine learning directly on your device, bypassing the traditional
requirement of internet connectivity and extensive computing power. It makes it easy to use
image and video recognition on device and in real-time.

<a href="https://www.clarifai.com/get-sdk" target="_blank">
  ![Apple SDK](/images/Andorid-iOs-Clarifai-Available.png)
</a>

The Apple SDK is currently available. You can get more information on
<a href="https://github.com/Clarifai/clarifai-apple-sdk" target="_blank">
  installing the sdk here.<span class="icon icon-link-out"></span>
</a>

### Start the SDK

The Clarifai SDK is initialized by calling the `startWithApiKey` method. We recommend to start it when your app finishes launching, but that is not absolutely required. And don't worry about hogging the launching of your app. We offload the work to background threads; there should be little to no impact.




{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=python %}
```python
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=java %}
```java
// Only for the Apple SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title=csharp %}
```csharp
// Only for the Apple SDK

```
{% endcode-tabs-item %}


{% code-tabs-item title=objective-c %}
```objective-c
@import Clarifai_Apple_SDK;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [[Clarifai sharedInstance] startWithApiKey:@"<Your API Key>"];

    return YES;
}

```
{% endcode-tabs-item %}


{% code-tabs-item title=php %}
```php
// Only for the Apple SDK

```


{% endcode-tabs-item %}

{% code-tabs-item title=cURL %}
```cURL
// Only for the Apple SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Inputs On Device

The SDK is built around a simple idea. You give inputs (images) to the library and it returns predictions (concepts). You need to create inputs to make predictions on them.

The sections below will showcase how to create Inputs from images on your device.

### Add Device Inputs

All inputs are created from a DataAsset object in the Apple SDK. A Data Asset is a container for the asset in question, plus metadata related to it. You can create a DataAsset initialized with an Image on Device or from a URL as shown in the example below.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=python %}
```python
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=java %}
```java
// Only for the Apple SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title=csharp %}
```csharp
// Only for the Apple SDK

```
{% endcode-tabs-item %}


{% code-tabs-item title=objective-c %}
```objective-c
// Initialize CAIImage object from an image URL
NSURL *imageURL = [NSURL urlWithString:@"<your image url>"];
CAIImage *image = [[CAIImage alloc] initWithURL:imageURL];

// Initialize CAIImage object with an image on device
UIImage *deviceImage = [UIImage ...];
CAIImage *localImage = [[CAIImage alloc] initWithImage:deviceImage];

// A Data Asset is a container for the asset in question, plus metadata
// related to it
CAIDataAsset *dataAsset = [[CAIDataAsset alloc] initWithImage:image];

// An input object contains the data asset, temporal information, and
// is a fundamental component to be used by models to predict
CAIInput *input = [[CAIInput alloc] initWithDataAsset:dataAsset];

```
{% endcode-tabs-item %}

{% code-tabs-item title=php %}
```php
// Only for the Apple SDK

```


{% endcode-tabs-item %}

{% code-tabs-item title=cURL %}
```cURL
// Only for the Apple SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Saving and Loading Inputs

After creating Inputs, it is also possible to save them in the SDK for later use. For example, you may want to store Inputs for further predictions in the future. Below is code that demonstrates how to save an Input and reload it from the SDK.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=python %}
```python
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=java %}
```java
// Only for the Apple SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title=csharp %}
```csharp
// Only for the Apple SDK

```
{% endcode-tabs-item %}


{% code-tabs-item title=objective-c %}
```objective-c
// Saving an input
[[Clarifai sharedInstance] saveEntities:@[input]];


// Loading an input
[[Clarifai sharedInstance]
             loadEntityId:@"Enter a Input ID here"
               entityType:CAIEntityTypeInput
        completionHandler:^(CAIDataModel *_Nullable entity, NSError *_Nullable error) {
            // The CAIDataModel returned here in the completion block is cast to a CAIInput object.
            CAIInput *input = (CAIInput *)entity;
        }];

```
{% endcode-tabs-item %}

{% code-tabs-item title=php %}
```php
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=cURL %}
```cURL
// Only for the Apple SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Prediction On Device
Just as with our API, you can use the predict functionality on device with our Public Models.

Predictions generate outputs. An output has a similar structure to an input. It contains a data asset and concepts. The concepts associated with an output contain the predictions and their respective score (degree of confidence.)

Note that the prediction results from pre-built models on the SDK may differ from those on the API. Specifically, there may be a loss of accuracy up to 5% due to the conversion of the models that allow them to be compact enough to be used on lightweight devices. This loss is expected within the current industry standards.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=python %}
```python
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=java %}
```java
// Only for the Apple SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title=csharp %}
```csharp
// Only for the Apple SDK

```
{% endcode-tabs-item %}


{% code-tabs-item title=objective-c %}
```objective-c
// See how to create an input from the examples above
CAIInput *input = [[CAIInput alloc] initWithDataAsset:dataAsset];

// The model in the sample code below is our General Model.
CAIModel *generalModel = [Clarifai sharedInstance].generalModel;
[generalModel predict:@[input] completionHandler:^(NSArray<CAIOutput *> * _Nullable outputs, NSError * _Nullable error) {
    // Iterate through outputs to learn about what has been predicted
    for (CAIOutput *output in outputs) {
    }
}];

```
{% endcode-tabs-item %}

{% code-tabs-item title=php %}
```php
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=cURL %}
```cURL
// Only for the Apple SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### On Device Public Models

Our team has developed a variety of pre-trained public models which our users can make predictions against. As of now, we have enabled our most comprehensive model, the General Model, to be loaded on device. For access to other models please contact sales@clarifai.com. The sample code below shows how to load the General Model and make a prediction against it.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=python %}
```python
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=java %}
```java
// Only for the Apple SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title=csharp %}
```csharp
// Only for the Apple SDK

```
{% endcode-tabs-item %}


{% code-tabs-item title=objective-c %}
```objective-c
// Get the General Model
CAIModel *generalModel = [Clarifai sharedInstance].generalModel;

// As well, models can be loaded by their id directly.
// Note that other objects, like inputs, can be loaded with this method too by changing the CAIEntityType.
[[Clarifai sharedInstance]
             loadEntityId:@"Enter a Model ID here"
                versionId:nil
               entityType:CAIEntityTypeModel
        completionHandler:^(CAIDataModel *_Nullable entity, NSError *_Nullable error) {

            // The CAIDataModel returned here in the completion block is cast to a CAIModel object.
            CAIModel *model = (CAIModel *)entity;

            // We can then begin to make predictions with the loaded model immediately.
            [model predict:@[inputs]
                completionHandler:^(NSArray<CAIOutput *> *_Nullable outputs, NSError *_Nullable error) {
                    for (CAIOutput *output in outputs) {
                        for (CAIConcept *concept in output.dataAsset.concepts) {
                            // Here we have access to the predicted concepts.
                        }
                    }
                }];
        }];

```
{% endcode-tabs-item %}

{% code-tabs-item title=php %}
```php
// Only for the Apple SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title=cURL %}
```cURL
// Only for the Apple SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}
