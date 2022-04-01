import os
import flask
from flask import Blueprint, jsonify, redirect, render_template, session, url_for
from flask import request
from db.DB import DB
from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, url_for)
from models.employee import Employee
from upload import upload_file, UPLOAD_FOLDER 
from functools import wraps


employee_services = Blueprint("employee_services", __name__)
# mydb = DB.mydb
mydb = DB.connect()

def login_required(fnc):
    @wraps(fnc)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            return fnc(*args, **kwargs)
        else:
            return redirect(url_for('user_services.login_page'))
    return wrap


@employee_services.route('/', methods=['GET'])
@login_required
def index():
    cursor = mydb.cursor(prepared=True)
    emp = "SELECT * FROM employee ORDER BY employee.order ASC"
    cursor.execute(emp) 
    row = cursor.fetchall()
    n = len(row)

    for i in range(n):
        row[i] = clear_bytearray(row[i])
    list_employees = []
    for emp in row:
        id = emp[0]
        firstName = emp[1]
        lastName = emp[2]
        order = emp[3]
        linkedIn = emp[4]
        xing = emp[5]
        role = emp[6]
        email = emp[7]
        photoUrl = emp[8]
        employee = Employee(id,firstName,lastName,order,linkedIn,xing,role,email,photoUrl)
        list_employees.append(employee)
    return render_template('index.html', list_employees = list_employees)

@employee_services.route('/delete/<email>', methods=['POST'])
@login_required
def delete_employee(email):
    cursor = mydb.cursor(prepared=True)
    q = '''DELETE FROM employee WHERE email=%s'''
    parameters = (email,)
    cursor.execute(q,parameters)
    mydb.commit()
    flash('Employee Removed Successfully')
    return redirect(url_for('employee_services.index'))



@employee_services.route("/register", methods=["GET"])
@login_required
def register():
    return render_template("register.html")


@employee_services.route("/register", methods=["POST"])
@login_required
def registration():
    cursor = mydb.cursor(prepared=True)
    data = request.form
    email = data["email"]
    cursor.execute("SELECT * FROM employee  WHERE email=%s", (email,))
    employee = cursor.fetchone()
    if employee != None:
        return render_template("register.html", email_error="This email is arleady registred")

    cursor = mydb.cursor(prepared=True)
    q = "INSERT INTO employee VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
    photoUrl = upload_file()
    parameters = (
        data["firstName"],
        data["lastName"],
        data["order"],
        data["linkedIn"],
        data["xing"],
        data["role"],
        data["email"],
        photoUrl,
    )
    cursor.execute(q, parameters)
    mydb.commit()

    return redirect(url_for("employee_services.index"))


@employee_services.route("/update/<email>", methods=["GET"])
@login_required
def upd(email):
    cursor = mydb.cursor(prepared=True)
    cursor.execute("SELECT * FROM employee WHERE email=%s", (email,))
    row = cursor.fetchone()

    if row == None:
        return redirect(url_for("employe.services.employees"))

    row = clear_bytearray(row)
    id = row[0]
    firstName = row[1]
    lastName = row[2]
    order = row[3]
    linkedIn = row[4]
    xing = row[5]
    role = row[6]
    email = row[7]
    photoUrl = row[8]
    

    employee = Employee(id, firstName, lastName, order, linkedIn, xing, role, email, photoUrl)

    return render_template("update.html", employee=employee)


@employee_services.route("/update/<email>", methods=["POST"])
@login_required
def update(email):
    data = request.form
    cursor = mydb.cursor(prepared=True)
    cursor.execute("SELECT * FROM employee WHERE email=%s", (email,))
    row = cursor.fetchone()
    row = clear_bytearray(row)
    q = """UPDATE `employee` SET `firstName`= %s,`lastName`=%s,`order`= %s,`linkedIn`=%s,`xing`=%s,`role`=%s,`photoUrl`=%s WHERE email=%s"""
    photo = row[8]
    file = request.files['photoUrl']
    if not file:
        photoUrl = photo
    else:
        photoUrl = upload_file()
        if photoUrl != photo:
            os.remove('static' + photo)
    parameters = (
            data["firstName"],
            data["lastName"],
            data["order"],
            data["linkedIn"],
            data["xing"],
            data["role"],
            photoUrl,
            email)
    DB.update_query(q,parameters)
    return redirect(url_for('employee_services.index'))


@employee_services.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('user_services.login_page'))

def clear_bytearray(rows):
    rows = list(rows)
    n = len(rows)
    for i in range(n):
        if isinstance(rows[i], bytearray):
            rows[i] = rows[i].decode()

    return rows
