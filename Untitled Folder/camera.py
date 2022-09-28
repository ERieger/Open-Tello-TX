from mmap import MADV_REMOVE
from djitellopy import tello
import cv2
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

while True:
    img = me.get_frame_read().frame
    print(img)
    img = cv2.resize(img, (360, 240))
    cv2.imshow("results", img)
    cv2.waitKey(1)