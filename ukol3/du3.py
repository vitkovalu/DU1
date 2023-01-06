import json
from pyproj import Transformer
from statistics import mean, median
from math import sqrt
from json.decoder import JSONDecodeError

wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)   #prevod na krovaka
min_vzdalenost = None
vystup = []       #prázdný seznam do kterých se uloží adresy pro výstupní soubor

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
        jtsk_adresy = wgs2jtsk.transform(adresa_x,adresa_y)    #převod na S-JTSK

        for kontejner in data_kontejnery["features"]:
            pristup = kontejner["properties"]["PRISTUP"]
            aktualni_kontejner = kontejner["properties"]["ID"] #ID ke kazdemu kontejneru
            if pristup == "volně":                             #vybírá jen volně přístupné
                kontejner_x = kontejner["geometry"]["coordinates"][0]
                kontejner_y = kontejner["geometry"]["coordinates"][1]  #do proměnných uloženy souřadnice kontejnerů
                vzdalenost = float(sqrt((jtsk_adresy[0]-kontejner_x)**2+(jtsk_adresy[1]-kontejner_y)**2))  #spoctené vzdálenosti pomocí Pythagorovy věty
                if min_vzdalenost == None or min_vzdalenost>vzdalenost:
                    min_vzdalenost = vzdalenost                      #ukládá se nejnižší vzdálenost
                    nejbliz_kontejner = aktualni_kontejner           #zároveň se ukládá ID nejbližšího kontejneru

            ulice = adresa["properties"]["addr:street"]
            cislo = adresa["properties"]["addr:housenumber"]
            aktualni_adresa = ulice + (" ") + cislo  #aby byla adresa ve stejném formátu jako kontejner['properties']['STATIONNAME'] 
            if pristup == "obyvatelům domu":                     #vybírá naopak ty které jsou přistupny obyvatelům domů
                if aktualni_adresa == kontejner['properties']['STATIONNAME']:    #porovnává zda je tsejná adresa domu a kontejneru
                    min_vzdalenost = 0                          # pokud ano, vzdálenosti se přiřadí hodnota 0

        if min_vzdalenost > 10000:
            print("Nejbližší kontejner se nachází dále než 10 km")
            exit()             #program se ukončí, je-li nejbližší kontejner vzdálen dál než 10 km

        adresa["properties"]["vzdalenost_ke_kontejneru"] = round(min_vzdalenost)   #do slovniku adresa se přidá nový klíč vzdálenost ke kontejneru
        adresa["properties"]["kontejner"] = nejbliz_kontejner                      # a ještě ID kontejneru
        min_vzdalenost = None  #opět se vynuluje
        vystup.append(adresa)   #do seznamu se přidají vzdálenost od kontejneru a ID

except KeyError:
    print("Soubor nemá všechny požadované atributy")

with open("adresy_kontejnery.geojson","w", encoding="utf-8") as out:       #vytvoří se výstupní soubor a úřídáse výstup seznam
    json.dump(vystup, out, ensure_ascii = False, indent = 2)          

vzdalenosti = [adresa["properties"]["vzdalenost_ke_kontejneru"] for adresa in data_adresy["features"]]
#do proměnné se ukládají nejmenší vzdálenosti
                                          
max_vzdalenost = max(vzdalenosti)    #vybere nehvětší vzdálenosti z celé proměnné nejnižších vzdáleností (vzdalenosti)
index_kontejneru= (vzdalenosti.index(max_vzdalenost))   #najde index maximální vzdálenosti, čímž se uloží/najde adresa toho místa
ulice = data_adresy["features"][index_kontejneru]["properties"]["addr:street"]
cislo_domu = data_adresy["features"][index_kontejneru]["properties"]["addr:housenumber"]

print(f"Průměrná vzdálenost ke kontejneru je {round(mean(vzdalenosti))} m")            
print(f"Medián vzdálenosti ke kontejneru: {round(median(vzdalenosti))} m")               
print(f"Nejdále ke kontejneru je z adresy {ulice} {cislo_domu} a to {round(max_vzdalenost)} m")