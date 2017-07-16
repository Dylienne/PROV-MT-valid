import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#data manipulation
# vcsdata = pd.read_csv('filewithgrades.csv', sep=';')
# vcs = pd.DataFrame(vcsdata).sample(n=33)
# vcs['n'] = 1
# grade = vcs['Grade']
# labels = vcs['Labels']

respo = pd.read_csv('provabbr.csv', sep=';')
respo.fillna(0)
respo['n'] = 1
respo = pd.get_dummies(respo)
print(respo)
respo.to_csv('dummies.csv', sep=',', index=False)

#df = pd.merge(respo, vcs, on="n") # variables from both dataframes

#program
# pivot = df.pivot_table(index= ["country"], columns = ["Grade"], values= "n")
# pivot['cluster']= cluster.fit_pr
#
# cluster = KMeans(n_clusters=4)
# del df['Labels']
# df['Grade'] = pd.to_numeric(df['Grade'], errors='coerce')
# df["cluster"] = cluster.fit_predict(df[df.columns[2:]])

#output
# print(vcs.tail())
# print("------")
# print(respo.tail())
# print("_______")
# print(df)
