# kanji-slayer-official

Kanji Slayer Discord Server: https://discord.gg/DYx34BBdsM

Kanji Slayer, the #1 Japanese learning RPG.

Project setup:
In VSCode, install Django and Django Template extensions.
Run these commands to get your virtual environment setup:
- pip install virtualenv
- virtualenv env
- source/env/bin activate 
The above command only works for Mac. If on windows, might need to Google.
You should see (env) in your terminal to know that you're in the virtual environment. 
- pip install requirements.txt
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

App file information:
- admin.py deals with the django admin, like when you need to make a model available in the admin panel. 
- apps.py you won't mess with this at all
- models.py is very important for databases
- tests.py is very important and used for writing tests
- views.py is handled for web requests and for returning responses. You use this a lot. 

Register new app:
- Go to settings.py and add the app to INSTALLED_APPS like 'game'

Models:
- Go to models.py and add this import:
- from django.db import models
- You write models using Python classes
- Whenever you create a model, you need to "python manage.py makemigrations" and then "python manage.py migrate"
- The migrations folder shows you what is being created in the database if you care.
- You can install the SQLite VSCode extension and CMD Shift P will let you run commands like db.sqlite3 file, you should have sqlite explorer in your explorer in VSCode where you can see all of your tables. Your new table should be at the very bottom. You can also use a database explorer application on your computer from Google. 
- models.CharField, models.IntegerField, models.BooleanField, models.ImageField, models.FileField
- You can create a tuple in your models, which you will see as SOURCE_CHOICES in the example screenshot. This seems to be common practice when you want to give options to be selected. The first value is the database text, and the second value is the display text. It sounds like to keep things less confusing, just use the same name for both. If you really wanted to conserve database data, then you could abbreviate the first one. 
- blank means empty string. 
- null means nothing is in the database. It's different than blank. 
<img width="511" alt="image" src="https://user-images.githubusercontent.com/41487993/201511883-322e67f7-d0d0-4bf8-85e0-0295acce8eb4.png">
- Foreign keys let you link a table to another table. Foreign keys always need to be passed the on_delete argument which tells Django how to handle what happens when you delete a key. You can do models.CASCADE that means if the other class is deleted, then it will delete both. models.SET_NULL means you will set value of foreign key to NULL, but you need to make sure null=TRUE is an arguement. You can do models.SET_DEFAULT if you have a default set. The simple way is models.CASCADE which means when the other class is deleted, then this one is deleted too. You need to be mindful when you do this. 
- In the below example, this foreign key lets you have every Lead with its own agent. You could create thousands of Leads in the database with their own agents. 
<img width="466" alt="image" src="https://user-images.githubusercontent.com/41487993/201512170-96f8dcbc-5fce-4e5c-a44d-ca8f89998e89.png">
- Django has a built in Users model which is very important and you will use it a lot. You will use this to tie users to your database models and for authentication. 

Model Managers:
<img width="690" alt="image" src="https://user-images.githubusercontent.com/41487993/201822809-81496cb5-2188-4960-923b-dbd620747ab3.png">

Querysets:
<img width="818" alt="image" src="https://user-images.githubusercontent.com/41487993/201822751-958ff8be-61b6-4b12-a893-054794d55144.png">
