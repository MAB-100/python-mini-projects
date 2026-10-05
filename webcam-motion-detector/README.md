# Webcam Motion Detector

Watches the webcam with OpenCV and detects when an object enters the frame. It compares each frame to the first one: grayscale, Gaussian blur, frame difference, threshold, dilate, then contours. Moving objects get a bounding box and snapshots are saved to `images/`. When the object leaves the frame, `emailing.send_mail()` is called with a snapshot.

## Run

```bash
pip install -r requirements.txt
python main.py   # press q to quit
```

`emailing.py` only prints a message. Swap in a real email sender to get alerts.
