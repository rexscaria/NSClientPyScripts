#!/usr/bin/python
import psutil
mem = psutil.disk_usage('/')
def bytes_to_G(bytes):
    return bytes/(1024.0*1024.0*1024.0)

result = 'SOD;total_free~%02.2f;total_size~%02.2f;total_used~%02.2f;EOD;' % (bytes_to_G(mem.free), bytes_to_G(mem.total), bytes_to_G(mem.used))
print result
