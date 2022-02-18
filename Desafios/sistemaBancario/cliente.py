
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta) -> None:
        super().__init__(nome, idade)
        self.conta = conta

    def criar_conta(self, conta):
        self.conta = conta
