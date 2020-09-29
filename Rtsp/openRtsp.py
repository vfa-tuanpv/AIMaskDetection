import cv2
import numpy as np
import logging

log = logging.basicConfig(level=logging.DEBUG)

vcap = cv2.VideoCapture("rtsp://user:a1234567890@192.168.0.123:554/Streaming/Channels/201/?transportmode=unicast")

while(1):
    ret,frame = vcap.read()
##    frame = cv2.resize(frame,(900, 600))
    cv2.imshow('VIDEO', frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

vcap.release()
cv2.destroyAllWindows()

