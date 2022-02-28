'''Contato Telefônico
O objetivo dessa atividade é implementar uma classe responsável 
por guardar um único contato da agenda telefônica do seu celular. 
Cada contato pode ter vários telefones.
'''
class Telefone:
    def __init__(self, label, numero) -> None:
        self._label = label
        self._numero = numero
    
    def validar(self):
        pass


class Contato:
    def __init__(self, nome:str='Vazio') -> None:
        self._nome = nome
        self._telefones = []
        
    def adicionar_telefone(self, label: str, telefone: str):
        self._telefones.append(Telefone(label, telefone))
    
    def remover_telefone(self, indice):
        del self._telefones[indice]
    
    def atualizar_contato(self, nome, *args):
        self._nome = nome
        self._telefones = []
        for fone in args:
            label, num = fone
            self._telefones.append(Telefone(label, num))
    
    def show(self):
        for n, fone in enumerate(self._telefones):
            print(f'[{n}:{fone._label}:{fone._numero}]', end='')
        print()

if __name__ == '__main__':
    c1 = Contato('Werberty')
    c1.adicionar_telefone('oi', '99')
    c1.adicionar_telefone('casa', '11')
    c1.remover_telefone(1)
    c1.atualizar_contato('Bety', ('tim', '9087'), ('fixo', '11021'))
    c1.show()

