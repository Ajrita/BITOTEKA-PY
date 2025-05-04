print(bool("")) #False jer nemamo ništa
print(bool(0)) #O nula broj je False kada pređe u bool
print(bool(0.0)) #False
print(bool("False")) #True
print(bool("0")) #True
print(bool(" ")) #True
print(bool(123)) #True
print(bool(-99)) #True
print(bool(0.99)) #True

a = 0
b = bool(a)
print(b) #False