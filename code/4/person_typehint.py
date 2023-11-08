# sample(class)
class Person:
  name: str
  alter: int

  def __init__(self, name, alter=None):
    self.name = name
    self.alter = alter
# end-sample

  #sample(method)
  def erhoehe_alter_um(self, jahre: int = 1) -> None:
    if self.alter is None:
        self.alter = 0
    self.alter += jahre
  # end-sample

# sample(object)

p = Person("Peter", 20)
p.erhoehe_alter_um()



# end-sample