import csv
try:
    # with open("toy.csv","r") as f:
    #     reader = csv.reader(f)
    #     data = list(reader)
    #     for row in data[1:]:
    #         for col in row:
    #             print(col,end=" ")
    #         print()    
    with open("toy.csv","r") as f:
        reader = csv.DictReader(f)
        print(list(reader))
except OSError as e:
    print(e)