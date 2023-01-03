import json
from pyproj import Transformer
from statistics import mean, median
from math import sqrt

wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)
min_vzdalenost = None
pocet_kontejneru =0

try:
    with open("adresy.geojson", encoding ="utf-8") as adresy:
        data_adresy = json.load(adresy)
except FileNotFoundError:
    print("Soubor neexistuje")
try:
    with open("kontejnery.json", encoding ="utf-8") as kontejnery:
        data_kontejnery = json.load(kontejnery)
except FileNotFoundError:
    print("Soubor neexistuje")

pocet_adres = len(data_adresy["features"])
pocet_kontejnery = len(data_kontejnery["features"])
print(f"{pocet_adres} adres")
print(f"{pocet_kontejnery} kontejnerů")

for adresa in data_adresy["features"]:
    adresa_x = adresa["geometry"]["coordinates"][0]
    adresa_y = adresa["geometry"]["coordinates"][1] 
    coord_adresy = wgs2jtsk.transform(adresa_x,adresa_y)
    for kontejner in data_kontejnery["features"]:
        pristup = kontejner["properties"]["PRISTUP"]
        aktualny_kontajner = kontejner["properties"]["ID"]
        if pristup == "volně":
            pocet_kontejneru+=1
            kontejner_x = kontejner["geometry"]["coordinates"][0]
            kontejner_y = kontejner["geometry"]["coordinates"][1]
            vzdalenost = float(sqrt((coord_adresy[0]-kontejner_x)**2+(coord_adresy[1]-kontejner_y)**2))


