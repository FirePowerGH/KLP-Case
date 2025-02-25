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
        # Viser innloggingsskjema
        return render_template('login.html')
    
    name = request.form['name']
    password = request.form['password']

    # Sjekker om brukeren finnes i databasen
    if db.checkUser(name, password):
        session['name'] = name
        return redirect('/bank')
    else:
        flash('Feil brukernavn eller passord')
        return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # Viser registreringsskjema
        return render_template('register.html')
    
    name = request.form['name']
    password = request.form['password']

    # Registrerer ny bruker i databasen
    db.regUser(name, password)
    print(f'User {name} registered with password: {password}')

    return redirect('/login')

@app.route('/bank', methods=['GET', 'POST'])
def bank():
    if 'name' not in session:
        # Sender til innloggingssiden hvis brukeren ikke er logget inn
        return redirect('/login')
    else:
        navn = session['name']
        
        if request.method == 'GET':
            # Henter og viser saldo for brukeren
            saldo = db.getSaldo(navn)
            print(saldo)
            return render_template('bank.html', saldo=saldo)
        
        # Oppdaterer saldo basert på innskudd eller uttak
        verdi = int(request.form['verdi'])
        db.updateSaldo(navn, verdi)
        return redirect('/bank')

@app.route('/logout')
def logout():
    # Logger ut brukeren ved å fjerne 'name' fra sesjonen
    session.pop('name', None)
    return redirect('/')

if __name__ == '__main__':
    # Starter Flask-applikasjonen
    app.run(debug=True, host='0.0.0.0')