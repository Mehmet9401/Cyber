import sqlite3

def init_db():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            username TEXT, 
            password TEXT, 
            role TEXT
        )
    ''')
    cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'adminpass', 'admin')")
    cursor.execute("INSERT INTO users (username, password, role) VALUES ('user', 'userpass', 'user')")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()

