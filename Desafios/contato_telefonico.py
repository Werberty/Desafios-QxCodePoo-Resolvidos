'''Contato Telefônico
O objetivo dessa atividade é implementar uma classe responsável 
por guardar um único contato da agenda telefônica do seu celular. 
Cada contato pode ter vários telefones.
'''

class Contato:
    def __init__(self, nome:str='Vazio') -> None:
        self._nome = nome
        self._telefones = {}
        
    def adicionar_telefone(self, label: str, telefone: str):
        self._telefones[label] = telefone
    
    def remover_telefone(self, indice):
        for n, key in enumerate(self._telefones):
            if indice == n:
                key_remove = key
        del self._telefones[key_remove]
    
    def atualizar_contato(self, nome, *args):
        self._telefones = dict(args)
        self._nome = nome
    
    def show(self):
        for n, (label, tele) in enumerate(self._telefones.items()):
            print(f'[{n}:{label}:{tele}]', end='')
        print()

if __name__ == '__main__':
    c1 = Contato('Werberty')
    c1.adicionar_telefone('oi', '99')
    c1.adicionar_telefone('casa', '11')
    c1.remover_telefone(1)
    c1.atualizar_contato('Bety', ('tim', '9087'), ('fixo', '11021'))
    c1.show()

