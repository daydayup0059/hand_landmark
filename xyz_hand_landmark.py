



import cv2
import mediapipe as mp
from os import listdir
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
image = cv2.flip(cv2.imread(file_path), 1)
  # Convert the BGR image to RGB before processing.
results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
print('Handedness:', results.multi_handedness)


def Normalize_landmarks(image, hand_landmarks):
    new_landmarks = []
    for i in range(0, len(hand_landmarks.landmark)):
        float_x = hand_landmarks.landmark[i].x
        float_y = hand_landmarks.landmark[i].y
        # Z坐标靠近屏幕增大，远离屏幕减小
        float_z = hand_landmarks.landmark[i].z
        print(float_z)
        width = image.shape[1]
        height = image.shape[0]

        pt = mp_drawing._normalized_to_pixel_coordinates(float_x, float_y, width, height)
        new_landmarks.append(pt)
    return new_landmarks
hands.close()