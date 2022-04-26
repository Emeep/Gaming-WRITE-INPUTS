import cv2
import pytesseract
from pytesseract import Output
import numpy
import os
import win32api, win32con
from pynput.keyboard import Key, Controller

keyboard = Controller()

pytesseract.pytesseract.tesseract_cmd = 'D:\\Python_Tesseract\\tesseract.exe'
cap = cv2.VideoCapture(0)
ret, frame = cap.read()


def Inputs(data: str):
    keys = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for a in data:
        if a == 'W':
            kp = 'w'
            keyboard.press(kp)

            for k in keys:
                if k != kp:
                    keyboard.release(k)
        elif a == 'A':
            kp = 'a'
            keyboard.press(kp)

            for k in keys:
                if k != kp:
                    keyboard.release(k)
        elif a == 'S':
            kp = 's'
            keyboard.press(kp)

            for k in keys:
                if k != kp:
                    keyboard.release(k)
        elif a == 'D':
            kp = 'd'
            keyboard.press(kp)

            for k in keys:
                if k != kp:
                    keyboard.release(k)
        elif a == 'R':
            for k in keys:
                keyboard.release(k)

while True:
    success, imgo = cap.read()

    imgo = cv2.flip(imgo, -1)
    imgo = cv2.resize(imgo, (540, 540), interpolation = cv2.INTER_AREA)

    imgo = imgo[-200:450, 200:300]

    img = cv2.cvtColor(imgo, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    img = cv2.GaussianBlur(img, (5,5), 0)
    img = 255 - img

    custom_config = '--psm 10 --oem 3 -c tessedit_char_whitelist=WASDR'
    boxes = pytesseract.image_to_boxes(img, config=custom_config)
    res = pytesseract.image_to_string(img, config=custom_config)
    # print(res)
    print(boxes)

    # Inputs(data=str(res))

    h, w = img.shape
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(imgo, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)


    cv2.imshow('image', imgo)
    cv2.waitKey(1)
    
    a = win32api.GetKeyState(0x26)  # up arrow key
    if a < 0:
        cap.release()
        cv2.destroyAllWindows()
        exit()