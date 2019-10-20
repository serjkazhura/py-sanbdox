""" Model for aircraft flights """


class Flight:
  """A flight with a particular passenger aircraft
  """

  def __init__(self, number, aircraft):
    if not number[:2].isalpha():
      raise ValueError("No airline code in '{}'".format(number))

    if not number[:2].isupper():
      raise ValueError("Invalid airline code '{}'".format(number))

    if not (number[2:].isdigit() and int(number[2:]) <= 9999):
      raise ValueError("Invalid route number '{}".format(number))

    self._number = number
    self._aircraft = aircraft
    rows, seats = self._aircraft.seating_plan()
    self._seating = [None] + [ {letter:None for letter in seats} for _ in rows ]

  def number(self):
    return self._number

  def airline(self):
    return self._number[:2]

  def aircraft_model(self):
    return self._aircraft.model()

  def _parse_seat(self, seat):
    """
      Parse a sit designator into a valid row number and letter
    
    Args:
      seat: A seat designator such as '12C' or '21F'

    Returns:
      A tuple containing an integer and a string for row and seat
    """
    rows, seat_letters = self._aircraft.seating_plan()

    letter = seat[-1]
    if letter not in seat_letters:
      raise ValueError("Invalid seat letter '{}'".format(letter))

    row_text = seat[:-1]
    try:
      row = int(row_text)
    except ValueError:
      raise ValueError("Invalid seat row '{}'".format(row_text))

    if row not in rows:
      raise ValueError("Invalid row number '{}'".format(row))

    return row, letter

  def allocate_seat(self, seat, passenger):
    """Allocate a seat to a passenger.

    Args:
      seat: A seat designator such as '12C' or '21F'
      passenger: The passenger name.

    Raises:
      ValueError: if the seat in unavailable.
    """
    row, letter = self._parse_seat(seat)

    if self._seating[row][letter] is not None:
      raise ValueError("Seat '{}' already occupied".format(seat))

    self._seating[row][letter] = passenger

  def relocate_passenger(self, from_seat, to_seat):
    """
    Relocating a passenger to a different sit.

    Args:
      from_seat: the existing sit designator for the passenger to be moved.
      to_seat: the new seat designator.
    """
    from_row, from_leter = self._parse_seat(from_seat)
    if self._seating[from_row][from_leter] is None:
      raise ValueError("No passenger to relocate in seat '{}'".format(from_seat))

    to_row, to_letter = self._parse_seat(to_seat)
    if self._seating[to_row][to_letter] is not None:
      raise ValueError("Seat '{}' already occupied".format(to_seat))

    self._seating[to_row][to_letter] = self._seating[from_row][from_leter]
    self._seating[from_row][from_leter] = None

  def num_available_seats(self):
    return sum(sum(1 for s in row.values() if s is None)
              for row in self._seating
              if row is not None)

  def make_boarding_cards(self, card_printer):
    for passenger, seat in sorted(self._passenger_seats()):
      card_printer(passenger, seat, self.number(), self.aircraft_model())

  def _passenger_seats(self):
    """An iterable series of passenger seating allocations.
    """
    row_numbers, seat_letters = self._aircraft.seating_plan()
    for row in row_numbers:
      for letter in seat_letters:
        passenger = self._seating[row][letter]
        if passenger is not  None:
          yield (passenger, "{0}{1}".format(row, letter))


class Aircraft:
  
  def __init__(self, registration):
    self._registration = registration
  
  def registration(self):
    return self._registration
  
  def num_seats(self):
    rows, row_seats = self.seating_plan()
    return len(rows) * len(row_seats)

  def seating_plan(self):
    return range(1,1), "A" # dummy implementation


class AirbusA319(Aircraft):

  def model(self):
    return "Airbus A319"
  
  def seating_plan(self):
    return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):
  
  def model(self):
    return "Boeing777"
  
  def seating_plan(self):
    # for simpilicy sake let's ignore complex 
    # sitting arrangement for the 1st class
    return range(1, 56), "ABCDEGHJK"


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