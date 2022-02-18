"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from banco import Banco
from conta import ContaPoupanca, ContaCorrente
from cliente import Cliente

banco1 = Banco()

cliente1 = Cliente('Werberty', 23, ContaCorrente('077', '05678', 300))
cliente2 = Cliente('João', 45, ContaPoupanca('099', '972348', 10))
cliente3 = Cliente('Maria', 33, ContaCorrente('1111', '9283478', 1500, 550))

banco1.agregar(cliente1)
banco1.agregar(cliente2)

print('Teste clinte2')

if banco1.checar(cliente2):
    cliente2.conta.sacar(522)
    cliente2.conta.depositar(70)

print('\nTeste clinte3')

if banco1.checar(cliente3):
    cliente3.conta.sacar(5)
    cliente3.depositar(30)
