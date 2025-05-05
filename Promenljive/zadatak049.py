"""Trošak struje: Čovek koji čita merač struje dolazi prvog u mesecu, dođe svakog meseca i 
pročita broj kwh struje koliko je potrošeno i zapiše, i svakog meseca se povećava broj,
on unosi prethodni mesec i ovaj mesec u program, i dobija koliko je potrošeno struje u dinarima.
Postoji mesečna fiksna pretplata od 1000 dinara i za svaki 1kwh potroši se 10dinara"""

prošli_mesec = float(input("Unesite utrošak za prethodni mesec: "))
trenutni_mesec = float(input("Unesite utrošak za ovaj mesec: "))
fiksna_pretplata = 1000
utrošak= trenutni_mesec - prošli_mesec
potrošnja = 10*utrošak
print("Vaš račun je", fiksna_pretplata+potrošnja, "din.")