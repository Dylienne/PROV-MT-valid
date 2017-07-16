import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/dylienneevery/Documents/PROV-MT-valid/processing/filewithgrades.csv', sep=';')
grade = df['Grade'].values


mean = np.mean(grade)
# sigma = np.std(grade)

# mu, sigma

#print(df.tail())
# print(mean)
# print(sigma)

print(grade)
print(type(grade))