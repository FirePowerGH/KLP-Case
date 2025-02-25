from flask import Flask, render_template, request, redirect, session, flash, get_flashed_messages
from backend.api import Database

app = Flask(__name__, template_folder='static/templates')
app.config['SECRET_KEY'] = "vwledigsceretkey"

db = Database()
db.createTable()

@app.route('/')
def index():
    db.createTable()
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    name = request.form['name']
    password = request.form['password']

    if db.checkUser(name, password):
        session['name'] = name
        return redirect('/bank')
    else:
        flash('Feil brukernavn eller passord')
        return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    name = request.form['name']
    password = request.form['password']

    db.regUser(name, password)
    print(f'User {name} registered with password: {password}')

    return redirect('/login')

@app.route('/bank', methods=['GET', 'POST'])
def bank():
    if request.method == 'GET':
        navn = session['name']
        saldo = db.getSaldo(navn)
        print(saldo)
        return render_template('bank.html', saldo=saldo)

@app.route('/transaksjon', methods=['POST'])
def transaksjon():
    navn = session['name']
    verdi = int(request.form['verdi'])
    db.updateSaldo(navn, verdi)
    return redirect('/bank')

@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 