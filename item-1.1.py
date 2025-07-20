def mostrar_integrantes():
    """
    Función que imprime en pantalla los nombres y apellidos 
    de los integrantes del grupo en formato de lista
    """

    integrantes = [
        "Christian Farias",
        "Pablo Duran", 
        "Jairo Badilla",
        "Diego Hernandez"
    ]

    print("===================================================")
    print("INTEGRANTES DEL GRUPO - EXAMEN TRANSVERSAL DRY7122")
    print("===================================================")
    
    for integrante in integrantes:
        print(f"- {integrante}")
    
    print("===================================================")


mostrar_integrantes()