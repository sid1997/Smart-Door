import os
import sys
import face_recognition
import pickle

name = sys.argv[1]
#print(name)
#print(sys.argv[2])
unknown_image = face_recognition.load_image_file(sys.argv[2])
try:
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    if os.path.getsize("./true_encodings.csv") == 0:
        dict={}
        dict[name] = unknown_encoding
        with open("./true_encodings.csv","wb") as f:
            pickle.dump(dict,f)

    else:
        with open("./true_encodings.csv", "rb") as f:
            dict = pickle.load(f)

        dict[name] = unknown_encoding

        with open("./true_encodings.csv","wb") as f:
            pickle.dump(dict,f)

except:
    print("No face detected, try other image")
    #for img in glob.glob(".jpg"):
    #known_image = face_recognition.load_image_file(img)
    #known_encoding = face_recognition.face_encodings(known_image)[0]
    #f.write(known_encoding)
