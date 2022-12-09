import csv
import math

#proměnné pro sedmidenní průtoky
sum_tyden=0

#SEDMIDENNÍ
try:
    with open ("vstup.csv", encoding="utf-8", newline='') as f,\
        open("vystup_7dni.csv","w",encoding="utf-8", newline='') as g:
        # chyba kdyz neexistuje
        reader = csv.reader(f, delimiter=",")
        for index, row in enumerate (reader, start =1):   #očísluje řádky, začíná 1
            cislo_radku= int(index)

            try:
                sum_tyden += float(row[-1])  #připočítá hodnotu každého řádku
            except ValueError:   #chyba kdyz neni cislo
                print("Průtok není zadán jako číslo") #TAKY NEFUNGUJE

            if cislo_radku%7 == 1:       #vypíše jen každý sedmy (začíná nulou), pokud je delitelné 7 se zbytkem 1
                #g.write(str(index) +": " + str(radek) +"\n")
                datum = (row[-2])
            if cislo_radku%7 == 0: 
                sedmidenni = round(sum_tyden/7,4)
                outrow = (f"{row[0]}, {row[1]}, {datum}, {sedmidenni}\n")
                g.write(outrow)
                sum_tyden = 0   #po sedmém se sum opět vynuluje
except FileNotFoundError:   #PROC NEFUNGUJE?????
    print("Soubor nenalezen")

#proměnné pro roční průtoky
sum_rok=0
dny=0
rok=0
#proměnné pro maxima a minima
maximum=0
minimum=math.inf
try:
    with open ("vstup.csv", encoding="utf-8", newline='') as f,\
        open("vystup_rok.csv","w",encoding="utf-8", newline='') as h:
        reader = csv.reader(f, delimiter=",")
        writer =csv.writer (h)
        for row in reader:
            datum_split = row[2].split(".")
            if rok ==0:
                prvni_den = row[0:-1]

            if rok != int(datum_split[-1]) and rok !=0:
                prumer_rok = round(sum_rok/dny,4)
                prvni_den.append(prumer_rok)
                writer.writerow(prvni_den)
                prvni_den = row[0:-1]
                sum_rok = 0
                dny =0      
            dny += 1
            sum_rok += float(row[-1])
            rok = int(datum_split[-1])
        #poslední rok už nesplňuje podmínku, proto nakonci zvlášť
        posledni_rok=round(sum_rok/dny,4) #posledni den
        prvni_den.append(posledni_rok)
        writer.writerow(prvni_den)

        if float(row[-1]) > maximum:   #prochází řádky a hledá maximální průtok
            datum_max = row[-2]
            maximum = float(row[-1])
        if float(row[-1]) < minimum:   #prochází řádky a hledá minimální průtok
            datum_min = row[-2]
            minimum = float(row[-1])
        print (f"Nejvyšší hodnota průtoku je {maximum} ze dne {datum_max}")
        print (f"Nejnižší hodnota průtoku je {minimum} ze dne {datum_min}")

except FileNotFoundError:   #PROC NEFUNGUJE?????
    print("Soubor nenalezen")
     