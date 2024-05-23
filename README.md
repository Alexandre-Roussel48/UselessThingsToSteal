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

### Database

```bash
ssh dokku@cluster-ig3.igpolytech.fr postgres:create utts-database
```

### Backend

```bash
git remote add dokku dokku@cluster-ig3.igpolytech.fr:utts-backend
ssh dokku@cluster-ig3.igpolytech.fr apps:create utts-backend
ssh dokku@cluster-ig3.igpolytech.fr postgres:link utts-database utts-backend
ssh dokku@cluster-ig3.igpolytech.fr config:set utts-backend KEY=VALUE
git push dokku main:master
```

### Frontend

```bash
git remote add dokku dokku@cluster-ig3.igpolytech.fr:uselessThingsToSteal
ssh dokku@cluster-ig3.igpolytech.fr apps:create uselessThingsToSteal
ssh dokku@cluster-ig3.igpolytech.fr config:set uselessThingsToSteal KEY=VALUE
git push dokku main:master
```