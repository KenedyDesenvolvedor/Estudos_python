# Codigo da classe 
class Conta:
    def __init__(self, num, cpf, nomeTitular, saldo):
        self.numero = num
        self.cpf = cpf
        self.nome = nomeTitular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    
    def gerar_extrato(self):
        print(f' Numero: {self.numero}\n CPF: {self.cpf}\n Nome {self.nome}\n Saldo: {self.saldo}\n')
    
    def transfereValor(self,contaDestino, valor):
        if self.saldo < valor:
            return(" Não existe saldo suficiente\n")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return(" Transferência realizada com sucesso\n")
c1 = Conta(1, "123.456.789-00", "João Silva", 9000)
c1.depositar(500)

valor_saque = 300
resultado_saque = c1.sacar(valor_saque)

if resultado_saque:
    print(f" Saque de R$ {valor_saque} realizado com sucesso.")
else:
    print(f" Saque de R$ {valor_saque} não realizado devido a saldo insuficiente.")

c1.gerar_extrato()

Conta1 = Conta(123,"88888888888", "Maria", 0)
Conta2 = Conta(124,"99999999999", "João", 500)

if Conta1 == Conta2:
    print(" São iguais")
else:
    print(" São diferentes")

print(Conta2.transfereValor(Conta1, 300))

Conta1.gerar_extrato()
Conta2.gerar_extrato()