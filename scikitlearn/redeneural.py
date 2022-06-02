from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

digits = datasets.load_digits()  # matriz 8x8
# print(digits.data[0].shape)

fig, axarr = plt.subplots(2, 10)
for i in range(0, 2):
    for j in range(0, 10):
        current = 20 - (i * 10 + j)
        axarr[i, j].imshow(digits.images[-current], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

# print(digits.target[-20]) # classe

# print(digits.data.shape)

mlp = MLPClassifier(hidden_layer_sizes=(5,), activation='logistic', max_iter=200, alpha=0.001, solver='sgd', tol=1e-9,
                    learning_rate_init=.1, verbose=True)

# print(digits.target.shape)

mlp = mlp.fit(digits.data[:-20], digits.target[:-20])

print(mlp.predict(digits.data[-20:])) # Classe predita
print(digits.target[-20:]) # Classe alvo