from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/shops')
def shops():
    return render_template('shops.html')

@app.route('/kontakts')
def kontakts():
    return render_template('kontakts.html')


if __name__ == "__main__":
    app.run(debug = True)