class CustomError(Exception):
    pass

def divide(a,b):
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as ex:
    print("\nErro dividido por zero\n")
    print(f"Detalhes do erro: {ex}\n")

def checa_valor(valor):
    if valor < 0:
        raise CustomError("Valor não pode ser negativo")
    
try:
    checa_valor(-10)
except CustomError as ex:
    print("\nErro personalizado capturado\n")
    print(f"Detalhes do erro: {ex}\n")