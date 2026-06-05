import sqlite3 as conector
from modelo import Veiculo

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()


comando = '''SELECT * FROM Veiculo;'''
cursor.execute(comando)

reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

    conexao.commit()

cursor.close()
conexao.close()