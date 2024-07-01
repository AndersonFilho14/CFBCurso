class Casa:
    taman_max=500
    energia = False
    cor = "Branca"

c1 = Casa()
c2 = Casa()
c3 = Casa()


c1.taman_max = 200
c1.cor = "preta"
c1.energia = True

print(f"o c1 é {c1.cor,c1.energia,c1.taman_max}")
print(f"o C2 é {c2.cor,c2.energia,c2.taman_max}")