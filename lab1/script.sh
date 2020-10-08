#!/bin/bash

sum=0;
num_of_iters=$1

if [ -n "$1" ]; 
	then echo "parameter is set to '$num_of_iters'"; 
	else num_of_iters=10; echo "parameter is unset, setting it to '10'"; 
fi

for ((i = 0;i<=$num_of_iters; i+=1));
do
    current_time=$( /usr/bin/time -f'%e' curl -s -o /dev/null -X POST -F 'input=55' http://localhost/cgi-bin/test.py 2>&1 )
	sum=$( echo "$sum + $current_time" | bc )
	echo Try: $i Current time: $current_time s Sum: $sum
done

mean=$( echo "$sum / $num_of_iters" | bc )

sqrt_operation=$(( sum * (1 - sum) / num_of_iters ))
echo sqrt_operation
standard_error=$(echo "scale=2;sqrt($sqrt_operation)" | bc)

echo standard error = $standard_error