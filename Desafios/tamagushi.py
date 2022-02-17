'''
Bichinho Virtual Tamaguhi

Você deve implementar um simulador de bichinho virtual. 
Ele poderá comer, brincar, dormir e tomar banho. E eventualmente morrerá, 
se você não cuidar bem dele.
'''

class Tamagushi:
    def __init__(self, energia, saciedade, limpeza) -> None:
        self._energia = energia
        self._saciedade = saciedade
        self._limpeza = limpeza
        self.diamante = 0
        self.idade = 0
        self.vivo = True
        self._niveis_max = {'E': energia, 'S': saciedade, 'L': limpeza}

    @property
    def niveis_max(self):
        return self._niveis_max

    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, valor):
        if valor <= 0:
            valor = 0
        elif valor > self.niveis_max['E']:
            valor = self.niveis_max['E']
        self._energia = valor
    
    @property
    def saciedade(self):
        return self._saciedade
    
    @saciedade.setter
    def saciedade(self, valor):
        if valor <= 0:
            valor = 0
        elif valor > self.niveis_max['S']:
            valor = self.niveis_max['S']
        self._saciedade = valor
    
    @property
    def limpeza(self):
        return self._limpeza
    
    @limpeza.setter
    def limpeza(self, valor):
        if valor <= 0:
            valor = 0
        elif valor > self.niveis_max['L']:
            valor = self.niveis_max['L']
        self._limpeza = valor

    def show(self):
        print('E:', self.energia, '/', self.niveis_max['E'], end='')
        print(' S:', self.saciedade, '/', self.niveis_max['S'], end='')
        print(' L:', self.limpeza, '/', self.niveis_max['L'], end='')
        print(f' D: {self.diamante} I: {self.idade}')

    def jogar(self):
        self.saciedade -= 1
        self.limpeza -= 3
        self.energia -= 2
        self.diamante += 1
        self.idade += 1

    def comer(self):
        self.saciedade += 4
        self.limpeza -= 2
        self.energia -= 1
        self.idade += 1

    def dormir(self, turnos=1):
        if (self.niveis_max['E'] - self.energia) >= 5:
            self.energia = self.niveis_max['E']
            self.idade += turnos
        else:
            print('Fail: não está com sono')

    def tomar_banho(self):
        self.limpeza = self.niveis_max['L']
        self.energia -= 3
        self.saciedade -= 1
        self.idade += 2


bixo = Tamagushi(20, 10, 15)
bixo.show()
bixo.comer()
bixo.comer()
bixo.comer()
bixo.comer()
bixo.comer()
bixo.comer()
bixo.comer()
bixo.comer()
bixo.show()
