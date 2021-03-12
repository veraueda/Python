segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
minutos = int(segundos) // 60
dias = int(segundos) // 86400
segundos_rest = int(segundos) % 3600
horas = minutos // 3600
minutos_rest = int(minutos) % 60
horas_rest = horas % 60
segundos_rest_final = segundos_rest % 60

print(dias, "dias, ", horas_rest, "horas, ", minutos_rest, "minutos e", segundos_rest_final, "segundos.")