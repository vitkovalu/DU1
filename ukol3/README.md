**VZDÁLENOSTI KE KONTEJNERŮM S TŘÍDĚNÝM ODPADEM**

**UŽIVATELSKÁ DOKUMENTACE**

Program spouští soubory obsahující adresy a kontejnery jedné čtvrti ve formátu JSON a Geo JSON – soubor obsahující adresy musí nést název adresy.geojson , soubor s kontejnery: kontejnery.geojson.

Program vypíše:
- počet načtených adres a kontejnerů
- průměr nejbližších vzdáleností ke kontejneru konejneru
- medián vzdáleností
- adresu vchodu, který má nejdelší vzdálenost ke kontejneru a jeho vzdálenost.

Výstupní soubor s názvem adresy_kontejnery.geojson obsahuje adresy vchodů rozšířené o ID nejbližšího kontejneru a vzdálenost k němu.


**VÝVOJÁŘSKÁ DOKUMENTACE**

Na začátku program spouští soubory adresy.geojson a kontejnery.json, oba soubory jsou oštřeny tak, že v případě že neexistuje nebo není validní JSON/GEOJSON, tak se ukončí. 
Program nejprve spočítá počet načtených kontejnerů a adres, dále postupně prochází adresy ze vstupního souboru a ukládá jejich souřadnice, původně ve WGS, které následně transformuje do S-JTSK. Ve vstupním souboru s kontejnery program neprve hledá ty, které jsou volně přístupny, pro ty opět najde souřadnice, v tom případě jsou rovnou v S-JTSK. Pomocí pythagorovy věty z již známých souřadnic adres vchodů i kontejnerů spočítá vzdálenosti mezi vchody kontejnery. Poté najde minimální vzdálenost kontejneru pro každou adresu. Následně program hledá kontejnery které jsou přístupné pouze obyvatelům domu, v tomto případě se na základě adresy kontejneru přiřadí ke stejn adrese hodnota nejnižší vzdálenosti 0. Zároveň se zaznamenává ID nejbližšího kontejneru.
Další podmínka je vytvořena pro případ, že by byl nejbližší kontejner vzdálen více než 10 km. V tom případě na to program upozorní a ukončí se.

Do seznamu, který bude vložen do výstupního souboru je vložena uprvaená adresa, ke které je nově připsána hodnota vzdálenosti k nejbližšímu kontejneru a jeho ID. 
Výstupním souborem programu je soubor s názvem adresy_kontejnery.geojson.
