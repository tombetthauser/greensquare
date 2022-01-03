#! /bin/bash

while :
do
  bash ./scripts/up.sh
  bash ./scripts/down.sh
  git pull --force
  sleep 3
done
