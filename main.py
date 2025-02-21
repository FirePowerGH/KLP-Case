from flask import Flask, render_template, request, jsonify
from backend.api import *

app = Flask(__name__, template_folder='static/templates')

@app.route('/')
def index():
    createTable()
    return render_template('index.html')

@app.route('/registrer', methods=['GET', 'POST'])
def registrer():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True) 