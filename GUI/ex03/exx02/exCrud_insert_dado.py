import psycopg2

conn = psycopg2.connect(database = "postgresDB",
                        user = "admin",
                        password = "admin123",
                        host = "127.0.0.1",
                        port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute("""INSERT INTO public."agendar" ("id", "nome", "telefone") VALUES (1, 'Cliente 1', '021999887766') """)
conn.commit()
print("Inserção realizada com sucesso!"); conn.close()