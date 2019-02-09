from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Loading config.json as params
with open('config.json','r') as file:
    params = json.load(file)

# Main Work
@app.route('/')
def home():
    return render_template('index.html',webname=params['websitename'])

app.run(debug=True)