from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


# Main Work
@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)