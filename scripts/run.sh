#!/bin/sh

set -e  # if any command fails below, entire script should fail

python manage.py wait_for_db
python manage.py collectstatic --noinput   # collect the static files and put it into configured static files directory. This will help serve all the static contents from the same place by reverse proxy.
python manage.py migrate

# running our uwsgi service
# --socket specifies, tcp socket on port 9000, this port will be used by our NGINX server to connect to our app (through uwsgi)
# --worker 4, specifies four different workers (can be set according to cpu cores, but 4 is a good number)
# --master enables uWSGI master process which manages the worker processes.
# --enable threads enables support for python multithreading if used in our application (by third party apps etc.)
# --module specifies the entry point of our app, which is app.wsgi.py

uwsgi --socket :9000 --workers 4 --master --enable-threads --module book_my_show.wsgi
