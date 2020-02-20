## Android SDK

Clarifai’s Android SDK enables machine learning directly on your device, bypassing the traditional
requirement of internet connectivity and extensive computing power. It makes it easy to use
image and video recognition on device and in real-time.

<a href="https://www.clarifai.com/get-sdk" target="_blank">
  ![Android SDK](/images/Andorid-iOs-Clarifai-Available.png)
</a>

The Android SDK is currently available. You can get more information on
<a href="https://github.com/Clarifai/clarifai-android-sdk" target="_blank">
  installing the SDK here<span class="icon icon-link-out"></span>
</a>


### Getting Started On Android
In order to run the SDK, you will need a Clarifai account. Please [create one here](https://portal.clarifai.com/signup) before proceeding with this guide.

Clarifai Android SDK supports applications running on Android API 21 (Version 5.0 “Lollipop”), or later.

### Install the SDK with an *.aar
Much of the Android SDK is built with Kotlin. As such, add the following to the project-level `build.gradle`:

```gradle
buildscript {
    ext.kotlin_version = "1.3.21"
    ext.kotlin_coroutine_version = '1.1.1'
    ...
    dependencies {
        ...
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
```

Next, place the `*.aar` file into the modules's `libs` folder of your application, creating one if necessary. In the app-level `build.gradle` file, add the following dependencies:

```gradle
repositories {
    flatDir {
        dirs 'libs'
    }
}
...
dependencies {
    ...
    implementation (name:'SDK_FILE_NAME', ext:'aar')
    implementation 'android.arch.lifecycle:extensions:1.1.1'
    implementation 'com.android.volley:volley:1.1.0'
    implementation 'com.google.protobuf:protobuf-java:3.5.0'
    implementation 'com.google.protobuf:protobuf-java-util:3.4.0'
    implementation 'com.loopj.android:android-async-http:1.4.9'

    implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
    implementation "org.jetbrains.kotlin:kotlin-reflect:$kotlin_version"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:$kotlin_coroutine_version"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:$kotlin_coroutine_version"
    ...
}
```
replacing `SDK_FILE_NAME`, with the name of the library(without `aar` extension) added to the `/app/libs` folder in the previous step.


### Start the SDK

The Clarifai SDK is initialized by calling `Clarifai.start(applicationContext, apiKey);` within the `com.clarifai.clarifai_android_sdk.core.Clarifai` package. We recommend starting it when your app has finished launching, but that is not absolutely required. Furthermore, work is offloaded to background threads, so there should be little to no impact on the launching of your app.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
import com.clarifai.clarifai_android_sdk.core.Clarifai;

public class MainActivity extends AppCompatActivity {
  private final String apiKey = "ENTER YOUR API KEY";
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    Clarifai.start(getApplicationContext(), apiKey);
  }
}
```

```kotlin
import com.clarifai.clarifai_android_sdk.core.Clarifai;

class MainActivity : AppCompatActivity() {
  val apiKey = "ENTER YOUR API KEY"
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)
    Clarifai.start(this, apiKey)
  }
}
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp
// Only for the Android SDK

```
{% endcode-tabs-item %}


{% code-tabs-item title="objective-c" %}
```objective-c
// Only for the Android SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL
// Only for the Android SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}




### Add Device Inputs with SDK

The SDK is built around a simple idea. You give inputs (images) to the library and it returns predictions (concepts). You need to add inputs to make predictions on it.

All inputs are created from a DataAsset object in the Android SDK. A Data Asset is a container for the asset in question, plus metadata related to it. You can create a DataAsset initialized with an Image on Device or from a URL as shown in the example below.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
import com.clarifai.clarifai_android_sdk.dataassets.DataAsset;
import com.clarifai.clarifai_android_sdk.dataassets.Image;
import com.clarifai.clarifai_android_sdk.datamodels.Input;
...

// Initialize Image object from an image URL
Image imageFromUrl = new Image(“”);

// Initialize Image object with an image on device with bitmap
Image imageFromBitmap = new Image(bitmap);

// A Data Asset is a container for the asset in question, plus
// metadata related to it
DataAsset dataAsset = new DataAsset(imageFromBitmap);

