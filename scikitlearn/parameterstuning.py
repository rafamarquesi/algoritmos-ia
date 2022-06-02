from sklearn import datasets
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn import metrics

'''Ajuste de parâmetros para os algoritmos, quando há poucos dados no dataset'''

digits = datasets.load_digits()

print(digits.target.shape)

inner_kf = model_selection.StratifiedKFold(n_splits=10, shuffle=True, random_state=None) # vai ser usado para o treinamento dos algoritmos
outer_kf = model_selection.StratifiedKFold(n_splits=3, shuffle=True, random_state=None) # vai ser usado para ajuste dos parâmetros

print('------ Started KNN parameters tuning')
knn = KNeighborsClassifier()
param_dist = {'n_neighbors': list(np.arange(1, 15)), 'metric': ['euclidean'], 'weights': ['uniform', 'distance']} # Parâmetros teste
grid_search = GridSearchCV(knn, param_grid=param_dist, cv=outer_kf, scoring='accuracy', refit=False)
grid_search.fit(digits.data, digits.target)
knn_best_params = grid_search.best_params_
print('KNN: {}\n\n'.format(knn_best_params))

print('------ Started Decision Tree parameters tuning')
decision_tree = DecisionTreeClassifier()
param_dist = {'max_depth': [3, 4, 5, 6, 7, 8, 9, 10]} # Parâmetros teste
grid_search = GridSearchCV(decision_tree, param_grid=param_dist, cv=outer_kf, scoring='accuracy', refit=False)
grid_search.fit(digits.data, digits.target)
decision_tree_best_params = grid_search.best_params_
print('Decision Tree: {}\n\n'.format(decision_tree_best_params))

knn = KNeighborsClassifier(**knn_best_params)
decision_tree = DecisionTreeClassifier(**decision_tree_best_params)

predicted_classes = dict()
predicted_classes['tree'] = np.zeros(digits.target.shape[0])
predicted_classes['knn'] = np.zeros(digits.target.shape[0])

for train, test in inner_kf.split(digits.data, digits.target):
    data_train, target_train = digits.data[train], digits.target[train]
    data_test, target_test = digits.data[test], digits.target[test]

    decision_tree = decision_tree.fit(data_train, target_train)
    decision_tree_predicted = decision_tree.predict(data_test)
    predicted_classes['tree'][test] = decision_tree_predicted

    knn = knn.fit(data_train, target_train)
    knn_predicted = knn.predict(data_test)
    predicted_classes['knn'][test] = knn_predicted

for classifier in predicted_classes.keys():
    print('====================================================')
    print('Resultados do classificador {}\n{}\n'.format(classifier, metrics.classification_report(digits.target,
                                                                                                  predicted_classes[
                                                                                                      classifier]
                                                                                                  )))
    print(
        'Matriz de confusão: \n{}\n\n\n'.format(metrics.confusion_matrix(digits.target, predicted_classes[classifier])))