import numpy as np
import time
from datetime import timedelta
import datetime
from collections import defaultdict

############################################################
#  time
############################################################
'''
timestamp = time.time()

print(timestamp)


now = datetime.datetime.now()
datetimeobj = datetime.datetime.fromtimestamp(1643761964.2927933)
aaa = now - datetime.timedelta(days=8) - datetime.timedelta(hours=14) - datetime.timedelta(minutes=20) - datetime.timedelta(seconds=33)
timestamp = time.mktime(aaa.timetuple())

# timestamp = time.strptime(now, "%Y-%m-%d %H:%M:%S")

datetimeobj = datetime.datetime.fromtimestamp(1643132984.0202706)
print(datetimeobj)
'''

############################################################
#  time
############################################################

a = np.linspace(.5, 0.95, int(np.round((0.95 - .5) / .05)) + 1, endpoint=True)

print(a)

p = defaultdict(list)

# print(p)

print(np.where(a>=0.5)[0][0])

print(np.where(a==0.45)[0])

############################################################
#  end
############################################################