from datetime import datetime


cantidadPersonasIngresar = int(input("Ingrese la cantidad de personas que desea registrar: "))
personas = []

# # print(range(6))

# # for n in [1,2,3,4,5,6]:
# #   print(n)

# # for y in range(cantidadPersonasIngresar):
# #   print(y)


# # for y in range(cantidadPersonasIngresar):
# #   nombrePersona = input("Ingrese el nombre : ")
# #   numDni = input("Ingrese el número de su DNI :")
# #   fechNacimiento = input("Ingrese su fecha de nacimiento aaaa/mm/dd : ")
# #   persona = {
# #     "Nombre": nombrePersona,
# #     "Dni": numDni,
# #     "Fecha de Nacimiento": fechNacimiento
# #   }

# #   personas.append(persona)

# # print(personas)




c = 0
while c < cantidadPersonasIngresar:
  nombrePersona = input("Ingrese el nombre : ")
  numDni = input("Ingrese el número de su DNI :")
  fechNacimiento = input("Ingrese su fecha de nacimiento aaaa/mm/dd : ")
  persona = {
    "Nombre": nombrePersona,
    "Dni": numDni,
    "Fecha de Nacimiento": fechNacimiento
  }
  personas.append(persona)
  
  c=c+1

def sortByDate(persona):
  return datetime.strptime(persona["Fecha de Nacimiento"], '%Y/%m/%d')

personas.sort(key=sortByDate)

print(personas)



# fechas = ["1872/04/13", "2021/03/12","1886/05/12"]

# #fecha = datetime.strptime("1982/12/03", '%Y/%m/%d')


# fechas.sort(key=sortByDate)

# print(fechas)








# class Persona:
#   def __init__(self, nombre, dni, fechaNacimiento):
#     self.nombre = nombre
#     self.dni = dni
#     self.fechaNacimiento = fechaNacimiento
