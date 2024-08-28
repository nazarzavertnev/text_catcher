import sqlite3

def connection():
    return sqlite3.connect('database/example.db')

def sqler(query, conn):
    return conn.cursor().execute(query).fetchall() 

def execute(query):
    conn = connection()
    output = sqler(query, conn)
    conn.commit()
    conn.close()
    return output