#!/bin/bash

date >> results_ping_remote.txt

ping -c $1 34.125.29.204 >> results_ping_remote.txt

echo "---------------------------------------------------------------" >> results_ping_remote.txt