import json
from pyproj import Transformer

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



