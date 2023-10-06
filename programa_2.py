

from PIL import Image
import matplotlib.pyplot as plt

#solicita ao usuário que digite o caminho completo do arquivo de imagem para cada uma das imagens.
caminho_imagem1 = input("Digite o caminho da primeira imagem (formato JPG): ")
caminho_imagem2 = input("Digite o caminho da segunda imagem (formato JPG): ")

imagem1 = Image.open(caminho_imagem1)
imagem2 = Image.open(caminho_imagem2)

print("Dimensões da imagem 1:", imagem1.size)
print("Dimensões da imagem 2:", imagem2.size)

# Exibir as imagens lidas
# Cria uma figura com duas subplots lado a lado
fig, axes = plt.subplots(1, 2)


# Exibe a primeira imagem na primeira subplot
axes[0].imshow(imagem1)
axes[0].set_title('Imagem 1')  # Define o título da subplot como "Imagem 1"
axes[0].axis('off')  # Desativa os eixos na subplot para remover marcações e números dos eixos


# Exibe a segunda imagem na segunda subplot
axes[1].imshow(imagem2)
axes[1].set_title('Imagem 2')  # Define o título da subplot como "Imagem 2"
axes[1].axis('off')  # Desativa os eixos na subplot para remover marcações e números dos eixos

plt.show()

# Função para aplicar o filtro convolucional
def aplicar_filtro(imagem1, imagem2):

    largura1, altura1 = imagem1.size
    largura2, altura2 = imagem2.size

    # Criar a imagem resultante com as dimensões da imagem 1
    imagem_resultante = Image.new("RGB", (largura1, altura1))


    # Percorrer as coordenadas da imagem 1
    for x in range(largura1):
        for y in range(altura1):
            # Obter o pixel correspondente da imagem 1
            pixel1 = imagem1.getpixel((x, y))

            # Calcular as coordenadas correspondentes na imagem 2
            x2 = int(x * largura2 / largura1)
            y2 = int(y * altura2 / altura1)

            # Obter o pixel correspondente da imagem 2
            pixel2 = imagem2.getpixel((x2, y2))

            # Calcular o resultado da convolução
            r = pixel1[0] * pixel2[0] // 255
            g = pixel1[1] * pixel2[1] // 255
            b = pixel1[2] * pixel2[2] // 255

            # Atribuir o pixel resultante na imagem resultante
            imagem_resultante.putpixel((x, y), (r, g, b))

    return imagem_resultante
    #A função retorna a imagem_resultante, que contém o resultado da convolução das duas imagens.

# Aplicar o filtro convolucional
imagem_resultante = aplicar_filtro(imagem1, imagem2)

imagem_resultante.save("imagem3_resultado.jpg", "JPEG")
print("O filtro convolucional foi aplicado e a imagem resultante foi gerada.")

# Exibir a imagem
plt.imshow(imagem_resultante)
plt.title('Imagem Resultante')
plt.axis('off')