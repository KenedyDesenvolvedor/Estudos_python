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