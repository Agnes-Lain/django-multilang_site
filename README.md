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

To run the project after clone from github run
```pip install -r requirements.txt```

If you want to run the app with prosgreSql server,you will need to create local database and replace the databaselink in multilang_sit/settings.py

to run the app locally , you can use eather
* python manage.py runserver
* python -m gunicorn multilang_site.asgi:application -k uvicorn.workers.UvicornWorker


