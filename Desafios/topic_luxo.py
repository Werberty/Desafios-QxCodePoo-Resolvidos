from abc import ABC
from ast import While

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
    
    def encontrar_lugar(self, idade):
        cadeiras_pref = [n for n, c in enumerate(self.cadeiras) if c=='@']
        cadeiras_nao_pref = [n for n, c in enumerate(self.cadeiras) if c=='=']
        if idade >= 60:
            if len(cadeiras_pref) != 0:
                return cadeiras_pref[0]
            elif len(cadeiras_nao_pref) !=  0:
                return cadeiras_nao_pref[0]
        elif idade < 60 and idade > 0:
            if len(cadeiras_nao_pref) != 0:
                return cadeiras_nao_pref[0]
            elif len(cadeiras_pref) != 0:
                return cadeiras_pref[0]
    
    def inserir_passageiro(self, nome, idade):
        verificador = self.verificar_passageiro(nome)
        if verificador:
            passageiro = Passageiro(nome, idade)
            cadeira_vazia = self.encontrar_lugar(passageiro.idade)
            if cadeira_vazia is not None:
                self.cadeiras[cadeira_vazia] += passageiro.nome
            else:
                print('Topic Lotada')

    def verificar_passageiro(self, nome):
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
topic.mostrar_cadeiras()
