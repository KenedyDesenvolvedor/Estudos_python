from classes.ContaCliente import ContaCliente
from classes.Banco import Banco
from classes.ContaComum import ContaComum
from classes.ContaVip import ContaVip

banco1 = Banco(999, "Teste")

conta_cliente1 = ContaCliente(1, 0.01, 0.01, 2000, 0.05)
conta_comum1 = ContaComum(2, 0.01, 0.01, 2000, 0.05)
conta_remunerada1 = ContaVip(3, 0.01, 0.01, 2000, 0.05)

banco1.adicionar_conta(conta_cliente1)
banco1.adicionar_conta(conta_comum1)
banco1.adicionar_conta(conta_remunerada1)

banco1.calcular_rendimento_mensal()
banco1.imprime_saldo_contas()