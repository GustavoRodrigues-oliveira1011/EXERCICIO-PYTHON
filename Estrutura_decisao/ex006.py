a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
c = float(input("Terceiro número: "))

if a >= b and a >= c:
    print(f"O maior é {a}")
elif b >= a and b >= c:
    print(f"O maior é {b}")
else:
    print(f"O maior é {c}")