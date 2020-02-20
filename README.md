# BrainNote

Une DoToList en python avec Flask.

Fonction : connexion, ajouter, modifier et supprimer des catégories ou des notes.

# Running the app locally
(You need to have installed MySQL locally to run the app)

# With a virtualenv:

# Create the virtualenv
$ mkvirtualenv flaskde
# Install dependencies
$ pip install -r requirements.txt
# Run the app
$ python3 flaskde/__init__.py
# Now point your browser to http://127.0.0.1:5000

# Without a virtualenv:

# For Linux and Mac:
$ export FLASK_APP=flaskde
$ export FLASK_ENV=development
$ flask run

# For Windows cmd, use set instead of export:
> set FLASK_APP=flasde
> set FLASK_ENV=development
> flask run

# For Windows PowerShell, use $env: instead of export:
> $env:FLASK_APP = "flaskde"
> $env:FLASK_ENV = "development"
> flask run

You’ll see output similar to this:

* Serving Flask app "flaskde"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761

Visit http://127.0.0.1:5000 in a browser and you should see the login page. Congratulations, you’re now running your Flaskde web application!
