# note that comprehensions should not have side effects
# use for loop if you wish to do side effects

words = "Why sometimes I have believed as many as six impossible things before breakfast".split()

compr = [len(word) for word in words]

print(compr)

# range

from math import factorial

compr = {len(str(factorial(x))) for x in range(20)}

print(compr)

# dictionary

from pprint import pprint as pp

country_to_capital = {'UK': 'London',
                      'Brazil': 'Brazilia',
                      'Belarus': 'Minsk',
                      'Canada': 'Ottawa'}

capital_to_coutry = {capital: country for country, capital in country_to_capital.items() }
pp(capital_to_coutry)

# filter

from math import sqrt

def is_prime(x):
  if (x < 2):
    return False
  for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

compr = [x for x in range(101) if is_prime(x)]
pp(compr)