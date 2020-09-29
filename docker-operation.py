#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
operation = form.getvalue("z")

if operation=='Available_images':
    cmd = 'sudo docker images'
    out=sp.getstatusoutput(cmd)
    if out[0]==0:
        print('Available Docker Images are -\n {}'.format(out[1]))
    else:
        print('Some ERROR : {}'.format(out[1]))
elif operation=='Launch_container':
    osname = form.getvalue("x")
    image = form.getvalue("y")
    cmd = 'sudo docker run -d -t -i --name {0} {1}'.format(osname,image)
    out = sp.getstatusoutput(cmd)
    if out[0]==0:
        print("Container Launched with OS {0} named {1}.".format(image,osname))
    else:
        print('Some ERROR : {}'.format(out[1]))
elif operation=='Stop_container':
    osname = form.getvalue("x")
    cmd = 'sudo docker stop {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    if out[0]==0:
        print("Container named {} is now stopped.".format(osname))
    else:
        print("Some ERROR : {}".format(out[1]))
elif operation=='Run_prelaunched_containers':
    osname = form.getvalue("x")
    cmd = 'sudo docker start {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    if out[0]==0:
        print("Container named {} is now active.".format(osname))
    else:
        print("Some ERROR : {}".format(out[1]))
elif operation=='Currently_running_containers':
    cmd = 'sudo docker ps'
    out = sp.getstatusoutput(cmd)
    if out[0]==0:
        print("Currently running docker containers are -\n{}".format(out[1]))
    else:
        print("Some ERROR : {}".format(out[1]))
