#Uvítat uživatele
print("Vítej v aplikaci mučení a výpočtů.Dnes můžeme počítat pouze obsahy obdelníků")
#deklarace (spíše inicializace) proměných
a = input("Zadejte proměnou a: ")
b = input("Zadejte proměnou b: ")
#NEZAPOMENOUT NA PŘETYOVÁNÍ ZE STRINGU NA INTEGER
a = int(a)
b = int(b)
#podmínka, kontrola,zda v proměných není zápor
if a>0 and b>0:
    vysledek = a*b
    print("Výsledek je: ", vysledek)
#Pokud neplatí první podmínka,tak vždy se provede else
else:
    print("S těmahle kusama mi připadáš jak vopica,si radši na to dam cigánka,sponzor pořadu")