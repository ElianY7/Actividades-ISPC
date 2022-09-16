class Consola:
  def __init__(self, modelo, agno_salida, cant_juegos):
    self.modelo = modelo  
    self.agno_salida = agno_salida
    self.cant_juegos = cant_juegos
    self.encendido = False
  
  def __str__(self):
    return self.modelo + " fue lanzado en el año " + self.agno_salida + " y tiene " + self.cant_juegos + " juegos."

  def encender(self):
    self.encendido = True
    print("\nLa consola " + self.modelo + " fue encendida.\n")


class Consola_Portatil(Consola):
    def __init__(self, modelo, agno_salida, cant_juegos, bateria, pantalla):
      Consola.__init__(self, modelo, agno_salida, cant_juegos)
      self.bateria = bateria
      self.pantalla = pantalla
      self.carga = False
   
    def __str__(self):
      return Consola.__str__(self) + "\nLa capacidad de su bateria es de " + self.bateria + "mAh y su pantalla es de tipo " + self.pantalla + "."

    def cargar(self):
      self.carga = True
      print("\nLa consola " + self.modelo + " esta siendo cargada.\n")


psp_1000 = Consola_Portatil("PSP", "2005", "398", "1200", "TFT LCD")
nintendo_switch = Consola_Portatil("Nintendo Switch", "2017", "7165", "4310", "IPS LCD")
play_1 = Consola("PS1", "1994", "2418")

print(psp_1000)
psp_1000.cargar()

print(nintendo_switch)
nintendo_switch.encender()

print(play_1)
play_1.encender()

