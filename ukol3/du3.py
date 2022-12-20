#ukol3
import json

with open("adresy.geojson", encoding ="utf-8") as f:
    data = json.load(f)

with open("kontejnery.json", encoding ="utf-8") as g:
    data = json.load(g)