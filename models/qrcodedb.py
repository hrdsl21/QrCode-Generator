import sqlite3

class Qrcodedb():
    def __init__(self, db_file='qrkod.db'):
        self.db_file = db_file
        
    def create_conn(self):
        return sqlite3.connect(self.db_file)

    def createQrkod(self, user_id, qr_data, image_data, pdf_data):
        with self.create_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO qr_codes (user_id, qr_data, image, pdf) VALUES (?, ?, ?, ?)
                ''',
                (user_id, qr_data, image_data, pdf_data)
            )
            conn.commit()
    

    def showQrkod(self, user_id):
        with self.create_conn() as conn:
            cursor = conn.cursor()
        cursor.execute(
            '''SELECT * FROM qr_codes WHERE user_id=?''',(user_id)
        )
        qr_codes = cursor.fetchall()
        return qr_codes
        

    # def getQrkodData(self, user_id):
    #     self.cursor.execute(
    #         '''
    #         SELECT image, pdf FROM qr_codes WHERE user_id = ?
    #         ''',
    #         (user_id)
    #     )
    #     qr_code_data = self.cursor.fetchall()
    #     return qr_code_data if qr_code_data else (None, None)

    # def close(self):
    #     self.conn.close()