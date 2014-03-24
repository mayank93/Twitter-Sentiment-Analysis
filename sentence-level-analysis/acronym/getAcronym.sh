#!/bin/bash
url="http://www.noslang.com/dictionary/"
for i in {a..z}
do
    wget $url$i
    python getAcronym.py $i
done
