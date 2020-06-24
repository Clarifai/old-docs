# Localized Search

With visual search, you can find images in your application based on their visual similarity with other images. Visual search leverages the same embedding structure that is used to power image classification and detection models, but does not require concepts and training. Visual search organizes your data based on the similarity of visual characteristics alone.

With localized search,



Doing visual search on our Platform is as simple as clicking a button. Consider the following application which is being used to classify various kinds of vehicles such as bike, bus, car, etc. If I wanted to search images that were similar to a bike, I would do the following



Press the magnifying glass button next to the concept of bike in the Explorer

This would bring up all the images that are in the application which are visually similar to the concept of a bike, as the custom model understands it.



With localized search, users can get a more granular search within their application inputs. Our localized search is an offering available for every application which uses either General Detection or Face Detection model as the Base Workflow. Our Detection models work by finding objects in images and videos and drawing bounding boxes around them. These objects can then be labeled to create rich applications to identify things at a granular level. With a localized search, users will be able to use the General Detection and Face Detection models to search for images within their application that have the same object.

Localized Search with General Detection Model

In applications based on the General Detection or Face Detection Base Workflow, the search is localized search by default. So, by repeating the steps of Visual Search, in Detection Models, we can not only get images with the objects in them, but also where in those images those objects are with the coordinated of the bounding boxes. Let’s go through the whole process
Create an application with the General Detection Model as the Base Workflow. This application will classify three things: a red couch, a silver refrigerator and a round wooden table.

Upload some images for each concept and then label them. The General Detection Model will detect the objects and ask you to confirm images with their correct label as shown below


Just like before, the magnifying glass can be used to search for images. This time, however, we will do a localized search instead of a visual similarity search.


If you open any of the images, you will not only get the images but also the bounding boxes with the labels of the objects detected.



Localized search using Face Detection Model

Localized search with Face Detection is even simpler than with the already easy-to-use General Detection Model. Once you upload images to an application you can use the magnifying glass next to the face of the person to find any images or timestamps of the videos that the person is in.

Consider this application which has the faces of various actors who played the character of The Doctor in the BBC sci-fi show Doctor Who.
By clicking on the magnifying glass next to an image, we can run a localized search on the inputs of the application. This will search across all the images and return them in an indexed form as shown below



If we click into one of the top returned images, we will see the face being searched labeled with a magnifying glass next to it.


If there is a video input in there as well, then it will return the indexed search results with timestamps of when and where the face is in the video.


If we were to click into the video, we will see where the face is detected in the video inputs as shown below
