from connect_sistema import connect


def tabelaUsuario():
    conn, cursor=connect()
    cursor.execute("""
    CREATE TABLE  usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login text,
    senha text
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def inserirUsuario(login,senha):
    conn, cursor = connect()
    cursor.execute("""
    INSERT INTO usuario(login,senha)
    values(?,?)
    """,(login,senha))
    conn.commit()
    cursor.close()
    conn.close()


def listarUsuarios():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM usuario;
    """)
    # Ele vai me devolver todos os
    # usuarios que encontrar na tabela usuario

    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


if __name__ == '__main__':
    # tabelaUsuario()
    # inserirUsuario("maria","1111")
    for usuario in listarUsuarios():
        print(usuario)


