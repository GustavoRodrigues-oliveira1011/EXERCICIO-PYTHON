a = float(input("Num 1: "))
b = float(input("Num 2: "))
c = float(input("Num 3: "))

if a < b: a, b = b, a
if a < c: a, c = c, a
if b < c: b, c = c, b

print(f"Ordem decrescente: {a}, {b}, {c}")