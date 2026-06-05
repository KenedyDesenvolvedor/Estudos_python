import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

comando1 = '''UPDATE Pessoa SET oculos = :usa_oculos WHERE cpf= :cpf;'''
cursor.execute(comando1, {"usa_oculos": False, "cpf": value})

conexao.commit()

cursor.close()
conexao.close()