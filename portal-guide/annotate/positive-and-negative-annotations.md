# Positive and Negative Annotations

When annotating your data, you have the option of providing both positive and negative labels for your concepts. Here is how your model interprets the labels that you add.

\(i\) If any concept is tagged with a positive annotation, that is treated as a positive label for that concept.

![](../../.gitbook/assets/annotation_i%20%282%29%20%282%29%20%283%29%20%284%29%20%284%29%20%284%29%20%284%29%20%287%29%20%284%29.jpg)

\(ii\) When a concept is tagged with a positive annotation, this also implies a negative label on all other concepts not also tagged as positive.

![](../../.gitbook/assets/annotation_ii%20%282%29%20%282%29%20%283%29%20%284%29%20%284%29%20%284%29%20%284%29%20%286%29.jpg)

\(iii\) When input image 2 is tagged with a negative annotation, and input image 1 is tagged positive, then both of these actions have the same effect on input image 2: all classes not tagged positive are implicitly negative already from \(ii\).

![](../../.gitbook/assets/annotation_iii%20%282%29%20%282%29%20%283%29%20%284%29%20%284%29%20%284%29%20%284%29%20%287%29.jpg)

\(iv\) If there are no positive annotations for any concept, then if any concept is tagged with a negative annotation, this is treated as a negative example for all concepts related to that image.

![](../../.gitbook/assets/annotation_iv%20%282%29%20%282%29%20%283%29%20%283%29%20%281%29.jpg)

\(v\) If there are no positive or negative annotations, the example is ignored.

![](../../.gitbook/assets/annotation_v%20%282%29%20%282%29%20%282%29%20%281%29.jpg)

