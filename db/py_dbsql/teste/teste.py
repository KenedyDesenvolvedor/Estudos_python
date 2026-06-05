import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="kenedy",
        password="Kenydev123",
        database="meu_banco"
    )
    print("✅ Conectou com sucesso!")
except Exception as e:
    print("❌ Erro:", e)