arquivo = open('Manipulacao-de-dados/ex04/dados.txt', 'r', encoding='utf-8')

conteudo = arquivo.readline()

print("tipo de conteudo: ", type(conteudo))

print('conteudo retorado pelo read: \n')

print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Proximo conteudo retornado: ")

print(repr(proximo_conteudo))

arquivo.close()