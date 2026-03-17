import sqlite3

def run_sql(query: str):
    conn = sqlite3.connect("data/sample.db")
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result