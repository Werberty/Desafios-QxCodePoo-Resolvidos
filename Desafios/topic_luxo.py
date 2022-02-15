from abc import ABC
import re

'''O objetivo dessa atividade é exercitar o que vocês aprenderam 
no cinema com algumas variações. Aqui, vamos implementar um 
sistema de alocação de passageiros em uma topic. Nossa topic 
tem uma quantidade máxima de passageiros, mas também define alguns 
assentos preferenciais.
'''


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
        self._cadeiras = list(
            f"{preferenciais*'@'}{(lotacao_max-preferenciais)*'='}")

    @property
    def cadeiras(self):
        return self._cadeiras

    def inserir_passageiro(self, nome, idade):
        verificador = self.verificar_passageiro(nome)
        if verificador:
            passageiro = Passageiro(nome, idade)
            cadeira_vazia = self.encontrar_lugar(passageiro.idade)
            if cadeira_vazia is not None:
                self.cadeiras[cadeira_vazia] += f'{passageiro.nome}:{passageiro.idade}'
            else:
                print('Topic Lotada')
        else:
            print('Passageiro já esta na topic')

    def remover_passageiro(self, nome):
        verificador = self.verificar_passageiro(nome)
        if not verificador:
            for n, cadeira in enumerate(self.cadeiras):
                # Variavel aux com caracteres indesejados
                aux = re.sub(nome, '', cadeira)
                for i in aux:  # deixando somente no nome do passageiro na variavel cadeira
                    cadeira = cadeira.replace(i, '')
                if nome == cadeira:
                    if aux[0] == '@':
                        self.cadeiras[n] = '@'
                    elif aux[0] == '=':
                        self.cadeiras[n] = '='
        else:
            print('Passageiro não está na topic')

    def encontrar_lugar(self, idade):
        cadeiras_pref = [n for n, c in enumerate(self.cadeiras) if c == '@']
        cadeiras_nao_pref = [
            n for n, c in enumerate(self.cadeiras) if c == '=']
        if idade >= 60:
            if len(cadeiras_pref) != 0:
                return cadeiras_pref[0]
            elif len(cadeiras_nao_pref) != 0:
                return cadeiras_nao_pref[0]
        elif idade < 60 and idade > 0:
            if len(cadeiras_nao_pref) != 0:
                return cadeiras_nao_pref[0]
            elif len(cadeiras_pref) != 0:
                return cadeiras_pref[0]

    def verificar_passageiro(self, nome):
        verificador = True
        for cadeira in self.cadeiras:
            aux = re.sub(nome, '', cadeira)
            for i in aux:
                cadeira = cadeira.replace(i, '')
            if nome == cadeira:
                verificador = False
        return verificador

    def mostrar_cadeiras(self):
        print('[', end=' ')
        for c in self.cadeiras:
            print(c, end=' ')
        print(']')


# Testes
topic = Topic(5, 2)
topic.inserir_passageiro('davi', 17)
topic.inserir_passageiro('joao', 103)
topic.inserir_passageiro('ana', 35)
topic.inserir_passageiro('rex', 20)
topic.inserir_passageiro('bia', 16)
topic.remover_passageiro('davi')
topic.inserir_passageiro('aragao', 96)
topic.inserir_passageiro('lucas', 23)
topic.remover_passageiro('marcelo')
topic.remover_passageiro('ana')
topic.inserir_passageiro('bia', 33)
topic.mostrar_cadeiras()
