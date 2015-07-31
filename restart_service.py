#!/usr/bin/python
import psutil
import sys
import re

cmd = ''
n_args = len(sys.argv)
if n_args == 2:
    process = sys.argv[1]
elif n_args == 3:
    process = sys.argv[1]
    cmd = sys.argv[2]
else:
    raise Exception("Argument error")

pinfo = '<>'
result = []
for proc in psutil.process_iter():
    try:
        flag = False
        if(re.match('^' + process + '$', proc.name())):
            pinfo = proc.as_dict(attrs=['name', 'status', 'exe'])
            result.append(pinfo)
    except psutil.NoSuchProcess:
        pass


message = ''
index = 0
if len(result):
    for proc in result:
        index = index + 1
        message += "'SOD;name~%s;state~%s;type~%s;desc~%s;EOD'" % (proc['name'], proc['status'], 'Linux Process',proc['exe'])
else:
    message = "Failed to open service %s: 1" % (process)

print message
