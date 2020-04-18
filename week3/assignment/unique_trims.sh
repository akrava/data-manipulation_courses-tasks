#!/bin/bash

python unique_trims.py data/dna.json > unique_trims.json
diff -u unique_trims.json solutions/unique_trims.json
