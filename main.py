from model.Persona import Persona
from model.curso import Curso

objPersona = Persona("Luis", "Salvatierra", "70504923", "diegollavemorales@gmail.com")
objPersona.saludar()

objCurso = Curso("C362635", "EPPO 1", 5)
objCurso.bienvenido()
objCurso.set_nombre("Base de Datos")
objCurso.set_credito(4)
objCurso.bienvenido()