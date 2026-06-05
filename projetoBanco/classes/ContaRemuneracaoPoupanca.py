from classes.Conta import Conta
from classes.Poupança import Poupanca

class ContaRemuneracaoPoupanca(Conta, Poupanca):
    def __init__(self, cliente, numero, saldo, taxa_remuneracao):
        Conta.__init__(self, cliente, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)
    
    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)