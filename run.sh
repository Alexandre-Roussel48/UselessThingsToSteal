#!/bin/bash

stop_processes() {
  echo "Stopping processes..."
  docker compose down
  pkill -P $$
}

trap stop_processes SIGINT

cd database
docker compose up --build &
cd ..

cd backend
npm run back &

wait