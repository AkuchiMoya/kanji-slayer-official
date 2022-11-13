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
