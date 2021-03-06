import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt


set = pd.read_csv('Processing/repository data.csv', sep=';')
df = pd.DataFrame(set)

survey = pd.read_csv('Processing/Provenance Ontology Research-report.csv', sep=';')
df_survey = pd.DataFrame(survey)
df1 = df_survey.ix[:,1:29]
df1.fillna(0, inplace=True)


#slicing
user  = df.iloc[:,5:7]
vcs = df.iloc[:,0:4]
ontology = df.iloc[:8:-1]

#User key figures: ratios
starsforks = np.divide(vcs.iloc[:,0],vcs.iloc[:,1])  #ratio stars and forks
starsforks.replace([np.inf, -np.inf], np.nan)
starsforks.mean()

# correlation

np.corrcoef(np.array(ontology['wasGeneratedBy', np.array(vcs['VCS-Commits'])]))


