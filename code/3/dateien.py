# sample(text-lesen)
# Datei öffnen und Inhalt lesen
with open("dateien/gedichte.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()

# Inhalt anzeigen
print(inhalt)
# end-sample

# sample(text-schreiben)
# Datei öffnen (w = write) oder erstellen
with open("dateien/zahlen.txt", "w") as datei:
    # Zahlen von 1 bis 100 durchlaufen
    for zahl in range(1, 101):
        datei.write(f"{zahl}\n")  # Zahl in die Datei schreiben 
                                  # und Zeilenumbruch hinzufügen
# end-sample


# sample(csv-lesen)
import csv

datei = 'dateien/schuelernoten.csv'

with open(datei, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'])
# end-sample

# sample(csv-schreiben)
import csv
datei = 'dateien/schuelernoten.csv'

# Öffne die Datei im Anhängemodus 'a' (append)
with open(datei, mode='a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Peter Peters", "7c", "Englisch", "2"])
# end-sample

# sample(datei-anlegen)
with open('dateien/leere_datei.txt', 'w', encoding='utf-8'):
    pass
# end-sample

# sample(datei-loeschen)
import os
datei = 'dateien/meine_datei.txt'

if os.path.exists(datei):
    os.remove(datei)
    print(f"Datei '{datei}' wurde gelöscht.")
else:
    print(f"Datei '{datei}' existiert nicht.")
# end-sample

with open('alt.txt', 'w', encoding='utf-8'):
    pass

# sample(datei-verschieben)
import shutil

shutil.move('alt.txt', 'dateien/alt.txt')           # verschieben
shutil.move('dateien/alt.txt', 'dateien/neu.txt')   # umbenennen
shutil.copy('dateien/neu.txt', 'dateien/neu2.txt')  # nur Inhalt
shutil.copy2('dateien/neu.txt', 'dateien/neu3.txt') # inkl. Metadaten
# end-sample

# sample(datei-schleife)
import os
for dateiname in os.listdir("dateien"):
    if dateiname.endswith(".txt"):
        print(dateiname) # Dateiname als String, z. B. "datei1.txt"
# end-sample

# sample(json)
import json

with open("dateien/buecher.json", "r", encoding="utf-8") as f:
    buecher = json.load(f)

# Titel aller Bücher ausgeben
for buch in buecher:
    print(buch["titel"])
# end-sample


# sample(json-edit)
import json

with open("dateien/buecher.json", "r", encoding="utf-8") as f:
    buecher = json.load(f)

neues_buch = {
    "titel": "Einführung in Python",
    "isbn": "978-1111111111",
    "autoren": ["Eva Beispiel"],
    "verlag": {
        "name": "Rheinwerk Verlag",
        "ort": "Bonn"
    }
}

buecher.append(neues_buch)      # Neues Buch hinzufügen

with open("dateien/buecher.json", "w", encoding="utf-8") as f:
    json.dump(buecher, f, ensure_ascii=False, indent=4)
# end-sample

# sample(config)
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

print(config.get("ALLGEMEIN", "SPRACHE"))
# end-sample