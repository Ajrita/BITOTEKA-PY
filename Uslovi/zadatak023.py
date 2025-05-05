"""Trazimo od korisnika da unese neku lozinku i procenimo po duzini da li je prihvatljiva,
 imamo funkciju len koja proverava duzinu stringa(teksta) i ukoliko je 8 ili vise karaktera kazemo da je prihvatljiva,
 ukoliko nije kazemo da nije"""

lozinka= input("Unesi lozinku: ")
if len(lozinka)<8:
    print("Lozinka je neprihvatljiva.")
else:
    print("Lozinka je prihvatljiva.")