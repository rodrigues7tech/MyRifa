class Assinantes:
    def __init__(self, nome, rg, telefone, numero):
        self.nome = nome
        self.__rg = rg
        self.telefone = telefone
        self.numero = numero

    # getters & setters
    @property
    def rg(self):
        return

