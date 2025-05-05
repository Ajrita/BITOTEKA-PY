"""Dajemo korisniku da unese trenutnu temperaturu, i vracamo mu kako da se obuce, na primer, 
ukoliko je ispod 8stepeni kazemo mu debela jakna, ukoliko je ispod 20 tanka jakna,
ukoliko je ispod 25 moze duks, ukoliko je preko moze majica"""

temperatura = float(input("Unesi trenutnu temperaturu: "))
if temperatura < 8:
    print("Obuci debelu jaknu.")
elif temperatura >= 8 and temperatura < 20:
    print("Obuci tanku jaknu.")
elif temperatura >= 20 and temperatura < 25:
    print("Možeš samo u duksu da izađeš.")
elif temperatura >= 25:
    print("Možeš samo u majici da izađeš.")
else:
    print("Unos je nevalidan")
