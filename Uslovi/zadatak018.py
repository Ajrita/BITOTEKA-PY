#mali kalkulator sa sabiranjem, oduzimanjem i množenjem
a = float(input("Unesite prvi broj:"))
b = float(input("Unesite drugi broj:"))
operacija = input("Unesite operaciju (+,- ili *): ")
if operacija == '+':
    print ("Rešenje je", a+b)
elif operacija == "-":
    print("Rešenje je:", a-b)
elif operacija == "*":
    print("Rešenje je:", a*b)
else:
    print("Nepoznata operacija.")
