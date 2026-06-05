import psycopg2

conn = psycopg2.connect(database ="postgresDB",
                        user = "admin",
                        password = "admin123",
                        host = "127.0.0.1",
                        port = "5432")
print("Conexão com Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute("""DELETE FROM public.agendar WHERE "id" = 1""")
conn.commit()
cont = cur.rowcount
print(cont, "Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!")
conn.close()