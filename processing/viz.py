#import datasets containing follow sets
# - vcs attributes
# - provenance ontology
# - timestamp extract
# - Survey data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#document load and spits

csv = pd.read_csv('repository data.csv', sep=';')
df = pd.DataFrame(csv)

# splitfiles
vcsfeatures = df[['VCS-Stars', 'VCS-Forks', 'VCS-Contributions', 'VCS-Commits']]
userfeatures = df[['USR-F', 'USR-R', 'USR-P']]

# sns.boxplot(vcsfeatures[:-1], vert=True)
#boxplots dataframes
# pd.DataFrame.boxplot(vcsfeatures, )
# pd.DataFrame.boxplot(userfeatures)
# plt.ylim(-100, 1800)
# plt.show()

#scatterplot
color = ("red", "green")
group = ("stars", "followers")
plt.scatter(vcsfeatures['VCS-Stars'], userfeatures['USR-F'], c = color)
plt.title('Scatter VCS stars and User followers')
plt.xlabel('Stars on repository')
plt.ylabel('github followers')
plt.legend(loc=2)
plt.ylim(-500, 5000)
plt.xlim(-500, 4000)
plt.show()


#seaborn
# sns.boxplot()
# plt.xlim(-100, 8000, 500)

#heatmap

# ax = sns.heatmap(vcsfeatures)
