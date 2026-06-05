from classes.Conta import Conta

c1 = Conta(1, 1000)
c2 = Conta(2, 50)
c3 = Conta(3, 0)

#c1._Conta__saldo = -5000

c1.saldo = -1500

print(f"até agora temos {Conta.get_total_contas()} contas criadas")
print(f"Muito obrigado por ser cliente do {Conta.nome_banco()}")
print(c1.saldo)
print(c2.saldo)

#print(f"Conta 1 com R${c1.saldo}")
#print(f"Conta 2 com R${c2.saldo}")

#c1.gerar_saldo()
#c2.gerar_saldo()