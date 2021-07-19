import random
import os
import time

os.system('cls')
cont = 0
print('\033[32m'+'-=' *15+'\033[0;0m')

###### Cria uma matriz 4 x 5 (4 linhas e 5 colunas) ######## 
cartela = [ [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20]
        ]
###### Cria uma lista com 20 elementos ######
listaNome = ['A','B','C','D','E','F','G','H','I','J','L','K','M','N','O','P','R','S','T','U']

###### Exibe a matriz no terminal######
for linha in range(0,4): 
    for coluna in range (0,5):
        print(f'[{cartela[linha][coluna]:^4}]', end='')
    print()
print('\033[32m'+'-=' *15+'\033[0;0m')
print()

###### repete o codigo e incrementa o contador se a condição for verdadeira ######
while (cont != 20):
    print('\033[32m'+'Verifique a disponibilidade do número na cartela acima!'+'\033[0;0m')
    nome = str(input('\033[32m'+'Informe o nome do assinante: '+'\033[0;0m'))
    numEscolhido = int(input('\033[32m'+'Insira qual número deseja assinar: '+'\033[0;0m'))

    ###### Verifica se o numero escolhido esta entre 1 e 20 ######
    ###### Percorre a matriz e substitui o numero selecionado por * ######
    if numEscolhido >0 and numEscolhido <21:
        for linha in range(0,4):
            for coluna in range (0,5):
                if cartela[linha][coluna] == numEscolhido:
                    cartela[linha][coluna] = '*'
                    time.sleep(2)
                    os.system('cls')

        print('\033[32m'+'-=' *15+'\033[0;0m')            
        for linha in range(0,4):
            for coluna in range (0,5):
                print(f'[{cartela[linha][coluna]:^4}]', end='')
            print()
        print('\033[32m'+'-=' *15+'\033[0;0m')
        print()
        cont +=1
        ###### Adicina o nome na lista referente a posição escolhida ######
        listaNome[numEscolhido-1] = nome
        
    else:
        ### Exibe erro na tela caso o número escolhido não esteja entre 1 e 20 ###
        print()
        print('\033[31m'+'ERRO: Insira um número entre 1 e 20'+'\033[0;0m')
        print('\033[31m'+'PRESSIONE ENTER PARA CONTINUAR'+'\033[0;0m')
        input()

print('CARTELA COMPLETA. PRESSIONE ENTER PARA SORTEAR O NÚMERO!')
input()

###### Gera um número aleatório entre 1 e 20 e exibe-o na tela ######
num = random.randrange(1,20)
print(f'O número sorteado é: {num}')

###### Exibe o nome da lisa refente ao numero sorteado ######
print(f'Parabéns {listaNome[num-1]}!!!! ')

input()
