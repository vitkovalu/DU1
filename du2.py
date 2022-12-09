import csv
import math

sum_tyden=0
sum_rok=0
pocet_dnu=0
rok=0
maximum=0
minimum=math.inf

with open ("prutoky.csv", encoding="utf-8", newline='') as f,\
    open("vystup_7dni.csv","w",encoding="utf-8", newline='') as g,\
    open("vystup_rok.csv","w",encoding="utf-8", newline='') as h:
    # chyba kdyz neexistuje
    reader = csv.reader(f, delimiter=",")
    writer =csv.writer (h)
    try:
        print("supr")
    except FileNotFoundError:   #PROC NEFUNGUJE?????
        print("Soubor nenalezen")
    
    for index, row in enumerate (reader, start =1):   #očísluje řádky, začíná 1
        cislo_radku= int(index)

        try:
            sum_tyden += float(row[-1])  #připočítá hodnotu každého řádku
        except ValueError:   #chyba kdyz neni cislo
            print("Průtok není zadán jako číslo") #TAKY NEFUNGUJE

            #SEDMIDENNÍ
        if cislo_radku%7 == 1:       #vypíše jen každý sedmy (začíná nulou), pokud je delitelné 7 se zbytkem 1
            #g.write(str(index) +": " + str(radek) +"\n")
            datum = (row[-2])
        if cislo_radku%7 == 0: 
            sedmidenni = round(sum_tyden/7,4)
            outrow = (f"{row[0]}, {row[1]}, {datum}, {sedmidenni}\n")
            g.write(outrow)
            sum_tyden = 0   #po sedmém se sum opět vynuluje
        #ROČNÍ 
        datum_split = row[2].split(".")

        if rok == 0:
            prvni_den = (row[0], row [1], row[2])
            
        if rok != int(datum_split[-1]) and rok !=0:
            prumer_rok = round(sum_rok/pocet_dnu,4)
            print(prvni_den)
            h.write(f"{prvni_den}, {prumer_rok}\n" )  #píše první den v roce, co tam je
            prvni_den = (row[0], row [1], row[2])
            sum_rok = 0
            pocet_dnu = 0

        pocet_dnu +=1
        sum_rok += float(row[-1])
        rok = int(datum_split[-1])
        
        #nepise rok 2021
        
        if float(row[-1]) > maximum:   #prochází řádky a hledá maximální průtok
            datum_max = row[-2]
            maximum = float(row[-1])    
        if float(row[-1]) < minimum:   #prochází řádky a hledá minimální průtok
            datum_min = row[-2]
            minimum = float(row[-1])  

    print (f"Nejvyšší hodnota průtoku je {maximum} ze dne {datum_max}")
    print (f"Nejnižší hodnota průtoku je {minimum} ze dne {datum_min}")
     