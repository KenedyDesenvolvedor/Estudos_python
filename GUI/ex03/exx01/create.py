import psycopg2 

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgresDB',
    user = 'admin',
    password = 'admin123'
)

cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT  EXISTS public."AGENDA"(
id integer NOT NULL,
nome text COLLATE pg_catalog."default" NOT NULL,
telefone char(12) COLLATE pg_catalog."default" NOT NULL)

               TABLESPACE pg_default;
               ALTER TABLE public. "AGENDA"
                OWNER to admin; 
               """)

cursor.execute("""
INSERT INTO public."AGENDA"(id, nome, telefone)
               VALUES (1, 'teste 1', '02199998888');
               """)

cursor.execute("""
INSERT INTO public. "AGENDA" (id, nome, telefone)
               VALUES (2, 'teste 2', '02188887777');
                """)

conn.commit()

cursor.execute("""
SELECT id, nome, telefone FROM public."AGENDA";
               """)

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")

conn.commit()
cursor.close()
conn.close( )