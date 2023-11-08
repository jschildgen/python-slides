# sample(class)
class Person:
  def __init__(self, name):
    self.name = name
    self.alter = None
# end-sample

# sample(method)
  def erhoehe_alter(self):
    if(self.alter == None):
      raise ValueError("Alter ist nicht gesetzt")
    self.alter += 1
# end-sample

# sample(method_param)
  def erhoehe_alter_um(self, jahre=1):
    if(self.alter == None):
      self.alter = 0
    self.alter += jahre
# end-sample

# sample(object)
p = Person("Peter")
p.alter = 22
p.erhoehe_alter()
print("%s ist %d Jahre alt" % (p.name, p.alter))
# end-sample

# sample(object1)
p = Person("Peter")
# end-sample

# sample(object2)
p = Person("Peter")
p.erhoehe_alter_um(10)
# end-sample

# sample(object3)
p = Person("Peter")
p.erhoehe_alter_um(10)
p.erhoehe_alter_um()   # entspricht p.erhoehe_alter_um(1)
# end-sample