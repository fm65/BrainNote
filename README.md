# BrainNote

###### Introduction
L’objectif de ce projet est d’industrialiser l’application de votre choix. Industrialiser une application signifie que vous devez installer, paramétrer et optimiser des outils afin qu’une équipe de développement de toute taille puisse installer, développer et déployer l’application le plus facilement et le plus rapidement possible.

Ce projet porte sur une application Do To List.

# Fonctionnalités de l'application

###### Langage
- Front : HTML, CSS
- Back : Python
- SGBD : MySQL

###### Fonctionnalité
- inscription
- connexion
- ajouter une note
- modifier une note
- supprimer une note

###### Outils
- Flask
- Docker
- Git
- Default CI

# Versionning

###### Workflow
Basic flow

# Déploiement

###### Running the app locally
(You need to have installed MySQL locally to run the app)

###### With a virtualenv:

###### Create the virtualenv
$ mkvirtualenv flaskde
###### Install dependencies
$ pip install -r requirements.txt
###### Run the app
$ python3 flaskde/__init__.py
###### Now point your browser to http://127.0.0.1:5000

###### Without a virtualenv:

###### For Linux and Mac:
$ export FLASK_APP=flaskde
$ export FLASK_ENV=development
$ flask run

###### For Windows cmd, use set instead of export:
> set FLASK_APP=flasde
> set FLASK_ENV=development
> flask run

###### For Windows PowerShell, use $env: instead of export:
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
