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
