data = input("Digite a data (dd/mm/aaaa): ")

partes = data.split("/")

dia = partes[0]
mes_indice = int(partes[1]) - 1
ano = partes[2]


meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

nome_mes = meses[mes_indice]

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")