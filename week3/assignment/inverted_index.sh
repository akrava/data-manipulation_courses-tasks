#!/bin/bash

python inverted_index.py data/books.json > inverted_index.json
diff -u inverted_index.json solutions/inverted_index.json
