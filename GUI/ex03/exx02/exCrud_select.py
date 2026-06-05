import psycopg2

conn = psycopg2.connect(database ="postgresDB",
                        user = "admin",
                        password = "admin123",
                        host = "127.0.0.1",
                        port = "5432")
print("Conexão com Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute(""" SELECT * FROM public.agendar WHERE "id" = 1""")
registro = cur.fetchone()
print(registro)
conn.commit()
print("Seleção realizada com sucesso!");
conn.close()