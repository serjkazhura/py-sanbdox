import sys

def calculate_average(a: int, b: int, c: int) -> float:
  return (a+b+c)/3

def main():
  avrg: float = calculate_average(1, 5, 3)
  print(avrg)

if __name__ == "__main__":
  main()