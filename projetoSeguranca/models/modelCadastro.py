from connect_sistema import connect

def criarTabelaCadastro():
    conn, cursor = connect()
    cursor.execute("""
    CREATE TABLE  produto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome text,
    marca text,
    valor real
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def insertProduto(nome:str, marca:str, valor:float):
    conn, cursor = connect()
    cursor.execute("""
    INSERT INTO produto(nome, marca,valor)
    values(?,?,?);""",(nome,marca,valor))
    conn.commit()
    cursor.close()
    conn.close()
    print("cadastrado com sucesso")


def listarProdutos():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM produto;
    """)
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista

if __name__ == '__main__':
    criarTabelaCadastro()