**VZDÁLENOSTI KE KONTEJNERŮM S TŘÍDĚNÝM ODPADEM**

**UŽIVATELSKÁ DOKUMENTACE**

Program spouští soubory s obsahující adresy a kontejnery jedné čtvrti ve formátu JSON a Geo JSON – soubor obsahující adresy musí nést názvem adresy.geojson , soubor s kontejnery kontejnery.geojson. Pokud je název souboru špatně zadán, program oznámí že soubor neexistuje.

Program ze vstupnícg dat vypíše počet načtených adres a kontejnerů. Dále vypíše průměr nejbližších vzdáleností ke kontejneru konejneru, medián vzdáleností a adresu vchodu, který má nejdelší vzdálenost ke kontejneru a jeho vzdálenost. Pokud je adresa nejbližšího kontejneru větší než 10 km, program skončí

Výstupní soubor s názvem adresy_kontejnery.geojson obsahuje adresy rozšířené o ID nejbližšího kontejneru a vzdálenost k němu.


**VÝVOJÁŘSKÁ DOKUMENTACE**

