#!/bin/sh

while true; do
    echo "Agent running..."
    sleep 60

    if [ $((RANDOM % 10000)) -eq 0 ]; then
    echo "Agent crashed!"
    exit 1
  fi
done