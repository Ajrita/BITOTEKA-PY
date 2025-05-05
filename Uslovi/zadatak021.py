"""Imamo web prodavnicu koja prodaje fejk parfeme (duplikate) i jedan parfem kosta 2hiljade dinara. 
Postarina za dostavu je 200 dinara, ali ako naruce u vrednosti od 10hiljada i vise onda je besplatna, 
prikazati koliko treba covek da plati ako hoce da kupi odredjen broj parfema,
input (ulaz) nam je samo koliko parfema hoce da kupi, na primer 2"""

parfemi = int(input("Koliko parfema želite da kupite: "))
cena_s_ptt = (parfemi * 2000) + 200
cena = (parfemi * 2000)

if cena >= 10000:
    print("Vaš račun je", cena, "din.")
elif cena >= 2000 and cena < 10000:
    print("Vaš račun je", cena_s_ptt, "din.")
else:
    print("Unos je nevalidan.")