"""Zadatak: Prosečna potrošnja Goriva
Opis: Traži od korisnika da unese pređenu distancu u kilometrima i količinu potrošenog goriva u litrima.
Formula: PotrošnjaNa100km = (PotrošenoGorivo / PređenaDistanca) * 100)"""
km = float(input("Unesi pređenu distancu u km: "))
gorivo = float(input("Unesi potrošeno gorivo u l: "))
prosečna_potrošnja = (gorivo/km) * 100
print("Prosečna potrošnja goriva tvog automobila je", prosečna_potrošnja, " litara na 100 km.")
