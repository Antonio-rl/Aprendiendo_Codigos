def Suma10n():
  #definiendo variable e inicializando variables
  contador,numero,suma=0,0,0
  #proceso y datos de entrada
  while contador<10:
    contador=contador+1
    numero=float(input(f"Ingrese el numero de la posicion {contador}:"))
    suma=suma+numero
  print(f"La suma de los 10 numeros ingresadoses: {suma}")
Suma10n()