import face_recognition
import sys
import numpy as np
import re
import os
import pickle

try:
    unknown_image = face_recognition.load_image_file(sys.argv[1])
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    if os.path.getsize("./true_encodings.csv") == 0:
        print("No image in the database")

    else:
        result = False
        with open("./true_encodings.csv", "rb") as f:
            dict = pickle.load(f)
        for key, value in dict.iteritems():
            bool = face_recognition.compare_faces([value],unknown_encoding,tolerance=0.45)
            result = result or bool[0]
        print(result)

except:
    print("No face detected, try other image")
