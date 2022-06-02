'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkX7yrpL1GA-joyog9Z16N6V)'''
#Bibliotecas
# import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras import Sequential
from keras.datasets import cifar10
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense

if __name__ == '__main__':
    # print(tf.__version__)

    #Carregando a base de imagens
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    # plt.imshow(X_train[0])
    # plt.show()

    print(np.unique(y_train))

    class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

    #Padronizando os valores das imagens [0-1] por questões de convergência
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    #Criando a rede neural
    #criando o modelo sequencial
    model = Sequential()

    #adicionando camadas de convolução e pooling
    model.add(Conv2D(filters=32, kernel_size=5, activation='relu', input_shape=[32,32,3]))
    model.add(MaxPool2D(pool_size=(2,2), strides=2, padding='valid'))
    model.add(Conv2D(filters=64, kernel_size=5, activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=2, padding='valid'))

    #Adicionando a camada de flattening
    model.add(Flatten())

    #Adicionando camadas densas
    model.add(Dense(units=1024, activation='relu'))

    #Camada de saída
    model.add(Dense(units=10, activation='softmax'))

    #Sumário do modelo
    print(model.summary())

    #Compilando o modelo
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    #Treinando o modelo
    model.fit(X_train, y_train, epochs=10)

    resposta = model.predict(X_test)

    #classes preditas
    print(np.argmax(resposta, axis=1))

    loss, accuracy = model.evaluate(X_test, y_test)

    print(loss)
    print(accuracy)

    #Testando na Prática
    image = X_test[0]
    plt.imshow(image)
    plt.show()

    print(X_test.shape)
    print(image.shape)

    imagem = image.reshape(1,32,32,3)

    print(np.argmax(model.predict(imagem), axis=1))

    print(class_names[int(np.argmax(model.predict(imagem), axis=1))])