stranica = int(input("Unesite stranicu kvadrata: "))
izbor = input("Unesite 'p' za površinu a 'o' za obim: ")
if izbor == 'p':
    print("Površina je:", stranica * stranica)
elif izbor == 'o':
    print("Obim je:", 4 * stranica)
else:
    print("Nevalidan izbor.")