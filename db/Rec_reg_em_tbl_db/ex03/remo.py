import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

comando = '''DELETE FROM Veiculo WHERE ano = 2001;'''
cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()