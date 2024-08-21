#!/usr/bin/bash

search="$1"
vars=("system" "secure" "global")

if [ -z "$search" ]; then
  echo "Usage: $0 <search_term>"
  exit 1
fi

for ind in "${vars[@]}"; do
  out=$(su -c "settings list $ind | grep '$search'" 2>&1)
  echo "[$ind]"
  echo "$out"
done

