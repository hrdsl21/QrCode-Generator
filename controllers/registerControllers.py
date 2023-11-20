from models.user import User
import hashlib

class Register:
    def register_user(self, username, password):
        
        password = password.encode('utf-8')
        hashed_password = hashlib.sha256(password).hexdigest()

        user = User()
        existing_user = user.checkUser(username, hashed_password)  

        if existing_user:
            return "Użytkownik o podanym loginie już istnieje"
        else:
            user.createUser(username, hashed_password) 
            return "Rejestracja udana. Możesz teraz się zalogować."
