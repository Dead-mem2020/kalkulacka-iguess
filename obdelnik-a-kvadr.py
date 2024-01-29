#Přivítání uživatele
print("Vítejte v kalkulačce pro obdelníky/kvádry: ")

while(True):
    #Iluze volby
    print("Pro objem zadejte 1: ")
    print("Pro obvod zadejte 2: ")
    print("Pro obsah zadejte 3:")
    print("Pro ukončení programu zadejte 4: ")
    #Deklarace
    volba = input("Zadejte vaši volbu: ")

    if volba == 1:
        print("Zvolil jste si výpočet objemu,hodnoty zadávejte v cm: ")
        a = int(input("Zadejte proměnou a: "))
        b = int(input("Zadejte proměnou b: "))
        c = int(input("Zadejte proměnou c: "))
        if a>0 and b>0 and c>0:
            vypocet = a*b*c
            print("Výsledek je: " ,vypocet " cm/3 ")

    elif volba == 2:
        print("Zvolil jste si výpočet obvodu,hodnoty zadávejte v cm: ")
        a = int(input("Zadejte proměnou a: "))
        b = int(input("Zadejte proměnou b: "))
        if a>0 and b>0:
            vypocet = 2*(a+b)
            print("Výsledek je:" ,vypocet, "cm")
        else:
            print("Ajaj alee,co sis to myslel?")


    elif volba == 3:
        print("Zvolil jste si výpočet obsahu,hodnoty zadávejte v cm: ")
        a = int(input("Zadejte proměnou a: "))
        b = int(input("Zadejte proměnou b: "))
        if a>0 and b>0:
            vypocet = a*b
            print("Výsledek je: " ,vypocet " cm/2 ")

    elif volba == 4:
        print("Program se u...kon...čí...")
        break

    else:
        print("Synt ERROR")