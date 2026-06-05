
class Extrato:
    def __init__(self):
        self.trasacoes = []
    
    def gerar_extrato(self, conta):
        print(f" Extrato da conta {conta}", )
        for transacao in self.trasacoes:
            print(f" {transacao[0]:15s} {transacao[1]:2.2f} {transacao[2].strftime("%d/%b/%Y")}")