

# Запуск контейнеров
docker-compose up - поднять контейнеры
docker-compose up --build --force-recreate - поднять и пересоздать
docker-compose up --build --force-recreate -d - поднять и демонизировать (боевой режим)
docker-compose down

# Посмотреть список всех контейнеров
docker ps -a  - Посмотреть список контейнеров
docker-compose ps - Посмотреть список контейнеров для данного docker-compose.yml

# Зайти внутрь контейнера
docker exec -it 0d7bbf3e2b67 sh (ctrl+p / ctrl+q выйти)

# Посмотреть логи демонизированного контейнера
docker logs django-wsgi --tail 100 --follow

# Выполнить команду внутри контейнера
docker exec django-wsgi python hello.py