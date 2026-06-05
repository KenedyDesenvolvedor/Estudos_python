import psycopg2

conn = psycopg2.connect(database = "postgresDB", 
                        user = "admin",
                        password = "admin123",
                        host = "127.0.0.1",
                        port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS Agendar(ID SERIAL PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Telefone CHAR(12)); """)
print("Tabela criada com sucesso!")
conn.commit()
conn.close()