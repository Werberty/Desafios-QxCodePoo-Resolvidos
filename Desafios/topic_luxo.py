from abc import ABC

class Passageiro(ABC):
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade


class Topic:
    def __init__(self, lotacao_max, preferenciais):
        self._lotacao_max = lotacao_max
        self._preferenciais = preferenciais
        self._cadeiras = list(f"{preferenciais*'@'}{(lotacao_max-preferenciais)*'='}")
    
    @property
    def cadeiras(self):
        return self._cadeiras
    
    def inserir_passageiro(self, nome, idade):
        verificador = self.verificar_passageiro(nome)
        if verificador:
            passageiro = Passageiro(nome, idade)
            for n, cadeira in enumerate(self.cadeiras):
                if passageiro.idade >= 60:
                    if cadeira == '@':
                        self.cadeiras[n] += passageiro.nome
                        return
                    elif cadeira == '=':
                        self.cadeiras[n] += passageiro.nome
                        return
                else:
                    if cadeira == '=':
                        self.cadeiras[n] += passageiro.nome
                        return
    
    def verificar_passageiro(self, nome): #verificar possiveis problemas ainda
        verificador = True
        for cadeira in self.cadeiras:
            cadeira = cadeira.replace('@', '')
            cadeira = cadeira.replace('=', '')
            if nome == cadeira:
                print('Passageiro ja existe')
                verificador = False
        return verificador

    def mostrar_cadeiras(self):
        print('[',end=' ')
        for c in self.cadeiras:
            print(c, end=' ')
        print(']')


topic = Topic(5, 2)
topic.inserir_passageiro('davi', 17)
topic.inserir_passageiro('joao', 103)
topic.inserir_passageiro('ana', 35)
topic.inserir_passageiro('rex', 20)
topic.inserir_passageiro('bia', 16) #não está adicionando a bia
topic.mostrar_cadeiras()
