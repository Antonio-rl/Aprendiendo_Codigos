def tablademultiplicar():
    texto=' TABLA DE MULTIPLICAR '
    print(format(texto,'=^100'))
    k=int(input("Digite el numero que desea multiplacar:"))
    for i in range(1,13):
        print(f'{i} x {k} = {i*k}')
tablademultiplicar()