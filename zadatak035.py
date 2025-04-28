"""Zadatak: Planiranje putovanja
Napiši program koji:
Traži od korisnika da unese svoje ime.
Traži da unese broj kilometara koje želi da pređe.
Traži da unese prosečnu brzinu kretanja (km/h).

Program treba da:
Izračuna koliko sati će trajati putovanje (koristeći deljenje: kilometara / brzina).
Ispiše prijateljsku poruku sa rezultatima."""

ime = input("Zdravo, unesi svoje ime: ")
km = float(input("Unesi koliko km želiš da pređeš: "))
brzina = float(input("Unesi brzinu kojom želiš da se krećeš: "))
sati= km/brzina
print(ime+",tvoje putovanje će trajati", sati, "sati. Srećan put," + ime + "!")