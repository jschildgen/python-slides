# sample(classes)
class Schiff:
    def __init__(self, name, max_geschwindigkeit):
        self.name = name
        self.max_geschwindigkeit = max_geschwindigkeit

    def verkaufswert(self):
        return self.max_geschwindigkeit * 10000
    
class Haus:
    def __init__(self, anzahl_zimmer):
        self.anzahl_zimmer = anzahl_zimmer

    def verkaufswert(self):
        return self.anzahl_zimmer * 50000

class Hausboot(Schiff, Haus):       # Schiff zuerst, dann Haus
    # ...
# end-sample
    def __init__(self, name, max_geschwindigkeit, anzahl_zimmer):
        Schiff.__init__(self, name, max_geschwindigkeit)
        Haus.__init__(self, anzahl_zimmer)


# sample(objects)
mein_hausboot = Hausboot("Mein Hausboot", 10, 3)
print(mein_hausboot.verkaufswert())  # 100000
# end-sample
