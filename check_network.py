#!/usr/bin/python
import psutil
import time
nw1 = psutil.net_io_counters(pernic=False)

interval = 1;
time.sleep(interval)

nw2 = psutil.net_io_counters(pernic=False)

result = '%d, %d, ' % (nw2.bytes_recv - nw1.bytes_recv, nw2.bytes_sent - nw1.bytes_sent)
print result
