# **VZDÁLENOSTI KE KONTEJNERŮM S TŘÍDĚNÝM ODPADEM**

**UŽIVATELSKÁ DOKUMENTACE**

Program spouští soubory obsahující adresy a kontejnery jedné čtvrti ve formátu JSON a GeoJSON – soubor obsahující adresy s názvem *adresy.geojson* musí nést atributy názvu ulice "addr:street", čísla domu "addr:housenumber" a souřadnice "coordinates" v souřadnicovém systému WGS, a soubor s kontejnery s názvem *kontejnery.json*  musí obsahovat atributy uvádějící adresu kontejneru "STATIONNAME", "PRISTUP" – uvedeno, zda je kontejner volně přístupný nebo pouze obyvatelům domu, a souřadnice "coordinates" v S-JTSK.

Program vypíše:
- počet načtených adres a kontejnerů
- průměr nejbližších vzdáleností ke kontejneru
- medián vzdáleností
- adresu vchodu, který má nejdelší vzdálenost ke kontejneru a jeho vzdálenost.

Výstupní soubor s názvem *adresy_kontejnery.geojson* obsahuje adresy vchodů rozšířené o ID nejbližšího kontejneru a vzdálenost k němu.


**VÝVOJÁŘSKÁ DOKUMENTACE**

Na začátku program spouští soubory *adresy.geojson* a *kontejnery.json*, oba soubory jsou ošetřeny tak, že se ukončí v případě že neexistuje, není validní JSON/GeoJSON nebo program nemá k otevření vstupního souboru oprávnění.

Program nejprve spočítá počet načtených kontejnerů a adres, dále postupně prochází adresy ze vstupního souboru a ukládá jejich souřadnice, původně ve WGS, které následně transformuje do S-JTSK. Ve vstupním souboru s kontejnery program nejprve hledá ty, které jsou volně přístupny, pro ty opět najde souřadnice, v tom případě jsou rovnou v S-JTSK. Pomocí pythagorovy věty z již známých souřadnic adres vchodů i kontejnerů spočítá vzdálenosti mezi vchody a kontejnery. Poté najde minimální vzdálenost kontejneru pro každou adresu. Následně program hledá kontejnery, které jsou přístupné pouze obyvatelům domu, v tomto případě se na základě adresy kontejneru přiřadí ke stejné adrese hodnota nejnižší vzdálenosti 0. Zároveň se zaznamenává ID nejbližšího kontejneru.
Další podmínka je vytvořena pro případ, že by byl nejbližší kontejner vzdálen více než 10 km. V tom případě na to program upozorní a ukončí se.

Do seznamu s adresami, který bude vložen do výstupního souboru, jsou připisovány hodnoty vzdálenosti k nejbližšímu kontejneru a jeho ID.
Výstupním souborem programu je soubor s názvem *adresy_kontejnery.geojson*. Atribut "vzdalenost_ke_kontejneru" uvádí v metrech vzdálenost k nejbližšímu kontejneru a "kontejner" ID nejbližšího kontejneru.
