import psycopg2

conexao = psycopg2.connect(
    database = "postgresDB",
    user = "admin",
    password = "admin123",
    host = "127.0.0.1",
    port = "5432"
)
print("Conexão com o Banco de Dados aberta com sucesso!")

meu_cursor = conexao.cursor()

if __name__ == '__main__':
    meu_cursor.execute('''
                       CREATE TABLE IF NOT EXISTS ITEM(
                        CODIGO SERIAL PRIMARY KEY,
                       NOME VARCHAR(100) NOT NULL,
                       PRECO NUMERIC(10, 2) NOT NULL);''')
    
    conexao.commit()
    print("Tabela criada com sucesso!")
    conexao.close()