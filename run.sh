#!/bin/bash

cd /home/ubuntu/UselessThingsToSteal/database
docker compose up --build &
cd ..

kill $(cat /home/ubuntu/UselessThingsToSteal/UselessThingsToSteal.pid)
source /home/ubuntu/UselessThingsToSteal/venv/bin/activate
/home/ubuntu/UselessThingsToSteal/venv/bin/gunicorn --daemon -b '0.0.0.0:80' --pid=/home/ubuntu/UselessThingsToSteal/UselessThingsToSteal.pid --error-log=/home/ubuntu/UselessThingsToSteal/errors.log server:app
