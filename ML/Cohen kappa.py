# confusion matrix


# #cohen kappa score
# y_true= grade
# y_predict = predictions
# c = confusion_matrix(y_true, clf1.predict(document))
# c/c.astype(np.float).sum(axis=1)
#
# def loss_function(test, predictions):
#     diff = np.abs(test-predictions).max()
#     return np.log(1+diff)
#
# loss = make_scorer(loss_function, greater_is_better = False)
# score = make_scorer(loss_function, greater_is_better = True)
#
# print(cohen_kappa_score(y_true, predictions))
#
# #variable importances
#
# np.argsort(varimp)[::-1]
# plt.hist(varimp)
# model =
# varimp = model.feature_importances_
# varimp = model.fit(repos, grade)
# varimp * 100
# features_names = repos.columns
# varimp = model.fit(repos, grade)
#
#
# indices
# array([ 2, 15,  3,  6, 10, 32,  1, 30, 19,  7, 33, 20,  9, 12, 22, 17, 26,
#         4,  5, 23,  0, 21, 16, 25, 24, 31, 13,  8, 11, 34, 28, 18, 35, 27,
#        14, 29])
#
#
# #summary
#
