from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario
from datetime import datetime, date

biblioteca = Biblioteca()

print("=== Bienvenido al Sistema de Gestión de Biblioteca ===")

while True:
    print("\n¿Qué quieres hacer?")
    print("1- Registrar libro")
    print("2- Registrar usuario")
    print("3- Crear préstamo")
    print("4- Devolver libro")
    print("5- Consultar préstamos activos")
    print("6- Consultar inventario (todos los libros/usuarios/libros en stock)")
    print("7- Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if not opcion.isdigit():
        print("Error: La opción debe ser un número.")
        continue
    opcion = int(opcion)
    
    try:
        match(opcion):
            case 1:
                isbn = input("Dame el ISBN: ")
                titulo = input("Dame el título: ")
                autor = input("Dame el autor: ")
                nuevo_libro = Libro(isbn, titulo, autor)
                biblioteca.registrar_libro(nuevo_libro)
                print("Libro registrado con éxito.")

            case 2:
                uid = input("Dame el identificador (ID): ")
                nombre = input("Dame el nombre: ")
                max_prestamos = input("Cuantos prestamos puede tener a la vez?")
                if max_prestamos == "":
                    nuevo_usuario = Usuario(uid, nombre)
                else:
                    if not max_prestamos.isdigit():
                        print("Introduce un número")
                        continue
                    max_prestamos = int(max_prestamos)
                    nuevo_usuario = Usuario(uid, nombre,max_prestamos)
                if biblioteca.registrar_usuario(nuevo_usuario):
                    print("Usuario registrado con éxito.")
                else:
                    print("Error: Ese identificador ya existe.")

            case 3:
                biblioteca.mostrar_info()
                isbn = input("Dime el ISBN del libro: ")
                uid = input("Dame el ID del usuario: ")
                fecha_hoy = date.today()

                prestamo = biblioteca.prestar_libro(isbn, uid, fecha_hoy)
                print(f"Préstamo creado. El libro debe devolverse el: {prestamo.fin.strftime('%d/%m/%Y')}")

            case 4:
                isbn = input("Dime el ISBN del libro a devolver: ")
                fecha_hoy = date.today()
                prestamo = biblioteca.devolver_libro(isbn, fecha_hoy)

                if prestamo:
                    print("Libro devuelto satisfactoriamente.")
                else:
                    print("No se encontró un préstamo activo para ese ISBN.")

            case 5:
                biblioteca.mostrar_prestamos_activos()

            case 6:
                    while True:
                        print("\n¿Qué quieres hacer?")
                        print("1- Mostrar libros en stock")
                        print("2- mostrar todos los libros")
                        print("3- Mostrar usuarios")
                        print("4- Salir")
                        entrada = input("Selecciona una opción: ")
                        if not entrada.isdigit():
                            print("Introduzca un número")
                            continue
                        entrada = int(entrada)
                        match(entrada):
                            case 1:
                                biblioteca.mostrar_stock()
                            case 2:
                                biblioteca.mostrar_libros_todos()
                            case 3:
                                biblioteca.mostrar_usuarios()
                            case 4:
                                print("Volviendo al menú principal....")
                                break
                            case _:
                                print("Opción no válida (1-4).")

            case 7:
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción no válida (1-7).")

    except RuntimeError as e:
        print(f"Error de operación: {e}")
    except ValueError as e:
        print(f"Error de datos: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")