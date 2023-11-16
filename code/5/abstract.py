# sample(abstract_class)
from abc import ABC, abstractmethod
class Lebewesen(ABC):
# end-sample
# sample(abstract_method)
  @abstractmethod
  def getDetails(self) -> str:
    pass
# end-sample


class Person(Lebewesen):
  name: str
  alter: int

  def __init__(self, name, alter=0):
    self.name = name
    self.alter = alter

  def getDetails(self):
    return "%s (%d)" % (self.name, self.alter)
  
#p = Lebewesen()        # TypeError: Can't instantiate abstract class
p = Person("Peter", 30)
print(p.getDetails())