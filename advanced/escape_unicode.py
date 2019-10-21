def escape_unicode(f):
  def wrap(*args, **kwargs):
    x = f(*args, **kwargs)
    return ascii(x)
  return wrap

@escape_unicode
def nother_city():
  return 'Менск'


class CallCount:
  def __init__(self, f):
    self.f = f
    self.counter = 0

  def __call__(self, *args, **kwargs):
    self.counter += 1
    return self.f(*args, **kwargs)

@CallCount
def hello(name):
  print('Hello {}'.format(name))
