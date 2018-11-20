import sys
import pickle

f = open("./true_encodings.csv","a+")

dict = pickle.load(f)

name = sys.argv[1]
if name in dict:
    del dict[name]
    with open("./true_encodings.csv","wb") as f:
        pickle.dump(dict,f)
        
else:
    print("No such name in the database")

f.close()
