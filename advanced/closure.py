def enclosing():
  x = 'closed over'
  def local_func():
    print(x)
  return local_func

if __name__ == "__main__":
  lf  = enclosing()
  lf()
  print(lf.__closure__)
