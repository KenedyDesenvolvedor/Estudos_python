import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    VALUES(99988877766, 'Hugo', '2000-01-12', True)'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()