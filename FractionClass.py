# Fraction Class

class Fraction(object):
    def __init__(self, top, bottom):
      self.top = top
      self.bottom = bottom
    
   # def __add__(self, other_fraction):
    def __str__(self):
      return str(self.top)+"/"+str(self.bottom)
half = Fraction (1, 2)
quarter = Fraction (1, 4)
print(half)
print(quarter)

