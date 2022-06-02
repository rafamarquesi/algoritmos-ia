import numpy as np
import cv2
import matplotlib.pyplot as plt

'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkVqc0zSWm2Atlb6GisgjvQT)'''

if __name__ == '__main__':
    arr1 = np.array([1, 2, 3, 4, 5])
    print('tipo array1: {}'.format(type(arr1)))
    print('tipo array1: {}'.format(arr1.dtype))

    arr2 = np.array([1.1, 2.2, 3.4, 4.6, 5.9])
    print('tipo array2: {}'.format(type(arr2)))
    print('tipo array2: {}'.format(arr2.dtype))

    arr3 = np.array([[1, 2, 3], [4, 5, 6]])
    print('array3: {}'.format(arr3))

    arr4 = np.array([1, 2, 3, 4, 5], dtype=np.uint8)
    print('array4: {}'.format(arr4.dtype))

    arr_zeros = np.zeros((5,5))
    print('Array zeros: {}'.format(arr_zeros))

    arr_range = np.arange(10)
    print('Array range: {}'.format(arr_range))

    arr_lin = np.linspace(0, 100, 15)
    print('Array linear espaçados: {}'.format(arr_lin))

    arr_rand_int = np.random.randint(100, size=10)
    print('Array randomizado inteiro: {}'.format(arr_rand_int))

    # Atributos
    print(arr1.dtype)

    arr5 = np.array(['Rafael', 35, 10.1])
    print(arr5.dtype)

    print('Número de dimensões: %s' % arr3.ndim)
    print('Quantidade de elementos dentro do array: %s' % arr3.size)
    print('Quantos elementos em cada dimensão: {}'.format(arr3.shape))
    print(arr3.shape[0] * arr3.shape[1])
    print(len(arr3.shape))

    arr6 = np.arange(16)
    print(arr6)
    print(arr6.shape)
    print('transforma o array em matriz ou vice e versa: ')
    print(arr6.reshape(4,4))

    arr7 = arr6.reshape(4,4)
    print(arr7)

    print(arr7.shape)
    print(arr7.reshape(8,2))
    print(arr7.reshape(8, 2, order='F'))

    print(arr1)
    print(arr1.reshape(1,-1))
    arr8 = arr1.reshape(1,-1)
    print(arr8)
    print(arr8.shape[1])

    # Acessando elementos do Array

    arr9 = np.arange(20).reshape(4,5)
    print(arr9[0,3])
    print(arr9[0][4])
    print(arr9[0:2])
    print(arr9[0:4:2])
    print(arr9[0:2,0:3])
    print(arr9[0:2,0])
    print(arr9[:,-1])
    print(arr9[:,:-1])
    print(arr9[[0,3]])
    print(arr9[[0, 3],-1])
    print(arr9[[True,False,True,False]])

    arr10 = np.random.randint(100, size=20)
    print(arr10)
    print(arr10 > 50)
    print(arr10[arr10 > 50])

    for linha in arr9:
        print(linha)

    for linha in arr9:
        for elemento in linha:
            print(elemento, end=',')
        print()

    # Operações
    arr11 = np.random.randint(100, size=20)
    print(arr11)
    print(arr11+1)

    arr12 = np.random.randint(100, size=1000000, dtype=np.uint8)
    print(arr12)
    print(arr12.shape)

    # %time
    for i in range(100):
        arr12 = arr12 + 1

    print(arr12.dtype)

    print(arr11)
    print(arr11 * 2)
    print(arr11 / 2)
    print(arr11 / arr11.sum())
    print(arr11 / arr11.max())

    arr13 = np.arange(5) + 1
    print(arr13)

    arr14 = np.arange(5) + 6
    print(arr14)

    print(arr13 + arr14)
    print(arr13 - arr14)
    print(arr13 * arr14)

    arr15 = np.array([[1,2,3],[4,5,6]])
    print(arr15)
    print(arr15 + 1)

    arr16 = np.arange(6) + 1
    print(arr16)
    arr16 = arr16.reshape(2,3)
    print(arr16)

    arr17 = np.zeros((3,2), dtype=np.uint8) + 2
    print(arr17)

    print(arr16 @ arr17)
    print(arr16.dot(arr17))

    arr18 = np.array([[2,1],[1,2]])
    print(arr18)

    arr19 = np.linalg.inv(arr18)
    print(arr19)

    print(arr18 @ arr19)

    print(arr14)
    print(arr14 > 8)
    arr13[0] = 20
    print(arr13)
    print(arr14 > arr13)

    print(arr16)
    print(arr16.T)

    print(arr16.sum())
    print(arr16.mean())
    print(arr16.max())
    print(arr16.min())
    print(arr16.sum(axis=1))

    # Utilitários
    arr17 = np.arange(36).reshape(6,6)
    print(arr17)

    arr18 = np.arange(6) + 36
    print(arr18)
    arr18 = arr18.reshape(1,-1)
    print(arr18)

    print(np.concatenate((arr17,arr18)))
    print(np.concatenate((arr17, arr18.T), axis=1))

    np.savetxt('teste_txt.txt', arr17, fmt='%d', header='a,b,c,d,e')
    arr_load = np.loadtxt('teste_txt.txt', dtype=np.uint8)
    print(arr_load)

    np.savez_compressed('teste_z_com', array1=arr17, array2=arr18)
    arr_load_zip = np.load('teste_z_com.npz')
    print(arr_load_zip.files)
    print(arr_load_zip['array1'])
    print(arr_load_zip['array2'])

    imagem = cv2.imread('unnamed.jpg')
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    print(imagem)

    plt.imshow(imagem)
    plt.show()

    imagem2 = imagem[100:400, 250:600]
    plt.imshow(imagem2)
    plt.show()

