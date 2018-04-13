#! /bin/bash

# Usage: killprocess processName

pattern=$1

while true; do
  taskkill | gawk -v pat="$pattern" '$0 ~ pat {system(sprintf("taskkill /PID %s", $2))}'
  sleep 21s
done
