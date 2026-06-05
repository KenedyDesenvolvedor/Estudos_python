with open('Manipulacao-de-dados/ex04/dados.txt', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    contador = texto.count("Olá")
    print("Total de Olás = ", contador)          