p1 = float(input("Preço do produto 1: "))
p2 = float(input("Preço do produto 2: "))
p3 = float(input("Preço do produto 3: "))

if p1 < p2 and p1 < p3:
    print("Compre o produto 1")
elif p2 < p1 and p2 < p3:
    print("Compre o produto 2")
else:
    print("Compre o produto 3")