from sklearn import tree, svm, linear_model, neighbors

# [height, weight, shoe size]
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37],
     [166,65,40], [190,90,47], [175,64,39], [177,70,40],
     [159,55,37], [171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
     'male', 'female', 'male', 'female', 'male']

# classifiers
clf_tree = tree.DecisionTreeClassifier()
clf_svm = svm.SVC()
clf_learn_model = linear_model.Perceptron()
clf_neighbors = neighbors.KNeighborsClassifier()

# training
clf_tree.fit(X, Y)
clf_svm.fit(X, Y)
clf_learn_model.fit(X, Y)
clf_neighbors.fit(X, Y)

# prediction
prediction = [[190,70,43]]
pred_tree = clf_tree.predict(prediction)
pred_svm = clf_svm.predict(prediction)
pred_learn_model = clf_learn_model.predict(prediction)
pred_neighbors = clf_neighbors.predict(prediction)

# print
print('tree: {}'.format(pred_tree))
print('svm: {}'.format(pred_svm))
print('learn_model: {}'.format(pred_learn_model))
print('neighbors: {}'.format(pred_neighbors))
