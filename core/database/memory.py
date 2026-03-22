import sqlite3

def init_memory():
    conn = sqlite3.connect('core/database/benalal_vault.db')
    cursor = conn.cursor()
    # جدول المنتجات
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory 
                      (id INTEGER PRIMARY KEY, name TEXT, price TEXT, platform TEXT)''')
    # جدول الأرباح
    cursor.execute('''CREATE TABLE IF NOT EXISTS finances 
                      (id INTEGER PRIMARY KEY, total_profit REAL)''')
    conn.commit()
    conn.close()

def save_product(name, price, platform):
    conn = sqlite3.connect('core/database/benalal_vault.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, price, platform) VALUES (?, ?, ?)", (name, price, platform))
    conn.commit()
    conn.close()
