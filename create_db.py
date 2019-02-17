import sqlite3


def createtable():
    conn = sqlite3.connect('todo.db')
    sql_query = """
    CREATE TABLE IF NOT EXISTS Todo (
    id INTEGER PRIMARY KEY,
    text1 TEXT,
    priority TEXT,
    complete boolean
    );
    """
    conn.execute(sql_query)
    conn.close()
