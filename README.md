# DU1
Uživatelská dokumentace
Program načítá vstupní soubor pojmenovaný vstup.csv, obsahující průměrné říční průtoky. Program vypočítá do výstupového souboru vystup_7dni.csv sedmidenní průtoky vstupních dat a do souboru vystup_rok.csv roční průměry. Na konci vypíše nejvyšší a nejnižší průtok ze vstupních dat spolu s datem, ve kterém k nim došlo.
Vstupní data musí být v tomto formátu:
	139000,QD,10.11.1980,   0.6700
139000,QD,11.11.1980,   0.5800
139000,QD,12.11.1980,   0.5800
139000,QD,13.11.1980,   0.5800
	
Vývojářská dokumentace
Na začátku jsou do programu naimportovány moduly csv a math, které budou potřeba.
Výjimka FileNotFoundError kontroluje jestli soubor s takovým názvem existuje.
Pomocí funkce with open je otevřen vstupní soubor, a s označením 'w' výstupový soubor.
Jednotlivé řádky jsou počítny pomocí cyklu a pomocí funkce enumarate jsou jednotlivé řádky postupně očíslovány. Do proměnné sum_tyden je postupně ukládán součet průtoků v poslední řádku. Pomocí podmínky hledá program první řádek ze sedmi dnů. Další podmínka ukládá do proměnné sedmidenni průměry spočtené za pomoci proměnné sum_tyden. Na konci podmínky je součet opět vynulován.
Opět je otevřen soubor vstup.csv a pro zapisování vytvořen vystup_rok.csv
V rámci for cyklu pro všechny řádky, funkce split rozdělila sloupec s datem. První podmínka hledá první řádek. Druhá podmínka platí pokud není proměnná rok stejná jako sloupec s rokem (datum_split[-1]). Do proměnné prumer_rok ukládá vypočtené průmery pomocí sum_rok/dny. Na konci podmínky je suma a počet dní v roce opět vynulovány. Po proběhnutí podmínky je do proměnné rok uložen nový sloupec s rokem a do proměnné sum_rok se opět sčítá poslední sloupec s průtoky a přičítají se jednotlivé dny. Poslední rok v datech není v rámci podmínky vypočten, takže pro něj je ještě vytvořen vlastní vypočet a výsledek pomocí append přidán.
Program prochází řádky a hledá hodnotu která je větší než dosavadní maximum – na začátku 0. Nové hodnoty ukládá do proměnné maximum, do proměnné datum_max uloží konkrétní datum.
Podobně prochází program a hledá hodnoty nižší než minimum – na počátku nekonečno a nové hodnoty zapisuje do proměnné minimum. Současně zapíše datum, kterého dne se průtok nachází.![image](https://user-images.githubusercontent.com/116714488/206853402-2f8633ed-b518-4596-af97-fce0c785a25c.png)
