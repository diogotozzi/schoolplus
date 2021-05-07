FROM python:3.9.5-alpine3.13

ENV PYTHONUNBUFFERED=1

# Django environment variables
ENV SECRET_KEY="eKjXBzmyCYhNjZBqpps8gUuHEWKYPJ4BsNkdAvUB9wSXce2ddNLaa24xrs8VrSLYxmQXBhHj"
ENV DATABASE_HOST="database"
ENV DATABASE_NAME="schoolplus"
ENV DATABASE_USER="root"
ENV DATABASE_PASSWORD="root"
ENV DATABASE_PORT="3306"

RUN apk update && apk add --no-cache \
    mysql-client \
    mariadb-dev \
    build-base \
    linux-headers

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["uwsgi", "--socket", ":9000", "--module", "schoolplus.wsgi", "--py-autoreload", "2"]
