from flask import Blueprint, render_template, request, redirect, flash
from controllers.loginControllers import Login 
from controllers.qrkodControllers import GeneratorQrKod
login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def LoginPage():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']


            login_controller = Login()
            result = login_controller.login_user(username, password)


            if "Zalogowano pomyślnie" in result:
                flash("Udało sie zalgować ")
                clear = GeneratorQrKod()
                clear.clear_folder()
                return redirect('qrkodgenerator') 
            
            
            elif "Użytkownik nie istnieje" in result:
                flash("Użytkownik nie istnieje. Jeśli chcesz utworzyć konto, przejdź do strony rejestracji.", 'info')


        return render_template('index.html')
    except Exception as e:
        # Handle the exception here, you can log it or display a generic error message
        flash(f"An error occurred: {str(e)}", 'error')
        return render_template('error.html')