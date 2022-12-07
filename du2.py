import csv
import math

sum=0
maximum=0
minimum=math.inf

with open ("prutoky.csv", encoding="utf-8", newline='') as f,\
    open("vystup_7dni.csv","w",encoding="utf-8", newline='') as g,\
    open("vystup_rok.csv","w",encoding="utf-8", newline='') as h:
    # chyba kdyz neexistuje
    try:
        print("supr")
    except FileNotFoundError:   #PROC NEFUNGUJE?????
        print("Soubor nenalezen")

    reader = csv.reader(f, delimiter=",")
    
    
    for index, row in enumerate (reader, start =1):   #očísluje řádky, začíná 1
        cislo_radku= int(index)
        #radek = ((row[-4])+ ", "+ (row[-3])+ ", "+(row[-2]))
        #radek = (f"{row[-4]} ", "+ {row[-4]}+ ", "+(row[-2]))
        try:
            sum += float(row[-1])  #připočítá hodnotu každého řádku
        except ValueError:   #chyba kdyz neni cislo
            print("Průtok není zadán jako číslo") #TAKY NEFUNGUJE
        
        if cislo_radku%7 == 1:       #vypíše jen každý sedmy (začíná nulou), pokud je delitelné 7 se zbytkem 1
            #g.write(str(index) +": " + str(radek) +"\n")
            datum = (row[-2])
        if cislo_radku%7 == 0:
            sedmidenni = round(sum/7,4)
            outrow = ((row[-4])+ ", "+ (row[-3])+ ", "+ str(datum)+ ", "+ str(sedmidenni) + "\n")
            g.write(outrow)
            sum = 0   #po sedmém se sum opět vynuluje
        
        datum_split = row[2].split(".")
        rok = int(datum_split[-1])
        #mesic = datum_split[1]
        #den = datum_split[0]
        pocet_dnu = 0            
        
        if float(row[-1]) > maximum:   #prochází řádky a hledá maximální průtok
            datum_max = row[-2]
            maximum = float(row[-1])
        
        if float(row[-1]) < minimum:   #prochází řádky a hledá minimální průtok
            datum_min = row[-2]
            minimum = float(row[-1])  
    
    print ("Nejvyšší hodnota průtoku je " + str(maximum) + " ze dne " + (datum_max))
    print ("Nejnižší hodnota průtoku je " + str(minimum) + " ze dne " + (datum_min))