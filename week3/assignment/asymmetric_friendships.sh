#!/bin/bash

python asymmetric_friendships.py data/friends.json > asymmetric_friendships.json
diff -u asymmetric_friendships.json solutions/asymmetric_friendships.json
