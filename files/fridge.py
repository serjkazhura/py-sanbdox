"""
Demonstrates raiding a refrigerator.
"""

from contextlib import closing

class RefrigeratorRaider:
  """Rade the fridge.
  """

  def open(self):
    print("Open the fridge door.")


  def take(self, item):
    print("Finding {}...".format(item))
    if item == 'elephant':
      raise RuntimeError("Why do you keep an elephant in the fridge?!")
    print("Taking {}".format(item))


  def close(self):
    print("Closing fridge door.")


def raid(item):
  with closing(RefrigeratorRaider()) as r:
    r.open()
    r.take(item)