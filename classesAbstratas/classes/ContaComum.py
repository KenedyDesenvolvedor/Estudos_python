from classes.ContaCliente import ContaCliente

class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, Valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, Valor_investido, taxa_rendimento)

    def calculor_rendimento(self):
        remuneracao = self.Valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF