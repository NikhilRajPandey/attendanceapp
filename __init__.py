from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Main Work
@app.route('/')
def home():
    return render_template('index.html')

app.run()