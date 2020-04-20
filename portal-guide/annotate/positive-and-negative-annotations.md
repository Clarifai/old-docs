# Positive and negative annotations

When annotating your data, you have the option of providing both positive and negative labels for your concepts. Here is how your model interprets the labels that you add.

\(i\) If any concept is tagged with a positive annotation, that is treated as a positive label for that concept.

![](../../images/annotation_i.jpg)

\(ii\) When a concept is tagged with a positive annotation, this also implies a negative label on all other concepts not also tagged as positive.

![](../../images/annotation_ii.jpg)

\(iii\) When input image 2 is tagged with a negative annotation, and input image 1 is tagged positive, then both of these actions have the same effect on input image 2: all classes not tagged positive are implicitly negative already from \(ii\).

![](../../images/annotation_iii.jpg)

\(iv\) If there are no positive annotations for any concept, then if any concept is tagged with a negative annotation, this is treated as a negative example for all concepts related to that image.

![](../../images/annotation_iv.jpg)

\(v\) If there are no positive or negative annotations, the example is ignored.

![](../../images/annotation_v.jpg)
