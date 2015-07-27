#!/usr/bin/python
import psutil
mem = psutil.virtual_memory()
def bytes_to_G(bytes):
    return bytes/(1024.0*1024.0*1024.0)

result = 'SOD;free_memory~%02.2f;total_memory~%02.2f;used_memory~%02.2f;EOD;' % (bytes_to_G(mem.available), bytes_to_G(mem.total), bytes_to_G(mem.total - mem.available))
print result
