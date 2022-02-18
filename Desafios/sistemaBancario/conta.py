from abc import ABC, abstractmethod
from banco import Banco
from cliente import Cliente

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo=0) -> None:
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insulficiente')
            return
        self.saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=0) -> None:
        super().__init__(agencia, numero_conta, saldo)
        self.limite = 300

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            print('Limite insulficente')
            return
        self.saldo -= valor
