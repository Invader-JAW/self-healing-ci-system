#!/bin/sh

while true; do
    echo "Agent running..."
    sleep 15

    if [ $((RANDOM % 10000)) -eq 0 ]; then
    echo "Agent crashed!"
    exit 1
  fi
done