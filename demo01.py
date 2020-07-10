import csv
import pprint

# with open('data/demo01.csv') as f:
#     print(f.read())


# with open('data/demo01.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
        
        
# with open('data/demo01.csv') as f:
#     reader = csv.reader(f)
#     l = [row for row in reader]

# print(l)


# with open('data/demo01.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#         print([int(v) for v in row])


# with open('data/demo01.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     l = [row for row in reader]
#     print(l)


with open('data/demo01_1.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    print("1")
    print(l)
    print("2")
    print([row[1:] for row in l[1:]])
    print("3")
    print([row[2:3] for row in l[2:3]])
    print("4")
    print([row[2] for row in l[2:]])
    






