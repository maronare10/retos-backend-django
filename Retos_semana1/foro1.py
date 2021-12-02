class Persona:
  def __init__(self, nombre,sexo,fechaNacimiento):
    self.__nombre = nombre
    self.__sexo = sexo
    self.__fechaNacimiento = fechaNacimiento 

  def saludar(self):
    print("Hola soy" + self.__nombre + "naci el" + self.__fechaNacimiento)


class Profesor(Persona):
  def __init__(self):
    super().__init__()

class Alumno(Persona):
  def __init__(self):
    super().__init__()

profesor = Profesor("mariana","femenino","3-12-1982")
profesor.saludar()

