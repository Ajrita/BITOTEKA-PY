"""ZADATAK 001: Da li imaš pravo na popust?
Tekst zadatka:
Napiši program koji traži od korisnika da unese svoj broj godina i zatim proverava da li ima pravo na popust.
Pravo na popust imaju sledeće kategorije korisnika:
svi koji imaju manje od 18 godina
svi koji imaju više od 65 godina
korisnici koji imaju tačno 18 ili tačno 65 godina nemaju pravo na popust.
Program treba da obradi korisnikov unos i prikaže odgovarajuću poruku:
"Imaš pravo na popust." ako korisnik ispunjava uslove
"Nemaš pravo na popust." ako ne ispunjava"""

godine = int(input("Unesi broj svojih godina: "))

if (godine > 0 and godine < 18) or (godine > 0 and godine > 65):
    print("Imaš pravo na popust.")
else:
    print("Nemaš pravo na popust.")