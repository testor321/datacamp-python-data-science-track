# Loading a pickled file
# Import pickle package
import pickle

# Open pickle file and load data: d
with open('../../Datasets/data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))