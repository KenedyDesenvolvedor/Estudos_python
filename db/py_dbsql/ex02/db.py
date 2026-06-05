import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''CREATE TABLE Marca(
    id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    sigla CHARACTER(2) NOT NULL,
    PRIMARY KEY (id)
    );'''

cursor.execute(comando)
conexao.commit()
cursor.close()
conexao.close()