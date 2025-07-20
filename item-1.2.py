import os

a=int(0)

while a != 2:
    print("------------------------------------------------------------------")
    print("¡Bienvenido al programa para ver si la Vlan es Extendida o Estandar!")
    print("1 - Iniciar Programa")
    print("2 - Salir")
    print("------------------------------------------------------------------")
    opcion=int(input("Selecciona un numero: "))
    os.system('clear')

    if opcion == 1:
        vlan=int(input("Selecciona el Numero de VLAN: "))
        if vlan >= 1 and vlan <= 1005:
            os.system('clear')
            print("Tu Numero de Vlan es Estandar...")
            input()
            os.system('clear')
        elif vlan >= 1006 and vlan <= 4094:
            os.system('clear')
            print("Tu Numero de Vlan es Extendida...")
            input()
            os.system('clear')
        else:
            os.system('clear')
            print("Tu numero de VLAN esta fuera del Rango de Estandar y Extendida...")
            input()
            os.system('clear')


    elif opcion == 2:
        a=2


    else:
        os.system('clear')
        print("Opcion Incorrecta, intentalo denuevo...")
        input()
        os.system('clear')