# README

## Project Intro ##
--------------------------------------------------------------------------------------------
This is an simple web application used the django framework, to manage articles. 
We can: 
* Check all the articles from the index with some content briefing;
* Read each article with details;
* Delete the article;
* Add new article

* Chat with OpenAI to get further information

The application support two language: English & French

## Project Setup ##
--------------------------------------------------------------------------------------------
First, clone the projet from github:
```gh repo clone Agnes-Lain/django-multilang_site```

Setup the local virtual environment:
```
  python3.10.6 -m venv env
  source env/bin/activate
```

To install all the package linked to the project
```
  pip install -r requirements.txt
```
Setup database
If you would like to run with sqlite3, you can simply uncomment the sqlite3 database setting and comment the posgreSql database, then run:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
If you want to run the app with prosgreSql server,you will need to create local database and replace the databaselink in multilang_sit/settings.py first before run the migration.

to run the app locally , you can use eather
```
python manage.py runserver
```
or

```
python -m gunicorn multilang_site.asgi:application -k uvicorn.workers.UvicornWorker
```

