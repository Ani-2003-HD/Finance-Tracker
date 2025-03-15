from flask import Flask
from routes import app as routes_app

app = Flask(__name__)
app.secret_key = "Aniruddha"

app.register_blueprint(routes_app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
