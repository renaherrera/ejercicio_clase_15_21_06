import os
from functions import *

cine = [["O","O","O","O"], ["O","O","O","O"], ["O","O","O","O"], ["O","O","O","O"], ["O","O","O","O"]]
clientes = []

while True:
    opc = menu( [1,2,3,4,5] )

    if opc == 1:
        print("\tPantalla >>")
        print("\t============================")
        for c in cine:
            for a in c:
                print("\t",a, end=" ")
            print()
    elif opc == 2:
        asiento_fila = int(input("Ingrese la fila de su asiento: "))
        asiento_columna = int(input("Ingrese la columna del asiento: "))
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")
        telefono = input("Ingrese su número de teléfono: ")

        cliente = [nombre, edad, telefono, asiento_fila, asiento_columna]

        clientes.append(cliente)

        fila = cine[asiento_fila-1]
        fila[asiento_columna-1] = "X"
    elif opc == 3:
        for i in range(len(clientes)):
            print(f"Cliente {i+1}")
            print(f"\tNombre: {clientes[i][0]}")
            print(f"\tEdad: {clientes[i][1]}")
            print(f"\tNum. Teléfono: {clientes[i][2]}")
            print(f"\tFila: {clientes[i][3]}")
            print(f"\tColumna: {clientes[i][4]}")
    elif opc == 4:
        pass
    else:
        print("ADIOS!")
        break