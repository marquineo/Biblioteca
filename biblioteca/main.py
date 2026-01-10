import Biblioteca

biblioteca = Biblioteca.Biblioteca()
print("Bienvenido a la biblioteca")
try:
    while True:
        print("que quieres hacer?")
        print("1- Registrar libro")
        print("2- Registrar usuario")
        print("3- Crear prestamo")
        print("4- Devolver libro")
        print("5- Consultar prestamos activos")
        print("6- Salir")
        opcion = input()
        if not opcion.isdigit():
            print("La opcion debe ser un número")
            continue
        opcion = int(opcion)
        if opcion < 1 or opcion > 6:
            print("La opcion debe ser 1-6")
            continue
        match (opcion):
            case 1:
                isbn = input("Dame el ISBN: ")
                autor = input("Dame el autor: ")
                titulo = input("Dame el titulo: ")
                biblioteca.registrar_libro(isbn, titulo, autor)
                print("Nuevo libro registrado")
            case 2:
                id = input("Dame el identificador: ")
                nombre = input("Dame el nombre: ")
                if not biblioteca.registrar_usuarios(id, nombre):
                    print("Ese identificar ya existe")
            case 3:
                biblioteca.mostrar_info()
                fecha_fin = input("Dame la fecha de expiración. ejemplo: 25/2/2026: ")
                isbn = input("Dime el ISBN del libro: ")
                id = input("Dame el identificador del usuario: ")
                biblioteca.crear_prestamo(fecha_fin, isbn, id)
                print("Prestamo creado satisfactoriamente")
            case 4:
                isbn = input("Dime el ISBN del libro: ")
                id = input("Dame el identificador del usuario: ")
                biblioteca.devolver_libro(id, isbn)
            case 5:
                biblioteca.mostrar_prestamos_activos()
            case 6:
                break
except ValueError as err:
    print(f"Error: {err}")


    #TODO controlar que los usuarios no puedan tener mas de 3 prestamos activos
    #FIXME Darle una vuelta a los test