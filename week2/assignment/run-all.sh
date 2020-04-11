#!/bin/bash

cd "$(dirname "$0")"

for x in {a..f} {h..i}; do
    /bin/bash ./part.sh ${x} reuters
done

/bin/bash ./part.sh g matrix
