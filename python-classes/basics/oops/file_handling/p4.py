f = None
try:
    f = open("python_intro.txt","a")
    data = ("\nPython is robust\n","Python has strong memory management mechanism\n")
    f.writelines(data)
    print("Operation Success...")
except OSError as e:
    print(e)
finally:
    if f is not None:
        f.close()