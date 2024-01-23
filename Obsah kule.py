#Uvítat uživatele
print("Buď zdráv,cestovateli!Chceš si vypočítat obsah kruhu?Nic neříkej,samozřejmě že chceš!Tak pojď,sedni si sem")
#deklarace (spíše inicializace) proměných
r = input("Táák,zadej mi poloměr (r) tvého kruhu a já to vypočítám: ")
#přetypování z stringu na int
r = int(r)
#podmínka, kontrola,zda v proměných není zápor
if 0>r:
     print("Ah,cestovateli,nejste tak moudrý,jak jste mi připadal.....ZVEDNĚTE SE A ODEJDĚTE IHNED!!")
#Pokud neplatí první podmínka,tak vždy se provede else
else:
   S = 3,14*(r**2)
   print("Jednoduché!Výsledek je: ", S)
