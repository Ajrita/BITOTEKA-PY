# Računanje nove cene i uštede nakon popusta
cena = float(input("Unesite cenu proizvoda: "))
popust = float(input("Unesite popust: "))
nova_cena = cena - (cena * popust/100)
usteda = cena - nova_cena
print ("Nova cena proizvoda je", nova_cena, " a ušteda je", usteda, "din.")