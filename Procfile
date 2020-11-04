# Used for our heroku deploy (Not needed for development)
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python manage.py
release: python manage.py migrate
web: gunicorn library.wsgi -b 0.0.0.0:$PORT --log-file -
