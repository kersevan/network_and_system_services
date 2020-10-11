#!/bin/bash

date >> results_ab_remote.txt

ab                                                      \
-n $1                                                   \
-p post-data.txt                                        \
-T 'application/x-www-form-urlencoded; charset=UTF-8'   \
http://34.125.29.204/cgi-bin/test.py                    \
>> results_ab_remote.txt


echo "---------------------------------------------------------------" >> results_ab_remote.txt