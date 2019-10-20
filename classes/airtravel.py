""" Model for aircraft flights """

from Flight import Flight
from Aircraft import AirbusA319

def console_card_printer(passenger, seat, flight_num, aircraft):
  output = "| Name: {0}"    \
           " Flight: {1}"   \
           " Seat: {2}"     \
           " Aircraft: {3}" \
           " |".format(passenger, flight_num, seat, aircraft)
  banner = '+' + '-' * (len(output) - 2) + '+'
  border = '|' + ' ' * (len(output) - 2) + '|'
  lines = [banner, border, output, border, banner]
  card = '\n'.join(lines)
  print(card)
  print()


def main():
  a = AirbusA319("G-EUPT")
  print(a.seating_plan())
  f = Flight("BA758", a)
  f.allocate_seat('12A', 'Guido van Rossum')
  f.allocate_seat('15F', 'Bjarne S')
  f.allocate_seat('15E', 'Andreas H')
  f.allocate_seat('1C', 'John M')
  f.allocate_seat('1D', 'Richard H')
  f.relocate_passenger('12A', '15D')
  f.make_boarding_cards(console_card_printer)

if __name__ == "__main__":
  main()