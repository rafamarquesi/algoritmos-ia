from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
import numpy as np
from sklearn import metrics

digits = datasets.load_digits()
print(digits.target.shape)

decision_tree = DecisionTreeClassifier()
knn = KNeighborsClassifier(n_neighbors=3)
naive_bayes = GaussianNB()

kf = model_selection.StratifiedKFold(n_splits=10)

predicted_classes = dict()
predicted_classes['tree'] = np.zeros(digits.target.shape[0])
predicted_classes['knn'] = np.zeros(digits.target.shape[0])
predicted_classes['naive'] = np.zeros(digits.target.shape[0])

for train, test in kf.split(digits.data, digits.target):
    data_train, target_train = digits.data[train], digits.target[train]
    data_test, target_test = digits.data[test], digits.target[test]

    decision_tree = decision_tree.fit(data_train, target_train)
    decision_tree_predicted = decision_tree.predict(data_test)
    predicted_classes['tree'][test] = decision_tree_predicted

    knn = knn.fit(data_train, target_train)
    knn_predicted = knn.predict(data_test)
    predicted_classes['knn'][test] = knn_predicted

    naive_bayes = naive_bayes.fit(data_train, target_train)
    naive_bayes_predicted = naive_bayes.predict(data_test)
    predicted_classes['naive'][test] = naive_bayes_predicted

# print(predicted_classes['tree'])

for classifier in predicted_classes.keys():
    print('====================================================')
    print('Resultados do classificador {}\n{}\n'.format(classifier, metrics.classification_report(digits.target,
                                                                                                  predicted_classes[
                                                                                                      classifier]
                                                                                                  )))
    print(
        'Matriz de confusão: \n{}\n\n\n'.format(metrics.confusion_matrix(digits.target, predicted_classes[classifier])))
