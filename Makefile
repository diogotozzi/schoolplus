.PHONY: bash clean install migration start stop test lint

bash:
	docker exec -ti python /bin/ash

clean:
	find . -name '*.pyc' -exec sudo rm -f {} +
	find . -name '*.pyo' -exec sudo rm -f {} +
	find . -name '*~' -exec sudo rm -f {} +
	find . -name '__pycache__' -exec sudo rm -fr {} +

install: # Install the project, first run
	docker-compose up &

migration:
	docker exec database mysql -h localhost -u root -proot -e "CREATE SCHEMA IF NOT EXISTS schoolplus DEFAULT CHARACTER SET utf8mb4;"
	docker exec python python manage.py makemigrations api
	docker exec python python manage.py sqlmigrate api 0001
	docker exec python python manage.py migrate

start:
	docker-compose start

stop:
	docker-compose stop

test: clean lint
	docker exec python python manage.py test --no-input

lint:
	docker exec python flake8 schoolplus api --exclude api/migrations/