// An input object contains the data asset, temporal information, and
// is a fundamental component to be used by models to train on or
// predict
Input input = new Input(dataAsset);
```

```kotlin
import com.clarifai.clarifai_android_sdk.dataassets.DataAsset
import com.clarifai.clarifai_android_sdk.dataassets.Image
import com.clarifai.clarifai_android_sdk.datamodels.Input

// Initialize Image object from an image URL
val imageFromUrl = Image(“”)

// Initialize Image object with an image on device with bitmap
val imageFromBitmap = Image(bitmap)

// A Data Asset is a container for the asset in question, plus
// metadata related to it
val dataAsset = DataAsset(imageFromBitmap)

// An input object contains the data asset, temporal information, and
// is a fundamental component to be used by models to train on or
// predict
val input = Input(dataAsset)
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp
// Only for the Android SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
// Only for the Android SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL
// Only for the Android SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}



### Load Models On Device

Clarifai has a variety of Pre-Built Models to predict against. However, only the `General Model` is readily available within the SDK. For access to other models please contact sales@clarifai.com. The sample code below shows how to load the `General Model` and make a prediction against it.



{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
import com.clarifai.clarifai_android_sdk.datamodels.Model;
...

//Get General Model
Model model = Clarifai.getInstance().getGeneralModel();
```

```kotlin
import com.clarifai.clarifai_android_sdk.datamodels.Model
...

//Get General Model
val model = Clarifai.getInstance().generalModel
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp
// Only for the Android SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
// Only for the Android SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL
// Only for the Android SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}




### Predict On Device
Just as with our API, you can use the predict functionality on device with any of our available Pre-Built Models. Predictions generate outputs. An output has a similar structure to an input. It contains a data asset and concepts. The concepts associated with an output contain the predictions and their respective score (degree of confidence).


Note that the prediction results from pre-built models on the SDK may differ from those on the API. Specifically, there may be a loss of accuracy up to 5% due to the conversion of the models that allow them to be compact enough to be used on lightweight devices. This loss is expected within the current industry standards.





{% code-tabs %}
{% code-tabs-item title="js" %}
```js
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="python" %}
```python
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="java" %}
```java
import com.clarifai.clarifai_android_sdk.datamodels.Input;
import com.clarifai.clarifai_android_sdk.datamodels.Model;
import com.clarifai.clarifai_android_sdk.utils.Error;
...

// See how to create an input from the examples above
Input input = new Input(dataAsset);

// Use the model you want to predict on. The model in the sample code
// below is our General Model.
final Model model = Clarifai.getInstance().getGeneralModel();
model.addInput(input);
model.predict(new Model.ModelCallbacks() {
  @Override
  public void PredictionComplete(boolean successful, Error error) {
    if (successful) {
      List<Output> outputs = model.getOutputs();
      for (Output output: outputs) {
        List<Concept> concepts = output.getDataAsset().getConcepts();
        // concepts now contains a list of each concept found by the prediction
      }
    } else {
      Log.e(TAG, error.getErrorMessage());
    }
  }
});
```

```kotlin
import com.clarifai.clarifai_android_sdk.datamodels.Input
import com.clarifai.clarifai_android_sdk.datamodels.Model
import com.clarifai.clarifai_android_sdk.utils.Error
...

// See how to create an input from the examples above
val input = Input(dataAsset)

// Use the model you want to predict on. The model in the sample code
// below is our General Model.
val model = Clarifai.getInstance().generalModel
model.addInput(input)
model.predict(object: Model.ModelCallbacks() {
  override fun PredictionComplete(successful: Boolean, error: Error?) {
    if (successful) {
      val outputs = model.outputs
      outputs.forEach {
        val concepts = it.dataAsset.concepts
        // concepts now contains a list of each concept found by the prediction
      }
    } else {
      Log.e(TAG, error?.errorMessage);
    }
  }
});
```

{% endcode-tabs-item %}

{% code-tabs-item title="csharp" %}
```csharp
// Only for the Android SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title="objective-c" %}
```objective-c
// Only for the Android SDK

```
{% endcode-tabs-item %}

{% code-tabs-item title="php" %}
```php
// Only for the Android SDK

```

{% endcode-tabs-item %}

{% code-tabs-item title="cURL" %}
```cURL
// Only for the Android SDK

```
{% endcode-tabs-item %}
{% endcode-tabs %}
