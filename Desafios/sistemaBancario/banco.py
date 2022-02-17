class banco:
    def __init__(self) -> None:
        self.contas = []
        self.clientes = []
    
    def agregar(self, conta, cliente):
        self.contas = self.contas.append(conta)
        self.clientes = self.clientes.append(cliente)
    
    def checar(self, cliente, conta):
        verificador = False
        for cont in self.contas:
            if cont == conta:
                verificador = True
        for cli in self.clientes:
            if cli == cliente:
                verificador = True
        return verificador
