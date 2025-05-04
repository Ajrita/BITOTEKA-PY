"""Mašina puni 0.75 litara u jednu bocu, svaka mašina puni 30 boca za jedan sat. Koliko litara može da napuni određen broj mašina za određen broj sati?
Unesemo broj mašina, i posle broj sati i dobijemo broj litara, može i broj boca koje se napune, ali tražimo litre"""
mašine = int(input("Unesi broj mašina: "))
sati = float(input("Unesi broj sati: "))
norma_na_sat = mašine*30*0.75
krajnji_rezultat = norma_na_sat*sati
print("Za zadati opseg, može se dobiti", krajnji_rezultat, "litara.")