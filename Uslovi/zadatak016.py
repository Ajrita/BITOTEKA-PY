"""Za unet broj poena 0-100, ispišite ocenu
5 -> 0-50
6 -> 51-60
7 -> 61-70
8 -> 71-80
9 -> 81-90
10 -> 91-100"""

poeni = int(input("Unesite broj poena: "))
if poeni>= 0 and poeni<51:
    print("Pao si, tvoja ocena je 5")
elif poeni>50 and poeni<61:
    print("Dobio si 6.")
elif poeni >60 and poeni<71:
    print("Dobio si 7.")
elif poeni >70 and poeni<81:
    print("Dobio si 8.")
elif poeni >80 and poeni<91:
    print("Dobio si 9.")
elif poeni >90 and poeni<=100:
    print("Dobio si 10.")
else:
    print("Nevalidan broj poena.")