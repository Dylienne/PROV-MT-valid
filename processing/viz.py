#import datasets containing follow sets
# - vcs attributes
# - provenance ontology
# - timestamp extract
# - Survey data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request

#document load and spits

# csv = pd.read_csv('repository data.csv', sep=';')
# df = pd.DataFrame(csv)
#
# # splitfiles
# vcsfeatures = df[['VCS-Stars', 'VCS-Forks', 'VCS-Contributions', 'VCS-Commits']]
# userfeatures = df[['USR-F', 'USR-R', 'USR-P']]
#
# # sns.boxplot(vcsfeatures[:-1], vert=True)
# # boxplots dataframes
#
# # pd.DataFrame.boxplot(vcsfeatures)
# # pd.DataFrame.boxplot(userfeatures)
# # plt.ylim(-100, 1800)
# # plt.show()
#
# # #scatterplot
# # color = ("red", "green")
# # group = ("stars", "followers")
# # plt.scatter(vcsfeatures['VCS-Stars'], userfeatures['USR-F'], c = color)
# # plt.title('Scatter VCS stars and User followers')
# # plt.xlabel('Stars on repository')
# # plt.ylabel('github followers')
# # plt.legend(loc=2)
# # plt.ylim(-500, 5000)
# # plt.xlim(-500, 4000)
# plt.show()
#
# # # seaborn
# stars = sns.load_dataset("vcsfeatures")
# sns.boxplot(stars)
# plt.xlim(-100, 8000, 500)
# plt.show()
#
#
# #heatmap
#
#
# # f, ax = plt.subplot(figsize=(12,9))
# corr= stars.corr()
#
# ax = sns.heatmap(corr, square=True)
# plt.show()
#

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(context="paper", font="monospace")

# Load the datset of correlations between cortical brain networks
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)
corrmat = df.corr()

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(12, 9))

# Draw the heatmap using seaborn
sns.heatmap(corrmat, vmax=.8, square=True)

# Use matplotlib directly to emphasize known networks
networks = corrmat.columns.get_level_values("network")
for i, network in enumerate(networks):
    if i and network != networks[i - 1]:
        ax.axhline(len(networks) - i, c="w")
        ax.axvline(i, c="w")
f.tight_layout()
