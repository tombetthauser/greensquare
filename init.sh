#! /bin/bash

while :
do
  bash ./script/up.sh
  bash ./script/down.sh
  git pull --force
  sleep 3
done