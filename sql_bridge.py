import sqlite3

def execute_query(db_path, sql):
    # Tutaj implementujesz realne połączenie, 
    # ale dla studentów zostawiasz bezpieczny przykład z sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()