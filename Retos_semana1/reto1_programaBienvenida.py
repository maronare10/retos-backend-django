from datetime import datetime


print("==========================================")
print("=========PROGRAMA DE BIENVENIDA===========")
print("==========================================")


nombre = input("Ingrese su nombre : ")
edad = int(input("Ingrese su edad : "))
fechaHoraActual = datetime.now()
horaActual = fechaHoraActual.time()
print(horaActual)

def rangoEdad():
  if (edad <= 17):
    if(horaActual.hour > 18 and horaActual.second > 0):
      print("Debes ir  dormir")
    else:
      print("Usted debe hacer su tarea")
  else:
    print("Ustede no está obligado a hacer nada")

rangoEdad()

