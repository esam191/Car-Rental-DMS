# Car-Rental-DMS

A car rental database management system built using Flask web framework. It provides an easy to use platform for customers to make reservations for renting cars by keeping track of the pick-up and drop-off locations. Features include reservation, car selection, and multiple views of data.

## Installation

Follow the instructions below to run the project on your local machine for development and testing purposes. 

- Clone project run in cmd as admin
```
git clone https://github.com/esam191/Car-Rental-DMS
```

### Prerequisites

Python and Flask need to be installed 

- Install [Python](https://www.python.org/downloads/release/python-390/)
```
pip install flask
```
- Install dependencies and run in cmd as admin in project folder

```
pip install -r requirements.txt
pip install wheel
pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl
pip install mysqlclient-1.3.13-cp27-cp27m-win_amd64.whl
python setup.py build
python setup.py install
```

### MySQL Database Setup

- Install [MySQL](https://dev.mysql.com/downloads/mysql/) Server, and include the MySQL Workbench in the installation
- Select the default developer installation
- When creating a user, select both the username and password as 'root'

| Username           | Password  |
| ------------- | ----- |
| root | root |

- When creating a database, create a schema and call it 'car-db'

| Schema      |     
| ------------- | 
| car-db | 

- Use the .sql scripts in the db/schema folder to create the tables and run the queries.

## Run Project

Go to the main folder and run the main.py file
```
python main.py
```

## Demo

Home Page

![Alt text](/main/static/img/home.JPG?raw=true "Home Page")

Sign Up Page

![Alt text](/main/static/img/signup.JPG?raw=true "Sign Up Page")

Login Page

![Alt text](/main/static/img/login.JPG?raw=true "Login Page")

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [MySQL Workbench](https://www.mysql.com/products/workbench/) - Used to construct the database

## Authors

* **Esam Uddin** - [esam191](https://github.com/esam191)

* **Ashwin Shanmugam** - [ashwin1609](https://github.com/ashwin1609)

* **Mihir Patel** - [mihikumar1212](https://github.com/mihikumar1212)


