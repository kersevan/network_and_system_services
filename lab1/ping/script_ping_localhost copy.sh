#!/bin/bash

date >> results_ping_localhost.txt

ping -c $1 localhost >> results_ping_localhost.txt

echo "---------------------------------------------------------------" >> results_ping_localhost.txt