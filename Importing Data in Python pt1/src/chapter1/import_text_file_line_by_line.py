#Importing text files line by line
# Read & print the first 3 lines
with open('../../Datasets/moby_dick.txt', mode='r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())