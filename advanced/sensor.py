import datetime
import itertools
import random
import time

class Sensor:
  def __iter__(self):
    return self
  
  def __next__(self):
    return random.random()

sensor = Sensor()
timestamps = iter(datetime.datetime.now, None) # iterator will never stop because None is never encountered

for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
  print(stamp, value)
  time.sleep(1)