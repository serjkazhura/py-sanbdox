iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator = iter(iterable)

n = next(iterator)

print(n)

# first iterable

def first(iterable):
  iterator = iter(iterable)
  try:
    return next(iterator)
  except StopIteration:
    raise ValueError("iterable is empty")

n = first(iterable)
print(n)

# generators

def gen123():
  yield 1
  yield 2
  yield 3

g = gen123()
print(g)
print(next(g))

for v in gen123():
  print(v)

