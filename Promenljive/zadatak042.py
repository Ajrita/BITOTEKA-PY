#prebacivanje/kastrovanje u tip promenljive - boolean
print(bool("")) #False jer nemamo ništa
print(bool(0)) #O nula broj je False kada pređe u bool
print(bool(0.0)) #O nula broj je False
print(bool("False")) #Bilo koji string koji nije prazan je True
print(bool("0")) #True
print(bool(" ")) #True
print(bool(123)) #True
print(bool(-99)) #True
print(bool(0.99)) #True

a = 0
b = bool(a)
print(b) #False