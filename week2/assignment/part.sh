#!/bin/bash

if [[ $# -eq 2 ]]; then
    sqlite3 "$2".db < part_"$1".sql > part_"$1".txt
else
    echo "pass the letter of the task to arguments"
    exit 1
fi

