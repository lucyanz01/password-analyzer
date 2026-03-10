from flask import Flask, send_from_directory
from routes import api 

app = Flask(__name__, static_folder='../public')

app.register_blueprint(api)

@app.route('/')
def index():
    return send_from_directory('../public', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)