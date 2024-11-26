import sqlite3 as sq

def connect():
    conn=sq.connect("sistema.db")
    cursor=conn.cursor()
    return conn, cursor