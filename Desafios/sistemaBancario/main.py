from banco import Banco
from conta import ContaPoupanca, ContaCorrente
from cliente import Cliente

b1 = Banco()
c1 = Cliente('Werberty', 23, ContaCorrente('077', '05678', 300))
c2 = Cliente('João', 45, ContaPoupanca('099', '972348', 10))
b1.agregar(c1)
b1.agregar(c2)
if b1.checar(c2):
    c2.conta.sacar(5)
print(c2.conta.saldo)
