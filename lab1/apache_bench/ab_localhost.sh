#!/bin/bash

date >> results_ab_localhost.txt

ab                                                      \
-n $1                                                   \
-p post-data.txt                                        \
-T 'application/x-www-form-urlencoded; charset=UTF-8'   \
http://localhost/cgi-bin/test.py                        \
>> results_ab_localhost.txt


echo "---------------------------------------------------------------" >> results_ab_localhost.txt