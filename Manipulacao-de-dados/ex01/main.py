import os
arquivo = open("exemplo.text", 'w', encoding='utf-8')

print("nome do arquivo: ",arquivo.name)
print("Modo de arquivo: ",arquivo.mode)

print("Arquivo está fechado?: ",arquivo.closed)

arquivo.write("ola mundo!")


arquivo.close()

print("Arquivo esta fechado agora?", arquivo.closed)


relpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)