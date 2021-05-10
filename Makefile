.PHONY: bash clean install migrate start stop test lint

bash:
	docker exec -ti python /bin/ash

clean:
	find . -name '*.pyc' -exec sudo rm -f {} +
	find . -name '*.pyo' -exec sudo rm -f {} +
	find . -name '*~' -exec sudo rm -f {} +
	find . -name '__pycache__' -exec sudo rm -fr {} +

install: # Install the project
	docker-compose up &

migrate:
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
	docker exec python flake8 schoolplus api
