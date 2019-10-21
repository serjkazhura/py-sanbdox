from pprint import pprint as pp

daily = [
  [12, 14, 15, 15, 17, 21],
  [13, 14, 14, 14, 16, 20],
  [2, 2, 3, 7, 9, 10]
  ]

def transpose():
  return list(zip(*daily))

if __name__ == '__main__':
  print('current')
  pp(daily)
  print('transposed')
  pp(transpose())