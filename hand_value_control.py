# Загрузка библиотек
import os
try:
    import cv2
    import mediapipe as mp
except ImportError:
    os.system("pip install mediapipe opencv-python")



# В этой переменной хранится значение
value = 0



# Конфигурация программы
# Ось координат ("x"/"y")
os = "y"
# Выведения значения в консоль (True/False)
printing = True



cam = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils



while True:
    # Выход из программы по нажатию клавиши Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break
    good, image = cam.read()
    image = cv2.flip(image, -1)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
            for id, point in enumerate(handLms.landmark):
                width, height, color  = image.shape
                width, height = int(point.x * height), int(point.y * height)
                if id == 8 and os == "x":
                    value = int(round(point.x * 100))
                    if printing == True:
                        print(value)
                    
                elif id == 8 and os == "y":
                    value = int(round(point.y * 100))
                    if printing == True:
                        print(value)
                    
                    
                    
    image = cv2.flip(image, -1)
    image = cv2.flip(image, 1)
    cv2.imshow("Hand Value Control", image)