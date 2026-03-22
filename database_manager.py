import sqlite3

def init_db():
    conn = sqlite3.connect('benalal_vault.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS confirmations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT,
            project_type TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_all_confirmations():
    conn = sqlite3.connect('benalal_vault.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM confirmations ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
    print("✅ Database System: Active")
