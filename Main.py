from Assinantes import Assinantes
from Cartela import Cartela
import random

cont = 0

### Matriz para criar tabela com 20 números
c =[ [1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20]
     ]

### LISTA PARA ARMAZENAR OS O DICIONARIO DADOS COM INFORMAÇÕES DOS ASSINANTES
assinaturas = list()
### DICIONARIO PARA ARMAZENAR AS INFORMAÇÕES
dados = dict()

### TITULO DO SISTEMA
print('-='*15)
print(f'{"           MY RIFA":^5}')
print('-='*15)

### CHAMA O METODO EXIBIRCARTELA DA CLASSE CARTELA
Cartela.exibirCartela(c)

### REPETIÇÃO PARA ARMAZENAR AS INFORMAÇÕES DOS 20 ASSINANTES
while cont != 20:
     dados.clear()
     print('Verifique a disponibilidade do número na cartela acima!')
     dados['nome'] = input("Informe o nome do assinante: ")
     dados['RG'] = input("Informe o RG do assinante: ")
     dados['telefone'] = input("Informe o telefone do assinante: ")
     dados['numEscolhido'] = int(input("Insira qual número deseja assinar: "))

     ### ARMAZENA OS DADOS RECEBIDOS NA CLASSE ASSINANTE
     p1 = Assinantes(dados['nome'], dados['RG'], dados['telefone'], dados['numEscolhido'])

     ### COPIA AS INFORMAÇÕES DO DICIONARIO E INSERE NA LISTA
     assinaturas.append(dados.copy())

     ### CHAMA O METODO ASSINARCARTELA DA CLASSE CARTELA E PASSA O NUMERO ESCOLHIDO COMO PARAMETRO
     Cartela.assinarCartela(dados['numEscolhido'], c)
     Cartela.exibirCartela(c)
     cont += 1

print('CARTELA COMPLETA. PRESSIONE ENTER PARA SORTEAR O NÚMERO!')
input()

###### Gera um número aleatório entre 1 e 20 e exibe-o na tela ######
num = random.randrange(1,20)
print(f'O número sorteado é: {num}')

###### Exibe o nome da lista refente ao numero sorteado ######
for p in assinaturas:
    if p['numEscolhido'] == num:
      print(f'Parabéns {p["nome"]}!!!! ')


#Exibe a lista com os dicionários inseridos. OBS: APENAS PARA VISUALIZAÇÃO
print()
print(assinaturas)

input()