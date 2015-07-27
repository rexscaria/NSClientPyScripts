#!/usr/bin/python
import psutil
import sys
import re
import datetime

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
        if(re.match('^' + process + '$' , proc.name(), re.I | re.U | re.X)):
            pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline', 'create_time', 'status', 'exe', 'memory_info_ex'])
            if(cmd != '' and pinfo['cmdline'] is not None and re.search(cmd, repr(pinfo['cmdline']))):
                result.append(pinfo)
            elif(cmd != '' and pinfo['cmdline'] is not None):
                pass
            else:
                result.append(pinfo)
    except psutil.NoSuchProcess:
        pass

message = ''
index = 0
if len(result):
    for proc in result:
        index = index + 1
        time = proc['create_time'] if proc['create_time'] else 0
        memory = (proc['memory_info_ex']).vms  if proc['memory_info_ex'] else 0
        cmdline = proc['cmdline'][0]  if len(proc['cmdline']) else ''
        message += "'SOD;filename~%s;time~%s;state~%s;pid~%d;memory~%ld;command_line~%s;EOD state'=1;0;0 " % (proc['exe'], time, proc['status'], proc['pid'],memory, cmdline)
    message += "'count'=%d;0;0" % (index)
else:
    message  = "'SOD;filename~%s;time~%s;state~%s;pid~%d;memory~%ld;command_line~%s;EOD state'=0;0;0 'count'=0;0;0" % (process, '', 'stopped', 0,0, '')

print message
