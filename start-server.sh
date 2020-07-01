#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi
# Port 8010 is used her as it's the gunicorn port.  nginx listens on 8020 which is also the exposed port in the Dockerfile.
python manage.py collectstatic
(gunicorn puppetincidentresponse.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"

