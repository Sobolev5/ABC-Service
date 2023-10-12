# Learning server for great things

Userful dev commands:
```
python manage.py runserver 0.0.0.0:1234 # run server 
python manage.py makemigrations
python manage.py migrate
```

Userful docker commands:
```
docker compose -f docker-compose.dev.yml up --build -d # run dev
docker compose -f docker-compose.prod.yml up --build -d # run dev
docker compose ps # show containers
docker compose down # stop containers
```

# CICD
ansible-playbook -i ./playbooks/inventory/hosts ./playbooks/push.yml 