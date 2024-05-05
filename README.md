# UselessThingsToSteal

**Collect the things so useless you steal them anyway**

## Install

Prerequisites -> ```npm```, ```docker```

```bash
git clone https://github.com/Alexandre-Roussel48/UselessThingsToSteal.git

cd UselessThingsToSteal

cd backend
npm install

cd ../frontend

npm install
cd ..
```

## Config

Rename file **database/docker-compose.yml.sample** -> **database/docker-compose.yml and complete informations**
Rename file **backend/.env.sample** -> **backend/.env and complete informations**

You can add or remove cards **carefully** in **backend/prisma/seed.js**.

First time :

```bash
cd database
docker compose up --build &

cd ../backend

npm run db

fg
(ctrl-c)
```

## Run (development mode)

```bash
cd database
docker-compose up --build
```

```bash
cd backend
npm run back
```

```bash
cd frontend
npm run dev
```

## Production

**TODO**