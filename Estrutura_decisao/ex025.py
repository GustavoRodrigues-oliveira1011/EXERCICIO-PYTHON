print("Responda apenas com 'S' para sim ou 'N' para não:")
p1 = input("Telefonou para a vítima? ").upper()
p2 = input("Esteve no local do crime? ").upper()
p3 = input("Mora perto da vítima? ").upper()
p4 = input("Devia para a vítima? ").upper()
p5 = input("Já trabalhou com a vítima? ").upper()

pontos = 0
if p1 == "S": pontos += 1
if p2 == "S": pontos += 1
if p3 == "S": pontos += 1
if p4 == "S": pontos += 1
if p5 == "S": pontos += 1

if pontos == 2:
    print("\nClassificação: Suspeita")
elif 3 <= pontos <= 4:
    print("\nClassificação: Cúmplice")
elif pontos == 5:
    print("\nClassificação: Assassino")
else:
    print("\nClassificação: Inocente")