"""Vožnja taksijem: Početak vožnje taksijem je 100 dinara, svaki minut vožnje je 10 dinara, 
svaki pređeni kilometar je 50 dinara. Input su minuti i broj pređenih kilometara"""

km = float(input("Unesi pređene km: "))
min = float(input("Unesi minutažu putovanja: "))
start = 100
pređeni_km = 50*km
otkucan_minut= 10*min
cena = start + (pređeni_km + otkucan_minut)
print("Iznos računa za vožnju je:", cena, "din.")