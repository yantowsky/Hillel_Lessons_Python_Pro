Як запускати

1. Переконайся, що .env файл створений із потрібними змінними:

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True


2. Підняти контейнери:

docker-compose up -d


3. Виконати міграції:

docker-compose exec web python manage.py migrate


4. Створити суперкористувача:

docker-compose exec web python manage.py createsuperuser


Django доступний на: http://127.0.0.1:8000