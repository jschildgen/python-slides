wochentage = ["Mo", "Di", "Mi", "Di", "Fr"]

wochentage[3] = "Do"
wochentage.append("Sa")     # fügt am Ende ein
wochentage.insert(0, "So")  # fügt an Position 0 (Anfang) ein

wochentage.remove("Mo")

wochentage.reverse()     # dreht die Liste um
print(wochentage)        # ["Sa", "Fr", "Do", "Mi", "Di", "So"]
wochentage.sort()        # sortiert die Liste
print(wochentage)        # ["Di", "Do", "Fr", "Mi", "Sa", "So"]