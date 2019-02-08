from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)