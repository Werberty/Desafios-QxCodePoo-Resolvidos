class Banco:
    def __init__(self) -> None:
        self.clientes = []
    
    def agregar(self, cliente):
        self.clientes.append(cliente)
    
    def checar(self, cliente):
        verificador = False
        for dados in self.clientes:
            if cliente == dados:
                if dados.conta.agencia == cliente.conta.agencia and dados.conta == cliente.conta:
                    verificador = True
        return verificador
