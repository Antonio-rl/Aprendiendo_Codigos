def IdentificadorNumeroMayor():
    pytho#Datos entrada
  num1=int(input("Ingrese el Primer valor numerico"))
  num2=int(input("Ingrese el Segundo valor numerico"))
  num3=int(input("Ingrese el Tercer valor numerico"))
    #Proceso
  if(num1>num2 and num1>num3):
    numMayor=num1
  elif num2>num1 and num2>num3:
    numMayor=num2
  else:
  numMayor=num3
  #Datos Salida
  print("El numero mayor es:",numMayor)

IdentificadorNumeroMayor()