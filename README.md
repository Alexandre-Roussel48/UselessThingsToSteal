![Affiche UTTS](https://github.com/user-attachments/assets/2295cf3f-274a-4613-8a49-01f4c9f9c859)

# UselessThingsToSteal

**Collect the things so useless you steal them anyway**

## Install

Prerequisites -> ```npm```, ```docker```

```bash
git clone https://github.com/Alexandre-Roussel48/UselessThingsToSteal.git

cd UselessThingsToSteal

cd UTTS_backend
npm install

cd ../UTTS_frontend

npm install
cd ..
```

## Config

Rename file **UTTS_database/docker-compose.yml.sample** -> **UTTS_database/docker-compose.yml and complete informations**
Rename file **UTTS_backend/.env.sample** -> **UTTS_backend/.env and complete informations**
Rename file **UTTS_frontend/.env.sample** -> **UTTS_frontend/.env and complete informations**

You can add or remove cards **carefully** in **backend/prisma/seed.js**.

First time :

```bash
cd UTTS_database
docker compose up --build &

cd ../UTTS_backend

npm run db

fg
(ctrl-c)
```

## Run (development mode)

```bash
cd UTTS_database
docker-compose up --build
```

```bash
cd UTTS_backend
npm run back
```

```bash
cd UTTS_frontend
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

ssh dokku@cluster-ig3.igpolytech.fr letsencrypt:set utts-backend email alexandre.roussel03@etu.umontpellier.fr
ssh dokku@cluster-ig3.igpolytech.fr ports:add utts-backend http:80:5000
ssh dokku@cluster-ig3.igpolytech.fr letsencrypt:enable utts-backend
ssh dokku@cluster-ig3.igpolytech.fr ports:add utts-backend https:443:5000
ssh dokku@cluster-ig3.igpolytech.fr ports:add utts-backend https:5001:5001
ssh dokku@cluster-ig3.igpolytech.fr ports:remove utts-backend http:5000:5000
ssh dokku@cluster-ig3.igpolytech.fr ports:remove utts-backend http:5001:5001
ssh dokku@cluster-ig3.igpolytech.fr ports:remove utts-backend http:80:5000
```

### Frontend

```bash
git remote add dokku dokku@cluster-ig3.igpolytech.fr:utts
ssh dokku@cluster-ig3.igpolytech.fr apps:create utts
ssh dokku@cluster-ig3.igpolytech.fr config:set utts KEY=VALUE
git push dokku main:master

ssh dokku@cluster-ig3.igpolytech.fr letsencrypt:set utts email alexandre.roussel03@etu.umontpellier.fr
ssh dokku@cluster-ig3.igpolytech.fr ports:add utts http:80:5002
ssh dokku@cluster-ig3.igpolytech.fr letsencrypt:enable utts
ssh dokku@cluster-ig3.igpolytech.fr ports:add utts https:443:5002
ssh dokku@cluster-ig3.igpolytech.fr ports:remove utts http:5002:5002
ssh dokku@cluster-ig3.igpolytech.fr ports:remove utts http:80:5002
```
