import json
from pyproj import Transformer
from statistics import mean, median
from math import sqrt

wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)

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

for adresa in data_adresy["features"]:
    coord_x = adresa["geometry"]["coordinates"][0]
    coord_y = adresa["geometry"]["coordinates"][1] 
    coord_adresy = wgs2jtsk.transform(coord_x,coord_y)



