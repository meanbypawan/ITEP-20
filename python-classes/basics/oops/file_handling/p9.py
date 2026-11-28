from Employee import Employee
import pickle
def write_employee():
    try:
        with open("employee.pkl","a+b") as f:
           e = Employee(100,"ABC",9009111222,21,"InfoBeans")
           pickle.dump(e,f)
           print("Operation success...")
    except OSError as e:
        print(e)

def read_employee():
   try:
      with open("employee.pkl","rb") as f:
         while True:
           e = pickle.load(f)
           print(e)

   except (EOFError) as e:
      print("EOF..")

   except OSError as e:
      print(e)

if __name__ == "__main__":
  #write_employee()
  read_employee()