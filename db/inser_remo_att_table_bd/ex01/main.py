import sqlite3 as conector 

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    VALUES (12345678900, 'João', '2000-01-31', 1);'''

comando1 = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    VALUES (12345678910, 'Maria', '2003-04-06', 1);'''

cursor.execute(comando1)

conexao.commit()

cursor.close()
conexao.close()