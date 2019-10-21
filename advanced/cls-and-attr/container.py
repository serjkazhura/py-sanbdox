import iso6346

class ShippingContainer:

  HEIGHT_FT = 8.5
  WIDTH_FT = 8.0

  next_serial = 1337

  @staticmethod
  def _make_bic_code(owner_code, serial):
    return iso6346.create(owner_code=owner_code,
                          serial=str(serial).zfill(6)) # zfill pads string with 0s


  @classmethod # if need to access the class  - use classmethod. otherwise use staticmethod.
  def _get_next_serial(cls):
    result = cls.next_serial
    cls.next_serial += 1
    return result

  @classmethod
  def create_empty(cls, owner_code, length_ft, *args, **kwargs):
    return cls(owner_code, contents=None, length_ft=length_ft, *args, **kwargs)

  @classmethod 
  def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
    return cls(owner_code, contents=list(items), length_ft=length_ft, *args, **kwargs)

  def __init__(self, owner_code, length_ft, contents):
    self.contents = contents
    self.length_ft = length_ft
    # we are using self here instead of ShippingContainer to achieve polymorphic behavior
    # we've overridden _make_bic_code in the refrigirated container
    self.bic = self._make_bic_code( 
      owner_code=owner_code, 
      serial=ShippingContainer._get_next_serial()
    )

  def _calc_volume(self):
    return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

  @property
  def volume_ft3(self):
    return self._calc_volume()


class RefrigiratedShippingContainer(ShippingContainer):

  MAX_CELSIUS = 4.0
  FRIDGE_VOLUME_FT3 = 100.0

  @staticmethod
  def _make_bic_code(owner_code, serial): # you CAN override static methods. crazy!!!!
    return iso6346.create(
      owner_code=owner_code,
      serial=str(serial).zfill(6),
      category='R'
    )

  @staticmethod
  def _c_to_f(celsius):
    return celsius * 9/5 + 32

  @staticmethod
  def _f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

  def __init__(self, owner_code, length_ft, contents, celsius):
    super().__init__(owner_code=owner_code, length_ft=length_ft, contents=contents) # init base class
    self.celsius = celsius

  @property
  def celsius(self):
    return self._celsius

  def _set_celsius(self, value):
    if value > RefrigiratedShippingContainer.MAX_CELSIUS:
      raise ValueError('Invalid temperature {}'.format(value))
    self._celsius = value


  @celsius.setter
  def celsius(self, value):
    self._set_celsius(value)

  @property
  def fahrenheit(self):
    return RefrigiratedShippingContainer._c_to_f(self.celsius)

  @fahrenheit.setter
  def fahrenheit(self, value):
    self.celsius = RefrigiratedShippingContainer._f_to_c(value)

  # @property
  # def volume_ft3(self):
  #   return super().volume_ft3 - RefrigiratedShippingContainer.FRIDGE_VOLUME_FT3

  def _calc_volume(self):
    return super()._calc_volume() - RefrigiratedShippingContainer.FRIDGE_VOLUME_FT3

class HeatedRefrigiratedShippingContainer(RefrigiratedShippingContainer):

  MIN_CELSIUS = -20.0

  # works but pretty ugly
  # @RefrigiratedShippingContainer.celsius.setter # pylint: disable=E1101
  # def celsius(self, value):
  #   if value < HeatedRefrigiratedShippingContainer.MIN_CELSIUS:
  #     raise ValueError("Invalid temperature {}".format(value))
  #   RefrigiratedShippingContainer.celsius.fset(self, value) # pylint: disable=E1101

  def _set_celsius(self, value):
    if value < HeatedRefrigiratedShippingContainer.MIN_CELSIUS:
      raise ValueError("Invalid temperature {}".format(value))
    super()._set_celsius(value)


if __name__ == "__main__":
  empty = ShippingContainer.create_empty('YML', length_ft=10.0)
  print(empty.bic)
  print(empty.volume_ft3)
  empty = RefrigiratedShippingContainer.create_empty('YML', celsius=3, length_ft=10.0)
  print(empty.bic)
  print(empty.celsius)
  print(empty.fahrenheit)
  print(empty.volume_ft3)
  empty = HeatedRefrigiratedShippingContainer.create_empty('YML', celsius=2, length_ft=10.0)
  empty.celsius = -2
  print(empty.bic)
  print(empty.celsius)
  print(empty.fahrenheit)
  print(empty.volume_ft3)