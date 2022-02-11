from abc import ABC
import enum

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
    def __init__(self, lotacao_max, preferenciais) -> None:
        self._lotacao_max = lotacao_max
        self._preferenciais = preferenciais
        self._cadeiras = list(f"{preferenciais*'@'}{(lotacao_max-preferenciais)*'='}")
    
    @property
    def cadeiras(self):
        return self._cadeiras
    
    def inserir_passageiro(self, nome, idade):
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
    
    def mostrar_cadeiras(self):
        print('[',end=' ')
        for c in self.cadeiras:
            print(c, end=' ')
        print(']')


topic = Topic(5, 2)
topic.inserir_passageiro('betim', 67)
topic.inserir_passageiro('Bia', 45)
topic.inserir_passageiro('ana', 17)
topic.inserir_passageiro('Luiz', 90)
topic.inserir_passageiro('Antonio', 109)
topic.inserir_passageiro('Cheila', 7)
topic.mostrar_cadeiras()

