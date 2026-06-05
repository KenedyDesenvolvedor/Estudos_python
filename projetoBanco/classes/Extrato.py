class Extrato:
    def __init__(self):
        self.transacoes = []
    
    def gerar_extrato(self,conta):
        print(f"Extrato da conta {conta}")
        for tran in self.transacoes:
            print(f"{tran[0]:15s} {tran[1]:2.2f} {tran[2].strftime('%d/%b/%Y')}")
        print(f"Saldo atual: {conta.saldo}\n")