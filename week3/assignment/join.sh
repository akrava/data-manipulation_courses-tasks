#!/bin/bash

python join.py data/records.json > join.json
diff -u join.json solutions/join.json
