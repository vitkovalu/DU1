import json
from pyproj import Transformer
from statistics import mean, median
from math import sqrt, inf

wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)   #prevod na krovaka
min_vzdalenost = inf
max_vzdalenost=0

try:
    with open("adresy.geojson", encoding ="utf-8") as adresy:    #nactení adres
        data_adresy = json.load(adresy)
except FileNotFoundError:
    print("Soubor neexistuje")

try:
    with open("kontejnery.json", encoding ="utf-8") as kontejnery: #nactení kontejnerů
        data_kontejnery = json.load(kontejnery)
except FileNotFoundError:
    print("Soubor neexistuje")

pocet_adres = len(data_adresy["features"])     
pocet_kontejnery = len(data_kontejnery["features"])    #spocten celkový pocet adres a kontejnerů
print(f"Načteno {pocet_adres} adresních bodů")
print(f"Načteno {pocet_kontejnery} kontejnerů na tříděný odpad")

try:
    for adresa in data_adresy["features"]:
        adresa_x = adresa["geometry"]["coordinates"][0]      
        adresa_y = adresa["geometry"]["coordinates"][1]        #do proměnných uloženy souřadnice ve wgs
        jtsk_adresy = wgs2jtsk.transform(adresa_x,adresa_y)   #převod na SJTSK

        for kontejner in data_kontejnery["features"]:
            pristup = kontejner["properties"]["PRISTUP"]
            aktualni_kontejner = kontejner["properties"]["ID"]

            if pristup == "volně":                             #vybírá jen volně přístupné
                kontejner_x = kontejner["geometry"]["coordinates"][0]
                kontejner_y = kontejner["geometry"]["coordinates"][1]  #do proměnných uloženy souřadnice kontejnerů
                vzdalenost = float(sqrt((jtsk_adresy[0]-kontejner_x)**2+(jtsk_adresy[1]-kontejner_y)**2))  #spoctené vzdálenosti pomocí Pythagorovi věty
                
                if min_vzdalenost == None or min_vzdalenost>vzdalenost:
                    min_vzdalenost = vzdalenost
                    nejbliz = aktualni_kontejner
            if min_vzdalenost > max_vzdalenost:
                max_vzdalenost = min_vzdalenost
                nejdal = aktualni_kontejner

        adresa["properties"]["vzdalenost_od_kont"] = min_vzdalenost
        adresa["properties"]["kontejner"] = nejbliz        
        min_vzdalenost = 0   #opět se vynuluje

except KeyError:
    print("neco je spatne")



