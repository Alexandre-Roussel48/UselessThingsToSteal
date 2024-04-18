# UselessThingsToSteal

**Collect the things so useless you steal them anyway**

## Install

Prerequisites -> ```npm```, ```python venv```, ```docker```

```bash
git clone https://github.com/Alexandre-Roussel48/UselessThingsToSteal.git

cd UselessThingsToSteal

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd frontVueJS_SPA
npm install
cd ..

cd static
npm install
cd ..
```

## Config

Rename file **database/docker-compose.yml.sample** -> **database/docker-compose.yml and complete informations**
Rename file **config.py.sample** -> **config.py and complete informations**

You can add or remove cards **carefully** in **models/__init__.py**.

First time :

```bash
cd database
docker compose up --build &
cd ..

source venv/bin/activate
python
>>> import models
>>> models.create_db()
>>> models.pop_cards()
(ctrl-d)

fg
(ctrl-c)
```

## Run (development mode)

```bash
	rundev.sh
cd database
docker compose up --build &
cd ..

source venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=server.py
flask run
```

```bash
cd frontVueJS_SPA
npm run dev
```

## Production

**TODO**

## Run (server mode)

```bash
	run.sh
cd database
docker compose up --build &
cd ..

kill $(cat UselessThingsToSteal.pid)
source venv/bin/activate
gunicorn --daemon -b '0.0.0.0:4800' --pid=UselessThingsToSteal.pid --error-log=./errors.log server:app
```