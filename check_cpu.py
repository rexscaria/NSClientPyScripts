#!/usr/bin/python
import psutil
cpus = psutil.cpu_percent(interval=0.1, percpu=True)
cpu_dict = {}
for index,value in enumerate(cpus, start=1):
    cpu_dict['core_id'+str(index)] = value

cpu_dict['total'] = reduce(lambda x,y: x+y, cpus)/len(cpus)

result = ''
for key in cpu_dict.keys():
     result += 'SOD;core_id~%s;load~%02.2f;time~%d;EOD;' % (key, cpu_dict[key], 10)

print result
