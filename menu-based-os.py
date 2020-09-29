#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp 
import cgi

form = cgi.FieldStorage()
inp = form.getvalue("i")

if 'launch' in inp or 'run' in inp or 'start' in inp or 'execute' in inp:
    if 'notepad' in inp or 'editor' in inp:
        out = sp.getstatusoutput('gedit')
        print("'gedit' text editor has been launched successfully.")
    elif 'firefox' in inp or 'browser' in inp or 'internet' in inp:
        out = sp.getstatusoutput('firefox')
        print("'firefox' browser has been launched successfully.")
    elif 'calendar' in inp or 'cal' in inp:
        out = sp.getstatusoutput('cal')
        print("The calendar of 2020 is as follows -\n {}".format(out[1]))
    elif 'date' in inp or 'day' in inp:
        out = sp.getstatusoutput('date')
        print("Today's date is -\n {}".format(out[1]))
    else:
        print("Doesn't support")
else:
    print("Please provide an action...")
        