from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os
import re

app = Flask(__name__, instance_relative_config=True)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'dev'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'eu-cdbr-west-02.cleardb.net'
app.config['MYSQL_USER'] = 'be63f11518eaeb'
app.config['MYSQL_PASSWORD'] = 'eb3aa71d'
app.config['MYSQL_DB'] = 'heroku_5ea03c56b0e78a0'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and \
            'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if user exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s', (username,))
        # Fetch one record and return result
        user = cursor.fetchone()
        # check user
        if user is None:
            msg = 'Incorrect authentication credentials!'
        elif not check_password_hash(user['password'], password):
            msg = 'Incorrect password!'
        # If user exists in users table in out database
        if msg is '':
            # Create session data, we can access this data in other routes
            session.clear()
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            # Redirect to home page
            return redirect(url_for('home'))
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" 
    #POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and \
            'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Check if user exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s', (username,))
        user = cursor.fetchone()
        # If user exists show error and validation checks
        if user:
            msg = 'User already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # User doesnt exists and the form data is valid, 
            #now insert new user into users table
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s)', 
                    (username,generate_password_hash(password), email))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)



@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # Check if task exists in MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM task WHERE author_id = %s', (session['id'],))
        tasks = cursor.fetchall()
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'], tasks=tasks)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the user info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE id = %s', [session['id']])
        user = cursor.fetchone()
        # Show the profile page with user info
        return render_template('profile.html', user=user)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/task', methods=['POST'])
def add_task():
    # Check if user is loggedin
    if 'loggedin' in session:
        # Check if "content"  POST requests exist (task add)
        if request.method == 'POST' and 'content' in request.form:
            # Create variables for easy access
            content = request.form['content']
            # Check if task exists in MySQL
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            if not content:
                return redirect('/home')

            cursor.execute(
                'INSERT INTO task (content, done, author_id)'
                'VALUES (%s, 0, %s)', 
                (content, session['id'])
            )
            mysql.connection.commit()
            return redirect('/home')



@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    # Check if task exists in MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if not cursor:
        return redirect('/home')
    cursor.execute('DELETE FROM task WHERE id = %s', (task_id,))
    mysql.connection.commit()
    return redirect('/home')



@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    # Check if task exists in MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT done FROM task WHERE id = %s', (task_id,))
    cursor_dict = cursor.fetchone()
    #if not cursor_dict['done']:
    #    return redirect('/home')
    if cursor_dict['done']:
        cursor.execute('UPDATE task SET done = %s WHERE id = %s', (False, task_id))
    else:
        cursor.execute('UPDATE task SET done = %s WHERE id = %s', (True, task_id))
    mysql.connection.commit()
    return redirect('/home')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
