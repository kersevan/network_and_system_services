#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

input = int(form.getvalue('input'))

sum = 0

for i in range(input+1):
    sum = sum + i


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI computation</title>")
print("</head>")
print("<body>")
print("<h2>Result of 0+1+...+%s is %s</h2>" % (input, sum))
print("</body>")
print("</html>")