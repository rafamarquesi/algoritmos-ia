'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkX7yrpL1GA-joyog9Z16N6V)'''
#Importações
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    imagem = cv2.imread('homer.jpg')
    # print(imagem)
    print(imagem.shape)

    plt.imshow(imagem)
    plt.show()

    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    plt.imshow(imagem_rgb)
    plt.show()

    print(imagem_rgb)

    #Convertendo
    imagem_gray = cv2.cvtColor(imagem_rgb,cv2.COLOR_RGB2GRAY)
    print(imagem_gray)

    plt.imshow(imagem_gray, cmap='gray')
    plt.show()

    imagem2 = cv2.imread('homer.jpg', 0)
    plt.imshow(imagem2, cmap='gray')
    plt.show()

    # Convertendo para Branca e Preta
    ret, imagem_binaria = cv2.threshold(imagem_gray, 127, 1, cv2.THRESH_BINARY)
    print(imagem_binaria)

    plt.imshow(imagem_binaria, cmap='gray')
    plt.show()

    # Filtros
    imagem_eq = cv2.equalizeHist(imagem_gray)
    plt.imshow(imagem_eq, cmap='gray')
    plt.show()

    imagem_canny = cv2.Canny(imagem_gray, 100, 200)
    print(imagem_canny)
    plt.imshow(imagem_canny, cmap='gray')
    plt.show()

    #Redimensionando as imagens
    imagem_resized = cv2.resize(imagem_gray, (1000,1000), interpolation=cv2.INTER_AREA)
    plt.imshow(imagem_resized, cmap='gray')
    plt.show()

    #Salvando a imagem
    cv2.imwrite('homer_modificado.jpg', imagem_resized)