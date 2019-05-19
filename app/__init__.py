import os
from flask import Flask
from flask_mongoengine import MongoEngine


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    db = MongoEngine()

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config['MONGODB_SETTINGS'] = {
            'db': 'bookstore_app',
            'host': 'localhost',
            'port': 27017
        }
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import order, inventory, book, customer, bookstore, auth
    app.register_blueprint(auth.bp)
    app.register_blueprint(bookstore.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(inventory.bp)
    app.register_blueprint(book.bp)
    app.register_blueprint(customer.bp)

    db.init_app(app)

    return app
