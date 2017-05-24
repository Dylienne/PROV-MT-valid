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

csv = pd.read_csv('/Users/dylienneevery/Dropbox (Personal)/SimpliLegal/Thesis dnki/VCS.csv', sep =';')
df = pd.DataFrame(csv)

# splitfiles
vcsfeatures = df[['VCS-Stars', 'VCS-Forks', 'VCS-Contributions', 'VCS-Commits']]
userfeatures = df[['USR-F', 'USR-R', 'USR-P']]
# time

#basic statistics
#feature engineering
stars = stars.drop(72)

#plotfiles
#boxplots dataframes
pd.DataFrame.boxplot(vcsfeatures)
pd.DataFrame.boxplot(userfeatures)
plt.ylim(-100, 5000)

#seaborn
sns.boxplot(stars)
plt.xlim(-100, 8000, 500)


