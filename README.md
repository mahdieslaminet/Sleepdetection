# sleep-detection
We want to detect whether the driver is asleep or awake

### Overview

The application uses the camera to capture video of a person. It processes each video frame using computer vision techniques from the cvzone library to detect the person's face and eyes. Based on the eye aspect ratio and blinking patterns over time, it classifies each frame as either "Awake" or "Asleep".

### Requirements

1. Python 3.x
2. OpenCV
cvzone
3. Webcam or video file showing a person's face

### Usage

- Capture video stream from webcam or load video file
- Detect face in each frame using cvzone face detector
- Detect eyes within face and calculate eye aspect ratio
- Track eye aspect ratio over time to detect blinking patterns
- Classify frame as "Awake" if eyes open and blinking, "Asleep" if eyes closed for extended time
- Visualize classification on each frame

### Accuracy

The accuracy of sleep detection depends on lighting conditions, camera image quality, face/eye detection performance, and choice of eye aspect ratio thresholds. Under good conditions, the application can achieve ~90% accuracy.

### References

- CVZone: https://www.computervision.zone/
- Facial landmarks: https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/
- Eye aspect ratio: https://www.pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/

## quick run 


- make and active virtualenv


- install requirements

    2. ``` python3 -m pip install matplotlib```
    3. ``` python3 -m pip install  mediapipe```
    4. ``` python3 -m pip install opencv-python```
    5. ``` python3 -m pip install cvzone```

- run projects 

    6. ```python3 ./sleep_detection.py ```

video link :
https://drive.google.com/drive/folders/1twiVu985mB-otxtbPlyLdVMJi9NiniyR?usp=sharing
