'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkX7yrpL1GA-joyog9Z16N6V)'''
#Importações
import keras.applications.xception
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import GlobalAveragePooling2D, Dense

if __name__ == '__main__':
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)

    #Criando um gerador de imagens
    dir_treino = 'cats_and_dogs/train'
    dir_teste = 'cats_and_dogs/test'

    data_generator = ImageDataGenerator(rescale=1/255.0)

    gerador_treino = data_generator.flow_from_directory(dir_treino, batch_size=32, target_size=(224,224), class_mode='sparse')
    gerador_teste = data_generator.flow_from_directory(dir_teste, batch_size=32, target_size=(224,224), class_mode='sparse')

    print(gerador_treino[0])

    print(len(gerador_treino))

    print(len(gerador_treino[0][0]))

    print(gerador_treino[0][0])

    plt.imshow(gerador_treino[0][0][0])
    plt.show()

    print(len(gerador_treino[0][0]))

    #Obtendo um modelo de rede neural (Xception)
    model = keras.applications.xception.Xception(input_shape=(224,224,3), include_top=False)

    average_pooling = GlobalAveragePooling2D()(model.output)

    hidden = Dense(2048, activation='relu')(average_pooling)

    pred = Dense(1, activation='sigmoid')(hidden)

    model_final = keras.models.Model(inputs=model.input, outputs=pred)

    #Sumário do Modelo
    print(model_final.summary())

    #Compilando o modelo
    model_final.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    #Treinando o modelo
    model_final.fit(gerador_treino, epochs=10)

    #Avaliando o modelo
    print(model_final.evaluate(gerador_teste))

    #Testando na prática
    img_teste = gerador_teste[0][0][0]
    plt.imshow(img_teste)
    plt.show()

    model_final.predict(img_teste.reshape(1,224,224,3))