from flask import Flask, Blueprint, render_template, request, flash, redirect
from controllers.registerControllers import Register


register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def RegisterPage():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            # Utwórz instancję kontrolera rejestracji
            registration_controller = Register()

            # Wywołaj metodę rejestracji i uzyskaj wynik
            result = registration_controller.register_user(username, password)

            if "udana" in result:
                flash(result, 'success')
                return redirect('/')  # Przekieruj użytkownika na stronę logowania po udanej rejestracji
            else:
                flash(result, 'error')
        return render_template('register.html') 
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')
        return render_template('error.html') 
    