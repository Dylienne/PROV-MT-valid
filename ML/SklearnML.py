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

#datasets
document = pd.read_csv('/Users/dylienneevery/Documents/PROV-MT-valid/processing/filewithgrades.csv', sep=';')
df = pd.DataFrame(document)
respondents = pd.read_csv()

#respondents
repo = pd.read_csv('/Users/dylienneevery/Documents/PROV-MT-valid/processing/Provenance Ontology Research-report.csv', sep=';')
repo.fillna(0)
dummies = pd.getdummies(repo)[:32]

#targets
grade = document['Grade'] #the y variable
document.__delitem__('Grade') #delete the last column x
document.__delitem__('Labels') #delete label

#normalize dataset
df_norm = (df - df.mean()) / (df.max()- df.min())

#transform
for i in range(document.shape[0]): #go through the rows
    if document.iloc[i,7] == "yes":
        document.iloc[i,7] = 1
    else:
        document.iloc[i,7] = 0

document = document.fillna(0)

#feature engineering
labels= document['Labels'] #new y variable
ratio = document['VCS-Stars']/document['VCS-Forks']


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
    print(f1_score(y_test, predictions, average= 'marco'))

# confusion matrix


#cohen kappa score
y_true= grade
y_predict = predictions
c = confusion_matrix(y_true, clf1.predict(document))
c/c.astype(np.float).sum(axis=1)

def loss_function(test, predictions):
    diff = np.abs(test-predictions).max()
    return np.log(1+diff)

loss = make_scorer(loss_function, greater_is_better = False)
score = make_scorer(loss_function, greater_is_better = True)

print(cohen_kappa_score(y_true, predictions))

#variable importances

np.argsort(varimp)[::-1]
plt.hist(varimp)
model =
varimp = model.feature_importances_
varimp = model.fit(repos, grade)
varimp * 100
features_names = repos.columns
varimp = model.fit(repos, grade)


indices
array([ 2, 15,  3,  6, 10, 32,  1, 30, 19,  7, 33, 20,  9, 12, 22, 17, 26,
        4,  5, 23,  0, 21, 16, 25, 24, 31, 13,  8, 11, 34, 28, 18, 35, 27,
       14, 29])


#summary






