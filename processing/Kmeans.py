import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#data manipulation

vcsdata = pd.read_csv('filewithgrades.csv', sep=';')
vcs = pd.DataFrame(vcsdata).sample(n=33)
vcs['n'] = 1
grade = vcs['Grade']
labels = vcs['Labels']

respo = pd.read_csv('provabbr.csv', sep=';')
respo.fillna(0)
respo['n'] = 1
respo = pd.get_dummies(respo)

df = pd.merge(respo, vcs)

#program
# pivot = df.pivot_table(index=, columns = grade)
# pivot['cluster']= cluster.fit_pr
#
# cluster = KMeans(n_clusters=4)
# pivot["cluster"] = cluster.fit_predict(pivot[pivot.columns[2:]])

#output
print(df.tail())
