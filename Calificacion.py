# Módulo 1
# Primer programa

print("Promedio de sus calificaciones")

#Desarrollo = 60
#Habilidades_Socioemocionales = 20
#Inglés = 2

Desarrollo = float(input("Ingrese su nota de Desarrollo \n"))
Ingles = float(input("Ingresa tu nota de Inglés \n"))
Habilidades_Socioemocionales = float(input("Ingresa tu nota de Habilidades Socioemocionales \n"))

Promedio = (Desarrollo * 0.6) + (Ingles * 0.2) + (Habilidades_Socioemocionales * 0.2)

print(Promedio)

if Promedio <= 30:
    print("Su resultado ha sido regular")

elif Promedio >= 40:
    print("su resultado ha sido bueno")

elif Promedio > 80:
    print("Su resultado ha sido excelente")

else:
    print("Error, intente ingresar las notas nuevamente")
