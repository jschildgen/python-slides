# sample(vergleich)
x = "Hallo"
if x != None:     # != ist der Ungleich-Operator
  print(x)
# end-sample

# sample(notandor)
hat_fuehrerschein = True
besitzt_auto = False

if not hat_fuehrerschein:
  print("Die Person besitzt keinen Führerschein.")

if hat_fuehrerschein and besitzt_auto:
  print("Auf geht's!")

if not hat_fuehrerschein or not besitzt_auto:
  print("Wir können nicht losfahren.")
# end-sample