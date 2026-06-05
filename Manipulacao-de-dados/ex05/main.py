arquivo = open('Manipulacao-de-dados/ex04/dados.txt', 'r', encoding='utf-8')

conteudo = arquivo.read()

print("tipo de conteudo: ", type(conteudo))

print('conteudo retorado pelo read: ')

print(repr(conteudo))

arquivo.close()