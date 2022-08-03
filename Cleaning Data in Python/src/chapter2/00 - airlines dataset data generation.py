import pandas as pd
import numpy as np
import names
from essential_generators import DocumentGenerator

full_pass_name = list()
survey_response_pass = list()

airlines = pd.read_csv("../../Datasets/airlines_final.csv", index_col=[0])

print(airlines.info())
print(airlines.head())


for i in range(0, airlines.shape[0]):
    sex = np.random.choice(['male', 'female'])
    if sex == 'male':
        prefix = np.random.choice(['Dr. ', 'Mr. ',  '', ''])
        full_pass_name.append(prefix + names.get_full_name(gender='male'))
    else:
        prefix = np.random.choice(['Dr. ', 'Ms. ', 'Miss ', '', ''])
        full_pass_name.append(prefix + names.get_full_name(gender='female'))

airlines.insert(loc=12, column='full_name', value=full_pass_name)

airlines_bad = airlines[(airlines['cleanliness'] == 'Dirty') |
                        (airlines['safety'] == 'Very unsafe') |
                        (airlines['satisfaction'] == 'Very unsatisfied')]

for i in range(0, airlines_bad.shape[0]):
    gen = DocumentGenerator()
    survey_response_pass.append(gen.sentence())

airlines_bad.insert(loc=13, column='survey_response', value=survey_response_pass)


print(airlines.info())
print(airlines.head())

airlines.to_csv("../../Datasets/airlines_final_v1.csv")
airlines_bad.to_csv("../../Datasets/airlines_bad_v1.csv")
