class Edificacion:

  def __init__(self, nombre, m2, pisos, altura):
    self.nombre = nombre
    self.m2 = m2
    self.pisos = pisos
    self.altura = altura

  def __str__(self):
    return self.nombre + " posee " + self.m2 + " metros cuadrados y tiene " + self.pisos + " pisos. Además su altura es de " + self.altura + "m.\n"

  
class Institucion_Educativa(Edificacion):

  def __init__(self, nombre, m2, pisos, altura, alumnos, aulas, cantinas, bibliotecas):
    Edificacion.__init__(self, nombre, m2, pisos, altura)
    self.alumnos = alumnos
    self.aulas = aulas
    self.cantinas = cantinas
    self.bibliotecas = bibliotecas

  def __str__(self):
    return Edificacion.__str__(self) + "Esta institución educativa alberga " + self.alumnos + " estudiantes los cuales estan distribuidos en " + self.aulas + " aulas y tienen a su disposición " + self.cantinas + " cantina/s y " + self.bibliotecas + " biblioteca/s.\n"
  

colegio_san_herrera = Institucion_Educativa("San Herrera", "6167", "2", "9", "1120", "20", "2", "1")
empire_state = Edificacion("Empire State", "8094", "102", "443,5")

print(colegio_san_herrera)

print(empire_state)
