# sameple(class)
class MeineKlasse():
  def __init__(self):
    self.__x = 42
# end-sample

# sample(object)
o = MeineKlasse()
print(o._MeineKlasse__x)  # Python nennt __x um in _Klassenname__x
# end-sample