#!/bin/bash

date >> results_curl_remote.txt

for i in `seq 1 $1`; do
    curl -s -o /dev/null -X POST -F 'input=555' http://34.125.29.204/cgi-bin/test.py -w $i.connect=%{time_connect}:transfer=%{time_starttransfer}:total=%{time_total} >> results_curl_remote.txt
    echo >> results_curl_remote.txt
done

echo "---------------------------------------------------------------" >> results_curl_remote.txt
