import csv

with open ("QD_138000_Data.csv", encoding="utf-8", newline='') as f:
    reader = csv.reader(f, delimiter=",")

    with open("vystup_7dni.csv","w",encoding="utf-8", newline='') as g:  #zalozen soubor pro sedmidenní prumery
        for index, row in enumerate (reader):
            cislo_radku= int(index)
            if cislo_radku%7 == 0:       #vypíše jen každý sedmy (začíná nulou), pokud je delitelné 7 beze zbytku
                g.write(str(index) + str(row) +"\n" )
            
    with open("vystup_rok.csv","w",encoding="utf-8", newline='') as h:  #zalozen soubor pro roční průměry
        for index, row in enumerate (reader):
            cislo_radku = int(index)
            if cislo_radku%365 == 0:
                h.write(str(index) + str(row) +"\n" )
