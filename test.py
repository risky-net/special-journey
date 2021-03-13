
print("Content-type: text/html\n\n")

import cgi, os
import cgitb
#remove the enable in production
cgitb.enable()
form = cgi.FieldStorage()
getFile = form['filename']
#check file open
if getFile.filename:
    print("<h1>Hello this is my Test<h1>")