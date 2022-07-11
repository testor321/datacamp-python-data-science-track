# Add total col as sum of individuals and family_members
import pandas as pd

homelessness = pd.read_csv("../../Datasets/homelessness.csv")

homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness)
