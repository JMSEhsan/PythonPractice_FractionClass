# Customizing classes, Overriding a special method
# Fraction Class
# Ref.: Ana Bell, Get Programming Learn to Code with Python, 2018

class Fraction(object):
    def __init__(self, top, bottom):
      self.top = top
      self.bottom = bottom

    def __add__(self, other_fraction):
      new_top = self.top*other_fraction.bottom + \
      self.bottom*other_fraction.top
     
      new_bottom = self.bottom*other_fraction.bottom

      return Fraction(new_top, new_bottom)

    def __str__(self):
      return str(self.top)+"/"+str(self.bottom)

    def __mul__(self, other_fraction):
      new_top = self.top*other_fraction.top
      new_bottom = self.bottom*other_fraction.bottom
      return Fraction(new_top, new_bottom)

half = Fraction (1, 2)
quarter = Fraction (1, 4)

half_string = str(half)      
print(half_string)
print("half_string type", type(half_string))

print(half)
print("half type", type(half))

print(quarter)

print(half+quarter)

print(half*quarter)
print(half.__mul__(quarter))
print(Fraction.__mul__(quarter,half))