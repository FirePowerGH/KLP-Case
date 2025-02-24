from flask import Flask, render_template, request, jsonify
from backend.api import *

app = Flask(__name__, template_folder='static/templates')

@app.route('/')
def index():
    createTable()
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def registrer():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    return 'Hai'

@app.route('/bank', methods=['GET', 'POST'])
def bank():
    return render_template('bank.html')

if __name__ == '__main__':
    app.run(debug=True) 