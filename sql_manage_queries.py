CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS
        CLIENTS(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT)'''

CHANGE_CLIENT_MESSAGE = '''UPDATE clients SET message = ? WHERE id = ?'''
  
CHANGE_CLIENT_PASS = '''UPDATE clients SET password = ? WHERE id = ?'''

REGISTER_USER = '''INSERT INTO CLIENTS (username, password) 
      VALUES (?, ?)'''

SELECT_USER = '''SELECT id, username, balance, message, email 
                FROM clients 
                WHERE username = ? AND password = ? LIMIT 1'''

SELECT_USER_EMAIL = '''SELECT email 
                FROM clients 
                WHERE username = ?
                LIMIT 1'''

