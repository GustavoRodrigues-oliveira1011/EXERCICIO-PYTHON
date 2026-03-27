def calcular_km(valor_pago, bandeirada=4.60, preco_km=0.96):
    if valor_pago < bandeirada:
        return "Valor insuficiente para a bandeirada."
    
    valor_rodado = valor_pago - bandeirada
    distancia = valor_rodado / preco_km
    return distancia

valor_pago_usuario = float(input("Quanto você pagou pela corrida? R$ "))

resultado = calcular_km(valor_pago_usuario)

if type(resultado) == float:
    print(f"Você percorreu {resultado:.2f} km.")
else:
    print(resultado)