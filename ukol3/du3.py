import json
from pyproj import Transformer

wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)

with open("adresy.geojson", encoding ="utf-8") as f:
    data = json.load(f)

with open("kontejnery.json", encoding ="utf-8") as g:
    data = json.load(g)