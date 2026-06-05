from abc import ABC, abstractmethod

class ContaCliente(ABC):
    def __init__(self, numero, IOF, IR, Valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.Valor_investido = Valor_investido
        self.taxa_rendimento = taxa_rendimento

    @abstractmethod
    def calculor_rendimento(self):
        remuneracao = self.Valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        valorIR = remuneracao * self.IR
        self.Valor_investido += remuneracao - valorIOF - valorIR
    
    def extrato(self):
        print(f"O saldo atual dda conta {self.numero} é: R$ {self.Valor_investido:.2f}")