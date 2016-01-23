#!/bin/sh

filename=$1

OLD_IFS=$IFS
IFS=","

while read p1 p2 p3 p4 p5 p6
do
 manager/gameManager \
    -a $p1 -p "" -u "" -n "greedy1" -r 1 -s 100 \
    -a $p2 -p "" -u "" -n "greedy2" -r 2 -s 98 \
    -a $p3 -p "" -u "" -n "greedy3" -r 3 -s 80 \
    -a $p4 -p "" -u "" -n "greedy4" -r 4 -s 70 \
    -a $p5 -p "" -u "" -n "greedy5" -r 5 -s 60 \
    -a $p6  -p "" -u "" -n "greedy6" -r 6 -s 20 \
   # -l logfiles/logfile12 \
   # -t
done < $filename
IFS=$OLD_IFS
