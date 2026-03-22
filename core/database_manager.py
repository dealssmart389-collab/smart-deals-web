import sqlite3

def save_deal(source, details):
    conn = sqlite3.connect('core/benalal_vault.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS deals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            details TEXT,
            time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('INSERT INTO deals (source, details) VALUES (?, ?)', (source, details))
    conn.commit()
    conn.close()
    print(f"✅ تم حفظ صيد الرادار من {source} في الخزنة.")
