import csv

try:
    with open("toy.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow(["Name","Price"])
        writer.writerow(['Remote car',1000])
        writer.writerow(['Teddy',2500])
        print("Operation success...")
except OSError as e:
    print(e)    