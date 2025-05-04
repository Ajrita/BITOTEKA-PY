"""Zadatak: Pretvaranje minuta u sekunde i sate
Korisnik unosi broj minuta u konzoli (može biti ceo ili decimalni broj).

Program treba da izračuna:
koliko sekundi ima u unetom broju minuta (1 minut = 60 sekundi)
koliko sati ima u unetom broju minuta (1 sat = 60 minuta)

Na kraju ispis u konzoli:
U ___ minuta ima ___ sekundi ili ___ sati."""

minuti=float(input("Unesite minute: "))
sekunde = minuti*60
sati = minuti/60
print("U",minuti, "minuta ima",sekunde, "sekundi ili", sati, "sati")

