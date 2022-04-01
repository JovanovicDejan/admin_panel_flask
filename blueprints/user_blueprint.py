from db.DB import DB

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

user_services = Blueprint("user_services", __name__)
mydb = DB.connect()


@user_services.route('/login', methods=['GET'])
def login_page():
    msg = ''
    return render_template('login.html', msg=msg)


@user_services.route('/login', methods=['POST'])
def login():
    cursor = mydb.cursor(prepared=True)
    msg = ''
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))

        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session['username'] = username

            return redirect(url_for('employee_services.index'))

        else:
            msg = 'Check your details, and try to login again!'
    return render_template('login.html', msg=msg)

