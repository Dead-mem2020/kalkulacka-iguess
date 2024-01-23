#přivítání uživatele
print("Vítám tě v kalkulačce na obvod obdelníků!")
 #deklarace (spíše inicializace) proměných
a = input("Zadejte proměnou a: ")
b = input("Zadejte proměnou b: ")
#přetypování z stringu na int
a = int(a)
b = int(b)

#podmínka, kontrola,zda v proměných není zápor
if a>0 and b>0:
    vysledek = 2*a+2*b
    print("Výsledek je: ", vysledek)

#pokud nebude platit první odmínka, provede se vždy else
else:
    #dáváme uživateli vědět,že je to kre-
    print("YOU STUPID NI-")
