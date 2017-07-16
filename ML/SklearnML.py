import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn import *
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
#datasets
document = pd.read_csv('/Users/dylienneevery/Documents/PROV-MT-valid/processing/filewithgrades.csv', sep=';')
df = pd.DataFrame(document)
#respondents
repo = pd.read_csv('/Users/dylienneevery/Documents/PROV-MT-valid/processing/Provenance Ontology Research-report.csv', sep=';')
repo.fillna(0)
# dummies = pd.getdummies(repo)[:32]

#targets
grade = document['Grade'] #the y variable
document.__delitem__('Grade') #delete the last column x
document.__delitem__('Labels') #delete label

#transform
for i in range(document.shape[0]): #go through the rows
    if document.iloc[i,7] == "yes":
        document.iloc[i,7] = 1
    else:
        document.iloc[i,7] = 0

document = document.fillna(0)

#feature engineering
# labels= document['Labels'] #new y variable
# ratio = document['VCS-Stars']/document['VCS-Forks']


#crossvalidation
kf = KFold(n_splits=3, shuffle= True)
kf.get_n_splits(document)
print(kf)

# program
clf1 = OneVsRestClassifier(LinearSVC()).fit(document, grade)
clf1.predict(document)

for train_index, test_index in kf.split(document):
    x_train = document.iloc[train_index,:]
    x_test = document.iloc[test_index,:]
    y_train = grade.iloc[train_index]
    y_test = grade.iloc[test_index]
    clf1 = OneVsRestClassifier(LinearSVC()).fit(x_train, y_train)
    predictions= clf1.predict(x_test)
    print(f1_score(y_test, predictions, average= 'weighted'))

#output
# print(predictions)
# print(type(predictions))
# print("____")
# print(clf1)
# print("______")
# print(x_train.tail())
# print("____")
# print(y_test.tail())
# print(document.tail())



