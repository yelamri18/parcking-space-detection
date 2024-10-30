import cvzone
from ultralytics import YOLO
import cv2
import math
import numpy as np
import pyautogui

# cap = cv2.VideoCapture(2)
cap = cv2.VideoCapture("videos\\p2.mp4")
model = YOLO("../yolov8/Yolo-Weights/best.pt")

classNames = ['occupied-parking-spots', 'parking spot']

# Définir des couleurs pour chaque classe (en BGR pour OpenCV)
colors = [(0, 0, 255), (0, 255, 0)]  # Rouge pour 'occupied-parking-spots', Vert pour 'parking spot'

# Récupérer la résolution de l'écran avec pyautogui
screen_width, screen_height = pyautogui.size()

# Créer une fenêtre redimensionnable
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)

# Redimensionner la fenêtre à la résolution de l'écran
cv2.resizeWindow("Webcam", screen_width, screen_height)

while True:
    success, img = cap.read()
    if not success:
        break

    # Redimensionner l'image pour l'adapter à la fenêtre si nécessaire
    img = cv2.resize(img, (screen_width, screen_height))

    # Initialiser les compteurs pour chaque classe à 0
    counts = [0, 0]  # [count_occupied_parking_spots, count_parking_spot]

    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            # Incrémenter le compteur pour la classe détectée
            counts[cls] += 1

            # Utiliser une couleur différente en fonction de la classe détectée
            color = colors[cls]

            # Dessiner le rectangle avec la couleur spécifique et une épaisseur plus grande pour une meilleure visibilité
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)

            # Afficher le nom de la classe et la confiance avec la même couleur
            label = f'{classNames[cls]} {conf}'
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Afficher le nombre d'objets détectés pour chaque classe sur l'image
    cv2.putText(img, f'Occupied Parking Spots: {counts[0]}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)  # Rouge pour 'occupied-parking-spots'
    cv2.putText(img, f'Parking Spots: {counts[1]}', (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)  # Vert pour 'parking spot'

    # Afficher la vidéo dans la fenêtre redimensionnée
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
