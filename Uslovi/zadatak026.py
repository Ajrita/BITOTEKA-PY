"""ZADATAK 003: Temperaturna zona
Tekst zadatka:
Unesi temperaturu u stepenima Celzijusa.
Na osnovu te vrednosti, ispiši kakav je osećaj napolju:
Ako je temperatura manja od 10, ispiši: "Hladno"
Ako je temperatura od 10 do 24, ispiši: "Umereno"
Ako je temperatura od 25 do 34, ispiši: "Toplo"
Ako je temperatura 35 ili više, ispiši: "Vruće" """

temperatura = float(input("Unesi temperaturu u Celzijusima: "))

if temperatura < 10:
    print("Hladno")
elif temperatura >= 10 and temperatura <= 24:
    print("Umereno")
elif temperatura >= 25 and temperatura <= 34:
    print("Toplo")
elif temperatura >=35:
    print ("Vruće")