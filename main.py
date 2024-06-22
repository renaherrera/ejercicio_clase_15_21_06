import os
from functions import *

while True:
    os.system("cls")
    opc = menu( [1,2,3,4,5] )
    os.system("cls")
    if opc == 1:
        opcion1()
    elif opc == 2:
        opcion2()
    elif opc == 3:
        opcion3()
    elif opc == 4:
        opcion4()
    else:
        print("ADIOS!")
        break