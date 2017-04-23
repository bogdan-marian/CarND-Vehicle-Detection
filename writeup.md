## Writeup

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector.
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./examples/car_not_car.png
[image2]: ./examples/HOG_example.jpg
[image3]: ./examples/sliding_windows.jpg
[image4]: ./examples/sliding_window.jpg
[image5]: ./examples/bboxes_and_heat.png
[image6]: ./examples/labels_map.png
[image7]: ./examples/output_bboxes.png

[image11]: ./output_images/car_hog_features.png
[image12]: ./output_images/notcar_hog_features.png
[image13]: ./output_images/vehicle_detection.png
[image14]: ./output_images/heat_map.png

[video1]: ./output_images/find_result.mp4

## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

The code for this project is located in the [Vehicle-Detection-and-Tracking.ipynb notebook](./Vehicle-Detection-and-Tracking.ipynb)

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Vehicle-Detection/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

You're reading it!

### Histogram of Oriented Gradients (HOG)

#### 1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The code for this step is perfomed by the method `get_hog_features`.  

I started by reading in all the `vehicle` and `non-vehicle` images.

I then explored different color spaces and different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.

I was basically settled on using `YCrCb` from the course exercise that encourage
using different color spaces for car identification

I `YCrCb` color space allso seamed to be the color space that I was also encourage to use by the
course instructors so in the end I god good results when training the classifiers
using `YCrCb`.




#### 2. Explain how you settled on your final choice of HOG parameters.

The channel use from the selected color space was a tuff choice but in the end still
the result of the score of the trained classifier made me decide to use all the channels.

These are the parameters use for selecting the HOG features:
- color space = YCrCb
- `orientations=9`
- `pixels_per_cell=(8, 8)`
- `cells_per_block=(2, 2)`

This is a representation for a vehicle and the hog
representation for each channel
![alt text][image11]

This is a representation of a non-vehicle and the hog representation for each channel
![alt text][image12]

Just by looking at the above representations it seams that I could Just
pick any channel and just use the classifier but the classifier allays score
with one ore two points higher then I was using all the channels.

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

I have used a linear support vector machine classifier in order to classify my data.

This is how I created the classifier:

`svc = LinearSVC()`

This is how I trained the classifier:

`svc.fit(X_train, y_train)`

### Sliding Window Search

#### 1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

On the sliding window search I ended up copying the same techniques from the course.
in the function `find_cars` i extract the hog features once and then
sub-subsample to get all of the overlaying windows.

#### 2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

I ended up searching for a car using these parameters with `find_cars`
- ystart = 400
- ystop = 656
- scale = 1.5

These provided a very good vehicle detection. Here it is one example.



![alt text][image13]
---

### Video Implementation

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](./output_images/find_result.mp4)


#### 2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.  

Here's an example result showing the heatmap from the data collected from one image
![alt text][image14]

##### Dealing with false pisitive

When analyzing one image I used value 1 for the threshold when with `apply_threashold` function

When analyzing images from the previous 10 frames I used a threshold of 2 when
filtering with `apply_threashold` function


---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

For the moment I do not like the fact that when there are 2 cars in close
proximity to each other the pipeline only draws a big box around them.

Also my pipeline does not handle very well cars very far away. I guess some more
experimentation will have to be performed to decide what scale will have
to be use and in what region for detecting distance cars.

Also a very obvious improvement for this project would be the code organization.
I would like everything to be organized in classes and to make it much easer
to understand for newbies in computer vision. This code organization will also
make it more simple on using multiple scalars when searching for a car.
