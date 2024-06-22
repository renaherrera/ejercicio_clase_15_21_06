import os
import datetime
import csv
import msvcrt

cine = [["O","O","O","O"], ["O","O","O","O"], ["O","O","O","O"], ["O","O","O","O"], ["O","O","O","O"]]
clientes = []
total_recaudado = 0

def menu(opciones):
    while True:
        print("MENU")
        print("-"*30)
        print("1. Mostrar asientos disponibles")
        print("2. Comprar entrada")
        print("3. Mostrar ventas realizadas")
        print("4. Generar archivo CSV de ventas")
        print("5. Salir")
        print("-"*30)
        
        try:
            opc = int(input("Ingrese la opción: "))

            if opc in opciones:
                break
            else:
                presionar_tecla_message("ERROR! opción incorrecta!")
        except:
            presionar_tecla_message("ERROR! el valor no es número")
    return opc

def opcion1():
    print("\tPantalla >>")
    print("\t============================")
    for c in cine:
        for a in c:
            print("\t",a, end=" ")
        print()
    presionar_tecla()

def opcion2():
    global total_recaudado
    asiento_columna,asiento_fila = validacion_asientos()
    nombre = validacion_nombre()
    edad = validacion_edad_precio("Ingrese su edad: ")
    telefono = validacion_telefono()
    precio = validacion_edad_precio("Ingrese el precio: ")
    
    if edad <= 18:
        os.system("cls")
        print("Aplica descuento de 20% por adolecente")
        precio = precio * 80/100
        total_recaudado += precio
    elif edad >= 65:
        os.system("cls")
        print("Aplica descuento de 15% por adulto mayor")
        precio = precio * 85/100
        total_recaudado += precio
    else:
        os.system("cls")
        print("No aplica descuento por edad!")
        total_recaudado += precio
        
    cliente = {
        "ID": len(clientes)+1,
        "asiento_fila": asiento_fila,
        "asiento_columna": asiento_columna,
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
        "precio": int(precio),
    }

    clientes.append(cliente)
    cine[asiento_columna-1][asiento_fila-1] = "X"
    print("Se ha comprado el asiento con éxito!")
    presionar_tecla()
def opcion3():
    if len(clientes) <= 0:
        presionar_tecla_message("ERROR! debe realizar una venta en la opción 2!")
    else:
        print("VENTAS REALIZADAS")
        for c in clientes:
            print(f"ID CLIENTE: {c['ID']}")
            print(f"\tNombre: {c['nombre']}")
            print(f"\tEdad: {c['edad']}")
            print(f"\tNum. Teléfono: {c['telefono']}")
            print(f"\tFila: {c['asiento_fila']}")
            print(f"\tColumna: {c['asiento_columna']}")
            print(f"\tTotal pagado: {c['precio']}")
        print(f"Total recaudado: {total_recaudado}")
        presionar_tecla()

def opcion4():
    if len(clientes) <= 0:
        presionar_tecla_message("ERROR! debe realizar una venta en la opción 2!")
    else:
        hf = datetime.datetime.now()
    
        with open(f"{hf.day}-{hf.month}-{hf.year}_{hf.hour}_{hf.minute}_{hf.second}.csv", "w", newline="") as archivo:
            escritor = csv.DictWriter(archivo, ["ID", "nombre", "edad", "telefono", "asiento_fila", "asiento_columna", "precio"])
            escritor.writeheader()
            escritor.writerows(clientes)
        presionar_tecla_message("Se ha creado el archivo con éxito!")
        

#-------------------------validaciones-----------------------------#

def validacion_asientos():
    while True:
        try:
            asiento_fila = int(input("Ingrese la fila de su asiento: "))
            asiento_columna = int(input("Ingrese la columna del asiento: "))
            
            if cine[asiento_fila-1][asiento_columna-1] == "X":
                presionar_tecla_message("ERROR! ese asiento esta ocupado!")
            else:
                return asiento_fila,asiento_columna
        except:
            presionar_tecla_message("ERROR! debe ser un entero!")

def validacion_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        
        if len(nombre) <= 2:
            presionar_tecla_message("ERROR! el nombre es inválido, debe tener mínimo 3 caracteres!")
        else:
            return nombre

def validacion_edad_precio(message):
    while True:
        try:
            variable = int(input(message))
            
            if variable <= 0:
                presionar_tecla_message("ERROR! no puede ser negativo!")
            else:
                return variable
        except:
            presionar_tecla_message("ERROR! debe ser un entero!")

def validacion_telefono():
    while True:
        try:
            telefono = int(input("Ingrese su número de teléfono: "))
            
            if len(str(telefono)) < 9:
                presionar_tecla_message("ERROR! el número de teléfono tiene que tener 9 dígitos!")
            else:
                return telefono
        except:
            presionar_tecla_message("ERROR! debe ser un entero!")

def presionar_tecla_message(message):
    os.system("cls")
    print(message)
    print(">> Presiona una tecla para continuar <<")
    msvcrt.getch()
    os.system("cls")

def presionar_tecla():
    print(">> Presiona una tecla para continuar <<")
    msvcrt.getch()
    os.system("cls")