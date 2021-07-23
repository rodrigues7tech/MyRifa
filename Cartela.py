class Cartela:
    def exibirCartela(cartela):
        for linha in range(0, 4):
            for coluna in range(0, 5):
                print(f'[{cartela[linha][coluna]:^4}]', end='')
            print()
        print('-=' * 15)
        print()

    def assinarCartela(numero, cartela):
        ###### Verifica se o numero escolhido esta entre 1 e 20 ######
        ###### Percorre a matriz e substitui o numero selecionado por * ######
        if numero > 0 and numero < 21:
            for linha in range(0, 4):
                for coluna in range(0, 5):
                    if cartela[linha][coluna] == numero:
                        cartela[linha][coluna] = '*'
        else:
            ### Exibe erro na tela caso o número escolhido não esteja entre 1 e 20 ###
            print()
            print('ERRO: Insira um número entre 1 e 20')
            print('PRESSIONE ENTER PARA CONTINUAR')
            input()
