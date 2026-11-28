import pickle
try:
    with open("company.pkl","rb") as f:
        e = pickle.load(f) # Deserialization
        print(e)
except OSError as e:
    print(e)        