import pickle
p = {
    "id":101,
    "name":"XYZ",
    "contact":9009111333,
    "age":27,
    "company_name":"InfoBeans"
}

#--> dump() 
#--> load()

try:
    with open("company.pkl","a+b") as f:
        pickle.dump(p,f) # Serialization
        print("Operation Success...")
except OSError as e:
    print(e)


