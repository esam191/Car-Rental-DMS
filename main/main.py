from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/reservation')
def reservation():
    return render_template('Reservation.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
