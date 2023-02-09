import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database = "service_db",
    user = "postgres",
    password = "1",
    host = "localhost",
    port = "5432"
)

cursor = conn.cursor()

@app.route('/login/',methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=\'{0}\' AND password=\'{1}\'".format(str(username), str(password)))
    records = list(cursor.fetchall())

    return render_template("account.html", full_name=records[0][1])