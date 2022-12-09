# Learning server for great things

Userful dev commands:
```
python manage.py runserver 0.0.0.0:1234 # run server 
python manage.py makemigrations
python manage.py migrate

export $(cat .env | xargs) && source interface/env/bin/activate && python interface/manage.py runserver 0.0.0.0:1234 # run server 
export $(cat .env | xargs) && source interface/env/bin/activate && python interface/manage.py makemigrations
export $(cat .env | xargs) && source interface/env/bin/activate && python interface/manage.py migrate
```

Userful docker commands:
```
docker-compose up --build -d # run stack
docker-compose ps # show containers
docker-compose down # stop stack
```