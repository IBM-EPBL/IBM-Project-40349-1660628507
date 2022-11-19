from flask import Flask,render_template,request,session,url_for,redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
import re
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")
@app.route("/website_user")
def website_user():
    return render_template("website_user.html")
@app.route("/register")
def register_user():
    return render_template("register_user.html")

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = "d5fb8c4fa8bd46638dadc4e751e0d68d"

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='pythonlogin'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('website_user'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

#  http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
                # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register_user.html', msg=msg)

@app.route("/frame")
def frame():
    return render_template("frame.html")
@app.route("/product")
def product():
    return render_template("product.html")
@app.route("/content")
def content():
    return render_template("content.html")

# womens 
@app.route("/churidars")
def churidars_dress():
    return render_template("churidars.html")
@app.route("/sarees")
def sarees_dress():
    return render_template("sarees.html")
@app.route("/western")
def western_dress():
    return render_template("western.html")

# Mens 
@app.route("/shorts")
def shorts_dress():
    return render_template("shorts.html")
@app.route("/t-shirts")
def tshirts_dress():
    return render_template("t-shirts.html")
@app.route("/jeans")
def jeans_dress():
    return render_template("jeans.html")
@app.route("/jackets")
def jacketss_dress():
    return render_template("jackets.html")
@app.route("/Pants")
def pants_dress():
    return render_template("Pants.html")
@app.route("/coarts")
def coats_dress():
    return render_template("coarts.html")

# kids dress 
@app.route("/kids_frocks")
def kids_frocks_dress():
    return render_template("kids_frocks.html")
@app.route("/boys_shirts")
def boys_shirts_dress():
    return render_template("boys_shirts.html")
@app.route("/boys_pants")
def boys_pants_dress():
    return render_template("boys_pants.html")

if __name__=="__main__":
    app.run(debug=True)