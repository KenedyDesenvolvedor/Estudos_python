import datetime
from classes.Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()
    
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.trasacoes.append(["DEPÓSITO", valor, datetime.datetime.today()])
    
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.trasacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True
        
    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return " Não existe saldo suficiente"
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.trasacoes.append(["TRANSFERENCIA", valor, datetime.datetime.today()])
            return " Transferencia realizada"
    
    def gerar_saldo(self):
        print(f" Numero: {self.numero}\n Saldo: R${self.saldo:1.2f}")