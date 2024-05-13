#!/bin/bash

stop_processes() {
  echo "Stopping processes..."
  docker compose down
  pkill -P $$
}

trap stop_processes SIGINT

cd UTTS_database
docker compose up --build &
cd ..

cd UTTS_backend
npm run back &

wait