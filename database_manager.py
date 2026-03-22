import sqlite3
import os

def init_db():
    conn = sqlite3.connect('benalal_vault.db')
    cursor = conn.cursor()
    # إنشاء جدول الطلبات المؤكدة
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
    print("✅ BenalalAI: Database 'benalal_vault.db' is Ready.")

if __name__ == "__main__":
    init_db()
