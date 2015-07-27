#!/usr/bin/python
import psutil
import time
io1 = psutil.disk_io_counters(perdisk=False)

interval = 1;
time.sleep(interval)

io2 = psutil.disk_io_counters(perdisk=False)

result = '%d, %d, %d, ' % (0, io2.read_count - io1.read_count, io2.write_count - io1.write_count)
print result
