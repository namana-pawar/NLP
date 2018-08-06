# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from seniority import projects
# Data Preprocessing

transactions = projects

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
#print(rules)
# Visualising the results
results = [rules]
i=1
for r in rules:
    print(r)
    i=i+1
    if i==3:
        break
for i in range(0:3):
    