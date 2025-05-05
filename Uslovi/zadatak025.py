"""ZADATAK 002: Da li možeš da polažeš vožnju?
Tekst zadatka:
Unesi koliko godina imaš i da li imaš ličnu kartu 
(odgovori sa "ima" ili "nema"). Vožnja se može polagati samo ako osoba ima 17 ili više godina i ima ličnu kartu."""

godine = float(input("Unesi broj godina: "))
lk = input("Da li imaš ličnu kartu (imam/nemam): ")

if godine >=17 and lk == 'imam':
    print("Možeš polagati vožnju.")
else:
    print("Ne možeš polagati vožnju.")
