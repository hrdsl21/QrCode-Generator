import sqlite3

class User:
    def __init__(self, db_file='qrkod.db'):
        self.db_file = db_file

    def create_connection(self):
        return sqlite3.connect(self.db_file)

    def createUser(self, username, hashed_password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO users (username, hashed_password) VALUES (?, ?)''',
                (username, hashed_password)
            )
            conn.commit()

    def checkUser(self, username, hashed_password):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''SELECT * FROM users WHERE username=? AND hashed_password=?''',
                (username, hashed_password)
            )
            user = cursor.fetchone()
            return user
        
        

