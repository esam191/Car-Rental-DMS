from flask import Flask, render_template, request, url_for, redirect, session
from flask_mysqldb import MySQL

app = Flask(_name_)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'car_db'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

# @app.before_request
# def before_request():
#     g.user = None
#     if 'user' in session:
#         g.user = session['user']

# @app.route('/logout')
# def logout():
#     session.clear()
#     return render_template('home.html')

# @app.route('/',method=['GET','POST'])
# def index():
#     if 'user' in session:
#         FirstName = session['user']

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        FirstName = request.form['FirstName']
        Password = request.form['Password'].encode('utf-8')
        ll = [FirstName, Password]
        conn = mysql.connection.cursor()
        conn.execute("SELECT * FROM customer WHERE FirstName='" + FirstName + "' and Password='" + Password+"'")
        data = conn.fetchone()
        if data is None:
            return "Invalid Username or Password"
        else:
            return render_template('Reservation.html')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Email = request.form['Email']
        StreetAddress = request.form['StreetAddress']
        Province = request.form['Province']
        PostalCode = request.form['PostalCode']
        DriversID = request.form['DriversID']
        Age = request.form['Age']
        PhoneNo = request.form['PhoneNo']
        City = request.form['City']
        Password = request.form['Password']

        ss = [FirstName,LastName,Email,StreetAddress,Province,PostalCode,DriversID,Age,PhoneNo,City,Password]
        conn = mysql.connection.cursor()
        conn.execute("INSERT INTO customer(FirstName,LastName,Age,PhoneNo,Email,StreetAddress,City,Province,PostalCode,DriversID,Password)"
                     " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(FirstName,LastName,Age,PhoneNo,Email,StreetAddress,City,Province,PostalCode,DriversID, Password))
        mysql.connection.commit()
        conn.close()
        #return 'success'
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/reservation', methods=['GET','POST'])
def reservation():
    if request.method == "POST":
        City = request.form['City']
        #D_Address = request.form['D_Address']
        ReserveFrom = request.form['ReserveFrom']
        ReserveTo = request.form['ReserveTo']
        P_Address = request.form['P_Address']
        Province = request.form['Province']
        Postal_Code = request.form['Postal_Code']
        Insurance = request.form['Insurance']

       # age = request.form['age']
        rr = [ReserveFrom,ReserveTo,Insurance,City,P_Address,Province,Postal_Code]
        conn = mysql.connection.cursor()
        conn.execute("INSERT INTO reservation(ReserveTo,ReserveFrom,Insurance) values(%s,%s,%s)",(ReserveTo,ReserveFrom,Insurance))
        conn.execute("INSERT INTO pick_up(City,P_Address,Province,Postal_Code) values(%s,%s,%s,%s)",(City,P_Address,Province,Postal_Code))
        mysql.connection.commit()
        conn.close()
        return 'success'
    return render_template('Reservation.html')

if _name_ == '_main_':
    # app.secret_key = "DATABASEPROJECT"
    app.run(debug=True, host='localhost')