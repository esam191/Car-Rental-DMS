from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'car_db'
#app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method =="POST":
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
        ss = [FirstName,LastName,Email,StreetAddress,Province,PostalCode,DriversID,Age,PhoneNo,City]
        conn = mysql.connection.cursor()
        conn.execute("INSERT INTO customer(FirstName,LastName,Age,PhoneNo,Email,StreetAddress,City,Province,PostalCode,DriversID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(FirstName,LastName,Age,PhoneNo,Email,StreetAddress,City,Province,PostalCode,DriversID))
        mysql.connection.commit()
        conn.close()
        return 'success'
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
        #conn.execute("INSERT INTO drop_off(D_Address) values(%s)",(D_Address))
        mysql.connection.commit()
        conn.close()
        return 'success'
    return render_template('Reservation.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
