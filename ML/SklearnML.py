import pandas as pd
from sklearn.model_selection import KFold
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score

document = pd.read_csv('/Users/dylienneevery/Dropbox (Personal)/SimpliLegal/Thesis dnki/csvsenseisergej.csv', sep=';')
#print(document)
grade = document['Grade'] #the y variable
document.__delitem__('Grade') #delete the last column x

#transform
for i in range(document.shape[0]): #go through the rows
    if document.iloc[i,6] == "yes":
        document.iloc[i,6] = 1
    else:
        document.iloc[i,6] = 0

document = document.fillna(0)

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
    print(f1_score(y_test, predictions, average= None))






