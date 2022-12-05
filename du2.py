import csv

with open ("QD_138000_Data.csv", encoding="utf-8", newline='') as f:
    with open("vystup_7dni.csv","w",encoding="utf-8", newline='') as g:  #zalozen soubor pro sedmidenní prumery
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            g.write(row[-2] + " " + row[-1] + "\n")
    with open("vystup_rok.csv","w",encoding="utf-8", newline='') as h:  #zalozen soubor pro roční průměry
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            h.write(row[-2] + " " + row[-1] + "\n")
