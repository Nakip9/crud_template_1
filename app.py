from flask import Flask, request, redirect, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
Scss(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Mytask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.id}'

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)