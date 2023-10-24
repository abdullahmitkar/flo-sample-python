import os
from flask import Flask, send_from_directory, render_template, redirect, request
import psycopg2
app = Flask(__name__)

DB_HOST = os.environ.get("your_database_host")
DB_PORT = os.environ.get("your_database_port")
DB_NAME = os.environ.get("your_database_name")
DB_USER = os.environ.get("your_database_user")
DB_PASSWORD = os.environ.get("your_database_password")

conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()

def create_login(passphrase, pin):
    # Convert passphrase to a single word and add pin to the end
    key = passphrase.replace(" ", "_") + pin

    # Insert a new record into the database
    cursor.execute("INSERT INTO users (key) VALUES (%s)", (key,))
    conn.commit()


def validate_login(passphrase, pin):
    # Convert passphrase to a single word and add pin to the end
    key = passphrase.replace(" ", "_") + pin

    # Search if the key exists in the database
    cursor.execute("SELECT * FROM users WHERE key = %s", (key,))
    user_data = cursor.fetchone()

    return user_data


port = int(os.environ.get("PORT", 5000))

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/validate_login', methods=['POST'])
def validate_login_route():
    passphrase = request.form.get('passphrase')
    pin = request.form.get('pin')

    user_data = validate_login(passphrase, pin)

    if user_data:
        return render_template('landing.html', user_data=user_data)
    else:
        return render_template('index.html', error_message="Record does not exist", passphrase=passphrase, pin=pin)


@app.route('/create_login', methods=['POST'])
def create_login_route():
    passphrase = request.form.get('passphrase')
    pin = request.form.get('pin')

    create_login(passphrase, pin)

    # After creating a login, redirect to the landing page
    user_data = validate_login(passphrase, pin)
    return render_template('landing.html', user_data=user_data)


@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)
