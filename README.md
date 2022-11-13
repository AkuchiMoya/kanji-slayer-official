# kanji-slayer-official
Kanji Slayer, the #1 Japanese learning RPG.

Project setup:
In VSCode, install Django and Django Template extensions.
Run these commands to get your virtual environment setup:
- pip install virtualenv
- virtualenv env
- source/env/bin activate 
The above command only works for Mac. If on windows, might need to Google.
You should see (env) in your terminal to know that you're in the virtual environment. 
- pip install django
- pip freeze > requirements.txt
- django-admin startproject kanjislayerofficial . 
The above line only needs to be ran the first time you start your project. You need the period. 

To install on another computer, you should be able to run the following:
- pip install -r requirements.txt

.gitignore file needs to be created with a python gitignore template from Google. 

Run the server:
- cd into the django directory
- python manage.py runserver
- python manage.py migrate

Information about some of the base files in this project:
- __init__.py just makes it a module
- asgi.py lets you run the django server asynchronously. You likely won't ever make any changes to this. 
- wsgi.py similar but using a different interface.
- settings.py this is a hub of settings to configure things like database connections, where your templates are, etc. Need to hide the SECRET_KEY when you move to production. Also need to turn DEBUG to false in this file when you move to production. ALLOWED_HOSTS is where you add domain names when you host a  Django server in production. INSTALLED_APPS is where you add additional apps. MIDDLEWARE you probably won't touch. In TEMPLATES the most important part is DIRS, you would need to specify folders for you templates there. WSGI_APPLICATION this points to the wsgi file by default. DATABASES is where you set up your database configuration, so when you go to production and use Postgres, you will configure it here. By default it's pointing to the sqlite3 database. AUTH_PASSWORD_VALIDATORS checks for user's passwords for some common security issues. TIME_ZONE can be configured. STATIC_URL is just the URL that stores your static files for things like JS, images, etc. 
- manage.py you don't mess with much, but allows you to execute commands through the command line. 

