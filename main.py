from flask import Flask
from routes.loginPage import login_bp
from routes.registerPage import register_bp
from routes.qrcodeGen import qrcodeGen_bp , qrcodeDownload_bp


app = Flask(__name__, template_folder='view')
app.secret_key = '98765443123123456678900'

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(qrcodeGen_bp)
app.register_blueprint(qrcodeDownload_bp)

if __name__ == '__main__':
    app.run(debug=True)
