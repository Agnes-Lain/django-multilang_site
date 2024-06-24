# README

## Project Intro ##
--------------------------------------------------------------------------------------------

To run the project after clone from github run
pip install -r requirements.txt

You can run with local db.sqlite3 for easy config.
If you want to run the app with prosgreSql server,you will need to create local database and replace the databaselink in multilang_sit/settings.py

to run the app, you can use eather
* python manage.py runserver
* python -m gunicorn multilang_site.asgi:application -k uvicorn.workers.UvicornWorker

## Super Admin access ##
* username: admin
* password: Admin12345
