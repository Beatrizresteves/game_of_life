import numpy
from time import sleep
import copy
import sys


# print('linhacoluna')
# 0 com 3 vizinhos -> 1
# 1 com 2 ou 3 vizinhos sobrevive
# O resto vira 0

# tempo 0:
# [0][0]: 0, [0][1]: 0, [0][2]: 0, [0][3]: 0
# [1][0]: 1, [1][1]: 1, [1][2]: 0, [1][3]: 0
# [2][0]: 0, [2][1]: 1, [2][2]: 0, [2][3]: 0
# [3][0]: 0, [3][1]: 0, [3][2]: 0, [3][3]: 0
# tempo 1:
# [0][0]: 0, [0][1]: 0, [0][2]: 0, [0][3]: 0
# [1][0]: 1, [1][1]: 1, [1][2]: 0, [1][3]: 0
# [2][0]: 1, [2][1]: 1, [2][2]: 0, [2][3]: 0
# [3][0]: 0, [3][1]: 0, [3][2]: 0, [3][3]: 0

print('\n')
input_do_usuario = input("Usar jogo padrão? s/n: ")

if input_do_usuario == 'n':
    while True:
        print('\n')
        input_do_usuario = input("Insira um número inteiro positivo e maior que zero (que será a largura e altura da matriz:) ")
        try:
            input_do_usuario = int(input_do_usuario)
            if int(input_do_usuario) > 0:
                TAMANHO_DA_MATRIZ = int(input_do_usuario)
                break
            else:
                print("Esse não é um número inteiro positivo maior que zero.")
        except:
            print("Esse não é um número inteiro.")
            continue

    matriz = numpy.zeros((TAMANHO_DA_MATRIZ, TAMANHO_DA_MATRIZ), dtype=numpy.int)

    while True:
        print('\n')
        print("Matriz atual: ")
        print(matriz)
        print('\n')
        input_do_usuario = input("Deseja inserir uma célula viva? s/n: ")
        print('\n')
        if input_do_usuario == 's':
            print("Número de linhas: ", TAMANHO_DA_MATRIZ)
            input_do_usuario = input("Insira o número da linha em que deseja inserir: ")
            try:
                linha = int(input_do_usuario) - 1
            except:
                print("Entrada inválida.")
                continue
            if linha not in range(TAMANHO_DA_MATRIZ):
                print("Não é um número válido.")
                continue
            print("Número de colunas: ", TAMANHO_DA_MATRIZ)
            input_do_usuario = input("Agora o número da coluna dessa linha: ")
            try:
                coluna = int(input_do_usuario) - 1
            except:
                print("Entrada inválida.")
                continue
            if coluna not in range(TAMANHO_DA_MATRIZ):
                print("Não é um número válido.")
                continue
            matriz[linha][coluna] = 1
        elif input_do_usuario == 'n':
            break
        else:
            print("Entrada inválida.")

elif input_do_usuario == 's':
# Matriz inicial padrão do site game of life:
    TAMANHO_DA_MATRIZ = 10
    matriz = numpy.zeros((TAMANHO_DA_MATRIZ, TAMANHO_DA_MATRIZ), dtype=numpy.int)
    matriz[1][2] = 1
    matriz[2][3] = 1
    matriz[3][1] = 1
    matriz[3][2] = 1
    matriz[3][3] = 1

else:
    print("Input inválido. Reinicie o programa.")
    sys.exit()

print('\n')
print("tempo 0: ")
print(matriz)
nova_matriz = copy.deepcopy(matriz)

for i in range(1000):
    for numero_da_linha, linha in enumerate(matriz):
        for numero_da_coluna, celula in enumerate(linha):
            vizinhos = []
            numero_de_vizinhos_vivos = 0

            # Se ele for da ponta:
            if numero_da_linha == 0 and numero_da_coluna == 0:
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita
            elif numero_da_linha == 0 and numero_da_coluna == TAMANHO_DA_MATRIZ-1:
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
            elif numero_da_linha == TAMANHO_DA_MATRIZ-1 and numero_da_coluna == 0:
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
            elif numero_da_linha == TAMANHO_DA_MATRIZ-1 and numero_da_coluna == TAMANHO_DA_MATRIZ-1:
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda

            # Se ele for da parede e nao da ponta.
            elif numero_da_linha == 0:
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita
            elif numero_da_coluna == 0:
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita
            elif numero_da_linha == TAMANHO_DA_MATRIZ-1:
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
            elif numero_da_coluna == TAMANHO_DA_MATRIZ-1:
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
            # Se não:
            else:
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
                vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
                vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
                vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita

            # Vizinho vivos:
            for vizinho in vizinhos:
                if vizinho == 1:
                    numero_de_vizinhos_vivos +=1
            
            # Transformação:
            if celula == 0 and numero_de_vizinhos_vivos == 3:
                nova_matriz[numero_da_linha][numero_da_coluna] = 1 # recebe 1
            elif (celula == 1 and numero_de_vizinhos_vivos == 2) or (celula == 1 and numero_de_vizinhos_vivos == 3):
                nova_matriz[numero_da_linha][numero_da_coluna] = 1 # recebe 1
            else:
                nova_matriz[numero_da_linha][numero_da_coluna] = 0 # recebe 0

    matriz = copy.deepcopy(nova_matriz)

    sleep(1)
    print('\n')
    print(f"tempo {i+1}: ")
    print(matriz)
    print('\n')