#Uvítat uživatele
print("Vítej,můj příteli.Pojďme spolu vypočítat nějaké obvody kvádrů")
#deklarace (spíše inicializace) proměných
a = input("Zadej mi stranu a: ")
b = input("Zadej stranu b: ")
c = input("A nakonec mi zadej stranu c: ")
#přetypování z stringu na int
a = int(a)
b = int(b)
c = int(c)
#podmínka, kontrola,zda v proměných není zápor
if a>0 and b>0 and c>0:
    vysledek = a*b*c
    print("Tenhle výsledek je: ", vysledek)
#Pokud neplatí první podmínka,tak vždy se provede else
else:
    print("Zdá se,že jsi neprošel druhou třídu ty KOK-")