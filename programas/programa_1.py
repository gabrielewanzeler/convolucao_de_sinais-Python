#inicialmente, importanto as bibliotecas necessárias.

import numpy as np
import matplotlib.pyplot as plt


# Solicitar ao usuário o caminho dos arquivos de texto
caminho_sinal1 = input("Digite o caminho do arquivo de texto para o sinal 1: ")     #aqui deve-se colocar o caminho do arquivo txt para o sinal 1
caminho_sinal2 = input("Digite o caminho do arquivo de texto para o sinal 2: ")     #aqui deve-se colocar o caminho do arquivo txt para o sinal 2

sinal1 = np.loadtxt(caminho_sinal1)
sinal2 = np.loadtxt(caminho_sinal2)


print("Tamanho do sinal 1:", len(sinal1))
print("Tamanho do sinal 2:", len(sinal2))

# função para realizar a convolução discreta
def convolucao_discreta(sinal1, sinal2):
    tamanho1 = len(sinal1)
    tamanho2 = len(sinal2)
    tamanho_resultado = tamanho1 + tamanho2 - 1
    resultado = np.zeros(tamanho_resultado)     #essa função serve para inicializar o array resultado com zeros.


    for n in range(tamanho_resultado):
        # o valor de n representa a posição atual no array 'resultado' que está calculando.

        for k in range(tamanho1):
            # o valor de k representa a posição atual no array sinal1 que estamos multiplicando com o array sinal2 durante a convolução.

            if n - k >= 0 and n - k < tamanho2:
                resultado[n] += sinal1[k] * sinal2[n - k]
                # realiza a multiplicação dos valores de sinal1[k] e sinal2[n - k]
                # e acumula o resultado na posição n do array resultado

    return resultado

# função para exibir os sinais e o resultado da convo lução graficamente
def exibir_grafico(sinal1, sinal2, resultado):

    # Cria uma nova figura com tamanho (largura, altura) de 10 por 6 polegadas.
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    # Plota um gráfico de hastes (stem plot) usando os valores de x de 0 a len(sinal1) e os valores de y do sinal1.
    plt.stem(range(len(sinal1)), sinal1)

    plt.title('Sinal 1')

    plt.subplot(3, 1, 2)
    # Plota um gráfico de hastes (stem plot) usando os valores de x de 0 a len(sinal2) e os valores de y do sinal2.
    plt.stem(range(len(sinal2)), sinal2)

    plt.title('Sinal 2')

    plt.subplot(3, 1, 3)
    # Plota um gráfico de hastes (stem plot) usando os valores de x de 0 a len(resultado) e os valores de y do resultado.
    plt.stem(range(len(resultado)), resultado)

    plt.title('Resultado da convolução')

    # Ajusta automaticamente os espaçamentos entre os subplots.
    plt.tight_layout()
    # Exibe o gráfico.
    plt.show()


def salvar_resultado_arquivo(resultado, nome_arquivo):
    np.savetxt(nome_arquivo, resultado)

resultado = convolucao_discreta(sinal1, sinal2)

exibir_grafico(sinal1, sinal2, resultado)

salvar_resultado_arquivo(resultado, 'resultado.txt')