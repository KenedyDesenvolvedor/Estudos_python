import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''SELECT * FROM Pessoa WHERE oculos = :usa_oculos;'''
cursor.execute(comando, {"usa_oculos": True})

registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

    cursor.close()
    conexao.close()