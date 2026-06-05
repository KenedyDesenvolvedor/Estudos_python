class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adiciona_conta(self, conta_cliente):
        self.contas.append(conta_cliente)

    def calcular_rendimento_mensal(self):
        for conta in self.contas:
            conta.calculo_rendimento()

    def imprime_saldo_contas(self):
        for conta in self.contas:
            conta.extrato()