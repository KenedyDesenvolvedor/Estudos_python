from classes.Extrato import Extrato
import datetime

class Conta:
    def __init__(self, clientes,numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()
    
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito", valor, datetime.datetime.today()])
    
    def sacar(self, valor):
        if self.saldo < valor:
            print(f"Não existe saldo suficiente na conta {self.numero} do cliente {self.clientes.cpf}")
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])
            return True
        
    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente!"
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["Transferência",  valor, datetime.datetime.today()])
            return "Transferencia realizada!"
    
    def gerar_saldo(self):
        print(f"Conta:{self.numero}\n Saldo: R${self.saldo:2.2f}")
    
