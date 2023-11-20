from models.user import User
import hashlib

class Login:
    def login_user(self, username, password):
        # Haszowanie hasła wprowadzonego przez użytkownika
        hashed_input_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Pobieranie zahashowanego hasła z bazy danych
        user = User()
        stored_user = user.checkUser(username, hashed_input_password)

        if stored_user:
            stored_username = stored_user[1]
            stored_password = stored_user[2]  
            # Porównanie zahashowanego hasła wprowadzonego przez użytkownika z hasłem zapisanym w bazie danych
            if username == stored_username and hashed_input_password == stored_password:
                return "Zalogowano pomyślnie"  
        else:
            return "Użytkownik nie istnieje"  