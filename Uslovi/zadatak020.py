"Proveri da li od dva uneta broja je makar jedan negativan"""
a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
if (a<0) or (b<0):
    print("Barem jedan broj je negativan")
else:
    print("Oba broja su pozitivna.")