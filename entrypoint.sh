#!/bin/sh

cd /app
#pip install -r requirements.txt
if [ "$DATABASE" = "postgres" ]
then
	echo "Waiting for postgres..."

	while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
	      sleep 0.1
	done

	echo "PostgreSQL started"
fi

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
