#  Object Tracking with OpenCV

This project demonstrates real-time object tracking of a car in a video using OpenCV's CSRT tracker in Python.  
The user manually selects the car in the first frame, and the program tracks it throughout the video.

---

##  Contents

| File               | Description                          |
|--------------------|------------------------------------|
| `car_tracking.py`  | Python script for object tracking  |
| `cars_video.mp4`   | Input video included in repo       |
| `output.mp4` | Sample vidoe of tracking      |

---

##  How to Run

1. Install required packages:

> pip install opencv-contrib-python

2. Run the script :

> python car_tracking.py

3. When prompted, select the car by drawing a bounding box and press SPACE or ENTER to start tracking.
4. Press 'q' to quit anytime.

---

## Videos

Input video: [Watch here on Google Drive](https://drive.google.com/file/d/1bfqS2yQ_YiqHfUCnRf3yFrf2k_IYYG4g/view?usp=sharing)

Output video (tracked): output.mp4 (included in repo) 

---

## Notes
+ The input video is too large to include directly in the repository, so it is hosted externally.

+ You can use any video by replacing cars_video.mp4 with your own.
