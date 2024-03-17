from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask_mysqldb import MySQL


import os

load_dotenv()


app = Flask(__name__, static_url_path='/static')

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')


mysql = MySQL(app)

@app.route('/')
def index():
    print(os.getenv('MYSQL_HOST'))
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    email = request.form['email']
    password= request.form['password']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO users (email,password) VALUES(%s,%s)', (email, password))
    mysql.connection.commit()
    cur.close()


    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)