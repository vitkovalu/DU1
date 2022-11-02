from turtle import forward, exitonclick, right, left, speed, circle, up, down, goto
import math
a = int(input("napiš počet řádků: "))
while a <1:     #aby tabulka nebyla záporná a 0 (žádná)
    print("Tabulka nelze vytvořit ze záporných čísel a 0")
    a = int(input("napiš počet řádků: "))
b = int(input("napiš počet sloupců: "))
while b <1:
    print("Tabulka nelze vytvořit ze záporných čísel a 0")
    b = int(input("napiš počet řádků: "))
speed(50)
S = 50 #délka strany
U = (math.sqrt(S**2+S**2)) #délka úhlopříčky čtverce
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
o = int((a*b)/2)  #počet opakování
for l in range(o):
    print("Na řadě jsou křížky")
    x= int(input("Zadej sloupec: ")) # určení souřadnic křížku
    while x>a:      #vrátit pokud je zadán sloupec nebo řádek mimo hrací pole
        print("V hracím poli není tolik sloupců")
        x= int(input("Zadej sloupec: "))
    while x<0:      #vrátit pokud je zadán sloupec nebo řádek mimo hrací pole
        print("V hracím poli není tolik sloupců")
        x= int(input("Zadej sloupec: "))
    y= int(input("Zadej řádek: "))
    while y>b:
        print("V hracím poli není tolik sloupců")
        y= int(input("Zadej řádek: "))
    while y<0:
        print("V hracím poli není tolik sloupců")
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
    # určení souřadnic kolečka
    print("Na řadě jsou kolečka")
    xx=int(input("Zadej sloupec: "))
    while xx>a:
        print("V hracím poli není tolik sloupců")
        xx= int(input("Zadej sloupec: "))
    while xx<0:
        print("V hracím poli není tolik sloupců")
        xx= int(input("Zadej sloupec: "))
    yy=int(input("Zadej řádek: "))
    while yy>b:
        print("V hracím poli není tolik sloupců")
        yy= int(input("Zadej řádek: "))
    while yy<0:
        print("V hracím poli není tolik sloupců")
        yy= int(input("Zadej řádek: "))
    up()
    goto(S/2+(xx-1)*S,(yy-1)*S)
    down()
    left(45)
    circle(S/2)
#pro případ že je lichý počet hracích polí
print("Na řadě jsou křížky")
x= int(input("Zadej sloupec: ")) # určení souřadnic křížku
while x>a:
    print("V hracím poli není tolik sloupců")
    x= int(input("Zadej sloupec: "))
while x<0:      #vrátit pokud je zadán sloupec nebo řádek mimo hrací pole
    print("V hracím poli není tolik sloupců")
    x= int(input("Zadej sloupec: "))
y= int(input("Zadej řádek: "))
while y>b:
    print("V hracím poli není tolik sloupců")
    y= int(input("Zadej řádek: "))
while y<0:
    print("V hracím poli není tolik sloupců")
    y= int(input("Zadej řádek: "))
#přesun pro kžížek 
up()
speed(10)
goto (S/2+(x-1)*S,S/2+(y-1)*S)
down() #křížek
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
exitonclick()