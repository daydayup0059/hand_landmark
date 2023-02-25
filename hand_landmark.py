#https://mp.weixin.qq.com/s?__biz=MzU5NDM1MjU5Mg==&mid=2247485621&idx=1&sn=5b5c2121ee5e8fa79e9d53ef0d7c0dad&chksm=fe03c80ac974411c481507c44458ea394e4b2ecfe0e1f1df7a9d0103507442435a03c159ceb1&scene=178&cur_album_id=1506331092608450562#rd
import cv2
import mediapipe as mp
from os import listdir
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
while cap.isOpened():
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    continue

  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
  image.flags.writeable = False
  results = hands.process(image)

  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
          image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
  cv2.imshow('result', image)
  if cv2.waitKey(5) & 0xFF == 27:
    break
cv2.destroyAllWindows()
hands.close()
cap.release()