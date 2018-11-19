import os
import sys
import face_recognition
#os.chdir("/home/sid/Desktop/SE_Facial_Recognition/known_images")

f = open("./true_encodings.txt","a+")

unknown_image = face_recognition.load_image_file(sys.argv[1])
try:
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    f.write(str(unknown_encoding)+"\n")

except:
    print("No face detected, try other image")
#for img in glob.glob(".jpg"):
#    known_image = face_recognition.load_image_file(img)
#    known_encoding = face_recognition.face_encodings(known_image)[0]
#    f.write(known_encoding)

f.close()
