def CalcularPrecioLapiz():
    #Datos Entrada
  cantidadL=int(input("Ingrese la cantidad de lapices:"))
    #Proceso
  if(cantidadL>=1000):
    costoPagar=cantidadL*0.85
  else:
    costoPagar=cantidadL*0.9
    #Datos Salida
  print("El costo total a pagar es:",costoPagar)
CalcularPrecioLapiz()