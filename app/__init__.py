from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

from app.controllers.controllerMain import main
from app.controllers.controllerCars import cars
from app.controllers.controllerUsers import users

app.register_blueprint(main)
app.register_blueprint(cars)
app.register_blueprint(users)

#if __name__ == '__main__':
app.run(debug=True)


