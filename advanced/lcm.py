class LoggingContextManager:
  def __enter__(self):
    print('LoggingContextManager.__enter__()')
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is None:
      print('LoggingContextManager.__exit__()')
    else:
      print('LoggingContextManager.__exit__({},{},{})'.format(exc_type, exc_val, exc_tb))
    return False # re raise the exception
