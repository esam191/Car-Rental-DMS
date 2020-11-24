from flask import Flask, render_template, request, url_for, redirect, session,jsonify
from flask_mysqldb import MySQL
from flask_restful import Api
import os
#from app import app
# from flaskext.mysql import MySQL
import db.helper as connection

app = Flask(__name__)
#app = Api(app)
app.secret_key = os.urandom(24)
# db = connection.Connection()
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'car_db'
app.config['MYSQL_PORT'] = 3306
# mysql.init_app(app)


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
        data = conn.fetchall()
        if len(data) > 0:
            session['Customer_ID'] = data[0][0]
            return redirect(url_for('reservation'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('Customer_ID')
    return redirect(url_for('login'))

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

        pp = [CardHolderName, PaymentType, Date, CardNumber, cvv, TotalAmount, LateFee]
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


@app.route('/view')
def view():
    if request.method =="post":
        return redirect(url_for('view1'))
    return render_template('view.html')

@app.route('/view1')
def view1():
    conn = mysql.connection.cursor()
    result = conn.execute("SELECT reservation.Reservation_ID, customer.FirstName, payment.TotalAmount FROM "
                          "((reservation INNER JOIN customer ON customer.Customer_ID = reservation.CustomerID) "
                          "INNER JOIN payment ON payment.PaymentID = reservation.CustomerID) ")
    result = [dict(resid=col[0],fname=col[1],totamt=col[2]) for col in conn.fetchall()]
    return render_template('view1.html',result=result)

@app.route('/view2')
def view2():
    conn = mysql.connection.cursor()
    result2 = conn.execute("SELECT FirstName, LastName, COUNT(*) FROM customer, payment"
                           " WHERE TotalAmount > ALL ( SELECT TotalAmount FROM Payment WHERE LateFee = 5)GROUP BY FirstName, LastName")
    result2 = [dict(fname=col[0], lname=col[1], count=col[2]) for col in conn.fetchall()]
    return render_template('view2.html', result2=result2)

@app.route('/view3')
def view3():
    conn = mysql.connection.cursor()
    result3 = conn.execute("SELECT * FROM payment WHERE TotalAmount > ( SELECT avg(TotalAmount) FROM payment WHERE payment.PaymentType = PaymentType)")
    result3 = [dict(pid=col[0], ptype=col[1], lfee=col[2],date=col[3],totamt=col[4],cid=col[5],cname=col[6],cnum=col[7],cvv=col[8]) for col in conn.fetchall()]
    return render_template('view3.html', result3=result3)

@app.route('/view6')
def view6():
    conn = mysql.connection.cursor()
    result6 = conn.execute("SELECT customer.FirstName, reservation.Reservation_ID FROM customer "
                           "LEFT JOIN reservation ON customer.Customer_ID= reservation.customerID ORDER BY customer.FirstName")
    result6 = [dict(fname=col[0], resid=col[1]) for col in conn.fetchall()]
    return render_template('view6.html', result6=result6)

@app.route('/view7')
def view7():
    conn = mysql.connection.cursor()
    result7 = conn.execute("SELECT  Make, Model,Year,SeatingCapacity, Color FROM car WHERE SeatingCapacity BETWEEN 3 AND 4 GROUP BY Color")
    result7 = [dict(make=col[0], model=col[1],year=col[2],sc=col[3],color=col[4]) for col in conn.fetchall()]
    return render_template('view7.html', result7=result7)

@app.route('/view8')
def view8():
    conn = mysql.connection.cursor()
    result8 = conn.execute("SELECT * FROM payment WHERE TotalAmount > (SELECT Sum(LateFee) FROM payment)"
                           " OR TotalAmount >= (SELECT DealType From deals WHERE DealType > 30)")
    result8 =[dict(pid=col[0], ptype=col[1], lfee=col[2],date=col[3],totamt=col[4],cid=col[5],cname=col[6],cnum=col[7],cvv=col[8]) for col in conn.fetchall()]
    return render_template('view8.html', result8=result8)

@app.route('/view9')
def view9():
    conn = mysql.connection.cursor()
    result9 = conn.execute("SELECT FirstName,LastName FROM customer WHERE EXISTS (SELECT TotalAmount FROM payment"
                           " WHERE customer.Customer_ID = payment.Customer_ID AND TotalAmount < 100)")
    result9 = [dict(fname=col[0], lname=col[1]) for col in conn.fetchall()]
    return render_template('view9.html', result9=result9)

@app.route('/view10')
def view10():
    conn = mysql.connection.cursor()
    result10 = conn.execute("SELECT reservation.Reservation_ID,customer.FirstName, customer.LastName "
                            "FROM reservation RIGHT JOIN customer ON reservation.CustomerID = customer.Customer_ID")
    result10 = [dict(resid=col[0], fname=col[1],lname=col[2]) for col in conn.fetchall()]
    return render_template('view10.html', result10=result10)

# @app.route('/api/<id>', methods=['GET', 'POST'])
# def api(id):
#     customer_id = id
#     conn = mysql.connection
#     details = conn.get_details(customer_id)
#     return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
    # app.secret_key = "DATABASEPROJECT"
