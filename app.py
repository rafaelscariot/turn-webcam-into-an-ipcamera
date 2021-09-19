from flask import Flask
from controllers import routes

app = Flask(__name__)
app.register_blueprint(routes.get_blueprint())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
