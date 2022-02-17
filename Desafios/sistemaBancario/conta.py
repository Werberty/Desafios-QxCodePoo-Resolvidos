from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo=0) -> None:
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        return super().sacar(valor)


class ContaCorrente(Conta):
    def __init__(self):
        self.limite = 300

    def sacar(self, valor):
        return super().sacar(valor)
