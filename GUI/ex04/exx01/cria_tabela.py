from conect import conexao, meu_cursor

meu_cursor.execute('''
                   CREATE TABLE IF NOT EXISTS PRODUTO(
                   CODIGO SERIAL PRIMARY KEY,
                   NOME VARCHAR(100) NOT NULL,
                   PRECO NUMERIC (10,2) NOT NULL);
                    ''')

conexao.commit()
print("Tabela criada com sucesso!")
conexao.close()