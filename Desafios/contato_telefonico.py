'''Contato Telefônico
O objetivo dessa atividade é implementar uma classe responsável 
por guardar um único contato da agenda telefônica do seu celular. 
Cada contato pode ter vários telefones.
'''

class Contato:
    def __init__(self, nome:str='Vazio') -> None:
        self._nome = nome
        self._telefone = {}
        
    def adicionar_telefone(self, label: str, telefone: str):
        self._telefone[label] = telefone
    
    def show(self):
        for n, (label, tele) in enumerate(self._telefone.items()):
            print(f'[{n}:{label}:{tele}]', end='')
        print()

if __name__ == '__main__':
    c1 = Contato('Werberty')
    c1.adicionar_telefone('oi', '99')
    c1.adicionar_telefone('casa', '11')
    c1.show()

