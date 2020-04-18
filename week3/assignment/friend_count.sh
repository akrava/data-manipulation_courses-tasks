#!/bin/bash

python friend_count.py data/friends.json > friend_count.json
diff -u friend_count.json solutions/friend_count.json
