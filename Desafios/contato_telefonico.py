'''Contato Telefônico
O objetivo dessa atividade é implementar uma classe responsável 
por guardar um único contato da agenda telefônica do seu celular. 
Cada contato pode ter vários telefones.
'''

class Contato:
    def __init__(self, nome='Vazio') -> None:
        self.nome = nome


if __name__ == '__main__':
    c1 = Contato('Werberty')
    print(c1.nome)

