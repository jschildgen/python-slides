# sample(classes)
class Kleinanzeige:
    def verkaufswert(self):
        return 70

class Schiff(Kleinanzeige):
    pass

class Haus(Kleinanzeige):
    def __init__(self, anzahl_zimmer):
        self.anzahl_zimmer = anzahl_zimmer

    def verkaufswert(self):
        return self.anzahl_zimmer * 50000

class Hausboot(Schiff, Haus):
    # ...
# end-sample
    def __init__(self, anzahl_zimmer):
        Haus.__init__(self, anzahl_zimmer)


# sample(objects)
mein_hausboot = Hausboot(3)
print(mein_hausboot.verkaufswert())
# end-sample
