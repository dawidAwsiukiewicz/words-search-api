words search API
===================
## Dependency

1. PIP (9.0.1)
2. Python (2.7)
3. Words Search Frontend
```
https://github.com/dawidAwsiukiewicz/words-search-frontend
```
4. sqlite3
5. redis-server (3.2)


## Instalation

1. Create virtuelenv in project dir and install requirements
```
$ virtualenv env
$ . env/bin/activate
(env)$ pip install -r requirements.txt
```

2. Create DB tables
```
(env)$ python manage.py migrate
```

## Start server

1. Run server
```
(env)$ python manage.py runserver
```

2. Run celery
```
(env)$ python manage.py celery worker
```
