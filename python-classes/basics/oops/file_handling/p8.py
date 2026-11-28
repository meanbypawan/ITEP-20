import pickle
try:
  with open("company.pkl","rb") as f:
    while True:
        e = pickle.load(f)
        print(e)
except EOFError as e:
   print("EOF..")        
except OSError as e:
   print(e)   