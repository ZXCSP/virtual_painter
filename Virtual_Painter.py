from turtle import distance
import fingertrackingmodule as ftm
import cv2
import os
import numpy as np

HEADER_LIST = []
BRUSH_THICKNESS = 25
ERASE_THICNESS = 100
DRAW = False
DRAW_COLOR = (0,0,0)
FOLDER_HEADERS = "Header"

imgCanvas = np.zeros((1080, 1920), np.uint8)

myList = os.Listdir(FOLDER_HEADERS)
for imgPath in myList:
    image = cv2.imread(FOLDER_HEADERS+ '/'+imgPath) 
    HEADER_LIST.append(image)
header = HEADER_LIST(-1)



WIDTH = 1920
HEIGHT = 1080


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, HEIGHT)
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

detector = ftm
distance
if distance < 45:
    
DRAW_COLOR = 0,0,255
while cap.isOpened():  # пока камера "работает"
        success, image = cap.read()  # получение кадра с камеры
        if not success:  # если не удалось получить кадр
            print('Не удалось получить кадр с web-камеры')
            continue  # возвращаемся к ближайшему циклу
        image = cv2.flip(image, 1)  
        detector.findHands(image)
        detector.findFingersPosition(image)
        if detector.result.multi_hand_landmarks:
            handCount
        w, h, c = header.shape()
        image[0:h, 0:w] = header

        cv2.imshow("window", image)
        if cv2.waitKey(1) & 0xFF == 27:  # Ожидаем нажатие ESC 
            break



