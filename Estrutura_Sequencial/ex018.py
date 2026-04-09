tamanho_mb = float(input("Tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Velocidade da internet (Mbps): "))

tempo_segundos = (tamanho_mb * 8) / velocidade_mbps 
tempo_minutos = tempo_segundos / 60  
100
print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.") 