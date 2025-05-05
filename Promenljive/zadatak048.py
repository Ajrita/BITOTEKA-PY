"""Potrebno je da se proveri koliko miligrama kofeina unesemo u toku dana, ako pijemo samo šoljice kafu i čašu koka kolu. 
Jedna šoljica kafe ima 40mg, Jedna čaša koka kole 20mg.
Unos su broj čaša koka kole i broj šoljica kafe"""

cocacola = int(input("Unesi broj čaša kokakole koje popiješ dnevno: "))
kafa = int(input("Unesi broj čaša kafe koje popiješ: "))
šoljica_kafe = 40*kafa
šoljica_kole = 20*cocacola
dnevno = šoljica_kafe + šoljica_kole
print("Ti unosiš", dnevno, "mg kofeina dnevno.")