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
                print("ERROR! el número no existe")
        except:
            print("ERROR! el valor no es número")
    return opc

    
