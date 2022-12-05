import csv
import math


maximum = 0
minimum = math.inf
with open ("prutoky.csv", encoding="utf-8", newline='') as f,\
    open("vystup_7dni.csv","w",encoding="utf-8", newline='') as g,\
    open("vystup_rok.csv","w",encoding="utf-8", newline='') as h:
    reader = csv.reader(f, delimiter=",")
    for index, row in enumerate (reader):
        cislo_radku= int(index)
        if cislo_radku%7 == 0:       #vypíše jen každý sedmy (začíná nulou), pokud je delitelné 7 beze zbytku
            g.write(str(index) +": " + (row[-2]) +"\n")

        if cislo_radku%365 == 0:
            h.write(str(index) + ": " + (row[-2]) +"\n")
        
        if float(row[-1]) > maximum:
            datum_max, maximum = row[-2], float(row[-1])
        
        if float(row[-1]) < minimum:
            datum_min, minimum = row[-2], float(row[-1])

        
    
    print ("Nejvyšší hodnota průtoku je " + str((maximum)) + " ze dne " + (datum_max))
    print ("Nejnižší hodnota průtoku je " + str((minimum)) + " ze dne " + (datum_min))