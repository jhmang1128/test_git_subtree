import numpy as np
import time
from datetime import timedelta
import datetime

timestamp = time.time()

print(timestamp)


now = datetime.datetime.now()
datetimeobj = datetime.datetime.fromtimestamp(1643761964.2927933)
aaa = now - datetime.timedelta(days=8) - datetime.timedelta(hours=14) - datetime.timedelta(minutes=20) - datetime.timedelta(seconds=33)
timestamp = time.mktime(aaa.timetuple())

# timestamp = time.strptime(now, "%Y-%m-%d %H:%M:%S")

datetimeobj = datetime.datetime.fromtimestamp(1643132984.0202706)
print(datetimeobj)