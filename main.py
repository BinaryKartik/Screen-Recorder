import datetime
import numpy as np
from PIL import ImageGrab
import cv2
from win32api import GetSystemMetrics
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
video = cv2.VideoWriter(f'Screen Recording {time}.mp4', fourcc, 20.0, (width, height))
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    video.write(frame)
    cv2.imshow('Screen Recorder', frame)
    if cv2.waitKey(4) == ord('q'):
        break
