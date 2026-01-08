from Biblioteca import Biblioteca

biblioteca = Biblioteca()

print("Bienbenido a la biblioteca")
try:
    while True:
        print("que quieres hacer?")
        print("1- Registrar libro")
        print("2- Registrar usuario")
        print("3- Crear prestamo")
        print("4- Gestionar devoluciones")
        print("5- Consultar prestamos activos")
        opcion = input()
        if not opcion.isdigit():
            print("La opcion debe ser un número")
            continue
        opcion = int(opcion)
        if opcion < 1 or opcion > 5:
            print("La opcion debe ser 1-5")
            continue
        match(opcion):
            case 1:
             pass   
except ValueError as err:
    print(f"Error: {err}")