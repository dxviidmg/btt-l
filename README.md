# P-MB

This repository has an products api

----

## Requirements

* Python 3.6.9+
* PostgreSQL 13.2+
* Virtual wrap
* requirements.txt

### PostgreSQL
To install PostgreSQL see https://www.postgresql.org/docs/9.5/static/installation.html

### Virtualenvwrapper

To install virtualenvwrapper see https://virtualenvwrapper.readthedocs.io/en/latest/

### requirements.txt
After cloning the project folder, in the root there is a file called requirements.txt. This file contains all the packages required to run the API. To install those packages, in your terminal run
`` shell
pip install -r requirements.txt
''

----

## Setting

At the root of the project, run
`` shell
python manage.py makemigrations
''
to generate the missing migrations. If none is created, that's fine. Now to apply those migrations, run
`` shell
python manage.py migrate
''

----

## Run server

Inside your virtual environment, using your settings and in the root folder, run
`` shell
python manage.py runserver
''
And the server will be active, to enter the Django REST Framework interface, in your web browser enter
''
http: // localhost: 8000
''