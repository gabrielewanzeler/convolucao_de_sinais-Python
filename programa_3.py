
#importação das bibliotecas que serão utilizadas.

import numpy as np
from scipy.io import wavfile


#parâmetros de cada um destes sinais: "senoidal", "onda_quadrada", "dente_de_serra", "triangular".


# Solicita ao usuário que informe o tipo de sinal escolhendo um número e armazena o valor digitado na variável 'tipo'.

tipo = input("Informe o tipo de sinal escolhendo um número: \n"
            "1 - senoidal \n"
            "2 - onda quadrada \n"
            "3 - dente de serra \n"
            "4 - triangular: \n")

# Solicita ao usuário que informe a frequência do sinal e converte o valor digitado para o tipo float, armazenando-o na variável 'freq'.
freq = float(input("Informe a frequência do sinal: "))


# Solicita ao usuário que informe a duração do sinal em segundos
# e converte o valor digitado para o tipo float, armazenando-o na variável 'duracao'.
duracao = float(input("Informe a duração do sinal (em segundos): "))


taxa_amostragem = 44100                     # Define a taxa de amostragem como 44100 Hz, que representa a quantidade de amostras por segundo.
# Taxa de amostragem em Hz, aqui está sendo definido no código pois não é um parâmetro do teclado... pode ser redefinido quando quiser.

def gerar_sinal(tipo, freq, duracao, taxa_amostragem):

    # Cria um array de tempo 't' usando np.linspace, com início em 0, duração 'duracao',
    # número de pontos igual a 'duracao * taxa_amostragem' e o parâmetro 'endpoint=False'
    # para excluir o ponto final do intervalo.
    t = np.linspace(0, duracao, int(duracao * taxa_amostragem), endpoint=False)


    # Verifica o valor do parâmetro 'tipo' e realiza ações correspondentes.
    if tipo == "1":
        sinal = np.sin(2 * np.pi * freq * t)
        nome_tipo = "senoidal"               # Atribui o nome "senoidal" à variável 'nome_tipo'.

    elif tipo == "2":
        sinal = np.sign(np.sin(2 * np.pi * freq * t))
        nome_tipo = "onda_quadrada"           # Atribui o nome "onda_quadrada" à variável 'nome_tipo'.

    elif tipo == "3":
        sinal = 2 * (t * freq - np.floor(0.5 + t * freq))
        nome_tipo = "dente_de_serra"          # Atribui o nome "dente_de_serra" à variável 'nome_tipo'.

    elif tipo == "4":
        sinal = np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1
        nome_tipo = "triangular"              # Atribui o nome "triangular" à variável 'nome_tipo'

    else:
        print("Tipo de sinal inválido.")       # Se o valor do parâmetro 'tipo' não for válido, imprime uma mensagem de erro.
        return None                            # Retorna 'None' para indicar que nenhum sinal foi gerado.

    return sinal, nome_tipo
    # Retorna o sinal gerado 'sinal' e o nome correspondente 'nome_tipo'.

# Chama a função gerar_sinal passando os parâmetros tipo, freq, duracao e taxa_amostragem,
# e atribui o retorno às variáveis dados e nome_tipo.

dados, nome_tipo = gerar_sinal(tipo, freq, duracao, taxa_amostragem)


# Verifica se a variável dados não é nula (None).
if dados is not None:

    # Cria o nome do arquivo de áudio usando as variáveis nome_tipo, freq e duracao.
    nome_arquivo = f"{nome_tipo}_{freq}Hz_{duracao}s.wav"

    # Escreve os dados no arquivo de áudio usando a função wavfile.write do módulo wavfile,
    # passando o nome do arquivo, taxa de amostragem e os dados convertidos para o tipo np.float32.
    wavfile.write(nome_arquivo, taxa_amostragem, dados.astype(np.float32))


    print(f"O arquivo de áudio '{nome_arquivo}' foi salvo com sucesso.")
    # Imprime uma mensagem informando que o arquivo de áudio foi salvo com sucesso.


#Observação: observamos que para o sinal senoidal deve ser atribuido uma frequência "alta" em relação aos outros, pois assim é melhor de ouvir o áudio gerado através dele.