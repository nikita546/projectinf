from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50), primary_key=True)
    discription


@app.route('/')
@app.route('/home')
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug = True)