from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'myBase'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # obtener datos
        usuario = request.form['usuario']
        correo = request.form['correo']
        password = request.form['password'].encode('utf-8')
        hash_pass = bcrypt.hashpw(password, bcrypt.gensalt())

        print(usuario)

        db = mysql.connection.cursor()
        db.execute('INSERT INTO users(correo, usuario, password) VALUES (%s, %s, %s)',
                   (correo, usuario, hash_pass))
        mysql.connection.commit()

        return "Recibido"

    else:
        return render_template("register.html")


if (__name__ == "__main__"):
    app.run(debug=True)
