"""Koliko jabuka moze da ubere određen broj osoba za određen broj dana pa na kraju pretvorimo jabuke u kg 
(ako je na primer 5 jabuka u kilogramu), ukoliko na primer jedna osoba može da ubere 100 jabuka dnevno, 
koliko mogu da uberu na primer 500 osoba za 30 dana, 2 ulaza (za broj osoba i broj dana) izlaz broj kilograma."""

broj_osoba = int(input("Unesi broj osoba: "))
broj_dana = float(input("Unesi broj dana: "))
dnevno = (broj_osoba*broj_dana)*100
kilo =((broj_osoba*broj_dana)*100)/5
print(broj_osoba,"osoba može za", broj_dana, "dana ubrati", dnevno, "jabuka, što je", kilo, "kg.")