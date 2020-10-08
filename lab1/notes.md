curl -s -o /dev/null -X POST -F 'input=55' http://localhost/cgi-bin/test.py -w %{time_connect}:%{time_starttransfer}:%{time_total}

curl -s -o /dev/null -X POST -F 'input=55' http://34.125.29.204/cgi-bin/test.py -w %{time_connect}:%{time_starttransfer}:%{time_total}