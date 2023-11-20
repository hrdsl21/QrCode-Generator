import sqlite3


conn = sqlite3.connect('qrkod.db')
cursor = conn.cursor()

# Tabela użytkowników
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
)
''')

# Tabela przechowująca QR codes
cursor.execute('''
CREATE TABLE IF NOT EXISTS qr_codes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    qr_data TEXT,
    image BLOB,
    pdf BLOB,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

conn.commit()
conn.close()