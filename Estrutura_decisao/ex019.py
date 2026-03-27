numero = int(input("Digite um número menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

partes = []

if centenas > 0:
    texto = f"{centenas} centena" if centenas == 1 else f"{centenas} centenas"
    partes.append(texto)

if dezenas > 0:
    texto = f"{dezenas} dezena" if dezenas == 1 else f"{dezenas} dezenas"
    partes.append(texto)

if unidades > 0:
    texto = f"{unidades} unidade" if unidades == 1 else f"{unidades} unidades"
    partes.append(texto)

resultado = ", ".join(partes[:-1])
if len(partes) > 1:
    resultado += " e " + partes[-1]
else:
    resultado = partes[0] if partes else "0 unidades"

print(f"Resultado: {resultado}")