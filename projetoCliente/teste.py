from classes.Cliente import Cliente
from classes.Conta import Conta

cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("224", "Maria", "Rua Y")

conta1 = Conta([cliente1, cliente2], 111, 0)

conta1.depositar(1000)
conta1.sacar(200)
conta1.sacar(150)
conta1.depositar(2000)
conta1.sacar(1000)

conta1.extrato.gerar_extrato(conta1.numero)

conta1.gerar_saldo()