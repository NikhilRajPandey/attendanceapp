from flask import Flask , render_template, session, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.secret_key = 'Very Secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////./databases/root.db'
db = SQLAlchemy(app)

# Classes or Table for Website
class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Class %r>' % self.classname

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(80), nullable=False)
    classname = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Student %r>' % self.studentname
    
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(80), nullable=False)
    classname = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Student %r>' % self.date

# Loading config.json as params
with open('config.json','r') as file:
    params = json.load(file)

# Checking User in session or not
def check_session():
    if 'user' in session and 'pass' in session:
        if session['user'] == params['username'] and session['pass'] == params['password']:
            return True
        return False
    return False


# Main Work
@app.route('/')
def home():
    if check_session():
        return render_template('admin.html',webname=params['websitename'])
    return render_template('index.html',webname=params['websitename'])

# Login Route
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usrname = request.form.get('username')
        paswrd =  request.form.get('password')

        if usrname == params['username'] and paswrd == params['password']:
            session['user'] = usrname
            session['pass'] = paswrd
            flash('You are succesfuly Login','success')
            return redirect('/')
        else:
            flash('Wrong details','danger')
            return redirect('/')
            
    return redirect('/')

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user',None)
    session.pop('pass',None)
    return redirect('/')

app.run(debug=True)