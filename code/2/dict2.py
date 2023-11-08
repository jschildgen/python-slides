vorwahl = { "DE": 49, "AT": 43, "CH": 41 }

for land in vorwahl:           # Iteration über Schlüssel
    print(land, vorwahl[land])

for land, vorw in vorwahl.items(): # Iteration über Items
    print(land, vorw)

for vorw in vorwahl.values():      # Iteration über Werte
    print(vorw)