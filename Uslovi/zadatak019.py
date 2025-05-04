#Unos iznosa u dinarima se konvertuje u evre ili dolare
#usd: rsd/100
#eur: rsd/117
iznos = float(input("Unesite iznos u dinarima: "))
izbor = input("Izaberi valutu za konverziju (usd ili eur): ")
if izbor == "usd":
    print("Vaš iznos je", iznos/100, "dolara")
elif izbor == "eur":
     print("Vaš iznos je", iznos/117, "evra")
else:
     print("Nevalidan unos")