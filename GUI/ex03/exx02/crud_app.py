import psycopg2
from psycopg2 import Error

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            database = 'postgresDB',
            user = 'admin',
            password = 'admin123'
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados PostgreSQL: {e}")
        return None

def create_contact(nome, telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO public."AGENDA" (nome, telefone)
            VALUES (%s, %s) RETURNING id;""", (nome, telefone))
            contact_id = cursor.fetchone()[0]
            conn.commit()
            print(f"Contato adicionado com ID: {contact_id}")
        except Error as e:
            print(f"Erro ao adicionar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def read_contacts():
    conn = connect_to_db()
    if conn is not None:
        cursor = conn. cursor()
        try:
            cursor.execute("""
SELECT id, nome, telefone FROM public."AGENDA"; """)
            contacts = cursor.fetchall()
            for contact in contacts:
                print(f"ID {contact[0]}, Nome: {contact[1]}, Telefone: {contact[2]}")
        except Error as e:
            print(f"Erro ao ler contatos: {e}")
        finally:
            cursor.close()
            conn.close()

def update_contact(contact_id, novo_nome, novo_telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE public."AGENDA"
                           SET nome = %s, telefone = %s
                           WHERE id = %s;
                           """,(novo_nome, novo_telefone, contact_id))
            conn.commit()
            print("Contato atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_contact(contact_id):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
DELETE FROM public."AGENDA" WHERE id = %s; """, (contact_id,))
            conn.commit()
            print("Contato deletado com sucesso.")
        except Error as e:
            print(f"Erro ao deletar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def main():
    while True:
        print("\nMENU:")
        print("1. Adicionar novo contato \n2. Mostrar todos os contatos \n3. Atualizar um conatato \n4. Deletar um contato \n5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            nome = input("Digite o Nome: ")
            telefone = input("Digite o Telefone: ")
            create_contact(nome, telefone)
        elif choice == '2':
            read_contacts()
        elif choice == '3':
            contact_id = int(input("Digite o ID do contato para atualizar: "))
            novo_nome = input("Novo Nome: ")
            novo_telefone = input("Novo Telefone: ")
            update_contact(contact_id, novo_nome, novo_telefone)
        elif choice == '4':
            contact_id = int(input("Digite o ID do contato para deletar: "))
            delete_contact(contact_id)
        elif choice == '5':
            print("Saindo ...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()