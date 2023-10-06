
import math
import numpy as np

# Carregar o sinal a partir do arquivo
arquivo_sinal = input("Digite o caminho do arquivo de texto para o sinal : ") #colocar aqui o endereço do arquivo txt.
# exemplo:  /content/sinal_teste2.txt

# Carregar o sinal a partir dos arquivos
sinal = np.loadtxt(arquivo_sinal)

print("Sinal carregado: ")
print(sinal)

n = int(input("Digite o valor de n para o número de coeficientes: "))


#a função coeficientes_fourier recebe como entrada o sinal discreto (sinal) e o número de coeficientes de Fourier a serem calculados (n).
#No final, retorna a lista coeficientes contendo os coeficientes de Fourier calculados.


def coeficientes_fourier(sinal, n):
    N = len(sinal)               
    coeficientes = []            

    for i in range(n):
        real = 0
        imaginario = 0

        for t in range(N):
            angle = 2 * math.pi * i * t / N
            real += sinal[t] * math.cos(angle)             # Calcula a parte real do coeficiente
            imaginario -= sinal[t] * math.sin(angle)       # Calcula a parte imaginária do coeficiente


        real /= N                           # Divide a parte real pelo tamanho do sinal
        imaginario /= N                     # Divide a parte imaginária pelo tamanho do sinal

        coeficientes.append((real, imaginario))           # Adiciona o coeficiente à lista de coeficientes

    return coeficientes

coeficientes = coeficientes_fourier(sinal, n)


# Itera sobre os coeficientes retornados pela função usando a função enumerate,
# que retorna um índice 'k' e os valores correspondentes 'real' e 'imaginario'.
for k, (real, imaginario) in enumerate(coeficientes):

    # Imprime o índice 'k' e os valores 'real' e 'imaginario' formatados com até 4 casas decimais.
    print(f"Coeficiente {k}: Real = {real:.4f}, Imaginário = {imaginario:.4f}")