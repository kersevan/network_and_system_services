#!/bin/bash

date >> results_curl_localhost.txt

for i in `seq 1 $1`; do
    curl -s -o /dev/null -X POST -F 'input=555' http://localhost/cgi-bin/test.py -w $i.connect=%{time_connect}:transfer=%{time_starttransfer}:total=%{time_total} >> results_curl_localhost.txt
    echo >> results_curl_localhost.txt
done

echo "---------------------------------------------------------------" >> results_curl_localhost.txt
