'''
Alocação de Sala de Cinema

O objetivo dessa atividade é implementar o sistema de alocação de uma única sala
de cinema. Se existem cadeiras livres, os clientes podem reservá-las. Também
podem desistir da reserva. O sistema deve mostrar quem está sentado em cada
cadeira.
'''

class Cliente:
    def __init__(self, nome, telefone, id) -> None:
        self.nome = nome
        self.telefone = telefone
        self.id = id


class Controle:
    def __init__(self) -> None:
        self.cliente = None

    def reservar(self, nome, telefone, id):
        self.cliente = Cliente(nome, telefone, id)
        aprovado = self.verificar(self.cliente)
        if aprovado:
            self.cadeiras[id] = f'{self.cliente.nome}:{self.cliente.telefone}'

    def cancelar(self, id):
        aprovado = self.verificar(self.cliente)
        if aprovado:
            print('Cliente não esta no cinema')
        self.cadeiras[id] = '-'

    def verificar(self, cliente):
        v = True
        if self.cadeiras[cliente.id] != '-':
            v = False
            print('Cadeira já esta ocupada')
            return v
        for lugar in self.cadeiras:
            if lugar != '-':
                lugar = lugar.split(':')
                if lugar[0] == cliente.nome:
                    print('Cliente já está no cinema')
                    v = False
                else:
                    v = True
        return v


class SalaDeCinema(Controle):
    def __init__(self, quantidade_cadeiras) -> None:
        self.cadeiras = list(quantidade_cadeiras*'-')

    def mostrar_sala(self):
        print('[ ', end='')
        for c in self.cadeiras:
            print(f'{c} ', end='')
        print(']')


sala = SalaDeCinema(10)
sala.reservar('Thomas', 9976, 5)
sala.reservar('Norman', 3333, 3)
sala.cancelar(5)
sala.mostrar_sala()
