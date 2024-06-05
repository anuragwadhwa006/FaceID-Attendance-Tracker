import cv2
import numpy as np
import xlwrite
import time

# Set the file paths for cascade classifier and trained model
cascade_path = r"D:\Anurag Wadhwa\Projects\FaceID Attendance Tracker\trainer\haarcascade_frontalface_default.xml"
trainer_path = r"D:\Anurag Wadhwa\Projects\FaceID Attendance Tracker\trainer\trainer.yml"

# Load the cascade classifier and trained model
face_cas = cv2.CascadeClassifier(cascade_path)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(trainer_path)

# Other initialization
start = time.time()
period = 8
flag = 0
filename = 'filename'
dict = {'item1': 1}
font = cv2.FONT_HERSHEY_SIMPLEX

# Start capturing video
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 7)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        id, conf = recognizer.predict(roi_gray)
        if conf < 50:
            if id == 1:
                id = 'anurag'
                if str(id) not in dict:
                    filename = xlwrite.output('attendance', 'class1', 1, id, 'yes')
                    dict[str(id)] = str(id)
            elif id == 2:
                id = 'krishna'
                if str(id) not in dict:
                    filename = xlwrite.output('attendance', 'class1', 2, id, 'yes')
                    dict[str(id)] = str(id)
            elif id == 3:
                id = 'Namrata Mam'
                if str(id) not in dict:
                    filename = xlwrite.output('attendance', 'class1', 3, id, 'yes')
                    dict[str(id)] = str(id)
        else:
            id = 'Unknown, cannot recognize'
            flag += 1
            break
        cv2.putText(img, str(id) + " " + str(conf), (x, y - 10), font, 0.55, (120, 255, 120), 1)

    cv2.imshow('frame', img)
    if flag == 99:
        print("Transaction Blocked")
        break
    if time.time() > start + period:
        break
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
