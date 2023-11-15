from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # appの設定
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # DBの設定
    db.init_app(app)
    from flask_app import models

    # Blueprintの登録
    from flask_app.views.stocks import stocks_bp
    app.register_blueprint(stocks_bp)


    return app