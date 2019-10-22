import math
import cmath

def inductive(ohms):
  return complex(0.0, ohms)

def capacitive(ohms):
  return complex(0.0, -ohms)

def resistive(ohms):
  return complex(ohms)

def impedance(components):
  z = sum(components)
  return z

if __name__ == "__main__":
  imp = impedance([inductive(10), resistive(10), capacitive(5)])
  phase = cmath.phase(imp)
  degrees = math.degrees(phase)
  print(phase)
  print(degrees)
  print('Voltage cycle lacks the current cycle by {} degrees'.format(degrees))
