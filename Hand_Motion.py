import cv2
import mediapipe as mp
import serial
import time

Index=0
Ring=0
Thumb=0
Middle=0
Pinky=0

# For Annotations on the hand
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
ser = serial.Serial(
        port="COM5",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

####################################################################################################################

## For webcam input:
cap = cv2.VideoCapture(0)
##For Video
prevTime = 0
with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,       #Detection Sensitivity
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    data=0
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)

####################################################################################################################
    #for counting fingers
    fingerCount = 0

    if results.multi_hand_landmarks:

      for hand_landmarks in results.multi_hand_landmarks:
        handIndex = results.multi_hand_landmarks.index(hand_landmarks)
        handLabel = results.multi_handedness[handIndex].classification[0].label

        handLandmarks = []

        for landmarks in hand_landmarks.landmark:
          handLandmarks.append([landmarks.x, landmarks.y])
        if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
          fingerCount = fingerCount + 1
        elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
          fingerCount = fingerCount + 1

        if handLandmarks[4][0] < handLandmarks[3][0]:# Thumb finger
          Thumb=1
        else:
          Thumb = 2


        if handLandmarks[8][1] < handLandmarks[6][1]:# Index finger
          fingerCount = fingerCount + 1
          Index=1
        else:
          Index=2



        if handLandmarks[12][1] < handLandmarks[10][1]:  # Middle finger
          fingerCount = fingerCount + 1
          Middle=1
        else:
          Middle=2


        if handLandmarks[16][1] < handLandmarks[14][1]:  # Ring finger
          fingerCount = fingerCount + 1
          Ring=1
        else:
          Ring=2


        if handLandmarks[20][1] < handLandmarks[18][1]: # Pinky
          fingerCount = fingerCount + 1
          Pinky=1
        else:
          Pinky=2

#######################################################################################################################

    # To Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime
    cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)
    cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break

##########################################################################################################
    # Encoding each case from a string to a Character

    m= f"P{Pinky}R{Ring}M{Middle}I{Index}T{Thumb}"

    if m=='P2R2M2I2T2':   #ooooo
      data='a'
    if m=='P2R2M2I2T1':   #oooo|
      data='b'
    if m=='P2R2M2I1T2':   #ooo|o
      data='c'
    if m=='P2R2M2I1T1':   #ooo||
      data='d'
    if m=='P2R2M1I2T2':   #oo|oo
      data='e'
    if m=='P2R2M1I2T1':   #oo|o|
      data='f'
    if m=='P2R2M1I1T2':   #oo||o
      data='g'
    if m == 'P2R2M1I1T1':  #oo|||
      data ='h'
    if m=='P2R1M2I2T2':   #o|ooo
      data='i'
    if m=='P2R1M2I2T1':   #o|oo|
      data='j'
    if m=='P2R1M2I1T2':   #o|o|o
      data='k'
    if m=='P2R1M2I1T1':   #o|o||
      data='l'
    if m=='P2R1M1I2T2':   #o||oo
      data='m'
    if m=='P2R1M1I2T1':   #o||o|
      data='n'
    if m=='P2R1M1I1T2':   #o|||o
      data='o'
    if m=='P2R1M1I1T1':   #o||||
      data='p'
    if m=='P1R2M2I2T2':   #|oooo
      data='q'
    if m=='P1R2M2I2T1':   #|ooo|
      data='r'
    if m == 'P1R2M2I1T2': #|oo|o
      data = 's'
    if m == 'P1R2M2I1T1': #|oo|| spiderman
      data = 't'
    if m=='P1R2M1I2T2':   #|o|oo
      data='u'
    if m=='P1R2M1I2T1':   #|o|o|
      data='v'
    if m == 'P1R2M1I1T2':  #|o||o
      data='w'
    if m=='P1R2M1I1T1':   #|o|||
      data='x'
    if m=='P1R1M2I2T2':   #||ooo
      data='y'
    if m=='P1R1M2I2T1':   #||oo|
      data='z'
    if m=='P1R1M2I1T2':   #||o|o
      data='&'
    if m=='P1R1M2I1T1':   #||o||
      data='$'
    if m=='P1R1M1I2T2':   #|||oo
      data='%'
    if m=='P1R1M1I2T1':   #|||o|
      data='*'
    if m=='P1R1M1I1T2':   #||||o
      data="#"
    if m=='P1R1M1I1T1':   #|||||
      data='!'
    # Sending data to Arduino
    lol = str(data)
    print(lol)
    ser.write(serial.to_bytes(lol.encode()))  # Encoding the data into Byte fromat and then sending it to the arduino
    time.sleep(0.002)  # Providing time to Arduino to Receive data.
    ser.flushInput()

cap.release()
ser.close()
print(handLandmarks)
