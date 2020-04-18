#!/bin/bash

python multiply.py data/matrix.json > multiply.json
diff -u multiply.json solutions/multiply.json
