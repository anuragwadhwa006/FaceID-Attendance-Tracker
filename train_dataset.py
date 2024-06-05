import os
import cv2
import numpy as np
from PIL import Image

def assure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(r"D:\Anurag Wadhwa\Projects\FaceID Attendance Tracker\haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(imageNp)
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids

faces, Ids = getImagesAndLabels(r'Dataset')
recognizer.train(faces, np.array(Ids))
print("Successfully trained")

# Ensure the directory exists
trainer_dir = r"D:\Anurag Wadhwa\Projects\FaceID Attendance Tracker\trainer"
assure_path_exists(trainer_dir)

# Write the trained model to the file
recognizer.write(os.path.join(trainer_dir, "trainer.yml"))

