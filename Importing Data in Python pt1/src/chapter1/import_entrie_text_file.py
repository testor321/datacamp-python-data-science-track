# Importing entire text files
# Open a file: file
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
print(fileDir)

file = open('../../Datasets/moby_dick.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file

file.close()
# Check whether file is closed
print(file.closed)
