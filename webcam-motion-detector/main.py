import glob
import os
import time

import cv2

from emailing import send_mail

IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)

video = cv2.VideoCapture(0)
time.sleep(1)  # give the camera some time to warm up

count = 0
first_frame = None
status_list = [0, 0]
image_with_object = None

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(dil_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        status = 1
        cv2.imwrite(os.path.join(IMAGES_DIR, f"{count}.png"), frame)
        count += 1
        all_images = glob.glob(os.path.join(IMAGES_DIR, "*.png"))
        image_with_object = all_images[len(all_images) // 2]

    status_list.append(status)
    status_list = status_list[-2:]

    # The object has just left the frame
    if status_list[0] == 1 and status_list[1] == 0:
        send_mail(image_with_object)

    cv2.imshow("Motion detector", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
