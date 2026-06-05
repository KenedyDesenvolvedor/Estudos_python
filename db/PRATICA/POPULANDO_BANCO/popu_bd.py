import sqlite3

def conectar_banco (nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao
def criar_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos(
                   Id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nome TEXT NOT NULL, 
                   Preço REAL NOT NULL,
                   Estoque INTEGER NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes(
                   Id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nome TEXT NOT NULL, 
                   Email TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos(
                   Id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Clientes_id INTEGER NOT NULL,
                   Produto_id INTEGER NOT NULL,
                   quantidade INTEGER NOT NULL,
                   data_pedido TEXT NOT NULL,
                   FOREIGN KEY (Clientes_id) REFERENCES Clientes(id),
                   FOREIGN KEY (Produto_id) REFERENCES Produto(id))''')
    
    conexao.commit()

    cursor.close()

def inserir_dados(conexao):
    cursor = conexao.cursor()

    produtos = [('Notebook', 2999.99, 10),
                ('Smartphone', 1999.99, 20),
                ('Tablet', 999.99, 30)]
    
    clientes = [('Alice', 'alice@linda.com'),
                ('Bob', 'quadrado@fenda-bikini.com'),
                ('Charlie', 'jr@hip-hop.com')]
    
    pedidos = [(1, 1, 2, '2023-06-15'),
               (2, 1, 2, '2023-06-16'),
               (3, 3, 3, '2023-06-17')]
    
    cursor.executemany('INSERT INTO Produtos (Nome, Preço, Estoque) VALUES (?, ?, ?)', produtos)

    cursor.executemany('INSERT INTO Clientes (Nome, Email) VALUES (?, ?)', clientes)

    cursor.executemany('''INSERT INTO Pedidos(
                       Clientes_id, Produto_id, Quantidade, Data_pedido)
                       VALUES (?, ?, ?, ?)''', pedidos)
    
    conexao.commit()
    cursor.close()

if __name__ == '__main__':
    conexao = conectar_banco('ecommerce.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    conexao.close()