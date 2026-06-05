from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.contaExpecial import ContaExpecial
from classes.ContaRemuneracaoPoupanca import ContaRemuneracaoPoupanca

cliente1 = Cliente(123, "João", "Rua x")
cliente2 = Cliente(321, "Maria", "Rua y")
cliente3 = Cliente(456, "Zezinho", "Rua z")

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaRemuneracaoPoupanca(cliente3, 3, 2000, 0.1)


conta1.depositar(300)
conta1.transfere_valor(conta2, 500)

conta2.sacar(700)

conta3.remuneraConta()
conta3.gerar_saldo()

conta1.extrato.gerar_extrato(conta1)
conta2.extrato.gerar_extrato(conta2)
conta3.extrato.gerar_extrato(conta3)
