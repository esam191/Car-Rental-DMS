from flask import Flask, render_template, request, url_for, redirect, session
from flask_mysqldb import MySQL
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'car_db'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        FirstName = request.form['FirstName']
        Password = request.form['Password']
        ll = [FirstName, Password]
        conn = mysql.connection.cursor()
        conn.execute("SELECT * FROM customer WHERE FirstName='" + FirstName + "' and Password='" + Password+"'")
        #conn.execute("""SELECT * FROM `customer` WHERE `FirstName` LIKE '{}' AND `Password` LIKE '{}'""".format(FirstName,Password))
        data = conn.fetchall()
        if len(data) > 0:
            session['Customer_ID'] = data[0][0]
            return redirect(url_for('reservation'))



        # if data is None:
        #     return "Invalid Username or Password"
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('Customer_ID')
    return redirect(url_for('home'))


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
    if 'Customer_ID' in session:
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
            return redirect(url_for('car'))
        return render_template('reservation.html')
    return redirect(url_for('login'))


@app.route('/payment', methods=['GET','POST'])
def payment():
    if request.method == "POST":
        CardHolderName = request.form['CardHolderName']
        PaymentType = request.form['PaymentType']
        Date = request.form['Date']
        CardNumber = request.form['CardNumber']
        cvv = request.form['cvv']
        TotalAmount = request.form['TotalAmount']
        LateFee = request.form['LateFee']

        pp = [CardHolderName,PaymentType,Date,CardNumber,cvv,TotalAmount,LateFee]
        conn = mysql.connection.cursor()
        conn.execute("INSERT INTO payment(PaymentType,LateFee,Date,TotalAmount,CardHolderName,CardNumber,cvv) values(%s,%s,%s,%s,%s,%s,%s)",(PaymentType,LateFee,Date,TotalAmount,CardHolderName,CardNumber,cvv))
        mysql.connection.commit()
        conn.close()
        return 'success'
    return render_template('payment.html')

@app.route('/car', methods=['GET','POST'])
def car():
    if request.method == "POST":
        LicensePlate = request.form['LicensePlate']
        Make = request.form['Make']
        Model = request.form['Model']
        Year = request.form['Year']
        SeatingCapacity = request.form['SeatingCapacity']
        Transmission = request.form['Transmission']
        Color = request.form['Color']
        cc = [LicensePlate,Make,Model,Year,SeatingCapacity,Transmission,Color]
        conn = mysql.connection.cursor()
        conn.execute("INSERT INTO car(LicensePlate,Make,Model,Year,SeatingCapacity,Transmission,Color) values(%s,%s,%s,%s,%s,%s,%s)",(LicensePlate,Make,Model,Year,SeatingCapacity,Transmission,Color))
        mysql.connection.commit()
        conn.close()
        return redirect(url_for('payment'))
    return render_template('cars.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
    
