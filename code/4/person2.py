# sample(class)
class Person:
  def __init__(self, name, alter=None):
    self.name = name
    self.alter = alter
# end-sample

# sample(method)
  def erhoehe_alter(self):
    if(self.alter == None):
      raise ValueError("Alter ist nicht gesetzt")
    self.alter += 1
# end-sample

# sample(objects)
p1 = Person("Peter")
p2 = Person("Katja", 21)
# end-sample

# sample(attributes)
p1 = Person("Peter")
p1.alter = 22
print(f"{p1.name} ist {p1.alter} Jahre alt")
# end-sample