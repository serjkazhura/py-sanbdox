"""Module for demostration of generator execution.
"""

def take(count, iterable):
  """Take items from the front of an iterable

  Args:
    count: the maximum number of items to retrieve
    iterable: the source series.

  Yields:
   At most 'count' from the 'iterable'
  """
  counter = 0
  for item in iterable:
    if counter == count:
      return
    counter += 1
    yield item


def distinct(iterable):
  """Return unique items by eliminating duplictes.

  Args:
    iterable: the source series.

  Yields:
    Unique elements in order from 'iterable'.
  """
  seen = set()
  for item in iterable:
    if item in seen:
      continue
    yield item
    seen.add(item) # this is thill the item yilded! not the next one


def run_take():
  items = [2, 4, 6, 8, 10]
  for item in take(3, items):
    print(item)


def run_distinct():
  items = [5, 7, 7, 6, 5, 5]
  for item in distinct(items):
    print(item)


def run_pipeline():
  items = [3, 6, 6, 2, 1, 1]
  for item in take(3, distinct(items)):
    print(item)


if __name__ == "__main__":
  million_squares = (x*x for x in range(1, 10)) # generator expression e.g. lazily evaluated
  print(million_squares) # little memory consumed, execute to produce results.
  print(list(million_squares)) # prints all the data
  print(list(million_squares)) # prints nothing as the generator is exausted (single use object)
  sum(x*x for x in range(1, 10000)) # note that since this is a gneerator it consumes little memory.
                                    # since only 2 int are loaded into memory 
                                    # by contrast comprehension will consume a lot.
                                    # since all the collection will be loaded in memory
  print(any([True, False, False]))
  print(all([True, False, False]))
  print('take:')
  run_take()
  print('distinct:')
  run_distinct()
  print('pipeline:')
  run_pipeline()
