import pickle

f = open("./true_encodings.csv","a+")

dict = pickle.load(f)
print(len(dict))
for key, value in dict.iteritems():
    print(key)

f.close()
