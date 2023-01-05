import json
from pyproj import Transformer
from statistics import mean, median
from math import sqrt
from json.decoder import JSONDecodeError

wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)   #prevod na krovaka
min_vzdalenost = None

try:
    with open("adresy.geojson", encoding ="utf-8") as adresy:    #nactení adres
        data_adresy = json.load(adresy)
except FileNotFoundError:
    print("Vstupní soubor s adresami neexistuje")
except JSONDecodeError:
    print("Vstupní soubor s adresami není validní")

try:
    with open("kontejnery.json", encoding ="utf-8") as kontejnery: #nactení kontejnerů
        data_kontejnery = json.load(kontejnery)
except FileNotFoundError:
    print("Vstupní soubor s kontejnery neexistuje")
except JSONDecodeError:
    print("Vstupní soubor s kontejnery není validní")

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
                    nejbliz_kontejner = aktualni_kontejner

        if min_vzdalenost > 10000:
            print("Nejbližší kontejner se nachází dále než 10 km")
            exit()             #program se ukončí, je-li nejbližší program vzdálenn dál než 10 km

        adresa["properties"]["vzdalenost_od_kont"] = min_vzdalenost
        adresa["properties"]["kontejner"] = nejbliz_kontejner        
        min_vzdalenost = None  #opět se vynuluje

except KeyError:
    print("Soubor nemá všechny požadované atributy")

vzdalenosti = [adresa["properties"]["vzdalenost_od_kont"] for adresa in data_adresy["features"]]
                                          
max_vzdalenost = round(max(vzdalenosti))
index_kontejneru= (vzdalenosti.index(max(vzdalenosti)))   #najde index maximální vzdálenosti, čímž se uloží/najde adresa toho místa
ulice = data_adresy["features"][index_kontejneru]["properties"]["addr:street"]
cislo_domu = data_adresy["features"][index_kontejneru]["properties"]["addr:housenumber"]

print(f"Průměrná vzdálenost ke kontejneru je {round(mean(vzdalenosti),1)} m")            
print(f"Medián vzdálenosti ke kontejneru: {round(median(vzdalenosti),1)} m")               
print(f"Nejdále ke kontejneru je z adresy {ulice} {cislo_domu} a to {max_vzdalenost} m")


