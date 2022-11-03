from turtle import forward, exitonclick, right, left, speed, circle, up, down, goto
import math
a = int(input("Napiš počet řádků: "))
while a <1:     #aby tabulka nebyla záporná a 0 (žádná)
    print("Tabulka nelze vytvořit ze záporných čísel a 0")
    a = int(input("Napiš počet řádků: "))
b = int(input("Napiš počet sloupců: "))
while b <1:
    print("Tabulka nelze vytvořit ze záporných čísel a 0")
    b = int(input("Napiš počet sloupců: "))
speed(50)
S = 50 #délka strany
U = (math.sqrt(S**2+S**2)) #délka úhlopříčky čtverce (pro vykreslení křížku)
#nakreslit mřížku
for i in range (a):
    for j in range (b):
        for k in range(4):
            forward(S)
            left(90)
        forward(S)
    left(90)
    forward(S)
    left(90)
    forward(b*S)
    left(180)
c = int(a*b)  #počet opakování
d = 0 #hodnota, ke které se pokaždé připočítá 1 po té co jeden hráč odehraje
#cyklus pro hru
for l in range (c):
    print("Na řadě jsou křížky")
    x= int(input("Zadej sloupec: ")) # určení souřadnic křížku
    while x>b or x<1:      #vrátit pokud je zadán sloupec nebo řádek mimo hrací pole (je větší než počet sloupců nebi menší než 0)
        print("Mimo hrací pole")
        x= int(input("Zadej sloupec: "))
    y= int(input("Zadej řádek: "))
    while y>a or y<1:
        print("Mimo hrací pole") #je větší než počet řádků nebo menší než 0
        y= int(input("Zadej řádek: "))
    #přesun pro kžížek
    up()
    goto (S/2+(x-1)*S,S/2+(y-1)*S)
    down()
    #křížek
    left(45)
    forward(U/2)
    left(180)
    forward(U)
    left(180)
    forward(U/2)
    left(90)
    forward(U/2)
    left(180)
    forward(U)
    d = d+1 #připočítá se, že křížek odehrál
    if d == c:  #kontroluje, jestli uz cislo neni vyšší než počet opakování
        print("Konec hry")
        break #ukončí, už se neopakuje a nevyžaduje další souřadnice
    #určení souřadnic kolečka
    print("Na řadě jsou kolečka")
    xx=int(input("Zadej sloupec: "))
    while xx>b or xx<1:
        print("Mimo hrací pole")
        xx= int(input("Zadej sloupec: "))
    yy=int(input("Zadej řádek: "))
    while yy>a or yy<1:
        print("Mimo hrací pole")
        yy= int(input("Zadej řádek: "))
    up()
    goto(S/2+(xx-1)*S,(yy-1)*S)
    down()
    left(45)      #otočení na správný směr
    circle(S/2)   #kolečko
    d= d+1 #připočítá se, že kolečko odehrálo
    if d == c: #kontroluje
        print("Konec hry")
        break #ukončí   
exitonclick()