import csv

with open ("QD_138000_Data.csv", encoding="utf-8", newline='') as f:
    reader = csv.reader(f, delimiter=",")

    with open("vystup_7dni.csv","w",encoding="utf-8", newline='') as g:  #zalozen soubor pro sedmidenní prumery
        for row in reader:
            for index, item in enumerate (reader, start = 1):
                g.write(f"{index}:  {row[-2]} {row[-1]} \n" )

    with open("vystup_rok.csv","w",encoding="utf-8", newline='') as h:  #zalozen soubor pro roční průměry
        for row in reader:
            h.write(row[-2] + " " + row[-1] + "\n")
