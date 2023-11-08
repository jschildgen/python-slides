# sample(classes)
class Schiff:
    name: str
    max_geschwindigkeit: int

    def __init__(self, name, max_geschwindigkeit):
        self.name = name
        self.max_geschwindigkeit = max_geschwindigkeit

    def fahre(self):
        print(f"{self.name} fährt auf dem Wasser.")

class Haus:
    anzahl_zimmer: int

    def __init__(self, anzahl_zimmer):
        self.anzahl_zimmer = anzahl_zimmer

class Hausboot(Schiff, Haus):   
    def __init__(self, name, max_geschwindigkeit, anzahl_zimmer):
        Schiff.__init__(self, name, max_geschwindigkeit)
        Haus.__init__(self, anzahl_zimmer)
# end-sample

# sample(objects)
mein_hausboot = Hausboot("Mein Hausboot", 10, 3)
mein_hausboot.fahre()
# end-sample
