"""Zadatak: Godine do Penzije
Opis: Traži od korisnika njegove trenutne godine i željene godine za odlazak u penziju.
Zadatak: Izračunaj i ispiši koliko godina mu je ostalo do penzije."""

godine = int(input("Koliko imaš godina: "))
penzionisanje = int(input("U kojoj godini ćeš se penzionisati? "))
arbajt = penzionisanje - godine
print("Do penzije ti je ostalo još", arbajt, "godina.")