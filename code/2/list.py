wochentage = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"]
print(wochentage[0])        # So
print(wochentage[6])        # Sa
print(wochentage[-1])       # Sa
print(len(wochentage))      # 7 (Länge der Liste)

print(wochentage)    # ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"]

werktage = wochentage[1:6]  # erzeugt neue Liste
print(werktage)             # ["Mo", "Di", "Mi", "Do", "Fr"]