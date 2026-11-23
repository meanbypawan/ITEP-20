def m1():
    try:
        raise ZeroDivisionError()
        print("Inside Try..")
        #return 100
    except Exception as e:
        print("Exception caught...")    
        #return 200 
    finally:
        print("finally executed...")
        #return 300
    return 400

print(m1())