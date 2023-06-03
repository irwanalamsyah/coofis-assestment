up:
	python manage.py runserver

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

database-up:
	docker-compose -f docker-compose.local.yaml up -d

database-down:
	docker-compose -f docker-compose.local.yaml down

database-down-format:
	docker-compose -f docker-compose.local.yaml down -v
